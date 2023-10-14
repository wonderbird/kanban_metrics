import inject
import numpy as np

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
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.consumer import Consumer
from iterative_metrics.eventing.event_aggregator import EventAggregator


class VisualizeWorkflowStepsAndWorkItems:
    """Show work items and workflow steps in screenshot."""

    def __init__(self) -> None:
        self._screenshot = None
        self._work_items = None
        self._workflow_steps = None
        VisualizeWorkflowStepsAndWorkItems.BoardScreenshotUpdated(self)
        VisualizeWorkflowStepsAndWorkItems.PotentialWorkflowStepsFound(self)
        VisualizeWorkflowStepsAndWorkItems.WorkItemsFound(self)

    def process_board_screenshot(self, screenshot: np.ndarray) -> None:
        self._screenshot = screenshot
        self.try_display_workflow_steps_and_work_items()

    def process_workflow_steps(self, workflow_steps: WorkflowSteps) -> None:
        self._workflow_steps = workflow_steps
        self.try_display_workflow_steps_and_work_items()

    def process_work_items(self, work_items: WorkItems) -> None:
        self._work_items = work_items
        self.try_display_workflow_steps_and_work_items()

    def try_display_workflow_steps_and_work_items(self):
        if (
            self._screenshot is None
            or self._work_items is None
            or self._workflow_steps is None
        ):
            return

        rectangles = [work_item.bounding_rectangle for work_item in self._work_items]
        rectangles += [
            workflow_step.bounding_rectangle for workflow_step in self._workflow_steps
        ]
        debug_show_rectangles_in_image(self._screenshot, rectangles)
        # TODO refactor this class to remove code duplication in sub classes

    class BoardScreenshotUpdated(Consumer):
        event_aggregator = inject.attr(EventAggregator)

        def __init__(self, outer_class) -> None:
            super().__init__(BoardScreenshotUpdated)
            self.event_aggregator.subscribe(self)
            self.outer_class = outer_class

        def consume(self, event: BoardScreenshotUpdated) -> None:
            self.outer_class.process_board_screenshot(event.screenshot)

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
