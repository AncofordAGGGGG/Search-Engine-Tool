import time
from typing import List, Dict

import requests
from bs4 import BeautifulSoup


BASE_URL = "http://quotes.toscrape.com"
REQUEST_DELAY = 6


def fetch_page(url: str) -> str:
    """
    Send a GET request to the given URL and return the HTML text.
    A 6-second delay is added after each request to follow coursework rules.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    time.sleep(REQUEST_DELAY)
    return response.text


def parse_quotes_page(html: str, page_url: str) -> List[Dict]:
    """
    Parse one quotes page and extract quote text, author, tags, and source URL.
    """
    soup = BeautifulSoup(html, "html.parser")
    results = []

    quote_blocks = soup.find_all("div", class_="quote")
    for block in quote_blocks:
        text_tag = block.find("span", class_="text")
        author_tag = block.find("small", class_="author")
        tag_elements = block.find_all("a", class_="tag")

        quote_data = {
            "text": text_tag.get_text(strip=True) if text_tag else "",
            "author": author_tag.get_text(strip=True) if author_tag else "",
            "tags": [tag.get_text(strip=True) for tag in tag_elements],
            "page_url": page_url,
        }
        results.append(quote_data)

    return results


def crawl_quotes(max_pages: int = 10) -> List[Dict]:
    """
    Crawl quote pages from quotes.toscrape.com up to max_pages.
    Stops early if there is no next page.
    """
    all_quotes = []
    current_url = BASE_URL
    pages_visited = 0

    while current_url and pages_visited < max_pages:
        html = fetch_page(current_url)
        page_quotes = parse_quotes_page(html, current_url)
        all_quotes.extend(page_quotes)

        soup = BeautifulSoup(html, "html.parser")
        next_button = soup.find("li", class_="next")

        if next_button and next_button.find("a"):
            next_href = next_button.find("a").get("href")
            current_url = BASE_URL + next_href
        else:
            current_url = None

        pages_visited += 1

    return all_quotes
