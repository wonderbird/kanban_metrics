import pytest

from iterative_metrics.eventing.event_aggregator import EventAggregator


class Subscriber:
    def __init__(self):
        self.received_event = False

    def consume(self):
        self.received_event = True


def test_consume():
    event_aggregator = EventAggregator()
    subscriber = Subscriber()
    event_aggregator.subscribe(subscriber)
    event_aggregator.publish()
    assert subscriber.received_event
