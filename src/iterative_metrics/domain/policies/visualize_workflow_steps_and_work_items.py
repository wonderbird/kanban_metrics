import inject

from iterative_metrics.adapters.outbound.debug_image import (
    debug_show_rectangles_in_image,
)
from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.event_collection import EventCollection
from iterative_metrics.eventing.wait_for_multiple_events import WaitForMultipleEvents


class VisualizeWorkflowStepsAndWorkItems(Consumer):
    """Show work items and workflow steps in screenshot."""

    _event_aggregator = inject.attr(EventAggregator)

    def __init__(self) -> None:
        super().__init__(EventCollection)
        self._event_aggregator.subscribe(self)

    def consume(self, event: EventCollection) -> None:
        if (
            not event.contains(BoardScreenshotUpdated)
            or not event.contains(PotentialWorkflowStepsFound)
            or not event.contains(WorkItemsFound)
        ):
            return

        screenshot = event.last(BoardScreenshotUpdated).screenshot
        workflow_steps = event.last(PotentialWorkflowStepsFound).workflow_steps
        work_items = event.last(WorkItemsFound).work_items

        rectangles = [work_item.bounding_rectangle for work_item in work_items]
        rectangles += [
            workflow_step.bounding_rectangle for workflow_step in workflow_steps
        ]
        debug_show_rectangles_in_image(screenshot, rectangles)
