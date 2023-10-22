from typing import Optional


class EventCollection:
    """A collection of events that have been waited for."""

    def __init__(self) -> None:
        self._events = []

    def append(self, event: object) -> None:
        self._events.append(event)

    def last(self, event_type: type) -> Optional[object]:
        # TODO check that the correct value is returned if no event received
        return self._events[-1]
