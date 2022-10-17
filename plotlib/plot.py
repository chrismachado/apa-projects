import matplotlib.pyplot as plt


def plot(data, default='list of data'):
    if default == 'list of data':
        __plot(data)


def __plot(list_of_alg):
    for algorithm in list_of_alg:
        name = algorithm[0]
        data = algorithm[1]
        time = algorithm[2]

        default_x_ticks = range(len(data))
        plt.xticks(default_x_ticks, data)

        plt.plot(default_x_ticks, time, markersize=20, label=name)
    plt.title("Insertion Sort Recursive x Merge Sort")
    plt.xlabel("Array length")
    plt.ylabel("Time in second")
    plt.legend()
    plt.show()
