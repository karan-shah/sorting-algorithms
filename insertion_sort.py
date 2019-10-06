import random


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


input_list = [random.randrange(1, 50, 1) for _ in range(30)]


insertion_sort(input_list)
