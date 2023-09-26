from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_read_board_screenshot():
    event_aggregator = EventAggregator()
    subscriber = BoardScreenshotUpdatedSubscriberMock(event_aggregator)

    BoardScreenshotController(event_aggregator).read_board_screenshot()

    assert subscriber.event is not None


class BoardScreenshotUpdatedSubscriberMock:
    def __init__(self, event_aggregator):
        self.event_type = BoardScreenshotUpdated

        self.event = None

        event_aggregator.subscribe(self)

    def consume(self, event):
        self.event = event
