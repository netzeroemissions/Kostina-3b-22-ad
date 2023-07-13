def string_reverse(string):
    result = string[::-1]
    return result

sentence = str(input('Введите текст: '))
print(string_reverse(sentence))