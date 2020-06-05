# only 1 branch and at least 1 pull req then they're def open source
import requests

def getData():
	url = "https://api.github.com/users/Meet-Vora/repos"
	response = requests.head(url=url)
	print(response.headers['link'])

getData()
