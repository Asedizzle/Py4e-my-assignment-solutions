import json, sqlite3

create = sqlite3.connect("students_coursesdb.sqlite")
wand = create.cursor()

wand.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE   
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id       INTEGER,
    course_id     INTEGER,
    role          INTEGER,
    PRIMARY KEY   (user_id, course_id)
);

''')

import json
filename = input('pleasse input a valid json file name')
if len(filename) < 1:
    filename = "roster_data.json"
    
jd = open(filename).read()
json_data = json.loads(jd)
#print(json_data)

for block in json_data:
    name = block[0]
    course = block[1]
    role = block[2]
    
    if name is None or course is None or role is None:
        continue
    
    wand.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', ( name, ))
    wand.execute('SELECT id FROM User WHERE name = ? ', ( name, ))
    user_id = wand.fetchone()[0]
    
    wand.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', ( course, ))
    wand.execute('SELECT id FROM Course WHERE title = ? ', ( course, ))
    course_id = wand.fetchone()[0]
    
    wand.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
                 VALUES ( ?, ?, ? )''', ( user_id, course_id, role ))
    
    create.commit()