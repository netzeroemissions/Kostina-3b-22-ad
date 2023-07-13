try:
    with open(input('Введите имя файла: ')) as file:
        content = file.read()
        print(content)
except Exception:
    print('Ошибка')