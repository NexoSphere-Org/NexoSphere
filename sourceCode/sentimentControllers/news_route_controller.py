from flask import request, jsonify
from datetime import datetime, timedelta
from .news_services import NewsServices
from .cosmos_mongodb_config import get_cosmos_mongodb


def handle_get_news():
    ticker_symbol = request.args.get("ticker_symbol")
    date_start = request.args.get("date_start")
    date_end = request.args.get("date_end")
    if not (ticker_symbol and date_start and date_end):
        return (
            jsonify(
                {"error": "missing query params. ticker_symbol, date_start, date_end"}
            ),
            400,
        )

    try:
        date_start_obj = datetime.strptime(date_start, "%Y-%m-%d")
        date_end_obj = datetime.strptime(date_end, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "check datetime format. yyyy-mm-dd"}), 400

    if date_start_obj > date_end_obj or date_end_obj.date() == datetime.today().date():
        return jsonify({"error": "invalid datetime range"}), 400

    _, db = get_cosmos_mongodb()
    news_controller = NewsServices(db)
    news_results = {}
    current_date = date_start_obj
    while current_date <= date_end_obj:
        results_of_date = news_controller.get_news_of_date(current_date, ticker_symbol)
        news_results[datetime.strftime(current_date, "%Y-%m-%d")] = results_of_date
        # news_results.extend(results_of_date)
        current_date += timedelta(days=1)

    return jsonify(news_results)
