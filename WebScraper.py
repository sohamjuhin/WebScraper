import requests
from bs4 import BeautifulSoup

# Function to scrape a website
def website_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extracting all the links from the website
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # Example: Extracting all the text from the website
    text = soup.get_text()
    print(text)

# Usage example
target_url = "http://example.com"  # Replace with the URL of the website you want to scrape
website_scraper(target_url)
