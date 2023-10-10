import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_step import WorkflowStep
from iterative_metrics.domain.workflow_steps import WorkflowSteps


@pytest.mark.parametrize(
    "number_of_workflow_steps",
    [0, 1, 2, 3],
)
def test_given_number_of_workflow_steps(number_of_workflow_steps, mocker):
    workflow_step = WorkflowStep(Rectangle(0, 0, 10, 10))
    mock_associate_with = mocker.patch.object(
        workflow_step, "associate_with", autospec=True
    )
    workflow_steps = [workflow_step] * number_of_workflow_steps

    subject = WorkflowSteps(workflow_steps)
    subject.associate_with(WorkItems([]))

    assert mock_associate_with.call_count == number_of_workflow_steps
