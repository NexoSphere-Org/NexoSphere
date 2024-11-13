import json
from sourceCode.stockpriceControllers.stockPriceYf import stockPrice
from stockpriceControllers.mongoDBConfig import mongoConnection

def generateDayStockOpeningTrend(ticker, daySpan):
    dayString = str(daySpan)
    return stockPrice(ticker, dayString)["Open"]

def generateFiveDayStockClosingTrend(ticker, daySpan):
    dayString = str(daySpan)
    return stockPrice(ticker, dayString)["Close"]


def generateFiveDayStockVolumeTrend(ticker, daySpan):
    dayString = str(daySpan)
    return stockPrice(ticker, dayString)["Volume"]


def storeDataMongoDB(data):
    collection = mongoConnection()
    collection.insert_one(data)
    return

# print(generateFiveDayStockClosingTrend("DOL.TO"))
# print(generateFiveDayStockVolumeTrend("DOL.TO"))