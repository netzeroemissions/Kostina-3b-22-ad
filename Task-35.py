n = int(input('Введите количество чисел ряда Фибоначчи: '))
number_1 = 1
number_2 = 1

if n == 0:
    print('')
elif n == 1:
    print(number_1)
elif n == 2:
    print(number_1)
    print(number_2)
else:
    print(number_1)
    print(number_2)
    for i in range(2, n):
        number_1, number_2 = number_2, number_1 + number_2
        print(number_2)