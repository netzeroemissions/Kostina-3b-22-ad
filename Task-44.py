try:
    file = open('test.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('Файл не найден')