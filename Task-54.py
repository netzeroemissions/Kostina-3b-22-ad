qt = input('Введите число: ')
list = []
i = 1
amount = 0

try:
    while i <= int(qt):
        list.append(i)
        i += 1
    print(list)

    for elem in list:
        amount += elem
    print(amount)
except Exception:
    print('Ошибка')