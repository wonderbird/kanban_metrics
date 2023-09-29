import inject

from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class ProcessBoardScreenshot(Consumer):
    event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(BoardScreenshotUpdated)
        self.event_aggregator.subscribe(self)

    def consume(self, event: BoardScreenshotUpdated) -> None:
        work_items = WorkItems.parse_screenshot(event.screenshot)
        self.event_aggregator.publish(WorkItemsFound(work_items))

        workflow_steps = WorkflowSteps.parse_screenshot(event.screenshot)
        self.event_aggregator.publish(PotentialWorkflowStepsFound(workflow_steps))
