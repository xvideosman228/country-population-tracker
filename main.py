import requests
from bs4 import BeautifulSoup

page_url = "https://www.worldometers.info/world-population/population-by-country/"


def fetch_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    try:
        page = requests.get(url, headers=headers, timeout=5)
        page.raise_for_status()
        return page.content         # Return HTML content if no error occurs
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.ConnectionError as connect_err:
        print(f"Connection error occurred. {connect_err}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    
    return None


fetch_page_content(page_url)
