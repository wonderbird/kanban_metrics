import matplotlib.pyplot as plt


def cumulative_flow_diagram():
    # %% Stack plot
    dates = [
        "28.08.23 16:30",
        "29.08.23 16:30",
        "30.08.23 16:30",
        "31.08.23 16:30",
        "01.09.23 16:30",
        "04.09.23 16:30",
        "05.09.23 16:30",
        "06.09.23 16:30",
        "07.09.23 16:30",
        "08.09.23 16:30",
    ]
    metrics = {
        "done        ": [0, 8, 8, 8, 8, 8, 8, 8, 8, 18],
        "share       ": [8, 0, 0, 0, 0, 1, 3, 4, 6, 1],
        "doing_cobo  ": [0, 2, 2, 3, 3, 3, 3, 3, 2, 2],
        "doing_other ": [1, 2, 3, 3, 3, 2, 3, 3, 3, 2],
        "agreed_cobo ": [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        "agreed_other": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    }

    show_cumulative_flow_diagram(dates, metrics)


def show_cumulative_flow_diagram(dates, metrics):
    fig, ax = plt.subplots()
    ax.stackplot(dates, metrics.values(), labels=metrics.keys(), alpha=0.8)
    fig.autofmt_xdate(rotation=45)
    ax.set_title("Cumulative Flow Diagram for Team ITerative")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of work items")
    ax.legend(loc="upper left", reverse=True)
    plt.show()
