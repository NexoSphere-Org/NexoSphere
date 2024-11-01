from datetime import datetime
import requests
import os
import copy

# Use environment variable for API token with default as 'demo'
# 'demo' api token is free, but only fetches news from AAPL.US.
EODHD_API_TOKEN = os.getenv("EODHD_API_TOKEN", "demo")
FINBERT_API_AUTH = os.getenv("FINBERT_API_AUTH", "GBJJDgfE9Fhimfwu3YwgwgTncOXl4ejm")


class NewsServices:
    def __init__(self, db):
        self.db = db

    # Retrieve news for a specific date and ticker symbol from database or fetch it if not exist
    def get_news_of_date(self, date_obj, ticker_symbol):
        news_list_db = self.get_news_from_db(date_obj, ticker_symbol)
        if news_list_db:
            print(
                f"{datetime.strftime(date_obj, '%Y-%m-%d')} - {ticker_symbol} found in DB."
            )
            return news_list_db
        else:
            print(
                f"{datetime.strftime(date_obj, '%Y-%m-%d')} - {ticker_symbol} not found in DB."
            )
            return self.fetch_and_process_news(date_obj, ticker_symbol)

    # query database for news on a specific date and ticker symbol
    def get_news_from_db(self, input_date, ticker_symbol):
        news_data_collection = self.db["newsData"]
        start_time = input_date.replace(hour=0, minute=0, second=0)
        end_time = input_date.replace(hour=23, minute=59, second=59)
        query = {
            "date": {"$gte": start_time.isoformat(), "$lte": end_time.isoformat()},
            "symbols": {"$in": [ticker_symbol]},
        }
        projection = {
            "_id": 0,
            "date": 1,
            "title": 1,
            "link": 1,
            "symbols": 1,
            "sentiment": 1,
        }
        return list(news_data_collection.find(query, projection))

    # fetch news from API and process it through sentiment analysis before storing to the databas
    def fetch_and_process_news(self, date, ticker_symbol):
        url = "https://eodhd.com/api/news"
        params = {
            "s": ticker_symbol,
            "from": datetime.strftime(date, "%Y-%m-%d"),
            "to": datetime.strftime(date, "%Y-%m-%d"),
            "api_token": EODHD_API_TOKEN,
            "fmt": "json",
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                raw_news_list = response.json()
                fields_to_insert = ["date", "title", "symbols", "link", "content"]
                raw_news_list = [
                    {key: item[key] for key in fields_to_insert if key in item}
                    for item in raw_news_list
                ]
                if len(raw_news_list) == 0:
                    return []
                processed_news = self.process_news(raw_news_list)

                return processed_news
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
            finbert_result = self.infer_finbert(news_obj)
            news_obj["sentiment"] = finbert_result[0]
            news_obj.pop("content", None)
            # {date, title, link, symbols, score: {'label: 'negative', 'score':'0.3456345'} }
            processed_news.append(news_obj)

        processed_news_copy = copy.deepcopy(processed_news)
        news_data_collection = self.db["newsData"]
        news_data_collection.insert_many(processed_news)

        return processed_news_copy

    def infer_finbert(self, news_obj):
        input_str = news_obj["title"] + " " + news_obj.get("content")
        input_str = self.cut_str_for_finbert(input_str)

        url = "https://huggingface-azure-demo1-finbert.eastus2.inference.ml.azure.com/score"
        payload = {"inputs": input_str}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {FINBERT_API_AUTH}",
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Finbert api error code: {response.status_code}")
                return [{}]
        except Exception as e:
            print(f"catch error infer_finbert(): {e}")
            return [{}]

    # Cut extra string if too long.
    def cut_str_for_finbert(self, text, max_tokens=512, avg_token_length=4):
        max_chars = max_tokens * avg_token_length
        truncated_text = text[:max_chars].rsplit(" ", 1)[0]
        return truncated_text.strip()
