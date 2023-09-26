from iterative_metrics.adapters.inbound.board_screenshot_controller import (
    BoardScreenshotController,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_read_board_screenshot():
    event_aggregator = EventAggregator()
    consumer = BoardScreenshotUpdatedConsumerMock(event_aggregator)

    BoardScreenshotController(event_aggregator).read_board_screenshot()

    assert consumer.event is not None


class BoardScreenshotUpdatedConsumerMock(Consumer):
    def __init__(self, event_aggregator: EventAggregator) -> None:
        super().__init__(BoardScreenshotUpdated)

        self.event = None

        event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotUpdated) -> None:
        self.event = event
