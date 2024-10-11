import requests
from bs4 import BeautifulSoup
import csv


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
    if not html_content:
        print("No HTML content to parse.")
        return None
    
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Find the table container
    table = soup.find('table', id='example2').tbody
    
    # Find all rows withing the table
    rows = table.find_all('tr')
    
    countries_list = []  # empty list
    
    # Loop through each row to get the corresponding column value
    for row in rows:
        dic = {}  # empty dict
        columns = row.find_all('td')
        
        dic['#'] = columns[0].text
        dic['Country (or dependency)'] = columns[1].text
        dic['Population (2024)'] = columns[2].text.replace(',', '')
        dic['Yearly Change'] = columns[3].text
        dic['Net Change'] = columns[4].text
        dic['Density (P/Km²)'] = columns[5].text.replace(',', '')
        dic['Land Area (Km²)'] = columns[6].text.replace(',', '')
        dic['Migrants (net)'] = columns[7].text.replace(',', '')
        dic['Fert. Rate'] = columns[8].text
        dic['Med. Age'] = columns[9].text
        dic['Urban Pop %'] = columns[10].text
        dic['World Share'] = columns[11].text
        
        countries_list.append(dic)  # Append dictionary to the list
    
    return countries_list  # Return the list of dictionaries


def save_to_csv(data):
    with open('data.csv', 'w', encoding='utf-8') as f:
        # Define the desired fieldnames for the CSV file
        fieldnames = ['#', 'Country (or dependency)', 'Population (2024)', 'Yearly Change', 'Net Change',
                      'Density (P/Km²)', 'Land Area (Km²)', 'Migrants (net)', 'Fert. Rate', 'Med. Age', 'Urban Pop %',
                      'World Share']
        
        # Create the CSV DictWriter object
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write the header row
        csv_writer.writeheader()
        
        # Write each row to the CSV file
        csv_writer.writerows(data)


if __name__ == '__main__':
    page_url = "https://www.worldometers.info/world-population/population-by-country/"
    
    html = fetch_page_content(page_url)
    
    population_data = parse_page_content(html)
    
    save_to_csv(population_data)
