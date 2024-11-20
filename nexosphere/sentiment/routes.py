from flask import request
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from nexosphere.sentiment import bp

from nexosphere.sentiment.stockpriceControllers.YfAPICalls.stockMarketNewsYf import stockMarketNews
from nexosphere.sentiment.stockpriceControllers.stockPriceService import generateDayStockOpeningTrend
from nexosphere.sentiment.sentimentControllers.news_route_controller import handle_get_news
from nexosphere.sentiment.sentimentControllers.schedule_task_controller import scheduled_task
from nexosphere.sentiment.tickerListService.tickerController import tickerRoutes

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=scheduled_task, trigger="cron", hour=1, next_run_time=datetime.now()
)

# Expose the ticker list service
tickerRoutes(bp)


@bp.route("/stockprice/<ticker>/<daySpan>")
def getStockPrice(ticker, daySpan):
    return generateDayStockOpeningTrend(ticker, daySpan)


@bp.route("/stockmarketnews/<ticker>/<int:count>")
def getStockMarketNews(ticker, count):
    return stockMarketNews(ticker, count)


@bp.route("/get-news", methods=["GET"])
def get_news():
    ticker_symbol = request.args.get("ticker_symbol")
    date_start = request.args.get("date_start")
    date_end = request.args.get("date_end")
    return handle_get_news(ticker_symbol, date_start, date_end)


# if __name__ == "__main__":
#     bp.run(debug=True, host="0.0.0.0", port=9874)  # Start the server
