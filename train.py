def only_odd(arr):
    result = 0
    for num in arr:
        if num % 2 != 0:
            result += num
    return result


print(only_odd([1,5,4,5,8,89,5,21,4]))