import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

movies = [('симпсоны', 'ситком', 8.2),
          ('друзья', 'ситком', 8.1),
          ('викинги', 'драма', 8.4),
          ('хронини нарнии', 'фэнтези', 8.5),
          ('гарри поттер', 'фэнтези', 8.0)]

cursor.executemany("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", movies)
conn.commit()
cursor.execute('SELECT * FROM movies WHERE genre = "мультфильм"')
rows = cursor.fetchall()

for row in rows:
    print(f'Фильм - {row[1]}, жанр {row[2]}, рейтинг: {row[3]}')

conn.close()