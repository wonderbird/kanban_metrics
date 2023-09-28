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


class TestMain:
    board_screenshot_path = (
        Path(__file__).parent.parent.resolve()
        / "data"
        / "full_board_width_808px_height_959px_resolution_96dpi.png"
    )

    def setup_method(self) -> None:
        inject.clear_and_configure(self.configuration)

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    def configuration(self, binder: inject.Binder) -> None:
        binder.bind(EventAggregator, EventAggregator())
        binder.bind(
            BoardScreenshotStorage, BoardScreenshotFile(self.board_screenshot_path)
        )

    def test_main(self):
        event_consumer_mock = self.EventConsumerMock()

        main()

        expected_screenshot = cv2.imread(str(self.board_screenshot_path))
        assert event_consumer_mock.event.screenshot.shape == expected_screenshot.shape

    class EventConsumerMock(Consumer):
        event_aggregator = inject.attr(EventAggregator)

        def __init__(self) -> None:
            super().__init__(BoardScreenshotUpdated)
            self.event = None
            self.event_aggregator.subscribe(self)

        def consume(self, event: BoardScreenshotFile) -> None:
            self.event = event
