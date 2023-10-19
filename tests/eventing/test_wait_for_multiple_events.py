from typing import List

import inject

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class TestWaitForMultipleEventsIntegrationTest:
    _event_aggregator = EventAggregator()

    def setup_method(self) -> None:
        inject.clear_and_configure(
            lambda binder: binder.bind(EventAggregator, self._event_aggregator)
        )

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    def test_given_waiting_for_single_event_when_event_published(self, mocker):
        WaitForMultipleEvents(self.callback, [AwaitedEvent1])
        consumer = EventCollectionConsumer()
        mock_consume = mocker.patch.object(consumer, "consume", autospec=True)
        self._event_aggregator.publish(AwaitedEvent1())
        mock_consume.assert_called_once()

    def test_given_waiting_for_two_events_when_all_events_published(self, mocker):
        mock_callback = mocker.patch.object(self, "callback", autospec=True)
        WaitForMultipleEvents(self.callback, [AwaitedEvent1, AwaitedEvent3])
        self._event_aggregator.publish(AwaitedEvent1())
        self._event_aggregator.publish(AwaitedEvent3())
        mock_callback.assert_called_once()

    def callback(self) -> None:
        pass


class EventCollection:
    pass


class EventCollectionConsumer(Consumer):
    # TODO all event_aggregator properties should be private
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(EventCollection)
        self._event_aggregator.subscribe(self)

    def consume(self, event: EventCollection) -> None:
        pass


class AwaitedEvent1:
    pass


class AwaitedEvent2:
    pass


class AwaitedEvent3:
    pass


class WaitForMultipleEvents:
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self, callback: callable, awaited_events: List[type]) -> None:
        self.callback = callback
        self.awaited_events = awaited_events
        self.waiting_for = []
        self.subscribe_to_events()

    def subscribe_to_events(self):
        # TODO https://www.geeksforgeeks.org/create-classes-dynamically-in-python/
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

        for event_type in self.awaited_events:
            DynamicConsumer(event_type, self)
            self.waiting_for.append(event_type)

    def consume(self, event: object) -> None:
        if event.__class__ in self.waiting_for:
            self.waiting_for.remove(event.__class__)

        if not self.waiting_for:
            self._event_aggregator.publish(EventCollection())
            self.callback()


def consumer_constructor(
    self: Consumer, event_type: type, outer_class: WaitForMultipleEvents
):
    self.event_type = event_type
    self._event_aggregator.subscribe(self)
    self._outer_class = outer_class


def consumer_consume(self: Consumer, event: object) -> None:
    self._outer_class.consume(event)


class TestWaitForMultipleEventsConsume:
    _event_aggregator = EventAggregator()

    def setup_method(self, mocker) -> None:
        inject.clear_and_configure(
            lambda binder: binder.bind(EventAggregator, self._event_aggregator)
        )

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    def test_given_waiting_for_single_event_when_no_event_published(self, mocker):
        mock_publish = mocker.patch.object(
            self._event_aggregator, "publish", autospec=True
        )

        subject = WaitForMultipleEvents(self.callback, [AwaitedEvent1])
        subject.consume(None)

        mock_publish.assert_not_called()

    def test_given_waiting_for_single_event_when_event_published(self, mocker):
        mock_publish = mocker.patch.object(
            self._event_aggregator, "publish", autospec=True
        )
        subject = WaitForMultipleEvents(self.callback, [AwaitedEvent1])
        subject.consume(AwaitedEvent1())
        mock_publish.assert_called_once()

    def test_given_waiting_for_two_events_when_only_one_event_published(self, mocker):
        mock_publish = mocker.patch.object(
            self._event_aggregator, "publish", autospec=True
        )
        subject = WaitForMultipleEvents(self.callback, [AwaitedEvent1, AwaitedEvent2])
        subject.consume(AwaitedEvent1())
        mock_publish.assert_not_called()

    def test_given_waiting_for_two_events_when_all_events_published(self, mocker):
        mock_publish = mocker.patch.object(
            self._event_aggregator, "publish", autospec=True
        )

        subject = WaitForMultipleEvents(self.callback, [AwaitedEvent1, AwaitedEvent3])
        subject.consume(AwaitedEvent1())
        subject.consume(AwaitedEvent3())
        mock_publish.assert_called_once()

    def callback(self) -> None:
        pass
