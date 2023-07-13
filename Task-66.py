import sqlite3

conn = sqlite3.connect('base.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, avg_score REAL)''')
students = [('Иванов', 19, 4.6), ('Петров', 20, 4.3), ('Сидоров', 18, 4.9), ('Ильин', 20, 4.5)]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()

for student in all_students:
    print(f'имя: {student[0]}, возраст: {student[1]}, средняя оценка: {student[2]}')

conn.close()