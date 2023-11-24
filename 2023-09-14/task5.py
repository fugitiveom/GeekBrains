# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = int(input("Введите n: "))
e = int(input("Введите e: "))

i = 1
result = 0

while i <= n:
    if i % e != 0 and i % 2 == 0:
        result += i
        print(i)
    i += 1

print(result)