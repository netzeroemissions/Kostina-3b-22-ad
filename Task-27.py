import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 11))
print('Массив: ', my_list)
print('Четные числа в массиве:')
for num in my_list:
    if num % 2 == 0:
        print(num)