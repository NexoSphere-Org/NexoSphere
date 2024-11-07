import pymongo

def mongoConnection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["StockPrice"]
    collection = db["StockPrice"]

    return collection


