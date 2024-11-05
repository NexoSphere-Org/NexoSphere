# problem:
# 1.eodhd api search ticker symbool with substring("AAPL"="AAPL.US"), database doesn't("AAPL"=>gets nothing)
# 2. should search database for every date, not search as date range

from datetime import datetime
import requests
import os
import copy
import time

EODHD_API_URL = os.getenv("EODHD_API_URL", "https://eodhd.com/api/news")
EODHD_API_TOKEN = os.getenv("EODHD_API_TOKEN", "671d2db756a3a1.75820387")
FINBERT_API_URL = os.getenv(
    "FINBERT_API_URL",
    "https://workspace1102-finbert.eastus2.inference.ml.azure.com/score",
)
FINBERT_API_AUTH = os.getenv("FINBERT_API_AUTH", "YDEo1Ge8BjRiANioFCXDkOpF13yWraNG")
T5_API_AUTH = os.getenv("T5_API_AUTH", "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")
T5_API_URL = os.getenv(
    "T5_API_URL",
    "https://e8nuunz76exd7o1d.eastus.azure.endpoints.huggingface.cloud/predict",
)


class NewsServices:
    def __init__(self, db):
        self.db = db

    # Retrieve news for a specific date and ticker symbol from database or fetch it if not exist
    def get_news_of_date(self, date_obj, ticker_symbol):
        news_list_db = self.get_news_from_db(date_obj, ticker_symbol)
        if news_list_db:
            print(
                f"{datetime.strftime(date_obj, '%Y-%m-%d')}-{ticker_symbol} found in DB."
            )
            print(news_list_db)
            return news_list_db
        else:
            print(
                f"{datetime.strftime(date_obj, '%Y-%m-%d')}-{ticker_symbol} NOT found in DB."
            )
            return self.fetch_and_process_news(date_obj, ticker_symbol)

    # query database for news on a specific date and ticker symbol
    def get_news_from_db(self, input_date, ticker_symbol):
        news_data_collection = self.db["newsData"]
        start_time = input_date.replace(hour=0, minute=0, second=0)
        end_time = input_date.replace(hour=23, minute=59, second=59)

        pipeline = [
            {
                "$match": {
                    "$and": [
                        {
                            "date": {
                                "$gte": start_time.isoformat(),
                                "$lte": end_time.isoformat(),
                            }
                        },
                        {"symbols": {"$in": ["AAPL.US"]}},
                    ]
                }
            },
            {"$project": {"_id": 0}},
        ]
        results = news_data_collection.aggregate(pipeline)
        news_list = [doc for doc in results]
        return news_list

    # fetch news from API and process it(summarization + sentiment analysis)
    def fetch_and_process_news(self, date, ticker_symbol):
        params = {
            "s": ticker_symbol,
            "from": datetime.strftime(date, "%Y-%m-%d"),
            "to": datetime.strftime(date, "%Y-%m-%d"),
            "api_token": EODHD_API_TOKEN,
            "fmt": "json",
        }
        try:
            response = requests.get(EODHD_API_URL, params=params)
            if response.status_code == 200:
                raw_news_list = response.json()
                fields_to_insert = ["date", "title", "symbols", "link", "content"]
                raw_news_list = [
                    {key: item[key] for key in fields_to_insert if key in item}
                    for item in raw_news_list
                ]
                if len(raw_news_list) == 0:
                    return []
                print(f"fetched {len(raw_news_list)} news from eodhd news api....")
                processed_news_list = self.process_news(raw_news_list)

                return processed_news_list
            else:
                print(f"eodhd api error code: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"eodhd api error: {e}")
            return []

    # perform sentiment analysis, store results.
    def process_news(self, news_list):
        processed_news = []
        for news_obj in news_list:
            text_for_finbert, summarized_content = self.summarize_news(news_obj)
            finbert_result = self.infer_finbert(text_for_finbert)
            news_obj["sentiment"] = finbert_result
            news_obj["summarization"] = summarized_content
            news_obj.pop("content", None)
            # {date, title, link, symbols, score: {'label: 'negative', 'score':'0.3456345'} }
            processed_news.append(news_obj)

        processed_news_copy = copy.deepcopy(processed_news)
        news_data_collection = self.db["newsData"]
        news_data_collection.insert_many(processed_news)

        return processed_news_copy

    # Cut extra string if too long.
    def summarize_news(self, news_obj, max_tokens=512, avg_token_length=4):
        max_chars = max_tokens * avg_token_length  # max string length finbert can take
        content_and_title = news_obj["title"] + ". " + news_obj["content"]

        if len(content_and_title) < max_chars:
            print(f"short news, skip T5 summarization.")
            summarized_content = news_obj["content"]
            return content_and_title.strip(), summarized_content
        else:
            summarized_content = self.infer_t5(content_and_title)
            if not summarized_content:
                print(f"t5 fails, fallback to truncation.")
                truncated_content_and_title = content_and_title[:max_chars].rsplit(
                    " ", 1
                )[0]
                summarized_content = news_obj["content"][:max_chars].rsplit(" ", 1)[0]
                return truncated_content_and_title.strip(), summarized_content.strip()
            else:
                return summarized_content, summarized_content

    def infer_t5(self, text, max_length=30):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {T5_API_AUTH}",
        }
        payload = {
            "inputs": f"summarize:{text}",
            "parameters": {"max_length": max_length},
        }
        try:
            print("t5 infering.....")
            start_time = time.time()
            response = requests.post(T5_API_URL, json=payload, headers=headers)
            end_time = time.time()
            t5_inference_time = round((end_time - start_time) * 1000, 2)
            if response.status_code == 200:
                summary = response.json()[0].get("translation_text", "")
                if not summary:
                    print("T5 returns empty")
                    return False
                print(f"T5 success, inference time: {t5_inference_time}")
                return summary
            else:
                print(f"T5 api error code: {response.status_code}")
                return False
        except Exception as e:
            print(f"catch error infer_t5(): {e}")
            return False

    def infer_finbert(self, news_text):
        payload = {"inputs": news_text}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {FINBERT_API_AUTH}",
        }
        try:
            response = requests.post(FINBERT_API_URL, json=payload, headers=headers)
            if response.status_code == 200:
                return response.json()[0]
            else:
                print(f"Finbert api error code: {response.status_code}")
                return {}
        except Exception as e:
            print(f"catch error infer_finbert(): {e}")
            return {}