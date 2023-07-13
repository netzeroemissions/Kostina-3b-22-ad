try:
    with open(test.txt) as file:
        file.write('Hello, world!')
except Exception:
    print('Ошибка')