import pytest

from iterative_metrics.domain.rectangle import Rectangle


@pytest.mark.parametrize(
    "expected_area, width, height",
    [
        (0, 0, 0),
        (1, 1, 1),
        (6, 2, 3),
    ],
)
def test_rectangle_area_for_width_height_expected(expected_area, width, height):
    rectangle = Rectangle(0, 0, width, height)
    assert rectangle.area == expected_area
