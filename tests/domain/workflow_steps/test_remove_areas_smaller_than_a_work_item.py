import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_item import WorkItem
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


def test_given_no_workflow_steps_and_single_work_item():
    work_items = WorkItems([WorkItem(Rectangle(0, 0, 0, 0))])
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
        [WorkflowStep(Rectangle(0, 0, 0, 0))] * number_of_workflow_steps
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == number_of_workflow_steps


@pytest.mark.parametrize(
    "number_of_workflow_steps",
    [1, 2, 3],
)
def test_given_some_workflow_steps_and_single_work_item_smaller_than_all_steps(
    number_of_workflow_steps,
):
    work_items = WorkItems([WorkItem(Rectangle(0, 0, 10, 10))])
    subject = WorkflowSteps(
        [WorkflowStep(Rectangle(0, 0, 100, 100))] * number_of_workflow_steps
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == number_of_workflow_steps


@pytest.mark.parametrize(
    "number_of_workflow_steps",
    [1, 2, 3],
)
def test_given_some_workflow_steps_and_single_work_item_height_larger_than_height_of_all_steps(
    number_of_workflow_steps,
):
    work_items = WorkItems([WorkItem(Rectangle(0, 0, 100, 100))])
    subject = WorkflowSteps(
        [WorkflowStep(Rectangle(0, 0, 10, 10))] * number_of_workflow_steps
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == 0


def test_given_some_workflow_steps_have_too_small_height():
    work_items = WorkItems([WorkItem(Rectangle(0, 0, 100, 100))])
    subject = WorkflowSteps(
        [
            WorkflowStep(Rectangle(0, 0, 101, 10)),
            WorkflowStep(Rectangle(0, 0, 101, 101)),
        ],
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == 1
    assert subject[0].bounding_rectangle.height == 101


def test_given_some_workflow_steps_have_too_small_width():
    work_items = WorkItems([WorkItem(Rectangle(0, 0, 100, 100))])
    subject = WorkflowSteps(
        [
            WorkflowStep(Rectangle(0, 0, 10, 101)),
            WorkflowStep(Rectangle(0, 0, 101, 101)),
        ],
    )

    subject.remove_areas_smaller_than_a_work_item(work_items)

    assert subject.count == 1
    assert subject[0].bounding_rectangle.width == 101
