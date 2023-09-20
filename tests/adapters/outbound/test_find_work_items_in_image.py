from pathlib import Path
import pytest

from iterative_metrics.adapters.outbound.find_work_items_in_image import (
    find_work_items_in_image,
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
def test_find_work_items_in_image(expected, filename):
    work_items = find_work_items_in_image(FIXTURE_DIR / filename)
    actual = len(work_items)
    assert actual == expected