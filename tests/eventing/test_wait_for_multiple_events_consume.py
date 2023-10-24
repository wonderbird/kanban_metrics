import inject
import pytest

from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.wait_for_multiple_events import WaitForMultipleEvents


class TestWaitForMultipleEventsConsume:
    _event_aggregator = EventAggregator()

    def setup_method(self) -> None:
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
        (actual_event,) = mock_publish.call_args[0]
        assert type(actual_event.last(AwaitedEvent1)) is AwaitedEvent1
        assert type(actual_event.last(AwaitedEvent3)) is AwaitedEvent3

    def test_given_waiting_for_two_events_and_all_events_published_when_another_event_published(
        self, mock_publish
    ):
        subject = WaitForMultipleEvents([AwaitedEvent1, AwaitedEvent2])
        subject.consume(AwaitedEvent1())
        subject.consume(AwaitedEvent2())

        # publish should be called after both events have been consumed
        mock_publish.assert_called_once()

        subject.consume(AwaitedEvent1())

        # publish may not be called after a single event has been consumed
        mock_publish.assert_called_once()

    def test_given_waiting_for_two_events_when_all_events_published_twice(
        self, mock_publish
    ):
        subject = WaitForMultipleEvents([AwaitedEvent1, AwaitedEvent2])
        subject.consume(AwaitedEvent1())
        subject.consume(AwaitedEvent2())
        subject.consume(AwaitedEvent1())
        subject.consume(AwaitedEvent2())

        assert mock_publish.call_count == 2


class AwaitedEvent1:
    pass


class AwaitedEvent2:
    pass


class AwaitedEvent3:
    pass
