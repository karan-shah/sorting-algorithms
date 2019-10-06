import random


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def inplace_quickSort(elements, a=0, b=None):
    if b is None:
        b = len(elements) - 1
    if a >= b:
        return
    pivot = elements[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and elements[left] <= pivot:
            left += 1
        while left <= right and elements[right] >= pivot:
            right -= 1
        if left < right:
            swap(elements, left, right)
    swap(elements, left, b)  # putting pivot at the center.

    inplace_quickSort(elements, a, left - 1)
    inplace_quickSort(elements, left + 1, b)


input_list = [random.randrange(1, 50, 1) for _ in range(30)]


inplace_quickSort(input_list)
