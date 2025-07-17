#!/usr/bin/env python3
import json
from time import time
from requests_html import HTMLSession
from datetime import datetime


url = "https://www.worldometers.info/ar"
file_path = "world_data.json"



def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


def saveData(names, counts, file_path) -> None:
    if not names or not counts:
        print("No data to write!")
        return

    data = {}
    for name, count in zip(names, counts):
        count_text = count.text.replace(",", "").strip()
        name_text = name.text.replace(",", "").strip()
        data[name_text] = count_text

    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Data was saved to JSON-file at {time_now}.")


@timer_func
def run() -> None:
    session = HTMLSession()
    page = session.get(url)
    page.raise_for_status()

    try:
        page.html.render(timeout=20)  # увеличенный таймаут рендеринга
    except Exception as e:
        print(f"Error while parsing the page: {e}")
        return

    counts = page.html.find('.counter-number')
    names = page.html.find('span.counter-item-double, span.counter-item')

    if not counts or not names:
        print("Cannot pick data!")
        return
    saveData(names, counts, file_path)

run()
