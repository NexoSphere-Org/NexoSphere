# TODO: Implement a more sophisticated aggregation algorithm

def aggregate_data_naively(yahoo_data, finnhub_data, alpha_vantage_data):

    aggregated_data = {
        "yahoo": yahoo_data,
        "finnhub": finnhub_data,
        "alpha_vantage": alpha_vantage_data
    }
    return aggregated_data