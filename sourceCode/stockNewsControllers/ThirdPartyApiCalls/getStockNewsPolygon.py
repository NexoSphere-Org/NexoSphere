# from dotenv import load_dotenv
# import os
# from pathlib import Path
# import requests
# import json

# from polygon import RESTClient
# from polygon.rest.models import (
#     TickerNews,
# )

# env_path = Path('/Users/n.k.barua/Desktop/NexoSphere/.env') 
# load_dotenv(dotenv_path=env_path)
# news_api_key = os.getenv('POLYGON_API_KEY')

# client = RESTClient(api_key=news_api_key)
# # print(news_api_key)

# news = []
# ticker="AAPL"
# timeStamp="2024-11-09T00:00:00-00:00"
# limit = 10
# url = f"https://api.polygon.io/v2/reference/news?ticker={ticker}&published_utc.gt={timeStamp}&limit={limit}&apiKey={news_api_key}"


# # Send GET request and get the response
# response = requests.get(url)

# data = response.json()

# # Save the JSON data to a file
# with open('response.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
# # for n in client.list_ticker_news("AAPL", order="desc", limit=1):
# #     news.append(n)

# # print(news)

# # print date + title
# # for index, item in enumerate(news):
# #     # verify this is an agg
# #     if isinstance(item, TickerNews):
# #         print("{:<25}{:<15}".format(item.published_utc, item.title))

# #         if index == 5:
# #             break
