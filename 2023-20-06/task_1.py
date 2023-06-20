def index_min_max(arr) -> list:
    i = 0
    min_ind = arr[0]
    max_ind = arr[0]
    while i < len(arr):
        if arr[i] > max_ind:
            max_ind = arr[i]
        if arr[i] < min_ind:
            min_ind = arr[i]
        i += 1
    return [max_ind, min_ind]

print(index_min_max([1,5,6,9,84,52,66,100]))