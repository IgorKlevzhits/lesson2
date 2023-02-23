# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
quantity_coins = int(input("Введите количество монет: "))
quantity_eagles = 0
quantity_tails = 0

for i in range(0, quantity_coins):
    if random.randint(0, 1) == 0:
        print("Орёл")
        quantity_eagles += 1
    else:
        print("Решка")
        quantity_tails += 1

print(f"Минимум нужно перевернуть {quantity_eagles if quantity_eagles < quantity_tails else quantity_tails} монет")