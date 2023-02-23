# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите число: "))
degree = 1
if number < 1:
    print(f"Hет степеней двойки которые были бы меньше числа {number}")
elif number == 1:
    print("1")
else:
    print("1")
    while degree * 2 <= number:
        degree *=2
        print(degree)
