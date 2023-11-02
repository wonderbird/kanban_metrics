import inject

from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.domain.events.workflow_steps_found import WorkflowStepsFound
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.event_collection import EventCollection


class ConsiderTeamBoardCustomization(Consumer):
    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(EventCollection)
        self._event_aggregator.subscribe(self)

    def consume(self, event: EventCollection) -> None:
        if not (
            event.contains(PotentialWorkflowStepsFound)
            and event.contains(WorkItemsFound)
        ):
            return

        workflow_steps = event.last(PotentialWorkflowStepsFound).workflow_steps
        work_items = event.last(WorkItemsFound).work_items
        workflow_steps.remove_areas_smaller_than_a_work_item(work_items)

        used_workflow_step_indices = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        filtered_workflow_steps = [
            workflow_steps[index] for index in used_workflow_step_indices
        ]

        self._event_aggregator.publish(
            WorkflowStepsFound(WorkflowSteps(filtered_workflow_steps))
        )
