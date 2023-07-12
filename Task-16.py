class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_information(self):
        print('Кошка по имени ', self.name,', Возраст ', self.age, ' лет, цвет ',self.color)