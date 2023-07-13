import random

x = int(input('Введите число: '))

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 11))
print('Массив: ', my_list)

if my_list.count(x) > 0:
    print('Число найдено в массиве')
else:
    print('Число не найдено в массиве')