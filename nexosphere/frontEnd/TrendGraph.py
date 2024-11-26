import matplotlib.pyplot as plt
import pandas as pd


def formatSentimentData(sentimentData):
    response = []
    for key in sentimentData.keys():
        for item in sentimentData[key]:
            a={"timestamp": item["date"], "label": item["sentiment"]["label"], "score": round(item["sentiment"]["score"],2)}
            response.append(a)
    response = pd.DataFrame(response)
    response['timestamp'] = pd.to_datetime(response['timestamp'])
    
    return response


def formatStockPriceData(stockData):
    priceSeriesData = pd.DataFrame(stockData["data"])
    priceSeriesData = priceSeriesData.reset_index()
    priceSeriesData['timestamp'] = pd.to_datetime(priceSeriesData['timestamp'])

    return priceSeriesData


def plotGraph(stockData, sentimentData):
    
    priceSeriesData = formatStockPriceData(stockData)
    sentimentSeriesData = formatSentimentData(sentimentData)

    #modified x values
    x_values = priceSeriesData["index"]
    
    # Create the figure and axis for subplots
    fig, ax1 = plt.subplots(figsize=(10, 6), nrows=2)

    # Adjust layout for more space between subplots
    plt.subplots_adjust(hspace=1)


    fig.patch.set_facecolor('black')
    ax1[0].set_facecolor('black')
    ax1[1].set_facecolor('black')

    # Top plot: Stock Price Trend Line
    ax1[0].plot(x_values, priceSeriesData['open'], color='#ff13f0', label="Price in $(CAD)", linewidth=2)
    ax1[0].set_xticklabels(priceSeriesData['timestamp'])
    ax1[0].set_ylabel('Stock Price in $CAD', fontsize=12, color='white') 
    ax1[0].tick_params(axis='y', labelcolor='white') 
    # Top plot title
    ax1[0].set_title('Stock Price Trend', fontsize=14, color='white')


    ax1[1].set_title('Sentiment Analysis Trend', fontsize=14, color='white')
    bar_colors = [
        '#FF3131' if sentiment == "negative" else 
        '#0000FF' if sentiment == "neutral" else 
        '#39FF14' 
        for sentiment in sentimentSeriesData["label"]]

    ax1[1].bar(sentimentSeriesData["timestamp"], sentimentSeriesData["score"], color=bar_colors, alpha=0.6, width=0.4, label="Sentiment")
    ax1[1].set_ylabel('Sentiment Score', fontsize=12, color='white')  # Y-axis label in white
    ax1[1].tick_params(axis='y', labelcolor='white')  # Y-ticks in white

    # Set the limits for sentiment score to range between -1 and 1
    ax1[1].set_ylim(-1.2, 1.2)  # Slightly extend the range for better visibility

    # Customize grid (subtle grid lines in gray)
    ax1[0].grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax1[1].grid(True, color='gray', linestyle='--', linewidth=0.5)

    # Customize ticks color to white for visibility
    ax1[0].tick_params(axis='x', colors='white')  
    ax1[1].tick_params(axis='x', colors='white')  

    ax1[0].legend(facecolor='black', edgecolor='white', labelcolor='white')
    ax1[1].legend(facecolor='black', edgecolor='white', labelcolor='white')


    plt.tight_layout()
    return plt

