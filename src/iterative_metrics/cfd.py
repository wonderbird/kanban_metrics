import matplotlib.pyplot as plt


def cfd():
    #%% Stack plot
    workdays = [4, 5, 6, 7, 8]
    metrics = {
        'done': [0, 1, 5, 5, 6],
        'share': [4, 3, 0, 1, 0],
        'doing': [2, 2, 1, 2, 2],
        'agreed': [0, 0, 1, 2, 2],
    }

    # plot
    fig, ax = plt.subplots()

    ax.stackplot(workdays, metrics.values(), labels=metrics.keys(), alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Cumulative flow diagram for Team ITerative')
    ax.set_xlabel('Day in September 2023')
    ax.set_ylabel('Number of work items')

    plt.show()
