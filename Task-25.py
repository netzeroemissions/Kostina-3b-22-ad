num = int(input('Введите число: '))
i = 2
j = 0
while num >= i * i and j != 1:
    if num % i == 0:
        j = 1
        i += 1
    else:
        i += 1
if j == 1:
    print('Число', num, 'составное')
else:
    print('Число', num, 'простое')