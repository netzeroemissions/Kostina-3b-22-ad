list_1 = [24, 36, 48, 60]
list_2 = [12, 18, 24, 36, 72]
result = list_1[0]
common_list = (list_1[1:] + list_2)

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

for elem in common_list:
    result = gcd(result, elem)

print('Наибольший общий делитель: ', result)