list = [5, 7, 11, 13, 15, 20, 25]
amount = 0
divider = 0
for elem in list:
    if elem > 10:
        amount += elem
        divider += 1
    else:
        continue
average = amount / divider
print('Среднее арифметическое элементов > 10: ', average)