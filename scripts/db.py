import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               password TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS question (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               creator_id INTEGER,
               type TEXT
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS exercises (
               id INTEGER PRIMARY KEY,
               name TEXT,
               instructions TEXT,
               test_cases_json TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes (
               id INTEGER PRIMARY KEY,
               name TEXT,
               questions_json TEXT
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS submissions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               time TEXT,
               student_name INTEGER,
               exercise_id INTEGER,
               submission_body TEXT
               )''')
conn.commit()

conn.close()