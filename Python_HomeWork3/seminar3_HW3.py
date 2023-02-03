from random import uniform


n = int(input('Введите размер списка:  '))
list1 = []
for i in range(n):
    f = uniform(0, n)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):

    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))
print(f'Список: {list1}.')
print(f'Максимальное и минимальное значение в списке: {max, min}.')
print(f'Раздница дробной части элементов: {(round(dif,2))}.')
