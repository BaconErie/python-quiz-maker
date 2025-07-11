'''
DB controller
'''
import sqlite3

conn: sqlite3.Connection
cursor: sqlite3.Cursor

def connect_db():
    global conn
    global cursor

    conn = sqlite3.connect('db.sqlite3', autocommit=True)
    cursor = conn.cursor()

class Instructor:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def get_instructor_by_id(cls, id: int) -> Instructor | None:
        pass

    def verify_password(self, password: str):
        pass

class Assignment:
    def __init__(self, id: int, name: str, creator: Instructor):
        pass

    @classmethod
    def get_assignment_by_id(cls, id: int) -> Assignment | None:
        cursor.execute('SELECT * FROM assignments WHERE id=?', (id,))

    def submit(self, name: str, **kwargs):
        pass

class Lab(Assignment):
    def __init__(self, id: int, name: str, creator: Instructor, directions: str, test_cases: list[tuple[str, str]]):
        super().__init__(id, name, creator)
        self.directions = directions
        self.test_cases = test_cases

    def submit(self, name: str, code: str, correct_test_cases: list[int]):
        pass

class Quiz(Assignment):
    def __init__(self, id: int, name: str, creator: Instructor, test_cases: list[tuple[str, str]], questions: list[Question]):
        super().__init__(id, name, creator)
        self.id = id
        self.name = name
        self.creator = creator
        self.test_cases = test_cases
        self.questions = questions

    def submit(self, name: str, answers: list[int]):
        pass

class Question:
    def __init__(self, quiz: Quiz, question: str, answers: list[str], correct_answer: int):
        self.quiz = quiz
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer