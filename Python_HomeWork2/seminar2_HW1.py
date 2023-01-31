sum = 0
num = input('Введите число: ')

for a in num:
    if a.isdigit():
        sum += int(a)
print('Сумма его цифр: ', sum)