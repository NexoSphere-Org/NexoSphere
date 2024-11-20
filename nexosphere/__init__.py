import os
from flask import Flask
from azure.cosmos import CosmosClient
import redis
from dotenv import load_dotenv

def create_app(test_config=None):
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)
    
    # Default configuration
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        COSMOS_URI=os.environ.get('COSMOS_URI'),
        COSMOS_KEY=os.environ.get('COSMOS_KEY'),
        REDIS_HOST=os.environ.get('REDIS_HOST', 'localhost'),
        REDIS_PORT=os.environ.get('REDIS_PORT', 6379)
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
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
    from nexosphere.aggregator import bp as aggregator_bp
    from nexosphere.sentiment import bp as sentiment_bp
    
    app.register_blueprint(aggregator_bp, url_prefix='/api/v1/aggregate')
    app.register_blueprint(sentiment_bp, url_prefix='/api/v1/sentiment')

    return app