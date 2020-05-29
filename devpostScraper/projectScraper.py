from html.entities import codepoint2name
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

projectLinks = [line.strip() for line in open('projects.txt', 'r')]

githubLinks = set()

for link in projectLinks:
	uClient = uReq(link)
	page_html = uClient.read() 
	uClient.close() 

	page = soup(page_html, "html.parser") 

	githubs = page.find("nav", {"class":"app-links"})
	if githubs == None:
		continue

	githubs = githubs.ul.findAll("li")
	for github in githubs:
		github = github.a['href']
		if "github.com" in github:
			print(github)
			githubLinks.add(github)

with open('githubs.txt', 'a') as file:
	for link in githubLinks:
		file.write(link + '\n')