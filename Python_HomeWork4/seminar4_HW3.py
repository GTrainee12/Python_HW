from random import randint
n = int (input('Задайте колличество элементов для последовательности чисел: '))
numbers = []
for i in range(n):
    numbers.append(randint (0,n))
print(numbers)
new_l = [i for i in numbers if numbers.count(i) == 1]
print(f"Исходный список: {numbers} -> Список из неповторяющихся элементов: {new_l}")