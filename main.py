import requests
import selectorlib
import smtplib
import ssl
import os

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


def send_email(message):
				host = "smtp.gmail.com"
				port = 465
				username = "anessuhonjic11@gmail.com"
				password = os.getenv("PASSWORD")
				receiver = "anessuhonjic11@gmail.com"
				context = ssl.create_default_context()

				with smtplib.SMTP_SSL(host, port, context=context) as server:
								server.login(username, password)
								server.sendmail(username, receiver, message)
								print("Email was sent!")


def store(extracted):
				"""Append extracted data to data.txt file

				Input Arguments: str: extracted data
				"""
				with open("data.txt", "a") as file:
								file.write(extracted + "\n")


def read(extracted):
				"""Read contents of file and return as string"""
				with open("data.txt", "r") as file:
								return file.read()


if __name__ == "__main__":
				# Scrape the web page
				scraped = scrape(URL)
				# Extract tour package data
				extracted = extract(scraped)
				print(extracted)
				content = read(extracted)

				# Check for upcoming tours
				if extracted != "No upcoming tours":
								# Check that extracted data is not already in the file
								if extracted not in content:
												store(extracted)
												send_email(message="New Event Found!")
