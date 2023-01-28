x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = (((x_coordinate_B - x_coordinate_A) ** 2+ (y_coordinate_B - y_coordinate_A) ** 2)** 0.5)
print(distance)