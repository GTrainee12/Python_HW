n = int(input('Введите число N: '))
l = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n%i == 0:
                l.append(i)
                n = int(n/i)
                restart = True
                break
    print(f'Простые множители числа {a} - {l}')
elif n == 1:
    print(f'Простые множители числа {a} - [1]')
