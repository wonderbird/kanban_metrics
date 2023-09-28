import inject
import numpy as np

from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class TestBoardScreenshotController:
    fake_screenshot = np.zeros((10, 9, 3), dtype=np.uint8)

    def setup_method(self) -> None:
        inject.clear_and_configure(self.configuration)

    def configuration(self, binder: inject.Binder) -> None:
        binder.bind(EventAggregator, EventAggregator())
        binder.bind(
            BoardScreenshotStorage,
            self.BoardScreenshotStorageStub(self.fake_screenshot),
        )

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    def test_read_board_screenshot(self):
        consumer = self.BoardScreenshotUpdatedConsumerMock()

        subject = BoardScreenshotController()
        subject.read_screenshot()

        expected_screenshot_shape = self.fake_screenshot.shape
        assert consumer.event.screenshot.shape == expected_screenshot_shape

    class BoardScreenshotStorageStub(BoardScreenshotStorage):
        def __init__(self, screenshot: np.ndarray) -> None:
            self.screenshot = screenshot

        def read_screenshot(self) -> np.ndarray:
            return self.screenshot

    class BoardScreenshotUpdatedConsumerMock(Consumer):
        event_aggregator = inject.attr(EventAggregator)

        def __init__(self) -> None:
            super().__init__(BoardScreenshotUpdated)
            self.event_aggregator.subscribe(self)
            self.event = None

        def consume(self, event: BoardScreenshotUpdated) -> None:
            self.event = event
