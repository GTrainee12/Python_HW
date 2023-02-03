# n = int(input('Введите число: '))
#
# def get_fibonacci(n):
#     f_n = []
#     a, b = 1, 1
#     for i in range(n-0):  # Номера фибоначи
#         f_n.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):    # Добавляем отрицательные номера
#         f_n.insert(0, a)
#         a, b = b, a - b
#     return f_n
#
# f_n = get_fibonacci(n)
# print(f"Список негафибоначчи: {get_fibonacci(n)}")
# print(f"Индексы после 0: {f_n.index(0)}")

n = int(input('Введите число: '))
n_f = [1,-1]
f = [1,1]

for i in range(2,n):
    list = f[i-1]+f[i-2]
    f.append(list)
    list2 = n_f[i-2] - n_f[i-1]
    n_f.append(list2)

n_f.reverse()
f.insert(0, 0)

print(f'Для вашего значения {n} список выглядит так => {n_f+f}')