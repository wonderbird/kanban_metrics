from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)


class BoardScreenshotController:
    def __init__(self, event_aggregator):
        self.event_aggregator = event_aggregator

    def read_board_screenshot(self):
        """Inform the system that the board screenshot has been updated."""
        self.event_aggregator.publish(BoardScreenshotUpdated())
