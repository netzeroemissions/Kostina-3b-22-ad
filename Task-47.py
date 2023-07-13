number = input('Введите число: ')
try:
    print(float(number) ** 2)
except Exception:
    print('Ошибка')