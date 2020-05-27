from html.entities import codepoint2name
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

hackathonLinks = [line.strip() + '/submissions?page=' for line in open('hackathons.txt', 'r')]
print(hackathonLinks)

submissionLinks = set()

for link in hackathonLinks:
	pageNum = 1
	while True:
		print("-----------------PAGE", pageNum)

		try:
			uClient = uReq(link + str(pageNum))
			page_html = uClient.read() 
			uClient.close() 
		except:
			print("ERROR")
			break # continue

		page = soup(page_html, "html.parser") 

		submissions = page.findAll("div", {"class":"gallery-item"})
		
		if submissions == []: # past final page
			break

		for submission in submissions:
			submissionLink = submission.a['href']
			print(submissionLink)
			submissionLinks.add(submissionLink)
		
		pageNum += 1

with open('projects.txt', 'a') as file:
	for link in submissionLinks:
		file.write(link + '\n')