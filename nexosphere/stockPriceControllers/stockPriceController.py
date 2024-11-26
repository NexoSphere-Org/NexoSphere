from flask import request
from stockPriceControllers.stockPriceService import getStockPrice

def stockPriceRoutes(app):
    
    @app.route("/stockPrice/<ticker>", methods=['GET'])
    def getStockPriceFromTicker(ticker):
        ticker = ticker.upper()
        
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        result = getStockPrice(ticker, start_date, end_date)
        
        if result == {}:
            return {"message": "Ticker Data not found"}, 404
        
        return result, 200
