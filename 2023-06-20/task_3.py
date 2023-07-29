def sum_min_to_max(arr) -> float:
    arr.sort()
    return sum(arr[1: -1])


def sum_min_to_max2(arr) -> float:
    min_num = arr[0]
    max_num = arr[0]
    i = 0
    while i < len(arr):
        if arr[i] > max_num:
            max_num = num
        elif arr[i] < min_num:
            min_num = num
    arr.remove(max_num)
    arr.remove(min_num)
    return sum(arr)



print(sum_min_to_max([1,5,6,4,8,87,5,7]))
print(sum_min_to_max2([1, 5, 6, 4, 8, 87, 5, 7]))