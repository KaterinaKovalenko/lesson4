# Есть список со словам “rock”, “scissors”, “paper”.
# Создайте прототип игры камень-ножницы-бумага с компьютером,
# в основе которой будет находится функции random.choice и input()

import random


def rand():
    list = ["rock", "scissors", "paper"]
    lis = random.choice(list)
    return lis


def win(lt, us):
    if us == lt:
        print("draw")
    elif us == "paper" and lt == "rock":
        print("you win")
    elif us == "rock" and lt == "scissors":
        print("you win")
    elif us == "scissors" and lt == "paper":
        print("you win")
    else:
        print("you lose")


us = input("выберете")
lt = rand()
print(lt)
w = win(lt, us)



