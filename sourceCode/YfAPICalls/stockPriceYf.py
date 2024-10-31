import json
import yfinance as yf

def stockPrice(ticker, daySpan):
    # Fetch stock data
    stock = yf.Ticker(ticker)
    daySpan = daySpan+"d"
    
    # Get historical market data
    data = stock.history(period=daySpan).to_json()
    
    return json.loads(data)

if __name__ == "__main__":
    print(stockPrice('CM.TO', "5"))