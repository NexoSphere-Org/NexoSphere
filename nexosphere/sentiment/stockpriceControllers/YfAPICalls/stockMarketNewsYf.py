import yfinance as yf
import json

def stockMarketNews(ticker, count):
    # Specify the ticker symbol
    stock = yf.Ticker(ticker)

    # Get news articles
    news = stock.news

    if len(news) > count:
        listNews = {}
        counter=0
        while(counter < count):
            listNews[counter] = news[counter]
            # print(type(news[counter]))
            counter+=1

        return listNews

    else:
        listNews = {}
        counter=0
        for item in news:
            listNews[counter] = item
            # print(type(news[counter]))
            counter+=1

        return listNews
    #     print(f"Title: {article['title']}")
    #     print(f"Link: {article['link']}")
    #     print(f"Published: {article['providerPublishTime']}")
    #     print()

if __name__ == "__main__":
    print(stockMarketNews('CM.TO',1))