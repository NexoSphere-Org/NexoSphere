from flask import Flask, jsonify
from YfAPICalls.stockMarketNewsYf import stockMarketNews
from stockPriceService import generateDayStockOpeningTrend
from sentimentControllers.news_route_controller import handle_get_news

app = Flask(__name__)


@app.route("/stockprice/<ticker>/<daySpan>")
def getStockPrice(ticker, daySpan):
    return generateDayStockOpeningTrend(ticker, daySpan)


@app.route("/stockmarketnews/<ticker>/<int:count>")
def getStockMarketNews(ticker, count):
    return stockMarketNews(ticker, count)


@app.route("/get-news", methods=["GET"])
def get_news():
    return handle_get_news()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9874)  # Start the server
