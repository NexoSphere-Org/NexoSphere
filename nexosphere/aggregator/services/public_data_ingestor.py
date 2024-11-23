"""
Module: ingest_public_api_data

This module provides functions to ingest financial market data from multiple 
public APIs. It includes functions to fetch historical stock data from Yahoo 
Finance, real-time stock data from Finnhub, and intraday time series data from 
Alpha Vantage. Each function handles the HTTP requests to the respective API 
and returns the data in JSON format if the request is successful.

Functions:
    - fetch_yahoo_finance_data(ticker): Fetches historical stock data for a 
      given ticker symbol from Yahoo Finance.
    - fetch_finnhub_data(ticker, api_key): Fetches stock data from the Finnhub 
      API for a given ticker symbol.
    - fetch_alpha_vantage_data(ticker, api_key): Fetches intraday time series 
      data for a given stock ticker from the Alpha Vantage API.
"""
import requests

def fetch_yahoo_finance_data(ticker):
    """
    Fetches historical stock data for a given ticker symbol from Yahoo Finance.
    Args:
        ticker (str): The ticker symbol of the stock to fetch data for.
    Returns:
        dict: A dictionary containing the JSON response from Yahoo Finance if 
        the request is successful.
        None: If the request fails, returns None.
    Raises:
        None: This function does not raise any exceptions but prints an error 
        message if the request fails.
    Example:
        >>> data = fetch_yahoo_finance_data("AAPL")
        >>> if data:
        >>>     print(data)
    """

    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"+
            "?interval=1m&range=1d")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()

    print(f"Error fetching Yahoo Finance data: {response.status_code}")
    return None

def fetch_finnhub_data(ticker, api_key):
    """
    Fetches stock data from the Finnhub API for a given ticker symbol.
    Args:
        ticker (str): The stock ticker symbol to fetch data for.
        api_key (str): The API key to authenticate the request.
    Returns:
        dict: A dictionary containing the stock data if the request is 
        successful.
        None: If the request fails, returns None and prints an error message.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the 
        HTTP request.
    Example:
        >>> data = fetch_finnhub_data("AAPL", "your_api_key")
        >>> if data:
        >>>     print(data)
    """

    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()

    print(f"Error fetching Finnhub data: {response.status_code}")
    return None

def fetch_alpha_vantage_data(ticker, api_key):
    """
    Fetches intraday time series data for a given stock ticker from the Alpha 
    Vantage API.
    Args:
        ticker (str): The stock ticker symbol to fetch data for.
        api_key (str): The API key for authenticating with the Alpha Vantage 
        API.
    Returns:
        dict: A dictionary containing the JSON response from the Alpha Vantage 
        API if the request is successful.
        None: If the request fails, returns None.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the 
        HTTP request.
    Example:
        >>> data = fetch_alpha_vantage_data("AAPL", "your_api_key")
        >>> if data:
        >>>    print(data)
    """

    url = ("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&"+
           f"symbol={ticker}&interval=1min&apikey={api_key}")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()

    print(f"Error fetching Alpha Vantage data: {response.status_code}")
    return None
