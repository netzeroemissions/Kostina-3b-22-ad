import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 101))
print('Массив: ', my_list)

my_list.sort()
print('Минимальное значение: ', my_list[0])
print('Максимальное значение: ', my_list[-1])