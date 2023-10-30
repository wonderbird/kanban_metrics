import inject

from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.workflow_steps_found import WorkflowStepsFound
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class ConsiderTeamBoardCustomization(Consumer):
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(PotentialWorkflowStepsFound)
        self._event_aggregator.subscribe(self)

    def consume(self, event: PotentialWorkflowStepsFound) -> None:
        used_workflow_step_indices = [1, 2, 4, 5, 7, 8, 9, 10, 11]

        filtered_workflow_steps = [
            event.workflow_steps[index] for index in used_workflow_step_indices
        ]

        self._event_aggregator.publish(
            WorkflowStepsFound(WorkflowSteps(filtered_workflow_steps))
        )
