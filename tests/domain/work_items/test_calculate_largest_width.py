from iterative_metrics.domain.rectangle import Rectangle
from iterative_metrics.domain.work_item import WorkItem
from iterative_metrics.domain.work_items import WorkItems


def test_given_no_work_items():
    subject = WorkItems([])
    assert subject.calculate_largest_width() == 0


def test_given_single_work_item():
    subject = WorkItems([WorkItem(Rectangle(0, 0, 10, 10))])
    assert subject.calculate_largest_width() == 10


def test_given_first_work_item_is_widest():
    largest_width = 100
    subject = WorkItems(
        [
            WorkItem(Rectangle(0, 0, largest_width, 10)),
            WorkItem(Rectangle(0, 0, largest_width - 10, 10)),
        ]
    )
    assert subject.calculate_largest_width() == largest_width


def test_given_second_work_item_is_widest():
    largest_width = 100
    subject = WorkItems(
        [
            WorkItem(Rectangle(0, 0, largest_width - 10, 10)),
            WorkItem(Rectangle(0, 0, largest_width, 10)),
        ]
    )
    assert subject.calculate_largest_width() == largest_width
