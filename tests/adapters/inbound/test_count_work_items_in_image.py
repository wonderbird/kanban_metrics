from pathlib import Path
import pytest

from iterative_metrics.adapters.inbound.count_work_items_in_image import (
    count_work_items_in_image,
)


FIXTURE_DIR = Path(__file__).parent.parent.parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        (0, "0_white_image_width_140px_height_100px_resolution_144dpi.png"),
        (1, "1_work_items_width_140px_height_100px_resolution_144dpi.png"),
        (2, "2_work_items_1_blocker_width_239px_height_236px_resolution_96dpi.png"),
        (11, "11_work_items_width_640px_height_480px_resolution_96dpi.png"),
        (43, "full_board_width_808px_height_959px_resolution_96dpi.png"),
    ],
)
def test_count_work_items_in_image(expected, filename):
    actual = count_work_items_in_image(FIXTURE_DIR / filename)
    assert actual == expected
