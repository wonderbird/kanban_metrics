import matplotlib.pyplot as plt


def cumulative_flow_diagram():
    #%% Stack plot
    workdays = ['04.09.2023', '05.09.2023', '06.09.2023', '07.09.2023', '08.09.2023']
    metrics = {
        'done': [0, 1, 5, 5, 6],
        'share': [4, 3, 0, 1, 0],
        'doing': [2, 2, 1, 2, 2],
        'agreed': [0, 0, 1, 2, 2],
    }

    fig, ax = plt.subplots()

    ax.stackplot(workdays, metrics.values(), labels=metrics.keys(), alpha=0.8)

    fig.autofmt_xdate(rotation=45)

    ax.set_title('Cumulative Flow Diagram for Team ITerative')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of work items')

    ax.legend(loc='upper left', reverse=True)

    plt.show()
