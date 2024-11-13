from flask import request, jsonify
from datetime import datetime, timedelta
from .news_services import NewsServices
from .cache_news_service import CacheNewsServices
from .database_config import get_cosmos_mongodb, get_redis_cache


def handle_get_news(ticker_symbol, date_start, date_end, api_call=True):
    if not (ticker_symbol and date_start and date_end):
        if api_call:
            return (
                jsonify(
                    {
                        "error": "missing query params. ticker_symbol, date_start, date_end"
                    }
                ),
                400,
            )
        else:
            return {
                "statusCode": 400,
                "error": "missing query params. ticker_symbol, date_start, date_end",
            }

    try:
        date_start_obj = datetime.strptime(date_start, "%Y-%m-%d")
        date_end_obj = datetime.strptime(date_end, "%Y-%m-%d")
    except ValueError:
        if api_call:
            return jsonify({"error": "check datetime format. yyyy-mm-dd"}), 400
        else:
            return {"statusCode": 400, "error": "check datetime format. yyyy-mm-dd"}

    if date_start_obj > date_end_obj or date_end_obj.date() == datetime.today().date():
        if api_call:
            return jsonify({"error": "invalid datetime range"}), 400
        else:
            return {"statusCode": 400, "error": "invalid datetime range"}

    _, db = get_cosmos_mongodb()
    new_services = NewsServices(db)
    r = get_redis_cache()
    cache_news_services = CacheNewsServices(r)

    ticker_symbol = ticker_symbol.upper()

    news_results = {}
    current_date = date_start_obj
    while current_date <= date_end_obj:
        cached_news = cache_news_services.get_cached_news(ticker_symbol, current_date)
        # if data exist in redis cache
        if len(cached_news):
            news_results[datetime.strftime(current_date, "%Y-%m-%d")] = cached_news
            print(
                f"get {len(cached_news)} from Cache for:{current_date}_{ticker_symbol} "
            )
        else:
            print(f"No cache for {current_date}_{ticker_symbol}")
            results_of_date = new_services.get_news_of_date(current_date, ticker_symbol)
            news_results[datetime.strftime(current_date, "%Y-%m-%d")] = results_of_date
        current_date += timedelta(days=1)

    if api_call:
        return jsonify(news_results)
    else:
        return news_results
