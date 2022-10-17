import numpy as np, contextvars, contextlib, random, time
from sorting import (
    insertion_sort,
    merge_sort
)
from plotlib import plot


@contextlib.contextmanager
def timeit(name, list):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    list.append(took)
    return list


if __name__ == '__main__':
    array_sizes = sorted(np.random.randint(10, 10001, 10))
    array_ninputs = np.random.randint(10, 21, 1)[0]
    array_inputs = [[np.random.uniform(-2 * array_size, 2 * array_size + 1, array_size) for i in range(array_ninputs)]
                    for array_size in array_sizes]

    arr_times = []

    # print(array_inputs)
    for array_input in array_inputs:
        # print(array_input[0])
        pass

    algorithms = {
        "insertion_sort_r": insertion_sort.sort,
        "merge_sort": merge_sort.sort,
    }

    for name, sort in algorithms.items():
        print("Algorithm: %s" % name)
        print("|", end='')
        print("-" * 40, end='|\n')
        print("| %s \t| \t%s \t |" % ("Time (s)", "Array Size"))

        for array_input in array_inputs:
            copy_arr = list(array_input[0])
            size = len(copy_arr)
            with timeit(name, arr_times):
                sort(copy_arr, size, recursive=True)
                # pass

            print("| %.4f \t| \t%d \t\t |" % (arr_times[-1], array_input[0].shape[0]))
        print("|", end='')
        print("-" * 40, end='|\n')

        assert copy_arr == sorted(array_input[0])

    list_of_alg = [['insertion $\mathcal{O}(n^{2})$', array_sizes, arr_times[:10]],
                   ['merge $\mathcal{O}(n\log{}n)$', array_sizes, arr_times[10:]],
                   ]

    plot.plot(list_of_alg)
