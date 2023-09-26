from pathlib import Path

import cv2

from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator


CLIENT_DATA_DIR = (
    Path(__file__).parent.parent.parent.parent.parent.resolve() / "client-data"
)


class BoardScreenshotController:
    def __init__(self, event_aggregator: EventAggregator) -> None:
        self.event_aggregator = event_aggregator

    def read_board_screenshot(self) -> None:
        """Inform the system that the board screenshot has been updated."""
        screenshot = cv2.imread((CLIENT_DATA_DIR / "kanban_board.png").__str__())
        self.event_aggregator.publish(BoardScreenshotUpdated(screenshot))
