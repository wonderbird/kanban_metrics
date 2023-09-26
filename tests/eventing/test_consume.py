from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_when_subscribed_to_event():
    event_aggregator = EventAggregator()

    consumer = FirstEventConsumer()
    event_aggregator.subscribe(consumer)

    event_aggregator.publish(FirstEvent("Hello World!"))

    assert consumer.received_event.message == "Hello World!"


def test_when_subscribed_to_different_event():
    event_aggregator = EventAggregator()

    firstConsumer = FirstEventConsumer()
    event_aggregator.subscribe(firstConsumer)
    secondConsumer = SecondEventConsumer()
    event_aggregator.subscribe(secondConsumer)

    event_aggregator.publish(FirstEvent("This message is ignored"))

    assert not secondConsumer.received_event


class FirstEvent:
    def __init__(self, message):
        self._message = message

    # getter for message property
    @property
    def message(self):
        return self._message


class FirstEventConsumer(Consumer):
    def __init__(self):
        super().__init__(FirstEvent)
        self.received_event = None

    def consume(self, event):
        self.received_event = event


class SecondEvent:
    pass


class SecondEventConsumer(Consumer):
    def __init__(self):
        super().__init__(SecondEvent)
        self.received_event = None

    def consume(self, event):
        self.received_event = event
