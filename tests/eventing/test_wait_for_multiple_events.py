import inject

from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class TestWaitForMultipleEvents:
    _event_aggregator = EventAggregator()

    def setup_method(self) -> None:
        inject.clear_and_configure(
            lambda binder: binder.bind(EventAggregator, self._event_aggregator)
        )

    @staticmethod
    def teardown_method() -> None:
        inject.clear()

    def test_given_waiting_for_single_event_when_no_event_published(self, mocker):
        mock_callback = mocker.patch.object(self, "callback", autospec=True)
        WaitForMultipleEvents(self.callback, [AwaitedEvent1()])
        mock_callback.assert_not_called()

    def test_given_waiting_for_single_event_when_event_published(self, mocker):
        mock_callback = mocker.patch.object(self, "callback", autospec=True)
        WaitForMultipleEvents(self.callback, [AwaitedEvent1()])
        self._event_aggregator.publish(AwaitedEvent1())
        mock_callback.assert_called_once()

    def test_given_waiting_for_two_events_when_only_one_event_published(self, mocker):
        mock_callback = mocker.patch.object(self, "callback", autospec=True)
        WaitForMultipleEvents(self.callback, [AwaitedEvent1(), AwaitedEvent2()])
        self._event_aggregator.publish(AwaitedEvent1())
        mock_callback.assert_not_called()

    def callback(self):
        pass


class AwaitedEvent1:
    pass


class AwaitedEvent2:
    pass


class WaitForMultipleEvents:
    event_aggregator = inject.attr(EventAggregator)

    def __init__(self, callback: callable, awaited_events: list) -> None:
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
                "event_aggregator": inject.attr(EventAggregator),
                "event_type": None,
            },
        )

        DynamicConsumer(AwaitedEvent1, self)
        self.waiting_for.append(AwaitedEvent1)

        DynamicConsumer(AwaitedEvent2, self)
        self.waiting_for.append(AwaitedEvent2)

    def consume(self, event: object) -> None:
        if event.__class__ in self.waiting_for:
            self.waiting_for.remove(event.__class__)

        if not self.waiting_for:
            self.callback()


def consumer_constructor(
    self: Consumer, event_type: type, outer_class: WaitForMultipleEvents
):
    self.event_type = event_type
    self.event_aggregator.subscribe(self)
    self.outer_class = outer_class


def consumer_consume(self: Consumer, event: object) -> None:
    self.outer_class.consume(event)
