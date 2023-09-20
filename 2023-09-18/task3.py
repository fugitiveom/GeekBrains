# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

def sum_of_fractions(num1, denom1, num2, denom2):
    return ((num1 * denom2) + (num2 * denom1)) / (denom1 * denom2)

def mul_of_fractions(num1, denom1, num2, denom2):
    return (num1 * num2) / (denom1 * denom2)

try:
    num1, denom1 = map(int, input("Введите первую дробь в виде a/b: ").split('/'))
    num2, denom2 = map(int, input("Введите вторую дробь в виде a/b: ").split('/'))
except ValueError:
    print("Вы ввели неправильную дробь")
else:
    print(f"Сумма дробей: {sum_of_fractions(num1, denom1, num2, denom2)}")
    print(f"Произведение дробей: {mul_of_fractions(num1, denom1, num2, denom2)}")