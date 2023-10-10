import pytest

from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_item import WorkItem
from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_step import WorkflowStep


@pytest.mark.parametrize("number_of_work_items", [0, 1, 2, 3])
def test_associate_with_given_all_work_items_inside_workflow_step(number_of_work_items):
    work_item = WorkItem(Rectangle(1, 1, 8, 8))
    work_items = WorkItems([work_item] * number_of_work_items)

    subject = WorkflowStep(Rectangle(0, 0, 10, 10))
    subject.associate_with(work_items)

    assert subject.number_of_work_items == number_of_work_items


def test_associate_with_given_work_item_outside_workflow_step():
    work_item = WorkItem(Rectangle(11, 11, 8, 8))
    work_items = WorkItems([work_item])

    subject = WorkflowStep(Rectangle(0, 0, 10, 10))
    subject.associate_with(work_items)

    assert subject.number_of_work_items == 0


def test_associate_with_given_some_work_items_inside_and_some_outside_workflow_step():
    work_item_inside = WorkItem(Rectangle(1, 1, 8, 8))
    work_item_outside = WorkItem(Rectangle(11, 11, 8, 8))
    work_items = WorkItems(
        [work_item_inside, work_item_outside, work_item_inside, work_item_outside]
    )

    subject = WorkflowStep(Rectangle(0, 0, 10, 10))
    subject.associate_with(work_items)

    assert subject.number_of_work_items == 2
