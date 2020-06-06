from bs4 import BeautifulSoup
import requests
# from urllib.request import urlopen

# import requests
# import sqlite3
# import json

def scraper(url):
	# opening up connection, grabbing the page
	source = requests.get(url).text

	# grab number of branches
	soup = BeautifulSoup(source, "lxml")
	all_elements = soup.findAll('ul', class_='numbers-summary')[0].findAll('li')
	num_branches = int(all_elements[1].span.text)

	# grab number of pull requests
	pull_req_header = soup.findAll('a', href='/Meet-Vora/BitFix/pulls')[0]
	num_pull_reqs = int(pull_req_header.find('span', class_='Counter').text)

	return num_branches, num_pull_reqs

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