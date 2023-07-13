import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, year INTEGER)''')
books = [('Трое в лодке, не считая собаки', 'Джером', 1960),
         ('Принц Каспиан', 'Льюис', 1981),
         ('Буря мечей', 'Мартин', 2000),
         ('Край вселенной', 'Хокинг', 2010),
         ('Homo deus', 'Харари', 2015)]
cursor.executemany('INSERT INTO books VALUES (?, ?, ?)', books)
conn.commit()

cursor.execute('SELECT * FROM books WHERE year > 2000')
selection = cursor.fetchall()

for book in selection:
    print(f'название: {book[0]}, автор: {book[1]}, год издания: {book[2]}')

conn.close()