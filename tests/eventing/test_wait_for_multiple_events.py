import inject
import pytest

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.event_collection import EventCollection
from iterative_metrics.eventing.wait_for_multiple_events import WaitForMultipleEvents


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
