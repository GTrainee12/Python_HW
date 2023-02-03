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