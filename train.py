def second_major(arr):
    arr = sorted(arr)
    first_major = arr[-1]
    sec_major = arr[-2]
    return first_major, sec_major


def second_major2(arr):
    fst_major = float('-inf')
    scnd_major = float('-inf')
    for n in arr:
        if fst_major < n:
            scnd_major = fst_major
            fst_major = n
        elif scnd_major < n and scnd_major < fst_major:
            scnd_major = n

    return fst_major, scnd_major


print(second_major([21, 2, 6, 8, 1000, 7, 5, 6, 2, 4, 5, 6, 9, 110]))
print(second_major2([21, 2, 6, 8, 1000, 7, 5, 6, 2, 4, 5, 6, 9, 110]))
