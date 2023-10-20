from typing import List

import inject
import pytest

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class EventCollection:
    pass


class EventCollectionConsumer(Consumer):
    # TODO all event_aggregator properties should be private in all consumers
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(EventCollection)
        self._event_aggregator.subscribe(self)

    def consume(self, event: EventCollection) -> None:
        pass


class TestWaitForMultipleEventsIntegrationTest:
    _event_aggregator = None
    _consumer = None

    def setup_method(self) -> None:
        # TODO: Document the following near the EventAggregator class:
        # EventAggregator and consumers must be initialized for each test.
        # Otherwise, the both will be shared between tests and the
        # tests will interfere with each other.
        self._event_aggregator = EventAggregator()

        inject.clear_and_configure(
            lambda binder: binder.bind(EventAggregator, self._event_aggregator)
        )

        self._consumer = EventCollectionConsumer()

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    @pytest.fixture
    def mock_consume(self, mocker):
        return mocker.patch.object(self._consumer, "consume", autospec=True)

    def test_given_waiting_for_single_event_when_event_published(self, mock_consume):
        WaitForMultipleEvents([AwaitedEvent1])
        self._event_aggregator.publish(AwaitedEvent1())
        mock_consume.assert_called_once()

    def test_given_waiting_for_two_events_when_all_events_published(self, mock_consume):
        WaitForMultipleEvents([AwaitedEvent1, AwaitedEvent3])
        self._event_aggregator.publish(AwaitedEvent1())
        self._event_aggregator.publish(AwaitedEvent3())
        mock_consume.assert_called_once()


class AwaitedEvent1:
    pass


class AwaitedEvent2:
    pass


class AwaitedEvent3:
    pass


class WaitForMultipleEvents:
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self, awaited_events: List[type]) -> None:
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

    @pytest.fixture
    def mock_publish(self, mocker):
        return mocker.patch.object(self._event_aggregator, "publish", autospec=True)

    def test_given_waiting_for_single_event_when_no_event_published(self, mock_publish):
        subject = WaitForMultipleEvents([AwaitedEvent1])
        subject.consume(None)
        mock_publish.assert_not_called()

    def test_given_waiting_for_single_event_when_event_published(self, mock_publish):
        subject = WaitForMultipleEvents([AwaitedEvent1])
        subject.consume(AwaitedEvent1())
        mock_publish.assert_called_once()

    def test_given_waiting_for_two_events_when_only_one_event_published(
        self, mock_publish
    ):
        subject = WaitForMultipleEvents([AwaitedEvent1, AwaitedEvent2])
        subject.consume(AwaitedEvent1())
        mock_publish.assert_not_called()

    def test_given_waiting_for_two_events_when_all_events_published(self, mock_publish):
        subject = WaitForMultipleEvents([AwaitedEvent1, AwaitedEvent3])
        subject.consume(AwaitedEvent1())
        subject.consume(AwaitedEvent3())
        mock_publish.assert_called_once()
