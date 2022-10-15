import numpy as np, contextlib, random, time
from sorting import (
    insertion_sort,
    merge_sort
)


@contextlib.contextmanager
def timeit(name):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print("The %s took: %.4fs" % (name, took))
    return took


if __name__ == '__main__':
    array_sizes = np.random.randint(10, 10001, 10)
    array_ninputs = np.random.randint(10, 21, 1)[0]
    array_inputs = [[np.random.uniform(-2 * array_size, 2 * array_size + 1, array_size) for i in range(array_ninputs)] for array_size in array_sizes]

    # print(array_inputs)
    for array_input in array_inputs:
        # print(array_input[0])
        pass

    # testing only
    number_of_items = 1001
    normal_arr = [random.randint(0, number_of_items) for i in range(number_of_items)]
    random.shuffle(normal_arr)
    # nearly_sorted_arr = nearly_sorted_array(number_of_items)
    reversed_arr = sorted(normal_arr, reverse=True)
    sorted_arr = sorted(normal_arr)

    algorithms = {
        "insertion_sort_r": insertion_sort.sort,
        "merge_sort": merge_sort.sort,
    }

    for name, sort in algorithms.items():
        for array_input in array_inputs:
            copy_arr = list(array_input[0])
            with timeit(name):
                sort(copy_arr)
            print("array size: %s" % array_input[0].shape)
            print("-" * 50)

        assert copy_arr == sorted(array_input[0])
