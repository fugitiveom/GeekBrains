# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for step in range(10):
    try:
        user_choise = int(input(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))
    except ValueError:
        user_choise = LOWER_LIMIT - 1
    if num == user_choise:
        print("Угадали!")
        break
