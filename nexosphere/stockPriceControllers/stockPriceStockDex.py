from stockdex import Ticker
from datetime import datetime

def getStockPriceFromStockDexAPI(tickerId, range='1d', granularity='15m'):

    tickerInfo = Ticker(ticker=tickerId)    
    try:
        price = tickerInfo.yahoo_api_price(range=range, dataGranularity=granularity)
    
    except:
        return {"error": "not found data"}
    
    else:
        result = price.to_dict(orient='records', index=True)
        result = processRawData(result, tickerId)

        return result


def processRawData(data, ticker):
    for entry in data:
        entry['timestamp'] =  entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        del entry['exchangeName'], entry['instrumentType'], entry['volume'], entry['timezone'], entry['exchangeTimezoneName']
        del entry['currency'], entry['low'], entry['high'], entry['close']
        entry['open'] = round(entry['open'], 2)
    result = {"ticker": ticker, "timeStamp": datetime.now(),"data": data}
    return result
