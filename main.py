import requests
from bs4 import BeautifulSoup

page_url = "https://www.worldometers.info/world-population/population-by-country/"


def fetch_page_content(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    
    page = requests.get(url, headers=headers, timeout=5)
    if page.status_code == 200:
        return page.content

    else:
        print("An error occurred !!")
        
fetch_page_content(page_url)


