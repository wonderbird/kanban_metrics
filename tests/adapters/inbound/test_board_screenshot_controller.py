import numpy as np

from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.ports.BoardScreenshotStorage import BoardScreenshotStorage
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_read_board_screenshot():
    event_aggregator = EventAggregator()
    consumer = BoardScreenshotUpdatedConsumerMock(event_aggregator)

    fake_screenshot = np.zeros((10, 9, 3), dtype=np.uint8)
    screenshot_storage_stub = BoardScreenshotStorageStub(fake_screenshot)

    subject = BoardScreenshotController(event_aggregator, screenshot_storage_stub)
    subject.read_board_screenshot()

    expected_screenshot_shape = fake_screenshot.shape
    assert consumer.event.screenshot.shape == expected_screenshot_shape


class BoardScreenshotStorageStub(BoardScreenshotStorage):
    def __init__(self, screenshot: np.ndarray) -> None:
        self.screenshot = screenshot

    def read_board_screenshot(self) -> np.ndarray:
        return self.screenshot


class BoardScreenshotUpdatedConsumerMock(Consumer):
    def __init__(self, event_aggregator: EventAggregator) -> None:
        super().__init__(BoardScreenshotUpdated)

        self.event = None

        event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotUpdated) -> None:
        self.event = event
