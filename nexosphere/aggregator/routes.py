from flask import request, jsonify, current_app
from nexosphere.aggregator import bp
from nexosphere.aggregator.services.data_aggregator import aggregate_data_naively
from nexosphere.aggregator.services.public_data_ingestor import *

@bp.route('/aggregate', methods=['GET'])
def aggregate():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Ticker symbol is required"}), 400

    finnhub_api_key = current_app.config["FINNHUB_API_KEY"]
    alpha_vantage_api_key = current_app.config["ALPHA_VANTAGE_API_KEY"]

    yahoo_data = fetch_yahoo_finance_data(ticker)
    finnhub_data = fetch_finnhub_data(ticker, finnhub_api_key)
    alpha_vantage_data = fetch_alpha_vantage_data(ticker, alpha_vantage_api_key)

    if yahoo_data and finnhub_data and alpha_vantage_data:
        aggregated_data = aggregate_data_naively(yahoo_data, finnhub_data, 
                                                 alpha_vantage_data)
        return jsonify(aggregated_data), 200
    else:
        return jsonify({"error": "Failed to fetch data from one or more sources"}),
        500