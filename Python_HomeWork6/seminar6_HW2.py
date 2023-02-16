from random import randint
length = int(input(" Введите длину массива:  "))
mas=[]
for i in range(length):
    mas.append(randint (-length,length))
print(mas)

mini=int(input("MIN= "))
maxi=int(input("MAX= "))

masi=[]
if maxi>=mini:
    for i in range(len(mas)):
        if maxi>=mas[i] and mini<=mas[i]:
            masi.append(i)

    print("Кол-во элементов: ",len(masi))
    print('Индексы: ',*masi)