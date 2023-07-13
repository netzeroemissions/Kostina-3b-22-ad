import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 11))
print('Массив: ', my_list)

amount = my_list[0]
for i in range(9):
    amount += my_list[i + 1]
print('Сумма: ', amount)