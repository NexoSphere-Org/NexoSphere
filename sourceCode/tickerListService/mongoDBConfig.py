import pymongo

def mongoConnection():
    client = pymongo.MongoClient("mongodb+srv://baruanishant97:Abcd1234@cluster0.d0ttz.mongodb.net/")

    db = client["StockPrice"]
    userCollection = db["UserData"]

    return userCollection

