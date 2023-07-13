import os

ext = str(input('Введите расширение файла: '))
dir_name = str(input('Введите путь к директории: '))
files = []

try:
    list_of_files = os.listdir(dir_name)

    for path in list_of_files:
        try:
            if path.split('.', 1)[1] == ext:
                files.append(path)
        except:
            continue

    print(files)
except FileNotFoundError:
    print('Ошибка')