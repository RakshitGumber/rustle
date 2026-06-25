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


if __name__ == "__main__":
    with open("rss.xml", "w", encoding="utf-8") as file:
        for feed in fetch_part():
            file.write(feed.text)
