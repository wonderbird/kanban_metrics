import inject

from iterative_metrics.domain.events.board_screenshot_updated_event import (
    BoardScreenshotUpdatedEvent,
)
from iterative_metrics.domain.events.work_items_found_event import WorkItemsFoundEvent
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class ProcessBoardScreenshot(Consumer):
    event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(BoardScreenshotUpdatedEvent)
        self.event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotUpdatedEvent) -> None:
        work_items = WorkItems.parse_screenshot(event.screenshot)
        self.event_aggregator.publish(WorkItemsFoundEvent(work_items))
