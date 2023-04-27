import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \ '
														'Chrome/112.0.0.0 Safari/537.36'
}

def scrape(url):
				"""Scrape the page source from the URL"""
				response = requests.get(url, headers=HEADERS)
				source = response.text
				return source

if __name__ == "__main__":
				print(scrape(URL))