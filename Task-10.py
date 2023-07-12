class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_information(self):
        print("Имя: ", self.name, " Возраст: ", self.age)