N = int(input('Введите число '))
factorial = 1
for i in range(N):
    i = i + 1
    factorial = i * factorial
    
    print(factorial, end=" ")