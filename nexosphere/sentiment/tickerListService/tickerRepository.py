from tickerListService.mongoDBConfig import mongoConnection

def findUserTickerChoices(user_id):
    userCollection = mongoConnection()
    result = userCollection.find_one({"_id": user_id})
    return result


def addUserTickerChoice(data):
    userCollection = mongoConnection()
    userCollection.insert_one(data)


def updateUserTickerChoices(user_id, tickersList):
    userCollection = mongoConnection()
    result = userCollection.update_one({"_id": user_id},
                              {"$set": {"tickers": tickersList}} )


