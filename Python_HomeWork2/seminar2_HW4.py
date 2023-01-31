from random import randint
n = int (input('Задайте коллчество N элементов: '))
numbers = []
for i in range(n):
    numbers.append(randint (-n,n))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Номера элементов: ', get_numbers(numbers))

x = int(input('Укажите позицию первого элемента: '))
y = int(input('Укажите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Множество элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)
