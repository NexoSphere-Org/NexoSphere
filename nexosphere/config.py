import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    COSMOS_URI = os.environ.get('COSMOS_URI')
    COSMOS_KEY = os.environ.get('COSMOS_KEY')
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)