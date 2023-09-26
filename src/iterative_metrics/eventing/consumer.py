from typing import Any


class Consumer:
    def __init__(self, event_type: Any) -> None:
        self.event_type = event_type

    def consume(self, event: Any) -> None:
        raise NotImplementedError()
