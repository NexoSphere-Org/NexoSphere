from flask import Flask
from YfAPICalls.stockMarketNewsYf import stockMarketNews
from stockPriceService import generateDayStockOpeningTrend

app = Flask(__name__)


@app.route('/stockprice/<ticker>/<daySpan>')
def getStockPrice(ticker, daySpan):
    return generateDayStockOpeningTrend(ticker, daySpan)

@app.route('/stockmarketnews/<ticker>/<int:count>')
def getStockMarketNews(ticker, count):
    return stockMarketNews(ticker, count)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9874)  # Start the server