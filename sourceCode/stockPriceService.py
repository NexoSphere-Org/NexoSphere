import json
from YfAPICalls.stockPriceYf import stockPrice

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
    # store the data in DB
    return

# print(generateFiveDayStockClosingTrend("DOL.TO"))
# print(generateFiveDayStockVolumeTrend("DOL.TO"))