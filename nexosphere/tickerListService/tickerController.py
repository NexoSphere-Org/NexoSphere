from flask_restx import Namespace, Resource, fields
from flask import request
from tickerListService.tickerService import getTickerChoices, addTickerChoice, updateTickerChoice, deleteTickerChoice

api = Namespace('tickers', description='Ticker operations')

ticker_model = api.model('Ticker', {
    'user_id': fields.Integer(required=True, description='The user ID'),
    'ticker': fields.String(required=True, description='The stock ticker symbol')
})

@api.route('/getTickers')
class GetTickers(Resource):
    @api.doc('get_tickers')
    @api.param('userId', 'The user ID')
    def get(self):
        """Fetch tickers for a given user ID"""
        userId = request.args.get('userId')
        result = getTickerChoices(int(userId))
        
        if result == {}:
            return {"message": "user not found"}, 404
        
        return result, 200

@api.route('/createTicker')
class CreateTicker(Resource):
    @api.doc('create_ticker')
    @api.expect(ticker_model, validate=True)
    def post(self):
        """Create a new ticker for a user"""
        user_id = request.json.get('user_id')
        ticker = request.json.get('ticker')
        
        result = addTickerChoice(int(user_id), ticker)
        
        if result != {}:
            return getTickerChoices(int(user_id)), 201
        
        return {"message": "user already exist"}, 403

@api.route('/updateTicker')
class UpdateTicker(Resource):
    @api.doc('update_ticker')
    @api.expect(ticker_model, validate=True)
    def put(self):
        """Update a ticker for a user"""
        user_id = request.json.get('user_id')
        ticker = request.json.get('ticker')
        
        result = updateTickerChoice(int(user_id), ticker)

        if result == {}:
            return {"message": "user not found"}, 404
        
        return getTickerChoices(int(user_id)), 200

@api.route('/deleteTicker')
class DeleteTicker(Resource):
    @api.doc('delete_ticker')
    @api.expect(ticker_model, validate=True)
    def delete(self):
        """Delete a ticker for a user"""
        user_id = request.json.get('user_id')
        ticker = request.json.get('ticker')
        
        result = deleteTickerChoice(int(user_id), ticker)

        if result == {}:
            return {"message": "user not found"}, 404
        
        return getTickerChoices(int(user_id)), 200