#!/usr/bin/env python3
# source - https://quantiux.com/blog/scraping-with-requests-html/
from requests_html import HTMLSession
from datetime import datetime
from pprint import pprint

class GetWorldData:
    def __init__(self, file, url) -> None:
        self.file = file
        self.url = url

    def saveData(self, names, counts) -> None:
        if not names or not counts:
            print("No data to add!")
            return

        for name, count in zip(names, counts):
            count_text = count.text.replace(",", "").strip()
            name_text = name.text.replace(",", "").strip()
            self.file.write(f"{name_text},{count_text}\n")
            print(f"{name_text},{count_text}")

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Data saved to {time_now}.")


    def run(self) -> None:
        session = HTMLSession()
        page = session.get(self.url)
        page.raise_for_status()

        try:
            page.html.render(timeout=30)
        except Exception as e:
            print(f"Error while parsing the page: {e}")
            return

        counts = page.html.find('.counter-number')
        names = page.html.find('span.counter-item')

        if not counts or not names:
            print("Unable to pick the data!")
            return
        self.saveData(names, counts)

def main() -> None:
    url = "https://www.worldometers.info/ru"
    with open("world_data.csv", "w", encoding="utf8") as file:
        world_data = GetWorldData(file, url)
        world_data.run()

if __name__ == "__main__":
    main()
