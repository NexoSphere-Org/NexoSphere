import pymongo
import os

def mongoConnection():
    client = pymongo.MongoClient(os.getenv("MONGO_URL"))

    db = client["StockPrice"]
    collection = db["StockPrice"]

    return collection


