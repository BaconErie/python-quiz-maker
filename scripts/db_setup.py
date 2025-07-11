import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS instructors (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               password TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               creator_id INTEGER,
               name TEXT,
               type TEXT
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS labs (
               id INTEGER PRIMARY KEY,
               directions TEXT,
               test_cases_json TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes (
               id INTEGER PRIMARY KEY,
               questions_json TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS submissions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               time TEXT,
               student_name INTEGER,
               assignment_id INTEGER,
               submission_body TEXT
               )''')
conn.commit()

conn.close()