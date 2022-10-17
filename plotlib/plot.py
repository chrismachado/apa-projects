import matplotlib.pyplot as plt


def plot(data, default='list of data'):
    if default == 'list of data':
        __plot(data)


def __plot(list_of_alg):
    for algorithm in list_of_alg:
        name = algorithm[0]
        data = algorithm[1]
        time = algorithm[2]
        plt.plot(data, time, markersize=20, label=name)
    plt.xlabel("Array length")
    plt.ylabel("Time in second")
    plt.legend()
    plt.show()
