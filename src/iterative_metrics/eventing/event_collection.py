from typing import Optional


class EventCollection:
    """A collection of events that have been waited for."""

    def __init__(self) -> None:
        self._events = {}

    def append(self, event: object) -> None:
        type_name = type(event).__name__
        self._events[type_name] = event

    def last(self, event_type: type) -> Optional[object]:
        """
        Return the last event of the given type.

        :raises KeyError: if no event of the type given as key has been received
        """

        # TODO check that the correct value is returned if no event received
        type_name = event_type.__name__
        return self._events[type_name]
