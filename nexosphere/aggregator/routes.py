from flask import jsonify
from nexosphere.aggregator import bp

@bp.route('/stocks', methods=['GET'])
def get_stocks():
    # Implement logic to fetch and aggregate stock data
    return jsonify({"message": "Stocks data"})

@bp.route('/options', methods=['GET'])
def get_options():
    # Implement logic to fetch and aggregate options data
    return jsonify({"message": "Options data"})