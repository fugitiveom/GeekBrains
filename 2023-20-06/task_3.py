def sum_min_to_max(arr) -> float:
    return sum(arr[1: -1])


def sum_min_to_max2(arr) -> float:
    i = 0
    result = 0
    while i < len(arr):
        if i > 0 and i < len(arr) -1:
            result += arr[i]
        i += 1
    return result


print(sum_min_to_max([1,5,6,4,8,87,5,7]))
print(sum_min_to_max2([1, 5, 6, 4, 8, 87, 5, 7]))