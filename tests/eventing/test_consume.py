from iterative_metrics.eventing.event_aggregator import EventAggregator


def test_when_subscribed_to_event():
    event_aggregator = EventAggregator()

    subscriber = FirstSubscriber()
    event_aggregator.subscribe(subscriber)

    event_aggregator.publish(FirstEvent())

    assert subscriber.received_event


def test_when_subscribed_to_different_event():
    event_aggregator = EventAggregator()

    firstSubscriber = FirstSubscriber()
    event_aggregator.subscribe(firstSubscriber)
    secondSubscriber = SecondEventSubscriber()
    event_aggregator.subscribe(secondSubscriber)

    event_aggregator.publish(FirstEvent())

    assert not secondSubscriber.received_event


class FirstEvent:
    pass


class FirstSubscriber:
    def __init__(self):
        self.received_event = False
        self.event_type = FirstEvent

    def consume(self):
        self.received_event = True


class SecondEvent:
    pass


class SecondEventSubscriber:
    def __init__(self):
        self.received_event = False
        self.event_type = SecondEvent

    def consume(self):
        self.received_event = True
