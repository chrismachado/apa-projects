# Merge Sort Algorithms


def sort(arr, size, **kwargs):
    __merge_sort(arr, size)


def __merge_sort(arr, size):
    if size > 1:
        larr = arr[:size // 2]
        rarr = arr[size // 2:]

        # recursion
        __merge_sort(larr, len(larr))
        __merge_sort(rarr, len(rarr))

        # merging
        i = j = k = 0
        while i < len(larr) and j < len(rarr):
            if larr[i] < rarr[j]:
                arr[k] = larr[i]
                i += 1
            else:
                arr[k] = rarr[j]
                j += 1
            k += 1

        while i < len(larr):
            arr[k] = larr[i]
            i += 1
            k += 1

        while j < len(rarr):
            arr[k] = rarr[j]
            j += 1
            k += 1

