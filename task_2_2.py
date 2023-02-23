# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random
sum_numbers = int(input("Введите сумму чисел: "))
product_numbers = int(input("Введите произведение чисел: "))
flag = False

for i in range(0, sum_numbers):
    if i * (sum_numbers - i) == product_numbers:
        print(f"Петя загадал числа {i} и {sum_numbers - i}")
        flag = True
        break
if not flag:
    print("Таких чисел нет!")