import matplotlib.pyplot as plt


def cumulative_flow_diagram():
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
        "11.09.23 16:30",
        "12.09.23 16:30",
        "13.09.23 16:30",
        "14.09.23 16:30",
        "15.09.23 16:30",
        "18.09.23 16:30",
        "19.09.23 16:30",
        "20.09.23 16:30",
        "21.09.23 16:30",
        "22.09.23 16:30",
        "25.09.23 16:30",
        "26.09.23 16:30",
        "27.09.23 12:30",
        "28.09.23 16:30",
        "29.09.23 16:30",
        "02.10.23 16:00",
        "04.10.23 16:00", ## 03.10. skipped because of public holiday
    ]
    metrics = {
        "done                ": [
            0,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            18,
            18,
            20,
            20,
            20,
            20,
            20,
            20,
            20,
            20,
            24,
            24,
            24,
            28,
            28,
            28,
            28,
            28,
        ],
        ########## Data added by Nik ##################
        # 29.09.2023
        # +1 sharing columns| (email)
        # +1 doing CoBo     | (License Activation)
        # doing other       | hasn't changed
        # +2 agreed cobo    | since it was empty
        # agreed other      | hasn't changed
        # --------------------------------------------
        # 02.10.2023
        # +1 sharing columns| (License Activation)
        # doing CoBo        | (Trivy)
        # doing other       | hasn't changed
        # -1 agreed cobo    | started on Trivy
        # agreed other      | hasn't changed
        # --------------------------------------------
        # 02.10.2023
        # sharing columns   | (+2 Firefighting Code Review for 966 | AX/BT Problems Taskforce)
        # doing CoBo        | hasn't changed
        # doing other       | hasn't changed
        # agreed cobo       | hasn't changed
        # agreed other      | hasn't changed
        ##############################################
        "both sharing columns": [8, 0, 0, 0, 0, 1, 3, 4, 6, 1, 2, 0, 0, 0, 2, 2, 3, 5, 5, 2, 2, 2, 0, 1, 2, 3, 5],
        "doing cobo          ": [0, 2, 2, 3, 3, 3, 3, 3, 2, 2, 1, 2, 2, 3, 3, 3, 3, 2, 3, 2, 3, 3, 1, 0, 1, 1, 1],
        "doing other         ": [1, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "agreed cobo         ": [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1],
        "agreed other        ": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
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


if __name__ == "__main__":
    cumulative_flow_diagram()
