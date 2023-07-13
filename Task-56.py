filename = input('Введите имя файла: ')
try:
    file = open(filename, 'r')
    text = file.read()
    file.close()

    word_list = []
    qt = 0
    qt_max = 0
    word_friq = ''

    for word in text.split(' '):
        word_list.append(word)

    for word in word_list:
        qt = word_list.count(word)
        if qt > qt_max:
            qt_max = qt
            word_friq = word

    print(word_friq)
except FileNotFoundError:
    print('Файл не найден')