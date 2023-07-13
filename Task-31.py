import calculator

a = float(input('Введите первое число: '))
action = input('Выберете действие (+, -, *, /): ')
b = float(input('Введите второе число: '))

if action == '+':
    print(calculator.addition(a, b))
elif action == '-':
    print(calculator.subtraction(a, b))
elif action == '*':
    print(calculator.multiplication(a, b))
elif action == '/':
    print(calculator.division(a, b))