class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department

class Quiz:
    def __init__(self, quiz_id, questions, answers):
        self.quiz_id = quiz_id
        self.questions = questions
        self.answers = answers

class Result:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score

s = Student("101", "Abhiram", "CSE")
q = Quiz("Q1", ["2+2?"], ["4"])
r = Result(s.student_id, 1)

print(s.student_id, s.name, s.department)
print(q.quiz_id, q.questions)
print(r.student_id, r.score)
