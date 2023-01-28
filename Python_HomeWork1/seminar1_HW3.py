quarterx = int(input('Введите координату x ≠ 0: '))
quartery = int(input('Введите координату y ≠ 0: '))

if quarterx == 0 and quartery == 0:
    print('У вас нулевые значения попробуйте снова')
elif quarterx > 0 and quartery > 0:
    print(f'Ваша точка находится в плоскости 1 ')
elif quarterx < 0 and quartery > 0:
    print(f'Ваша точка находится в плоскости 2 ')
elif quarterx < 0 and quartery < 0:
    print(f'Ваша точка находится в плоскости 3 ')
elif quarterx > 0 and quartery < 0:
    print(f'Ваша точка находится в плоскости 4 ')