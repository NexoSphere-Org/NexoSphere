
from flask_restx import Namespace, Resource, fields
from flask import request
from stockPriceControllers.stockPriceService import getStockPrice

api = Namespace('stock_prices', description='Stock Price operations')

stock_price_model = api.model('StockPrice', {
    'ticker': fields.String(required=True, description='The stock ticker symbol')
})

@api.route('/getStockPrices')
class GetStockPrices(Resource):
    @api.doc('get_stock_prices')
    @api.param('ticker', 'The stock ticker symbol')
    def get(self):
        """Fetch stock prices for a given ticker symbol"""
        ticker = ticker.upper()
        
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        result = getStockPrice(ticker, start_date, end_date)
        
        if result == {}:
            return {"message": "Ticker Data not found"}, 404
        
        return result, 200
        
