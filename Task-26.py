a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
m = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
min_factor = m // (a + b)
print('Наименьший общий множитель двух чисел =', min_factor)