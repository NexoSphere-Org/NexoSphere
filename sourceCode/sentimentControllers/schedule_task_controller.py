from .database_config import get_cosmos_mongodb, get_redis_cache
from .news_services import NewsServices
from .cache_news_service import CacheNewsServices
from datetime import datetime, timedelta


def scheduled_task():

    today = datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    days_to_cache = 5
    cache_start = today - timedelta(days=days_to_cache)
    cache_end = today - timedelta(days=1)

    _, db = get_cosmos_mongodb()
    ticker_symbols_list = get_popular_tickers(db)
    news_services = NewsServices(db)
    r = get_redis_cache()
    cache_news_services = CacheNewsServices(r)

    temp_date = cache_start
    while temp_date <= cache_end:
        for ticker_symbol in ticker_symbols_list:
            print(f"----- caching for: {temp_date}-{ticker_symbol} -----")

            # Fetch and process the news, make sure mongodb has all cache data
            db_news_list = news_services.get_news_of_date(temp_date, ticker_symbol)
            if not len(db_news_list):  # if no news for this day
                print(f"No news for {temp_date}-{ticker_symbol}")
                continue

            # check if redis cache has cache for this ticker and date
            cached_news = cache_news_services.get_cached_news(ticker_symbol, temp_date)
            if not len(cached_news):
                cache_news_services.cache_news(db_news_list)
                print(f"!!! Caching {len(db_news_list)} news to Redis")
            else:
                print(f"!!! {len(cached_news)} news already exist in Redis")

            print(f"---- {temp_date}-{ticker_symbol} DONE -----")

        temp_date += timedelta(days=1)
    cache_news_services.delete_expired_cache(today, days_to_cache)


def get_popular_tickers(db):
    # _, db = get_cosmos_mongodb()
    ticker_symbol_collection = db["popularTickerSymbols"]
    documents = ticker_symbol_collection.find({})
    ticker_symbols_list = [doc["symbol"] for doc in documents]
    return ticker_symbols_list
