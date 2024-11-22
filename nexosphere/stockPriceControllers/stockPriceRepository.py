from stockPriceControllers.mongoDBConfig import mongoConnection


def addStockDataToDB(data):
    collection = mongoConnection()
    collection.insert_one(data)


def getStockDataFromDB(ticker):
    collection = mongoConnection()
    result = collection.find({"ticker": ticker}).sort({"timeStamp": -1}).limit(1)
    for item in result:
        return item


def deleteStockDataFromDB(objectId):
    collection = mongoConnection()
    collection.delete_one({"_id": objectId})

