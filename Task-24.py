class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def presentation(self):
        print(self.name, ', ', self.age, ' лет, зарплата: ', self.salary, sep='')

employee1 = Employee('Иванов Иван Иванович', 28, 60000)

employee1.presentation()