import streamlit as st
import requests
from datetime import datetime
from TrendGraph import plotGraph
import os

# Retrieve environment variables
BASE_URL = os.getenv("BASE_URL")

# Function to fetch ticker options from the backend
def fetch_ticker_options(user_id):
    url = f"{BASE_URL}/user/getTickers"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return ["" ] + list(response.json().values())  # First item is empty for "no selection"
    else:
        st.error("Failed to fetch ticker options.")
        return []

# Function to fetch stock price data from the backend
def fetch_stock_price_data(ticker_symbol, start_date, end_date):
    url = f"{BASE_URL}/stockPrice/{ticker_symbol}"
    params = {"start_date": start_date, "end_date": end_date}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch stock price data for {ticker_symbol}.")
        return {}

# Function to fetch sentiment analysis data from the backend
def fetch_sentiment_data(ticker_symbol, start_date, end_date):
    url = f"{BASE_URL}/get-news"
    params = {"ticker_symbol": ticker_symbol, "date_start": start_date, "date_end": end_date}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch sentiment data for {ticker_symbol}.")
        return {}

# Function to handle user input for dates
def get_date_inputs():
    start_date = st.date_input('Select Start Date', max_value=datetime.today())
    end_date = st.date_input('Select End Date', max_value=datetime.today())
    
    return start_date, end_date

# Function to handle the main functionality for generating the trend analysis
def generate_trend_analysis(selected_option, start_date, end_date):
    # Fetch stock price and sentiment data
    stock_price_data = fetch_stock_price_data(selected_option, start_date, end_date)
    sentiment_data = fetch_sentiment_data(selected_option, start_date, end_date)
    
    if "data" in stock_price_data and len(sentiment_data) > 0:
        # Generate the plot
        plot = plotGraph(stock_price_data, sentiment_data)
        
        # Display the plot
        try:
            st.pyplot(plot)
        except Exception as e:
            st.error(f"Error displaying plot: {str(e)}")
    else:
        st.error(f"Error fetching data for ticker: {selected_option}")

# Main Streamlit app layout
def main():
    # Title of the app
    st.markdown("<div style='text-align: center;'><h1>Stock Price Trend with Sentiment Analysis</h1></div>", unsafe_allow_html=True)

    # Fetch ticker options
    options = fetch_ticker_options(user_id=12347)
    
    # Allow the user to select a ticker
    selected_option = st.selectbox('Choose Ticker:', options)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Get start and end date inputs
    start_date, end_date = get_date_inputs()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Trigger the analysis when the button is clicked
    if selected_option != "" and st.button('Generate Trend Analysis') and start_date and end_date:
        # Secondary title
        st.markdown("<div style='text-align: center;'><h2>Stock Price Trend with Sentiment Analysis</h2></div>", unsafe_allow_html=True)
        
        # Add another gap
        st.markdown("<br><br>", unsafe_allow_html=True)

        # Generate the trend analysis
        generate_trend_analysis(selected_option, start_date, end_date)

# Run the app
if __name__ == "__main__":
    main()
