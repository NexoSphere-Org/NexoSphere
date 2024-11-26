from flask import request
from .news_route_controller import handle_get_news

def stockSentimentRoute(app):
    @app.route("/get-news", methods=["GET"])
    def get_news():
        ticker_symbol = request.args.get("ticker_symbol")
        date_start = request.args.get("date_start")
        date_end = request.args.get("date_end")
        return handle_get_news(ticker_symbol, date_start, date_end)