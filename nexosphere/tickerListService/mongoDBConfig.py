import pymongo
import os
from dotenv import load_dotenv


def mongoConnection():
    load_dotenv()
    client = pymongo.MongoClient(os.getenv("MONGO_URL"))

    db = client["StockPrice"]
    userCollection = db["UserData"]

    return userCollection

