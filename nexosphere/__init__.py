import os
from flask import Flask
from azure.cosmos import CosmosClient
import redis
from dotenv import load_dotenv
from nexosphere.config import Config

def create_app(test_config=None):
    # Load environment variables from .env file
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))

    app = Flask(__name__, instance_relative_config=True)
    # Default configuration
    # Load configuration from Config class
    app.config.from_object(Config)
    

    if test_config is not None:
        app.config.update(test_config)

    # # Initialize CosmosDB
    # cosmos_client = CosmosClient(app.config['COSMOS_URI'], app.config['COSMOS_KEY'])
    # app.cosmos_client = cosmos_client

    # # Initialize Redis
    # redis_client = redis.Redis(
    #     host=app.config['REDIS_HOST'],
    #     port=app.config['REDIS_PORT']
    # )
    # app.redis_client = redis_client

    # Register blueprints
    
    if os.environ.get('ENABLE_AGGREGATOR', 'true').lower() == 'true':
        from nexosphere.aggregator import bp as aggregator_bp
        app.register_blueprint(aggregator_bp, url_prefix='/api/v1/aggregator')

    if os.environ.get('ENABLE_SENTIMENT', 'false').lower() == 'true':
        from nexosphere.sentiment import bp as sentiment_bp
        app.register_blueprint(sentiment_bp, url_prefix='/api/v1/sentiment')

    return app