import math

points = [(1, 2), (3, 4), (-1, 5), (6, -3)]

def length(point):
    x = point[0]
    y = point[1]
    return math.sqrt(x ** 2 + y ** 2)

sorted_list = sorted(points, key=length)
print(sorted_list)

# проверка
list_of_length = []
for point in points:
    list_of_length.append(length(point))
print('Проверка расстояний', list_of_length)