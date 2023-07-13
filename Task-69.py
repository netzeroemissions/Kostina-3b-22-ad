import sqlite3

conn = sqlite3.connect('staff.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS staff
(id INTEGER PRIMARY KEY, name TEXT, position INTEGER, zp INTEGER)''')

staff = [('Иван', 'генеральный директор', 60000),
         ('Игорь', 'коммерческий директор', 50000),
         ('Михаил', 'разработчик', 40000),
         ('Анна', 'аналитик', 30000)]

cursor.executemany("INSERT INTO staff (name, position, zp) VALUES (?, ?, ?)", staff)
conn.commit()
cursor.execute('SELECT * FROM staff WHERE position = "менеджер"')
rows = cursor.fetchall()

for row in rows:
    print(f'Имя - {row[1]}, должность - {row[2]}, зарплата {row[3]} р.')

conn.close()