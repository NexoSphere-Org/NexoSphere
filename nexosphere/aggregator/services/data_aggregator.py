# TODO: Implement a more sophisticated aggregation algorithm

from typing import List, Dict, Any
import pandas as pd
# from stockdex import StockDex
# from polygon import RESTClient
# from alpha_vantage.timeseries import TimeSeries

def aggregate_data_naively(data_sources: List[Any], source_names: List[str]) -> Dict[str, Any]:
    """
    Aggregates data from multiple sources into a dictionary using provided source names as keys.

    Args:
        data_sources (List[Any]): A list of data sources to be aggregated.
        source_names (List[str]): A list of names corresponding to each data source.

    Returns:
        Dict[str, Any]: A dictionary where keys are source names and values are the corresponding data sources.
    """

    aggregated_data = {}
    for source, name in zip(data_sources, source_names):
        aggregated_data[name] = source
    return aggregated_data

def aggregate_data_normalized(data_sources: List[Dict[str, Any]], source_names: List[str]) -> Dict[str, Any]:
    """
    Aggregates normalized data from multiple sources into a dictionary using provided source names as keys.

    Args:
        data_sources (List[Dict[str, Any]]): A list of dictionaries containing normalized data to be aggregated.
        source_names (List[str]): A list of names corresponding to each data source.

    Returns:
        Dict[str, Any]: A dictionary where keys are source names and values are the corresponding normalized data sources.
    """

    aggregated_data = {}
    for source, name in zip(data_sources, source_names):
        aggregated_data[name] = source
    return aggregated_data

def normalize_alpha_vantage(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalizes data from the Alpha Vantage API into a dictionary.

    Args:
        data (Dict[str, Any]): A dictionary containing the JSON response from the Alpha Vantage API.

    Returns:
        Dict[str, Any]: A dictionary containing normalized data from the Alpha Vantage API.
    """

    normalized_data = {}
    if "Time Series (1min)" in data:
        normalized_data["open"] = [float(data["Time Series (1min)"][key]["1. open"]) for key in data["Time Series (1min)"]]
        normalized_data["high"] = [float(data["Time Series (1min)"][key]["2. high"]) for key in data["Time Series (1min)"]]
        normalized_data["low"] = [float(data["Time Series (1min)"][key]["3. low"]) for key in data["Time Series (1min)"]]
        normalized_data["close"] = [float(data["Time Series (1min)"][key]["4. close"]) for key in data["Time Series (1min)"]]
        normalized_data["volume"] = [float(data["Time Series (1min)"][key]["5. volume"]) for key in data["Time Series (1min)"]]
    return normalized_data

def normalize_polygon(data: Dict[str, Any]) -> Dict[str, Any]:
    normalized_data = {
        data["t"]: {
            "open": data["o"],
            "high": data["h"],
            "low": data["l"],
            "close": data["c"],
            "volume": data["v"],
            "time": data["t"],
            "volume_weighted": data.get("vw")
        }
    }
    return normalized_data

def normalize_yahoo_finance(data: Dict[str, Any]) -> Dict[str, Any]:
    timestamps = data["timestamp"]
    quotes = data["indicators"]["quote"][0]
    normalized_data = {}
    for i, timestamp in enumerate(timestamps):
        normalized_data[timestamp] = {
            "open": quotes["open"][i],
            "high": quotes["high"][i],
            "low": quotes["low"][i],
            "close": quotes["close"][i],
            "volume": quotes["volume"][i],
            "time": timestamp,
            "volume_weighted": None  # Yahoo Finance does not provide volume weighted data
        }
    return normalized_data