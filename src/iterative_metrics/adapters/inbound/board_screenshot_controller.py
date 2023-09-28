import inject

from iterative_metrics.domain.events.board_screenshot_updated_event import (
    BoardScreenshotUpdatedEvent,
)
from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator


class BoardScreenshotController:
    event_aggregator = inject.attr(EventAggregator)
    board_screenshot_storage = inject.attr(BoardScreenshotStorage)

    def read_screenshot(self) -> None:
        """Inform the system that the board screenshot has been updated."""
        screenshot = self.board_screenshot_storage.read_screenshot()
        self.event_aggregator.publish(BoardScreenshotUpdatedEvent(screenshot))
