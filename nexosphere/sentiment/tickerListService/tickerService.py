# GET, POST, UPDATE, DELETE for ticker choices.
from nexosphere.sentiment.tickerListService.tickerRepository import *


def getTickerChoices(userId):

    tickerChoicesList = findUserTickerChoices(userId)
    
    if tickerChoicesList != None:
        return tickerChoicesList['tickers']
    else:
        return {}


def addTickerChoice(user_id, ticker):

    result = findUserTickerChoices(user_id)

    #user not exist
    if result == None:
        newData = {"_id": user_id, "tickers": {"1": ticker}}
        return addUserTickerChoice(newData)
    
    #if user exist
    return {}



def updateTickerChoice(user_id, ticker):
    
    result = findUserTickerChoices(user_id)

    if result != None and len(result["tickers"]) < 5:    
        if ticker not in result['tickers'].values():
            newList = updateTickerList(result["tickers"], ticker)
            return updateUserTickerChoices(result["_id"], newList)
        else:
            return result['tickers']
    
    return {}


def deleteTickerChoice(user_id, ticker):
    result = findUserTickerChoices(user_id)

    if result == None:
        return {}
    else:
        delKey = 0
        oldTickers = result['tickers']
        for item in oldTickers.keys():
            if oldTickers[item] == ticker:
                delKey = int(item)
        
        if delKey != 0:
            del oldTickers[str(delKey)]
            result['tickers'] = reOrderTickerList(result['tickers'], delKey)
        
        return updateUserTickerChoices(user_id, result['tickers'])


def reOrderTickerList(dic, delKey):
    if delKey == len(dic) + 1:
        return dic
    for i in range(delKey, len(dic)+1):
        dic[str(i)] = dic[str(i+1)]
    del dic[str(len(dic))]
    return dic


def updateTickerList(result, ticker):
    counter = 0
    for key in result.keys():
        if counter < int(key):
            counter = int(key)
    result[str(counter+1)] = ticker
    return result


