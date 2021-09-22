"""
Solution to Grade School task on Exercism.

https://exercism.org/tracks/python/exercises/grade-school
"""


from __future__ import annotations

from functools import cmp_to_key


def sort_students(first: Student, second: Student) -> int:
    """
    Compare two Student objects.

    Args:
        first (Student): first student to compare.
        second (Student): second student to compare.

    Returns:
        int: 1 if first > second else -1

    """
    if first.grade == second.grade:
        return 1 if second.name < first.name else -1
    return 1 if second.grade < first.grade else -1


class Student(object):
    """Class for students."""

    def __init__(self, name: str, grade: int):
        """
        Initialize Student object.

        Args:
            name (str): student's name.
            grade (int): student's grade.

        """
        self.name: str = name
        self.grade: int = grade


class School(object):
    """Class for school."""

    def __init__(self):
        """Initialize School object."""
        self.students: list = []

    def add_student(self, name: str, grade: int) -> None:
        """
        Add student to school.

        Adds student to students' list and sorts it.

        Args:
            name (str): student's name.
            grade (int): student's grade.

        """
        self.students.append(Student(name, grade))
        self.students.sort(key=cmp_to_key(sort_students))

    def roster(self) -> list:
        """
        Get list with students' names.

        Returns:
            list: list with students' names.

        """
        return [student.name for student in self.students]

    def grade(self, grade_number: int) -> list:
        """
        Get all students with specified grade.

        Args:
            grade_number (int): student's grade.

        Returns:
            list: list with students' names with specified grades.

        """
        return [
            student.name
            for student in self.students
            if student.grade == grade_number
        ]
