# 1) Напишите программу, которая генерирует случайное число от 1 до 10, и пусть
# пользователь угадает, какое число было сгенерировано. Результат должен быть отправлен обратно
# пользователю с помощью оператора печати.

import random


def ran():
    ran1 = random.randrange(1, 10)
    return ran1


def choice():
    if func == us:
        print("you guessed")
    else:
        print("you lose")


us = int(input("выберете число от 1 до 10  "))
func = ran()
print(func)
choice()







