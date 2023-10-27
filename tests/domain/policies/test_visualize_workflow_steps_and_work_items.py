import inject
import numpy as np

from iterative_metrics.domain.events.board_screenshot_updated import (
    BoardScreenshotUpdated,
)
from iterative_metrics.domain.events.potential_workflow_steps_found import (
    PotentialWorkflowStepsFound,
)
from iterative_metrics.domain.events.work_items_found import WorkItemsFound
from iterative_metrics.domain.policies.visualize_workflow_steps_and_work_items import (
    VisualizeWorkflowStepsAndWorkItems,
)
from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_item import WorkItem
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_step import WorkflowStep
from iterative_metrics.domain.workflow_steps import WorkflowSteps
from iterative_metrics.eventing.event_aggregator import EventAggregator
from iterative_metrics.eventing.wait_for_multiple_events import WaitForMultipleEvents


class TestVisualizeWorkflowStepsAndWorkItems:
    def setup_method(self) -> None:
        self._event_aggregator = EventAggregator()
        inject.clear_and_configure(self.configuration)

    @staticmethod
    def teardown_method(self) -> None:
        inject.clear()

    def configuration(self, binder: inject.Binder) -> None:
        binder.bind(EventAggregator, self._event_aggregator)

    def test_(self, mocker):
        mock_debug_show = mocker.patch(
            "iterative_metrics.domain.policies.visualize_workflow_steps_and_work_items.debug_show_rectangles_in_image"
        )
        WaitForMultipleEvents(
            [BoardScreenshotUpdated, PotentialWorkflowStepsFound, WorkItemsFound]
        )
        VisualizeWorkflowStepsAndWorkItems()

        fake_screenshot = np.zeros((1, 1, 3), dtype=np.uint8)
        self._event_aggregator.publish(BoardScreenshotUpdated(fake_screenshot))

        work_item_bounding_rectangle = Rectangle(1, 1, 1, 1)
        work_items = WorkItems([WorkItem(work_item_bounding_rectangle)])
        self._event_aggregator.publish(WorkItemsFound(work_items))

        workflow_step_bounding_rectangle = Rectangle(0, 0, 10, 10)
        workflow_steps = WorkflowSteps([WorkflowStep(workflow_step_bounding_rectangle)])
        self._event_aggregator.publish(PotentialWorkflowStepsFound(workflow_steps))

        expected = [work_item_bounding_rectangle, workflow_step_bounding_rectangle]
        mock_debug_show.assert_called_once_with(fake_screenshot, expected)
