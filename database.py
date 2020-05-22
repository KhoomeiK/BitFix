import csv
import sqlite3

def parse(file):
    volunteers = []
    projects = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        # burns the first title line 
        csv_reader.__next__()

        # reads the rest of the informational lines
        for line in csv_reader:
            # print(line)
            # checks if the 5th column contains the case-sensitive word "Volunteer"
            if "Volunteer" in line[4]:
                volunteers.append(line)
            else:
                projects.append(line)
                
    return volunteers, managers

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return conn

def create_tables(c):
    projects_table = """CREATE TABLE IF NOT EXISTS projects (
                    email text PRIMARY KEY,
                    name text NOT NULL,
                    phone text,
                    type text NOT NULL,
                    host text NOT NULL,
                    repo text NOT NULL,
                    stack text NOT NULL,
                    languages text NOT NULL,
                    frameworks text NOT NULL,
                    category text NOT NULL,
                    covid text,
                    keep_updated text,
                    description text NOT NULL
                ); """

    volunteers_table = """CREATE TABLE IF NOT EXISTS volunteers (
                            email text PRIMARY KEY,
                            name text NOT NULL,
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

    c.execute(projects_table)
    c.execute(volunteers_table)
    # return c

def populate():
    database = 'database.db'
    conn = create_connection(database)

    with conn:
        c = conn.cursor()
        create_tables(c)

        volunteers, projects = parse('responses.csv')

        for project in projects:
            c.execute('INSERT INTO projects (name, email, phone, type, host, repo, stack, languages, frameworks, category, covid, keep_updated, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                [project[1], project[2], project[3], project[4], project[12], project[13], project[16], project[17], project[18], project[19], project[20], project[21], project[23]])
            print(c.lastrowid)

        for volunteer in volunteers:
            c.execute('INSERT INTO volunteers (name, email, phone, type, role, stack, languages, frameworks, availability, social_good, covid, keep_updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                [volunteer[1], volunteer[2], volunteer[3], volunteer[4], volunteer[5], volunteer[6], volunteer[7], volunteer[8], volunteer[9], volunteer[10], volunteer[11], volunteer[21]])
            print(c.lastrowid)

    conn.close()
