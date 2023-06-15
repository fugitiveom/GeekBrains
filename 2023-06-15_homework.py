def arith(arr):
    return sum(arr)/len(arr)


def factorial(n):
    if n <= 0 or n % 2 != 0:
        return "Факториал может быть расчитан только из целого положительного числа"
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result

print(arith([1,2,6,45,8,5,3]))
print(factorial(10))