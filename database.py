import sqlite3
from parser import parse

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    	return conn

def create_tables(conn):
    projects_table = """CREATE TABLE IF NOT EXISTS projects (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    email text NOT NULL,
                    phone text,
                    type text NOT NULL,
                    host text NOT NULL,
                    repo text NOT NULL,
                    stack text NOT NULL,
                    languages text NOT NULL,
                    frameworks text NOT NULL,
                    category text NOT NULL,
                    covid text,
                    keep_updated text
                    description text NOT NULL
				); """

	volunteers_table = """CREATE TABLE IF NOT EXISTS volunteers (
		                    id integer PRIMARY KEY,
		                    name text NOT NULL,
		                    email text NOT NULL,
		                    phone text,
		                    type text NOT NULL,
		                    role text NOT NULL,
		                    stack text NOT NULL,
		                    languages text NOT NULL,
		                    frameworks text NOT NULL,
		                    availability text NOT NULL,
		                    social_good text NOT NULL,
		                    covid text,
		                    keep_updated text
	                	);"""

    c = conn.cursor()
    c.execute(projects_table)
    c.execute(volunteers_table)

database = 'database.db'
conn = create_connection(database)
create_tables(conn)

volunteers, projects = parse()

for project in projects:
	c.execute('INSERT INTO projects (name, email, phone, type, host, repo, stack, languages, frameworks, category, covid, keep_updated, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
		[project[1], project[2], project[3], project[4], project[12], project[13], project[16], project[17], project[18], project[19], project[20], project[21], project[23]])

for volunteer in volunteers:
	c.execute('INSERT INTO volunteers (name, email, phone, type, role, stack, languages, frameworks, availability, social_good, covid, keep_updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
        [volunteer[1], volunteer[2], volunteer[3], volunteer[4], volunteer[5], volunteer[6], volunteer[7], volunteer[8], volunteer[9], volunteer[10], volunteer[11], volunteer[21]])