import inject

from iterative_metrics.domain.events.board_status_determined import (
    BoardStatusDetermined,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class DetermineBoardStatus(Consumer):
    event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(PotentialWorkflowStepsFound)
        self.event_aggregator.subscribe(self)

    def consume(self, event: PotentialWorkflowStepsFound) -> None:
        self.event_aggregator.publish(BoardStatusDetermined(event.workflow_steps))
