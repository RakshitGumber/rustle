import json

import feedparser
import requests

sources = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://openai.com/news/rss.xml",
    "https://techcrunch.com/feed/",
    "https://hnrss.org/frontpage",
]

headers = {"User-Agent": "Rustle/1.0"}


def fetch_part():
    for url in sources:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            yield response

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            continue


def extract_data(txt):
    feed = feedparser.parse(txt)

    clean_data = {
        "title": feed.feed.get("title", ""),
        "link": feed.feed.get("link", ""),
        "description": feed.feed.get("description", ""),
        "updated": feed.feed.get("updated", ""),
        "items": [],
    }

    for entry in feed.entries:
        clean_item = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "description": entry.get("description", ""),
            "published": entry.get("published", ""),
            "id": entry.get("id", ""),
            "author": entry.get("author", ""),
        }
        clean_data["items"].append(clean_item)

    return json.dumps(clean_data, indent=4)


if __name__ == "__main__":
    with open("rss.json", "w", encoding="utf-8") as file:
        for feed in fetch_part():
            file.write(extract_data(feed.text))
