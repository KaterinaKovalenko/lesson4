# 1) Сгенерировать случайное число с помощью randint и вывести его на экран

import random
r = random.randint(1, 1000000000)
print(r)

# 2)Дан список чисел [1,2,3,4,5,6].
# Перемешать список с помощью функции random.shuffle
# и вывести случайное число с помощью random.choice

list1 = [1, 2, 3, 4, 5, 6]
random.shuffle(list1)
print(list1)
print(random.choice(list1))

# 3)Сгенерировать случайное число с плавающей точкой
# с помощью random.random() и вывести его на экран

r1 = random.random()
print(r1)

# 4)Сгенерировать случайное число с плавающей точкой
# в диапазоне от 0 до 25 с помощью random.uniform и вывести его на экран

r2 = random.uniform(0, 25)
print(r2)
