import pytest

from iterative_metrics.domain.rectangle import Rectangle


@pytest.mark.parametrize(
    "first, second",
    [
        (Rectangle(0, 0, 1, 1), Rectangle(2, 0, 1, 1)),
        (Rectangle(0, 0, 1, 1), Rectangle(0, 2, 1, 1)),
        (Rectangle(0, 0, 1, 1), Rectangle(-2, 0, 1, 1)),
        (Rectangle(0, 0, 1, 1), Rectangle(0, -2, 1, 1)),
    ],
    ids=[
        "first is left of second",
        "first is above second",
        "first is right of second",
        "first is below second",
    ],
)
def test_when_not_overlapping(first, second):
    assert not first.contains(second)


@pytest.mark.parametrize(
    "first, second",
    [
        (Rectangle(0, 0, 2, 2), Rectangle(1, 1, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(-1, 1, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(1, -1, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(-1, -1, 2, 2)),
        (Rectangle(1, 1, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(-1, 1, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(1, -1, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(-1, -1, 2, 2), Rectangle(0, 0, 2, 2)),
    ],
    ids=[
        "first contains top left corner of second",
        "first contains top right corner of second",
        "first contains bottom left corner of second",
        "first contains bottom right corner of second",
        "second contains top left corner of first",
        "second contains top right corner of first",
        "second contains bottom left corner of first",
        "second contains bottom right corner of first",
    ],
)
def test_when_overlaps_partially(
    first,
    second,
):
    assert not first.contains(second)


@pytest.mark.parametrize(
    "first, second",
    [
        (Rectangle(0, 0, 2, 2), Rectangle(0, 1, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(1, 0, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(0, -1, 2, 2)),
        (Rectangle(0, 0, 2, 2), Rectangle(-1, 0, 2, 2)),
        (Rectangle(0, 1, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(1, 0, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(0, -1, 2, 2), Rectangle(0, 0, 2, 2)),
        (Rectangle(-1, 0, 2, 2), Rectangle(0, 0, 2, 2)),
    ],
    ids=[
        "first contains top side of second",
        "first contains left side of second",
        "first contains bottom side of second",
        "first contains right side of second",
        "second contains top side of first",
        "second contains left side of first",
        "second contains bottom side of first",
        "second contains right side of first",
    ],
)
def test_when_only_one_side_overlaps_partially(
    first,
    second,
):
    assert not first.contains(second)


@pytest.mark.parametrize(
    "first, second",
    [
        (Rectangle(0, 0, 4, 2), Rectangle(1, -1, 2, 4)),
        (Rectangle(0, 0, 2, 4), Rectangle(-1, 1, 4, 2)),
        (Rectangle(1, -1, 2, 4), Rectangle(0, 0, 4, 2)),
        (Rectangle(-1, 1, 4, 2), Rectangle(0, 0, 2, 4)),
    ],
    ids=[
        "second overlaps middle of first horizontally",
        "second overlaps middle of first vertically",
        "first overlaps middle of second horizontally",
        "first overlaps middle of second vertically",
    ],
)
def test_when_middle_overlaps_partially(
    first,
    second,
):
    assert not first.contains(second)


def test_when_first_contains_second():
    assert Rectangle(0, 0, 4, 4).contains(Rectangle(1, 1, 2, 2))


def test_when_second_contains_first():
    assert not Rectangle(1, 1, 2, 2).contains(Rectangle(0, 0, 4, 4))
