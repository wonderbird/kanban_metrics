from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator


class BoardScreenshotController:
    def __init__(self, event_aggregator: EventAggregator) -> None:
        self.event_aggregator = event_aggregator

    def read_board_screenshot(self) -> None:
        """Inform the system that the board screenshot has been updated."""
        self.event_aggregator.publish(BoardScreenshotUpdated())
