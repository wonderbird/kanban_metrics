from typing import Any

from iterative_metrics.eventing.consumer import Consumer


class EventAggregator:
    """
    Minimal event aggregator, no thread safety, prevents consumers from being garbage collected.
    """

    def __init__(self) -> None:
        self.consumers = {}

    def subscribe(self, consumer: Consumer) -> None:
        event_type_name = consumer.event_type.__name__

        if not self.has_consumers(event_type_name):
            self.consumers[event_type_name] = []

        self.consumers[event_type_name].append(consumer)

    def publish(self, event: Any) -> None:
        event_type_name = event.__class__.__name__

        if not self.has_consumers(event_type_name):
            return

        for consumer in self.consumers[event_type_name]:
            consumer.consume(event)

    def has_consumers(self, event_type_name: Any) -> bool:
        return event_type_name in self.consumers
