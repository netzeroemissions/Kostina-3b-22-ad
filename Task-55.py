string = input('Введите список целых чисел через запятую: ')
numbers = []
try:
    for elem in string.split(','):
        numbers.append(int(elem))
    print(sorted(numbers)[0])
except Exception:
    print('Ошибка')