import requests
import json

# URL for the Yahoo Finance AAPL summary page

ticker = "AAPL"
sample_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1m&range=1d"
OUTPUT_FILE = "data/raw_data_output.json"

def save_to_json_file(data, output_file):
    try:
        # Write the fetched data to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {output_file}")
    except IOError as io_err:
        print(f"File I/O error occurred: {io_err}")

def get_ticker_data(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        # Check if request was successful
        if response.status_code == 200:
            # Attempt to parse JSON response
            data = response.json()
            return data
        else:
            # Print status code and response text for debugging
            print(f"Error: Received status code {response.status_code}")
            print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    except ValueError as e:
        print("Failed to parse JSON:", e)

def main():
    # Fetch the Nobel Prize data
    print("Fetching Nobel Prize data...")
    data = get_ticker_data(sample_url)
    
    if data:
        # If data is successfully fetched, save it to a file
        save_to_json_file(data, OUTPUT_FILE)
    else:
        print("Failed to fetch Nobel Prize data.")

if __name__ == "__main__":
    main()