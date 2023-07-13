list = []
num = ''
while num != 'end':
    num = input('Введите число или слово end, чтобы закончить список: ')
    if num == 'end':
        break
    else:
        list.append(int(num))

print(sorted(list)[:2])