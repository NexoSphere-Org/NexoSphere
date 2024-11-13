from datetime import datetime, timedelta


class CacheNewsServices:
    def __init__(self, r):
        self.r = r

    def get_cached_news(self, ticker_symbol, date_obj):
        date_str = date_obj.strftime("%Y-%m-%d")

        news_list = []
        key_pattern = f"news:{date_str}:*"
        for key in self.r.scan_iter(key_pattern):
            if "counter" in key:
                continue
            news_data = self.r.json().get(key)
            for symbol in news_data["symbols"]:
                if ticker_symbol == symbol.split(".")[0] or ticker_symbol == symbol:
                    news_list.append(news_data)
                    break
        return news_list

    def cache_news(self, news_list):
        for news in news_list:
            date_str = news["date"][:10]
            key_suffix = self.r.incr(f"news:{date_str}:counter")
            key = f"news:{date_str}:{key_suffix:03d}"
            # news_json = json.dumps(news)
            self.r.json().set(key, "$", news)

    def delete_expired_cache(self, today, days_to_cache):
        expired_date = today - timedelta(days=days_to_cache + 1)
        expired_date_str = datetime.strftime(expired_date, "%Y-%m-%d")

        key_pattern = f"news:{expired_date_str}:*"
        matching_keys = self.r.keys(key_pattern)
        for key in matching_keys:
            self.r.delete(key)
        print(f"{key_pattern} deleted")
        print()
