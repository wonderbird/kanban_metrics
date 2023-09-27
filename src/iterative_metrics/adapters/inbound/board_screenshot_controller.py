from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.ports import BoardScreenshotStorage
from iterative_metrics.eventing.event_aggregator import EventAggregator


class BoardScreenshotController:
    def __init__(
        self,
        event_aggregator: EventAggregator,
        board_screenshot_storage: BoardScreenshotStorage,
    ) -> None:
        self.event_aggregator = event_aggregator
        self.board_screenshot_storage = board_screenshot_storage

    def read_board_screenshot(self) -> None:
        """Inform the system that the board screenshot has been updated."""
        screenshot = self.board_screenshot_storage.read_board_screenshot()
        self.event_aggregator.publish(BoardScreenshotUpdated(screenshot))
