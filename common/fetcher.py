import requests


class Fetcher:

    @staticmethod
    def fetch_page(url):
        while True:
            f = requests.get(url)
            if f.status_code < 500:
                break
        return f
