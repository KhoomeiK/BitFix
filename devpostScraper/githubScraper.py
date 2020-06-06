from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

import requests
import sqlite3
import json

def scraper(url):
	# opening up connection, grabbing the page
	uClient = urlopen(url)
	page_html = uClient.read()
	uClient.close()

	# html parsing
	soup = BeautifulSoup(page_html, "lxml")
	all_elements = soup.findAll('ul', class_='numbers-summary')[0].findAll('li')
	num_branches = int(all_elements[1].span.text)
	num_pull_reqs = all_elements

	print(all_elements)

url = "https://github.com/Meet-Vora/BitFix"
scraper(url)

# def get_issues(repo):
# user_name = 'Meet-Vora'
# repo_name = 'Slackbot'
# # gets the JSON-formatted data from the GitHub API
# response = requests.get("https://api.github.com/repos/" + user_name + "/" + repo_name + "/issues")
# print(response)
# print(response.links)
	

# get_issues('https://github.com/doc19org/medicam')