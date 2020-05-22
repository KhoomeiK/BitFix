import sqlite3
from repository_reader import get_issues

# keywords to check in Issues
languages = {'Python', 'Node', 'JavaScript', 'HTML', 'CSS', 'Java', 'C', 'C++', 'C#', 'Objective C', 'Go', 'Rust', 'Swift', 'Kotlin', 'Dart', 'Ruby', 'PHP', 'SQL', 'R', 'MATLAB', 'Assembly'}
frameworks = {'Flask', 'Django', 'Express', 'React', 'Vue', 'Angular', 'React Native', 'Flutter', 'SpringBoot', '.NET', 'Rails', 'Laravel', 'WordPress', 'Unity', 'MySQL', 'Postgres', 'SQLite', 'Mongo', 'Firebase', 'Redis', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit', 'Pandas'}
keywords = languages.union(frameworks)
database = 'database.db'

def compare():
	conn = sqlite3.connect(database)

	with conn:
		c = conn.cursor()
		c.execute('SELECT repo, languages, frameworks FROM projects;')
		projects = c.fetchall()
		c.execute('SELECT email, languages, frameworks FROM volunteers;')
		volunteers = c.fetchall()

		assignments = dict((vol[0], []) for vol in volunteers) # {volEmail: []}

		for proj in projects:
			print(proj[0], '-----------------------')
			issues = get_issues(proj[0]) # get issues for github repo
			projTech = set(proj[1].split(',') + proj[2].split(',')) # create set of langs & frameworks for proj

			for vol in volunteers:
				volTech = set(vol[1].split(',') + vol[2].split(',')) # create set of langs & frameworks for vol
				overlap = projTech.intersection(volTech) # overlap of proj and vol
				if len(overlap) > 1:
					print(vol[0], len(overlap)) # email, number of overlapping tech

					ct = 0 # num of issues assigned
					for issue in issues:
						issueWords = set(issue['title'].split(' ')).union(set(issue['labels'])).intersection(keywords) # keywords in issue
						if len(issueWords) > 1 and ct < 3:
							assignments[vol[0]].append(issue) # assign issue to vol
							ct += 1
	return assignments

# to be passed to emailer					
# print(compare())
