A = 21
result = 0

fi_1 = 0
fi_2 = 1

for i in range(A + 1):
    result = fi_1 + fi_2
    fi_1 = fi_2
    fi_2 = result
    print(result)