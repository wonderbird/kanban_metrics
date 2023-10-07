import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.workflow_step import WorkflowStep
from iterative_metrics.domain.workflow_steps import WorkflowSteps


@pytest.mark.parametrize(
    "number_of_workflow_steps",
    [0, 1, 2, 3],
    ids=["0 workflow steps", "1 workflow step", "2 workflow steps", "3 workflow steps"],
)
def test_given_no_work_item_assigned_when(number_of_workflow_steps):
    workflow_steps = [
        WorkflowStep(Rectangle(0, 0, 10, 10)) for _ in range(number_of_workflow_steps)
    ]

    subject = WorkflowSteps(workflow_steps)

    actual = subject.work_items_per_workflow_step
    expected = [0 for _ in range(number_of_workflow_steps)]
    assert actual == expected
