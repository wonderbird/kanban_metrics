from pathlib import Path

import cv2

from iterative_metrics.adapters.outbound.board_screenshot_file import (
    BoardScreenshotFile,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.main import main

BOARD_SCREENSHOT_PATH = (
    Path(__file__).parent.parent.parent.resolve() / "client-data" / "kanban_board.png"
)


class EventConsumerMock(Consumer):
    def __init__(self, event_aggregator: EventAggregator) -> None:
        super().__init__(BoardScreenshotUpdated)
        self.event = None
        event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotFile) -> None:
        self.event = event


def test_main():
    event_aggregator = EventAggregator()
    event_consumer_mock = EventConsumerMock(event_aggregator)

    board_screenshot_file = BoardScreenshotFile(BOARD_SCREENSHOT_PATH)
    main(event_aggregator, board_screenshot_file)

    expected_screenshot = cv2.imread(str(BOARD_SCREENSHOT_PATH))
    assert event_consumer_mock.event.screenshot.shape == expected_screenshot.shape
