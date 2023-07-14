def arith(arr) -> float:
    return sum(arr)/len(arr)


def arith2(arr) -> float:
    result = 0
    for num in arr:
        result += num
    return result / len(arr)


print(arith([4,5,4,6,8,12,4]))
print(arith2([4,5,4,6,8,12,4]))