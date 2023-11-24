# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input("Введите количество рядов: "))
asterisks = -1

for row in range(rows):
    spaces = (rows - (row + 1)) * ' '
    asterisks += 2
    print(spaces, asterisks * '*', spaces)
