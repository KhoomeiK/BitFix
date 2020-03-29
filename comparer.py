import sqlite3
from issues import fetchIssues

# keywords to check in Issues
languages = 'Python', 'Node', 'JavaScript', 'HTML', 'CSS', 'Java', 'C', 'C++', 'C#', 'Objective C', 'Go', 'Rust', 'Swift', 'Kotlin', 'Dart', 'Ruby', 'PHP', 'SQL', 'R', 'MATLAB', 'Assembly'
frameworks = 'Flask', 'Django', 'Express', 'React', 'Vue', 'Angular', 'React Native', 'Flutter', 'SpringBoot', '.NET', 'Rails', 'Laravel', 'WordPress', 'Unity', 'MySQL', 'Postgres', 'SQLite', 'Mongo', 'Firebase', 'Redis', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit', 'Pandas'

database = 'database.db'
conn = sqlite3.connect(database)

with conn:
	c = conn.cursor()
	c.execute('SELECT repo, languages, frameworks FROM projects;')
	projects = c.fetchall()
	c.execute('SELECT email, languages, frameworks FROM volunteers;')
	volunteers = c.fetchall()

	assignments = dict((vol[0], []) for vol in volunteers)

	for proj in projects:
		print(proj[0], '-----------------------')
		issues = fetchIssues(proj[0])
		projTech = set(proj[1].split(',') + proj[2].split(','))

		for vol in volunteers:
			volTech = set(vol[1].split(',') + vol[2].split(','))
			overlap = projTech.intersection(volTech)
			if len(overlap) > 1:
				print(vol[0], len(overlap))
				assignments[vol[0]].append(issues.pop())

print(assignments)