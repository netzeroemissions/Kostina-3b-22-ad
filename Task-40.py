try:
    file = open('test.txt', 'r')
    print('Файл существует')
    file.close()
except FileNotFoundError:
    print('Файл не существует')