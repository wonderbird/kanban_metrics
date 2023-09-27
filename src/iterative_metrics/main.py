from pathlib import Path

import inject

from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.adapters.inbound.count_work_items_in_image import (
    count_work_items_in_image,
)
from iterative_metrics.adapters.inbound.cumulative_flow_diagram import (
    cumulative_flow_diagram,
)
from iterative_metrics.adapters.outbound.board_screenshot_file import (
    BoardScreenshotFile,
)
from iterative_metrics.domain.ports import BoardScreenshotStorage
from iterative_metrics.eventing.event_aggregator import EventAggregator

BOARD_SCREENSHOT_PATH = (
    Path(__file__).parent.parent.parent.resolve() / "client-data" / "kanban_board.png"
)


@inject.params(
    event_aggregator=EventAggregator,
    board_screenshot_storage=BoardScreenshotStorage,
)
def main(
    event_aggregator: EventAggregator = None,
    board_screenshot_storage: BoardScreenshotStorage = None,
) -> None:
    BoardScreenshotController(
        event_aggregator, board_screenshot_storage
    ).read_board_screenshot()

    if BOARD_SCREENSHOT_PATH.exists():
        number_of_work_items = count_work_items_in_image(BOARD_SCREENSHOT_PATH)
        print(
            f"{number_of_work_items} work_items identified in {BOARD_SCREENSHOT_PATH}"
        )

    cumulative_flow_diagram()


def configuration(binder: inject.Binder) -> None:
    binder.bind(EventAggregator, EventAggregator())
    binder.bind(BoardScreenshotStorage, BoardScreenshotFile(BOARD_SCREENSHOT_PATH))


if __name__ == "__main__":
    inject.configure(configuration)
    main()
