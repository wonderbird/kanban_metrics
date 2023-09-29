import logging
from typing import Any

import inject

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class LogEvent(Consumer):
    """Log the string representation of captured events."""

    event_aggregator = inject.attr(EventAggregator)
    logger = logging.getLogger(__name__)

    def __init__(self, event_type: Any) -> None:
        super().__init__(event_type)
        self.event_aggregator.subscribe(self)

    def consume(self, event: Any) -> None:
        self.logger.info(str(event))
