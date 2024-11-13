import yfinance as yf
import json
from datetime import datetime

def stockMarketNews(ticker, count=10):
    # Specify the ticker symbol
    stock = yf.Ticker(ticker)

    # Get news articles
    news = stock.news
    time=[]

    if len(news) > count:
        listNews = {}
        counter=0
        while(counter < count):
            listNews[counter] = news[counter]
            # time.append(getTime(news[counter]['providerPublishTime']))
            # print(type(news[counter]))
            counter+=1

        return listNews

    else:
        listNews = {}
        counter=0
        for item in news:
            listNews[counter] = item
            # print(type(news[counter]))
            # time.append(getTime(news[counter]['providerPublishTime']))
            counter+=1

        return listNews
    #     print(f"Title: {article['title']}")
    #     print(f"Link: {article['link']}")
    #     print(f"Published: {article['providerPublishTime']}")
    #     print()

# def getTime(str):

#     # Convert the Unix timestamp string to an integer
#     unix_timestamp = int(str)

#     # Convert to a datetime object
#     dt_object = datetime.fromtimestamp(unix_timestamp)

#     # Print the datetime object in a human-readable format
#     return dt_object

# if __name__ == "__main__":
#     news, time = stockMarketNews('MSFT')
#     print(len(news))
#     print(" ")
#     print(time)

data = stockMarketNews("AAPL")

# Save the JSON data to a file
with open('responseGetNews.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
