import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_step import WorkflowStep
from iterative_metrics.domain.workflow_steps import WorkflowSteps


def test_given_no_workflow_steps_and_no_work_items():
    work_items = WorkItems([])
    subject = WorkflowSteps([])

    try:
        subject.remove_areas_smaller_than_a_work_item(work_items)
    except BaseException:
        pytest.fail("should not raise an exception")


@pytest.mark.parametrize(
    "number_of_workflow_steps",
    [1, 2, 3],
)
def test_given_some_workflow_steps_and_no_work_items(number_of_workflow_steps):
    work_items = WorkItems([])
    subject = WorkflowSteps(
        [WorkflowStep(Rectangle(0, 0, 0, 0)) for _ in range(number_of_workflow_steps)]
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == number_of_workflow_steps
