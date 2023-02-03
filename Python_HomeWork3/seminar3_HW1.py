from random import randint

def l(n):
    l = []
    for i in range(n):
        l.append(randint(0, n))
    return l
n = int(input('Введите число N: '))
numbers = l(n)
summ = 0
for i in range(1, len(numbers), 2):
    summ += numbers[i]
print(f"{numbers} -> сумма элементов на нечётных позициях: {summ}")