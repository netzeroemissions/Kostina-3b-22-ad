class Book:
    def __init__(self, name, author, publishing_year, genre):
        self.name = name
        self.author = author
        self.publishing_year = publishing_year
        self.genre = genre

    def print_information(self):
        print(self.name, ', ', self.author, ' (', self.publishing_year, '), ',self.genre)