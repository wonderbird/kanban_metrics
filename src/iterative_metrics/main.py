from pathlib import Path

import inject

from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.adapters.inbound.cumulative_flow_diagram import (
    cumulative_flow_diagram,
)
from iterative_metrics.adapters.outbound.board_screenshot_file import (
    BoardScreenshotFile,
)
from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator

BOARD_SCREENSHOT_PATH = (
    Path(__file__).parent.parent.parent.resolve() / "client-data" / "kanban_board.png"
)


def main() -> None:
    BoardScreenshotController().read_screenshot()

    cumulative_flow_diagram()


def configuration(binder: inject.Binder) -> None:
    binder.bind(EventAggregator, EventAggregator())
    binder.bind(BoardScreenshotStorage, BoardScreenshotFile(BOARD_SCREENSHOT_PATH))


if __name__ == "__main__":
    inject.configure(configuration)
    main()
