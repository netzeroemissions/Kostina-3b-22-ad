def calculator(a, b, operator):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print('На 0 делить нельзя')
    print(result)

num_1 = float(input('Введите первое число: '))
action = input('Выберете действие (+, -, *, /): ')
num_2 = float(input('Введите второе число: '))

calculator(num_1, num_2, action)