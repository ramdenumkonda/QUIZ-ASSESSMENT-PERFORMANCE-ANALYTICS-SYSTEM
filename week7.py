from datetime import datetime

class Record:
    def __init__(self, record_id):
        self._record_id = record_id
        self._timestamp = datetime.now()

    def get_id(self):
        return self._record_id

class Student(Record):
    def __init__(self, student_id, name):
        super().__init__(student_id)
        self.__name = name

    def get_name(self):
        return self.__name

class Result(Record):
    def __init__(self, student_id, score):
        super().__init__(student_id)
        self.__score = score

    def get_score(self):
        return self.__score

s = Student("101", "Abhiram")
r = Result("101", 90)

print(s.get_id(), s.get_name())
print(r.get_id(), r.get_score())
