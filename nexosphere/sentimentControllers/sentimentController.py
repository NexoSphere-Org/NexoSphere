from flask_restx import Namespace, Resource, fields
from flask import request
from .news_route_controller import handle_get_news

api = Namespace('sentiment', description='Sentiment operations')

news_model = api.model('News', {
    'ticker_symbol': fields.String(required=True, description='The stock ticker symbol'),
    'date_start': fields.String(required=True, description='The start date for the news'),
    'date_end': fields.String(required=True, description='The end date for the news')
})

news_data_model = api.model('NewsData', {
    '_id': fields.String(required=True, description='The id of the request'),
    'date': fields.String(required=True, description='The date of the news'),
    'title': fields.String(required=True, description='The title of the news'),
    'symbols': fields.String(required=True, description='The stock ticker symbols list'),
    'link': fields.String(required=True, description='The source of the news'),
    'sentiment': fields.String(required=True, description='The sentiment analysis of the news'),
    'summarization': fields.String(description='The summary of the news')
    
    
})

@api.route('/get-news')
class GetNews(Resource):
    @api.doc('get_news')
    @api.expect(news_model, validate=True)
    @api.marshal_with(news_data_model, as_list=True)
    def get(self):
        """Fetch news for a given stock ticker symbol and date range"""
        ticker_symbol = request.args.get("ticker_symbol")
        date_start = request.args.get("date_start")
        date_end = request.args.get("date_end")
        return handle_get_news(ticker_symbol, date_start, date_end)