N = int(input('Введите длину массива: '))
Array = [0]*N
Array[0] = int(input('Введите первый элемен: '))
difference = int(input('Введите разность: '))
print(f"Ваш первый эллемет в массиве {Array[0]}")
for i in range(1, N):
    Array[i] = Array[i-1]+difference
print(Array)
