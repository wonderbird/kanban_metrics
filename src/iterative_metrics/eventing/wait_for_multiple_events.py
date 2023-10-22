from typing import List

import inject

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.event_collection import EventCollection


class WaitForMultipleEvents:
    """
    Wait for multiple events and publish them as an EventCollection.

    When a policy requires multiple events to be published before it can
    execute its logic, it can use this class to wait for all events.

    Once this class has received all awaited events, it will publish an
    EventCollection containing all awaited events.

    Definition: A "policy" is a class that subscribes to events and
    publishes events. It is responsible for executing the logic of the
    application. In Domain Driven Design, policies reflect the business
    rules (when event, then logic).
    """

    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self, awaited_events: List[type]) -> None:
        self._awaited_events = awaited_events
        self._waiting_for = []
        self._events = EventCollection()
        self.subscribe_to_events()

    def subscribe_to_events(self):
        DynamicConsumer = type(
            "DynamicConsumer",
            (Consumer,),
            {
                "__init__": consumer_constructor,
                "consume": consumer_consume,
                "event_type": None,
                "_event_aggregator": inject.attr(EventAggregator),
                "_outer_class": None,
            },
        )

        for event_type in self._awaited_events:
            DynamicConsumer(event_type, self)
            self._waiting_for.append(event_type)

    def consume(self, event: object) -> None:
        if event.__class__ in self._waiting_for:
            self._events.append(event)
            self._waiting_for.remove(event.__class__)

        if not self._waiting_for:
            self._event_aggregator.publish(self._events)
            # TODO verify that the event is emptied after publishing


def consumer_constructor(
    self: Consumer, event_type: type, outer_class: WaitForMultipleEvents
):
    self.event_type = event_type
    self._event_aggregator.subscribe(self)
    self._outer_class = outer_class


def consumer_consume(self: Consumer, event: object) -> None:
    self._outer_class.consume(event)
