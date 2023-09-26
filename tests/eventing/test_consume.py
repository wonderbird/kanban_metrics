from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_when_subscribed_to_event():
    event_aggregator = EventAggregator()

    subscriber = FirstSubscriber()
    event_aggregator.subscribe(subscriber)

    event_aggregator.publish(FirstEvent("Hello World!"))

    assert subscriber.received_event.message == "Hello World!"


def test_when_subscribed_to_different_event():
    event_aggregator = EventAggregator()

    firstSubscriber = FirstSubscriber()
    event_aggregator.subscribe(firstSubscriber)
    secondSubscriber = SecondEventSubscriber()
    event_aggregator.subscribe(secondSubscriber)

    event_aggregator.publish(FirstEvent("This message is ignored"))

    assert not secondSubscriber.received_event


class FirstEvent:
    def __init__(self, message):
        self._message = message

    # getter for message property
    @property
    def message(self):
        return self._message


class FirstSubscriber:
    def __init__(self):
        self.received_event = None
        self.event_type = FirstEvent

    def consume(self, event):
        self.received_event = event


class SecondEvent:
    pass


class SecondEventSubscriber:
    def __init__(self):
        self.received_event = None
        self.event_type = SecondEvent

    def consume(self, event):
        self.received_event = event
