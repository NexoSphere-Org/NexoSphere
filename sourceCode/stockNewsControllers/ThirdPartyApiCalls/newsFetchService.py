from newsYfHelper import stockMarketNews
from sourceCode.tickerListService.tickerService import getTickerChoices
from scrapperHelper import getNewsScrapper

def getUserNewsFromTickers(userId):
    #get tickerList
    tickerList = getTickerChoices(userId)
    newList = {}
    
    #store as dic
    for ticker in tickerList:
        newList[ticker] = stockMarketNews(ticker)
    
    return newList

def getNewsContent(url):
    return getNewsScrapper(url)

def getNewsSummary(text):
    return getSummaryFromText(text)

def getSentimentResultsFromSummary(summarizedText):
    return getSentimentAnalysis(summarizedText)

#dummy functions for now
def getSummaryFromText(text):
    return {}

#dummy functions for now
def getSentimentAnalysis(summarizedText):
    return {}