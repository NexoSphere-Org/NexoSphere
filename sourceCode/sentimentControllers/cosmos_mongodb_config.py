import pymongo

CONNECTION_STRING = "mongodb://coen6313-zihan-cosmos-account:bTl7V4yrgnEbxYEIiOSA73bdVxToegWNbQ6iOcnyvmP6zdRevnVnUjZcdG2RBgtXkDq6owSrF0ulACDbWtrsjQ==@coen6313-zihan-cosmos-account.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@coen6313-zihan-cosmos-account@"
DATABASE_NAME = "coen6313-db"

client = None


def get_cosmos_mongodb():
    global client
    global db
    if client is None:
        client = pymongo.MongoClient(CONNECTION_STRING)
        db = client[DATABASE_NAME]

    return client, db
