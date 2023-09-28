from pathlib import Path

import cv2
import inject

from iterative_metrics.adapters.outbound.board_screenshot_file import (
    BoardScreenshotFile,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.main import main

BOARD_SCREENSHOT_PATH = (
    Path(__file__).parent.parent.parent.resolve() / "client-data" / "kanban_board.png"
)


def test_main():
    inject.clear_and_configure(configuration)
    event_consumer_mock = EventConsumerMock()

    main()

    expected_screenshot = cv2.imread(str(BOARD_SCREENSHOT_PATH))
    assert event_consumer_mock.event.screenshot.shape == expected_screenshot.shape


def configuration(binder: inject.Binder) -> None:
    binder.bind(EventAggregator, EventAggregator())
    binder.bind(BoardScreenshotStorage, BoardScreenshotFile(BOARD_SCREENSHOT_PATH))


class EventConsumerMock(Consumer):
    event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(BoardScreenshotUpdated)
        self.event = None
        self.event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotFile) -> None:
        self.event = event
