from typing import Optional, Any


class EventCollection:
    """A collection of events that have been waited for."""

    def __init__(self) -> None:
        self._events = {}

    def append(self, event: Any) -> None:
        type_name = type(event).__name__
        self._events[type_name] = event

    def last(self, event_type: type) -> Optional[Any]:
        """
        Return the last event of the given type.

        :raises KeyError: if no event of the type given as key has been received
        """

        type_name = event_type.__name__
        return self._events[type_name]

    def contains(self, event_type: type) -> bool:
        type_name = event_type.__name__
        return type_name in self._events
