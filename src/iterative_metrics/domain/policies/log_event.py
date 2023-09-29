import logging

import inject

from iterative_metrics.domain.events.work_items_found_event import WorkItemsFoundEvent
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class LogEvent(Consumer):
    """Log the string representation of captured events."""

    event_aggregator = inject.attr(EventAggregator)
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__(WorkItemsFoundEvent)
        self.event_aggregator.subscribe(self)

    def consume(self, event: WorkItemsFoundEvent) -> None:
        self.logger.info(str(event))
