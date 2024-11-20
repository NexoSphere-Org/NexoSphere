import pymongo
import redis
import os

COSMOS_CONNECTION_STRING = os.getenv("COSMOS_CONNECTION_STRING")
DATABASE_NAME = os.getenv("DATABASE_NAME")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PWD = os.getenv("REDIS_PWD")

cosmos_mongodb_client = None


def get_cosmos_mongodb():

    global cosmos_mongodb_client
    global cosmos_db
    if cosmos_mongodb_client is None:
        cosmos_mongodb_client = pymongo.MongoClient(COSMOS_CONNECTION_STRING)
        cosmos_db = cosmos_mongodb_client[DATABASE_NAME]
        print("creating new mongodb connection")

    return cosmos_mongodb_client, cosmos_db


r = None


def get_redis_cache():
    global r
    if r == None:
        r = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD, decode_responses=True
        )
        print("creating new redis connection")
    return r
