# Insertion Sort Algorithms


def sort(arr, recursive=False):
    if recursive:
        __insertion_sort(arr, len(arr))
    else:
        __insertion_sort(arr, len(arr))


def __insertion_sort(arr, size):
    for i in range(size):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


def __insertion_sort_recursive(arr, size):
    if size == 0:
        return
    __insertion_sort_recursive(arr, size - 1)
    i = size - 1
    while i > 0 and arr[i - 1] > arr[i]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
    return arr
