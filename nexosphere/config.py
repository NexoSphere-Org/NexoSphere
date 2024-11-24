import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    COSMOS_URI = os.environ.get('COSMOS_URI')
    COSMOS_KEY = os.environ.get('COSMOS_KEY')
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY')
    ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
    POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY')