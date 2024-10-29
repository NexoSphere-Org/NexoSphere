from stockdex import Ticker
import json

ticker = Ticker(ticker="AAPL")

# Price data (use range and dataGranularity to make range and granularity more specific)
price = ticker.yahoo_api_price(range='1d', dataGranularity='1m')
print(price)

def save_to_json_file(data, output_file):
    try:
        # Write the fetched data to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {output_file}")
    except IOError as io_err:
        print(f"File I/O error occurred: {io_err}")

with open('stockdex.json', 'w') as f:
    json_list = price.to_json(orient="index", indent=4)
    f.write(json_list)
