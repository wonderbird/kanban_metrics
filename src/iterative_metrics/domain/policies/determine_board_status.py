import inject

from iterative_metrics.domain.events.board_status_determined import (
    BoardStatusDetermined,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.event_collection import EventCollection


class DetermineBoardStatus(Consumer):
    """
    Associate workflow steps with work items.

    This policy combines event listeners for WorkItemsFound and
    PotentialWorkflowStepsFound. When both events have been received, it
    associates the workflow steps with the work items and publishes a
    BoardStatusDetermined event.
    """

    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(EventCollection)
        self._event_aggregator.subscribe(self)

    def consume(self, event: EventCollection) -> None:
        if not (
            event.contains(WorkItemsFound)
            and event.contains(PotentialWorkflowStepsFound)
        ):
            return

        work_items = event.last(WorkItemsFound).work_items
        workflow_steps = event.last(PotentialWorkflowStepsFound).workflow_steps

        workflow_steps.associate_with(work_items)

        self._event_aggregator.publish(BoardStatusDetermined(workflow_steps))
