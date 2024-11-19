from flask import Flask, request
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from stockpriceControllers.YfAPICalls.stockMarketNewsYf import stockMarketNews
from stockpriceControllers.stockPriceService import generateDayStockOpeningTrend
from sentimentControllers.news_route_controller import handle_get_news
from sentimentControllers.schedule_task_controller import scheduled_task
from tickerListService.tickerController import tickerRoutes

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()
# scheduler.add_job(
#     func=scheduled_task, trigger="interval", seconds=60, next_run_time=datetime.now()
# )
scheduler.add_job(
    func=scheduled_task, trigger="cron", hour=1, next_run_time=datetime.now()
)


# expose the ticker list service
tickerRoutes(app)


@app.route("/stockprice/<ticker>/<daySpan>")
def getStockPrice(ticker, daySpan):
    return generateDayStockOpeningTrend(ticker, daySpan)


@app.route("/stockmarketnews/<ticker>/<int:count>")
def getStockMarketNews(ticker, count):
    return stockMarketNews(ticker, count)


@app.route("/get-news", methods=["GET"])
def get_news():
    ticker_symbol = request.args.get("ticker_symbol")
    date_start = request.args.get("date_start")
    date_end = request.args.get("date_end")
    return handle_get_news(ticker_symbol, date_start, date_end)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9874)  # Start the server
