# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

def to_hexadecimal(number):
    if number == 0:
        return '0'

    hex_chars = '0123456789ABCDEF'
    result = ''

    while number > 0:
        remainder = number % 16
        result = hex_chars[remainder] + result
        number //= 16

    return result

try:
    num = int(input("Введите целое число: "))
    if num < 0:
        raise ValueError("Введите положительное целое число")
except ValueError:
    print("Введите положительное целое число")
else:
    hexadecimal = to_hexadecimal(num)
    print(f"Шестнадцатеричное представление: 0x{hexadecimal}")
    print(f"Проверка функцией hex(): {hex(num)}")
