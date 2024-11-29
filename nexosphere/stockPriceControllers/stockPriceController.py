
from flask_restx import Namespace, Resource, fields
from flask import request
from stockPriceControllers.stockPriceService import getStockPrice
from datetime import datetime

api = Namespace('stock_prices', description='Stock Price operations',path='/')

stock_price_model = api.model('StockPrice', {
    'ticker': fields.String(required=True, description='The stock ticker symbol')
})

@api.route('/stockPrice/<ticker>', methods=['GET'])
class GetStockPrices(Resource):
    @api.doc('get_stock_prices')
    @api.param('start_date', 'The start date for fetching stock prices')
    @api.param('end_date', 'The end date for fetching stock prices')
    def get(self, ticker):
        """Fetch stock prices for a given ticker symbol"""
        ticker = ticker.upper()
        
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        result = getStockPrice(ticker, start_date, end_date)
        
        if result == {}:
            return {"message": "Ticker Data not found"}, 404
        for item in result:
            if isinstance(result[item], datetime):
                result[item] = result[item].isoformat()
        return result, 200
        
