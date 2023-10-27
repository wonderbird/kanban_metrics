import inject

from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.workflow_steps_found import WorkflowStepsFound
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class ConsiderTeamBoardCustomization(Consumer):
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(PotentialWorkflowStepsFound)
        self._event_aggregator.subscribe(self)

    def consume(self, event: PotentialWorkflowStepsFound) -> None:
        workflow_steps = event.workflow_steps

        self._event_aggregator.publish(WorkflowStepsFound(workflow_steps))
