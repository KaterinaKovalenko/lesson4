# Напишите программу, которая принимает ваше имя в качестве входных данных,
# а затем ваш возраст в качестве входных данных
# и приветствует вас следующим текстом:
# «Здравствуйте, <имя>, в ваш следующий день рождения вам будет <возраст + 1> лет»


def day_b():
    name = input("Whot is your name? ")
    age = int(input("How old are yoy? "))
    return name, age


name, age = day_b()
print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")
