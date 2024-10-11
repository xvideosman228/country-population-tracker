# 🌍 Population Data Scraper
## 📖 Description
A robust Python web scraper that collects current population data from worldometers.info for all countries worldwide. The program extracts comprehensive demographic information including population, growth rates, density, and more, saving it in a structured CSV format for easy data analysis.

## ✨ Features
- Real-time population data scraping
- Comprehensive demographic metrics including:
  - Population counts
  - Yearly change rates
  - Population density
  - Land area
  - Migration data
  - Fertility rates
  - Median age
  - Urbanization rates
  - World population share
- Robust error handling
- Clean CSV output format
- User-agent handling for reliable scraping

## 🚀 How to Use
1. **Set up your environment**:  
   Make sure you have Python installed on your system.

2. **Install dependencies**:  
   Run the following command to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scraper**:  
   Execute the script:
   ```bash
   python main.py
   ```
   The script will automatically:
   - Fetch the latest population data
   - Process the information
   - Generate a CSV file (data.csv)


## 📊 Example Output

### CSV File (data.csv)
| # | Country (or dependency) | Population (2024) | Yearly Change | Net Change | Density (P/Km²) | Land Area (Km²) | Migrants (net) | Fert. Rate | Med. Age | Urban Pop % | World Share |
|---|-----------------------|------------------|---------------|------------|-----------------|----------------|---------------|-------------|-----------|-------------|-------------|
| 1 | India | 1450935791 | 0.89% | 12,866,195 | 488 | 2973190 | -630830 | 2.0 | 28 | 37% | 17.78% |
| 2 | China | 1419321278 | -0.23% | -3,263,655 | 151 | 9388211 | -318992 | 1.0 | 40 | 66% | 17.39% |
| 3 | United States | 345426571 | 0.57% | 1,949,236 | 38 | 9147420 | 1286132 | 1.6 | 38 | 82% | 4.23% |
| 4 | Indonesia | 283487931 | 0.82% | 2,297,864 | 156 | 1811570 | -38469 | 2.1 | 30 | 59% | 3.47% |
| 5 | Pakistan | 251269164 | 1.52% | 3,764,669 | 326 | 770880 | -1401173 | 3.5 | 20 | 34% | 3.08% |

## 💻 Code Highlights
### Error Handling
```python
def fetch_page_content(url):
    """Fetch the HTML content of a given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
    }
    try:
        page = requests.get(url, headers=headers, timeout=5)
        page.raise_for_status()
        return page.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    # ... more error handling
```

## 🛠️ Potential Enhancements
- Add command-line arguments for custom output file names
- Implement data comparison with historical records
- Add data visualization capabilities
- Create a simple web interface using Flask
- Add automated scheduling for regular data updates
- Implement data validation and cleaning
- Add support for different output formats (JSON, Excel)
- Include data visualization exports

## 👨‍💻 Author
Khaled Soudy

## 🧱 Project Structure
```
population-scraper/
├── main.py          # Main script with scraping logic
├── requirements.txt # Project dependencies
├── .gitignore      # Git ignore file
└── README.md       # Project documentation
```

## 📦 Dependencies
The project relies on the following Python packages:
- beautifulsoup4==4.12.3
- requests==2.32.3
- lxml==5.3.0
- And other supporting packages listed in `requirements.txt`

## ⚠️ Disclaimer
Please ensure you follow worldometers.info's robots.txt and terms of service when using this scraper. Be respectful of the website's resources and implement appropriate delays between requests if needed.

## 📞 Support
If you encounter any issues or have questions, please open an issue in the GitHub repository.

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

## 📄 License
This project is open source and available under the MIT License.

---
Stay informed about global population statistics! 🌍📊