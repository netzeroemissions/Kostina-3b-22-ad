class Student:
    def __init__(self, name, surname, course, grades):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = grades

    def calculate_avg_grade(self):
        avg_grade = sum(self.grades) / len(self.grades)
        return avg_grade