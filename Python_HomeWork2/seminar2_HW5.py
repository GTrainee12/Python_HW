import random
list1 = [random.randint(0,30) for i in range(random.randint(5,30))]
print(f"Основной список:\n {list1}")
random.shuffle(list1)
print(f"Список после перемешивания:\n{list1}")