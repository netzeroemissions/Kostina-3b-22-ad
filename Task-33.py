string = input('Введите текст: ')
list = []
for letter in string:
    try:
        list.index(letter)
    except:
        list.append(letter)

for sign in list:
    print(sign, ' ', string.count(sign))