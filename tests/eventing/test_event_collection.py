import pytest

from iterative_metrics.eventing.event_collection import EventCollection


class TestEventCollection:
    def test_last_given_no_events_received(self):
        event_collection = EventCollection()
        with pytest.raises(KeyError):
            event_collection.last(object)

    def test_append_given_one_event(self):
        event_collection = EventCollection()
        event_collection.append(Event1(1))
        last_event = event_collection.last(Event1)
        assert type(last_event) is Event1
        assert last_event.value == 1

    def test_append_given_two_events_of_same_type(self):
        event_collection = EventCollection()
        event_collection.append(Event1(1))
        event_collection.append(Event1(2))
        last_event = event_collection.last(Event1)
        assert type(last_event) is Event1
        assert last_event.value == 2

    def test_append_given_two_events_of_different_type(self):
        event_collection = EventCollection()
        event_collection.append(Event1(1))
        event_collection.append(Event2(2))

        last_event1 = event_collection.last(Event1)
        assert type(last_event1) is Event1
        assert last_event1.value == 1

        last_event2 = event_collection.last(Event2)
        assert type(last_event2) is Event2
        assert last_event2.value == 2


class Event1:
    def __init__(self, value: int = 0) -> None:
        self.value = value


class Event2:
    def __init__(self, value: int = 0) -> None:
        self.value = value
