from mongoDBConfig import mongoTickerNewsConnection

class newsRepository:
    def __init__(self, collectionName):
        self.database = mongoTickerNewsConnection()
        self.collectionName = collectionName

    def findData(self, id):
        newsCollection = self.database[self.collectionName]
        result = newsCollection.find_one({"_id":id})
        return result


    def addData(self, data):
        newsCollection = self.database[self.collectionName]
        newsCollection.insert_one(data)


    def deleteData(self, id):
        newsCollection = self.database[self.collectionName]
        newsCollection.delete_one({"_id": id})


