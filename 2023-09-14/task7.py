# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

input_range = range(1, 1000)


def get_user_input(request: str) -> str:
    return input(request)


def value_to_int(num: str) -> int:
    try:
        return int(num)
    except ValueError:
        return int()


def is_value_in_range(val: int, _range: range) -> bool:
    return True if val in _range else False


def count_digit_num(num: int) -> int:
    digits = 0
    while num >= 1:
        num = num // 10
        digits += 1
    return digits


def print_sqare(num: int) -> None:
    print(num**2)


def print_mul_digits(num) -> None:
    num = str(num)
    mul = int(num[0]) * int(num[1])
    print(mul)


def print_reversed_num(num: int) -> int:
    print(str(num)[::-1])


def main():
    num_in_range = False
    while not num_in_range:
        user_num = get_user_input("Введите число от 1 до 999: ")
        user_num = value_to_int(user_num)
        num_in_range = is_value_in_range(user_num, input_range)
    digits_num = count_digit_num(user_num)
    if digits_num == 1:
        print("Это цифра")
        print_sqare(user_num)
    elif digits_num == 2:
        print("Это двузначное число")
        print_mul_digits(user_num)
    elif digits_num == 3:
        print("Это трехзначное число")
        print_reversed_num(user_num)


if __name__ == '__main__':
    main()
