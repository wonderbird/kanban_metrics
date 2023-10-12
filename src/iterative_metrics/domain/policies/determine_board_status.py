import inject

from iterative_metrics.domain.events.board_status_determined import (
    BoardStatusDetermined,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class DetermineBoardStatus:
    """
    Associate workflow steps with work items.

    This policy combines event listeners for WorkItemsFound and
    PotentialWorkflowStepsFound. When both events have been received, it
    associates the workflow steps with the work items and publishes a
    BoardStatusDetermined event.
    """

    event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        self._work_items = None
        self._workflow_steps = None
        DetermineBoardStatus.PotentialWorkflowStepsFound(self)
        DetermineBoardStatus.WorkItemsFound(self)

    def process_workflow_steps(self, workflow_steps: WorkflowSteps) -> None:
        self._workflow_steps = workflow_steps
        self.try_associate_workflow_steps_with_work_items()

    def process_work_items(self, work_items: WorkItems) -> None:
        self._work_items = work_items
        self.try_associate_workflow_steps_with_work_items()

    def try_associate_workflow_steps_with_work_items(self):
        if self._work_items is not None and self._workflow_steps is not None:
            self._workflow_steps.associate_with(self._work_items)
            self.event_aggregator.publish(BoardStatusDetermined(self._workflow_steps))

    class PotentialWorkflowStepsFound(Consumer):
        event_aggregator = inject.attr(EventAggregator)

        def __init__(self, outer_class) -> None:
            super().__init__(PotentialWorkflowStepsFound)
            self.event_aggregator.subscribe(self)
            self.outer_class = outer_class

        def consume(self, event: PotentialWorkflowStepsFound) -> None:
            self.outer_class.process_workflow_steps(event.workflow_steps)

    class WorkItemsFound(Consumer):
        event_aggregator = inject.attr(EventAggregator)

        def __init__(self, outer_class) -> None:
            super().__init__(WorkItemsFound)
            self.event_aggregator.subscribe(self)
            self.outer_class = outer_class

        def consume(self, event: WorkItemsFound) -> None:
            self.outer_class.process_work_items(event.work_items)
