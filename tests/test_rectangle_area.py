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
