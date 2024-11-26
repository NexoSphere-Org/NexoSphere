from stockPriceControllers.stockPriceRepository import *
from stockPriceControllers.stockPriceStockDex import getStockPriceFromStockDexAPI

from datetime import datetime, timedelta
import threading


#function to delete old entry and store currently fetched data
def dataHygieneFunction(oldEntryId, newData):
    deleteStockDataFromDB(oldEntryId)
    addStockDataToDB(newData)

#get stocks
def getStockPrice(ticker, start_date, end_date):
    #first get from DB
    data = getStockDataFromDB(ticker)
    # print("db data fetched, first check")

    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    range = (end_date - start_date).days if (end_date - start_date).days > 0 else 1
    
    if data != None and start_date != None and end_date != None:
        

        #if older than 15 min, discard, and fetch again.
        if data["timeStamp"] < (datetime.now() - timedelta(minutes=15)):
            #fetch new data
            newData = getStockPriceFromStockDexAPI(ticker, range=f"{range}d")

            #error
            if newData != {"error": "not found data"}:
                # print("appi returned data")
                threading.Thread(target=dataHygieneFunction, args=(data["_id"], newData)).start()
                return newData
            else:
                return {}
        
        else:    
            #if fresh data, return it.
            # print("returned db data")
            del data["_id"]
            return data
    
    #data not found fetching data
    newData = getStockPriceFromStockDexAPI(ticker, range)
    if newData != {"error": "not found data"}:
        #store in DB
        threading.Thread(target=addStockDataToDB, args=(newData,)).start()
        # print("returning fresh API data")
        return newData
    else:
        return {}

