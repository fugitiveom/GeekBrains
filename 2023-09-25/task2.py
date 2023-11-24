# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не
# хешируем, используйте его строковое представление.

def return_args(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

print(return_args(name="Vasya", age=30, custom_object={1, 2, 3}))