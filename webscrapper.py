import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Function to scrape news headlines from cointelegraph for Bitcoin and Blockchain sections
def scrape_news_cointelegraph(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headlines specifically for the Bitcoin and Blockchain sections
        headlines = soup.find_all('span', class_='post-card-inline__title')
        headlines_text = [headline.text.strip() for headline in headlines]
        return headlines_text
    else:
        print(f"Failed to fetch {url}")
        return []

# Function to scrape news headlines from blockchaintechnology-news for Altcoins and Ethereum
def scrape_news_blockchain_tech(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headlines using h3 a tags
        headlines = soup.find_all('h3')
        headlines_text = [headline.a.text.strip() for headline in headlines if headline.a]
        return headlines_text
    else:
        print(f"Failed to fetch {url}")
        return []

# Function to scrape news headlines from coindesk
def scrape_news_coindesk(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract headlines using h2 and h3 tags
        headlines_h2 = soup.find_all('h2')
        headlines_h3 = soup.find_all('h3')

        # Extract text from h2 and h3 headlines
        headlines_text_h2 = [headline.text.strip() for headline in headlines_h2]
        headlines_text_h3 = [headline.text.strip() for headline in headlines_h3]

        # Combine both sets of headlines
        headlines_text = headlines_text_h2 + headlines_text_h3

        return headlines_text
    else:
        print(f"Failed to fetch {url}")
        return []

# File path to store headlines
file_path = r"C:\Users\trupt\Documents\crypto_news_headlines.xlsx"

# URLs for different sources
bitcoin_url = 'https://cointelegraph.com/tags/bitcoin/'
blockchain_url = 'https://cointelegraph.com/tags/blockchain/'
altcoins_url = 'https://www.blockchaintechnology-news.com/categories/cryptocurrency/altcoins/'
ethereum_url = 'https://www.blockchaintechnology-news.com/categories/cryptocurrency/ethereum/'
coindesk_url = 'https://www.coindesk.com/'

# Scrape headlines from different sources
bitcoin_headlines = scrape_news_cointelegraph(bitcoin_url)
blockchain_headlines = scrape_news_cointelegraph(blockchain_url)
altcoins_headlines = scrape_news_blockchain_tech(altcoins_url)
ethereum_headlines = scrape_news_blockchain_tech(ethereum_url)
coindesk_headlines = scrape_news_coindesk(coindesk_url)

# Combine all headlines and save to Excel file
if all([bitcoin_headlines, blockchain_headlines, altcoins_headlines, ethereum_headlines, coindesk_headlines]):
    combined_headlines = bitcoin_headlines + blockchain_headlines + altcoins_headlines + ethereum_headlines + coindesk_headlines
    df = pd.DataFrame({'All Headlines': combined_headlines})
    
    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        existing_data = existing_data.append(df)
        existing_data.to_excel(file_path, index=False)
        print(f"All headlines appended to", file_path)
    else:
        df.to_excel(file_path, index=False)
        print(f"All headlines saved to a new file:", file_path)
else:
    print(f"Failed to scrape headlines from one or more URLs.")
