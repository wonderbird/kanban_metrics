import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.workflow_step import WorkflowStep
from iterative_metrics.domain.workflow_steps import WorkflowSteps


def test_given_empty():
    subject = WorkflowSteps([])
    with pytest.raises(IndexError):
        _ = subject[0]


def test_given_steps_present_when_accessing_index_out_of_range():
    subject = WorkflowSteps([WorkflowStep(Rectangle(0, 0, 0, 0))])
    with pytest.raises(IndexError):
        _ = subject[1]


def test_given_steps_present_when_accessing_single_contained_step():
    subject = WorkflowSteps([WorkflowStep(Rectangle(0, 0, 0, 0))])
    actual = subject[0]
    assert actual.number_of_work_items == 0


def test_given_steps_present_when_accessing_multiple_contained_steps():
    subject = WorkflowSteps(
        [
            WorkflowStep(Rectangle(0, 0, 0, 0)),
            WorkflowStep(Rectangle(0, 0, 0, 0)),
            WorkflowStep(Rectangle(0, 0, 0, 0)),
            WorkflowStep(Rectangle(0, 0, 0, 0)),
            WorkflowStep(Rectangle(0, 0, 0, 0)),
        ]
    )
    actual = subject[1:3]
    assert len(actual) == 2
