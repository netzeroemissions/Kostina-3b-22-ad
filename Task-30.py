string = input('Введите текст: ')
vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщъь'
qt_vow = 0
qt_con = 0
for letter in string:
    try:
        vowels.index(letter)
        qt_vow += 1
    except ValueError:
        consonants.index(letter)
        qt_con += 1
print('Количество гласных: ', qt_vow, ', количество согласных: ', qt_con)