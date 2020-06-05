import requests
import sqlite3
import json

def get_issues(repo):
	issues = []

	# checks if the link is a link to github
	if "github.com" not in repo:
		return None

	link_parts = repo.split('/')
	github_index = link_parts.index("github.com")

	# makes sure there are at least two more elements after "github.com"
	# in the list
	if len(link_parts) < github_index + 3:
		return None
		
	# saves username and repository name from the repo parameter inputted 
	user_name, repo_name = link_parts[github_index + 1], link_parts[github_index + 2]

	# gets the JSON-formatted data from the GitHub API
	response = requests.get("https://api.github.com/repos/" + user_name + "/" + repo_name + "/issues")
	
	# checks if Github repo's issues link is invalid (i.e. cannot be found)
	response_json = response.json()
	if type(response_json) is not list and response_json['message'] == 'Not Found':
		return None
	
	for issue in response.json():
		if type(issue) == dict:
			url_list = issue['url'].split("/")

			# create unique link for each issue by getting the issue number from each URL
			issue_link = repo + "/issues/" + url_list[-1]

			# save title of issue
			title = issue['title']

			# populate list of labels
			labels = []
			for label in issue["labels"]:
				labels.append(label["name"])

			# add each key value pair into dictionary of issues
			issues.append({'link': issue_link, 'title': title, 'labels': labels})
	return issues

# get_issues('https://github.com/doc19org/medicam')