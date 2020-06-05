import requests
import sqlite3
import json

# def get_issues(repo):
user_name = 'Meet-Vora'
repo_name = 'Slackbot'
# gets the JSON-formatted data from the GitHub API
response = requests.get("https://api.github.com/repos/" + user_name + "/" + repo_name + "/issues")
print(response)
print(response.links)
	

# get_issues('https://github.com/doc19org/medicam')