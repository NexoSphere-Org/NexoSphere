import requests
from bs4 import BeautifulSoup
import json


def getNewsScrapper(url):
    # Send a GET request to fetch the page content
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')  # You can also use 'lxml' for faster parsing

        # Find the main body of the content (you'll need to adjust the selector based on the site)
        # main_content = soup.find('div', class_='article-body')
        # # Extract all text from the page
        # main_content = soup.get_text(separator='\n', strip=True)  # Separator adds line breaks for readability
        
        # Find all <p> tags with a class that starts with 'yf-'
        paragraphs = soup.find_all('p', class_=lambda class_name: class_name and class_name.startswith('yf-'))

        text = ""
        # Extract and print the text from each paragraph
        for p in paragraphs:
            text = text + (p.get_text(strip=True))

        return text
        # return {"content": main_content}
        # if main_content:
        #     # Extract the text or all paragraphs inside the main content
        #     paragraphs = main_content.find_all('p')  # Get all <p> tags (paragraphs)

        #     # Print or save the extracted text
        #     article_text = "\n".join([para.get_text(strip=True) for para in paragraphs])
        #     return article_text
        # else:
        #     return "Main content not found."
    # else:
    #     return {"content": ""}

text = {"text": getNewsScrapper("https://finance.yahoo.com/news/apple-launch-smart-home-camera-190404945.html")}

with open('responseScrappedText.json', 'w') as json_file:
    json.dump(text, json_file, indent=4)