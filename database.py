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
		                    type text NOT NULL,
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
	c.execute('INSERT INTO projects () VALUES ();', project)

for volunteer in volunteers:
	c.execute('INSERT INTO volunteers () VALUES ();', volunteer)