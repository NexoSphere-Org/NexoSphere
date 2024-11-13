import pymongo

def mongoTickerNewsConnection():
    # client = pymongo.MongoClient("mongodb+srv://baruanishant97:Abcd1234@cluster0.d0ttz.mongodb.net/")
    client = pymongo.MongoClient("mongodb://admin:password@localhost:27017/")

    db = client["stockNews"]

    return db

# r = mongoTickerNewsConnection("sentimentScore")
# print(r)
# result = r.find_one({"_id": "https://finance.yahoo.com/news/apple-next-device-ai-wall-203611108.html"})
# print(result)
