from flask import Flask, jsonify

from stockpriceControllers.YfAPICalls.stockMarketNewsYf import stockMarketNews
from stockpriceControllers.stockPriceService import generateDayStockOpeningTrend
from sentimentControllers.news_route_controller import handle_get_news
from tickerListService.tickerController import tickerRoutes

app = Flask(__name__)
#expose the ticker list service
tickerRoutes(app)

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
