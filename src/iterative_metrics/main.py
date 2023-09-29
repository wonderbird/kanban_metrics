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
from iterative_metrics.domain.policies.log_event import LogEvent
from iterative_metrics.domain.policies.process_board_screenshot import (
    ProcessBoardScreenshot,
)
from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator

BOARD_SCREENSHOT_PATH = (
    Path(__file__).parent.parent.parent.resolve() / "client-data" / "kanban_board.png"
)


def main() -> None:
    inject.configure(dependencies)
    configure_event_handling_policies()

    BoardScreenshotController().read_screenshot()

    cumulative_flow_diagram()


def dependencies(binder: inject.Binder) -> None:
    """Configure dependencies, i.e. repositories, infrastructure, etc."""
    binder.bind(EventAggregator, EventAggregator())
    binder.bind(BoardScreenshotStorage, BoardScreenshotFile(BOARD_SCREENSHOT_PATH))


def configure_event_handling_policies():
    ProcessBoardScreenshot()
    LogEvent()


if __name__ == "__main__":
    main()
