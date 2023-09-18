import pytest

from iterative_metrics.rectangle import Rectangle


@pytest.mark.parametrize(
    "width, height, expected_area",
    [
        (0, 0, 0),
        (1, 1, 1),
        (2, 3, 6),
    ],
)
def test_rectangle_area_for_width_height_expected(width, height, expected_area):
    rectangle = Rectangle(0, 0, width, height)
    assert rectangle.area == expected_area


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
def test_rectangle_intersects_when_non_intersecting_then_return_false(
    first,
    second,
):
    assert first.intersects(second) == False


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
def test_rectangle_intersects_when_corner_overlaps_then_return_true(
    first,
    second,
):
    assert first.intersects(second) == True


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
def test_rectangle_intersects_when_first_contains_side_of_second_then_return_true(
    first,
    second,
):
    assert first.intersects(second) == True


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
def test_rectangle_intersects_when_one_overlaps_middle_of_another_then_return_true(
    first,
    second,
):
    assert first.intersects(second) == True


@pytest.mark.parametrize(
    "first, second",
    [
        (Rectangle(0, 0, 4, 4), Rectangle(1, 1, 2, 2)),
        (Rectangle(1, 1, 2, 2), Rectangle(0, 0, 4, 4)),
    ],
    ids=[
        "first contains second",
        "second contains first",
    ],
)
def test_rectangle_intersects_when_one_contains_another_then_return_true(
    first,
    second,
):
    assert first.intersects(second) == True
