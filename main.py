import requests
import selectorlib

# URL to scrape
URL = "https://programmer100.pythonanywhere.com/tours/"

# Headers to use for HTTP request
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \ '
														'Chrome/112.0.0.0 Safari/537.36'
}

def scrape(url):
				"""Scrape the page source from the URL

				Input Arguments: url (str): URL to be scraped
				Returns: str: HTML source page
				"""
				response = requests.get(url, headers=HEADERS)
				source = response.text
				return source

def extract(source):
				"""Extract structured data from the page source using a YAML file

				Input Arguments: str: HTML source page
				Returns: list: List of tour packages
				"""
				extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
				value = extractor.extract(source)["tours"]
				return value

if __name__ == "__main__":
				# Scrape the web page
				scraped = scrape(URL)

				# Extract tour package data
				extracted = extract(scraped)
				print(extracted)
