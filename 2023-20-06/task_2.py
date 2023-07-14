def reverse_arr(arr) -> list:
    return arr[::-1]


def reverse_arr2(arr) -> list:
    return list(reversed(arr))


def reverse_arr3(arr) -> list:
    i = -1
    result = []
    while i >= -len(arr):
        result += [arr[i]]
        i -= 1
    return result


print(reverse_arr([1,2,5,5,6,2,4,4]))
print(reverse_arr2([1,2,5,5,6,2,4,4]))
print(reverse_arr3([1,2,5,5,6,2,4,4]))