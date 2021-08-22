from functools import cmp_to_key

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @staticmethod
    def sort(first, second):
        if first.grade == second.grade:
            return 1 if second.name < first.name else -1
        return 1 if second.grade < first.grade else -1

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(Student(name, grade))
        self.students.sort(key=cmp_to_key(Student.sort))

    def roster(self):
        return [student.name for student in self.students]

    def grade(self, grade_number):
        return [student.name for student in self.students
                if student.grade == grade_number]


