import requests
from bs4 import BeautifulSoup


def fetch_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    try:
        page = requests.get(url, headers=headers, timeout=5)
        page.raise_for_status()
        return page.content  # Return HTML content if no error occurs
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.ConnectionError as connect_err:
        print(f"Connection error occurred. {connect_err}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    
    return None


def parse_page_content(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Find the table container
    table = soup.find('table', id='example2').tbody
    
    # Find all rows withing the table
    rows = table.find_all('tr')
    
    countries_list = []  # empty list
    
    # Loop through each row to get the corresponding column value
    for row in rows:
        dic = {}  # empty dict
        
        dic['Sort'] = row.find_all('td')[0].text
        dic['Country'] = row.find_all('td')[1].text
        dic['Population (2024)'] = row.find_all('td')[2].text.replace(',', '')
        dic['Yearly Change'] = row.find_all('td')[3].text
        dic['Net Change'] = row.find_all('td')[4].text
        dic['Density (P/Km2)'] = row.find_all('td')[5].text.replace(',', '')
        dic['Land Area (Km2)'] = row.find_all('td')[6].text.replace(',', '')
        dic['Migrants (net)'] = row.find_all('td')[7].text.replace(',', '')
        dic['Fert. Rate'] = row.find_all('td')[8].text
        dic['Mid. Age'] = row.find_all('td')[9].text
        dic['Urban Pop'] = row.find_all('td')[10].text
        dic['World Share'] = row.find_all('td')[11].text
        
        countries_list.append(dic)   # Append dictionary to the list
    
    return countries_list            # Return the list of dictionaries


if __name__ == '__main__':
    page_url = "https://www.worldometers.info/world-population/population-by-country/"
    
    html = fetch_page_content(page_url)
    
    parse_page_content(html)
