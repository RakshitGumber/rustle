import requests

sources = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://openai.com/news/rss.xml",
    "https://techcrunch.com/feed/",
    "https://hnrss.org/frontpage",
]


def fetch_part():
    for url in sources:
        response = requests.get(url)

        if response.status_code == 200:
            yield response
        else:
            print(f"Failed: {url}")


if __name__ == "__main__":
    for feed in fetch_part():
        print(feed.text)
