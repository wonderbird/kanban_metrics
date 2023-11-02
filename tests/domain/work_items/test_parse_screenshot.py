from pathlib import Path

import cv2
import pytest

from iterative_metrics.domain.work_items import WorkItems

FIXTURE_DIR = Path(__file__).parent.parent.parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        (0, "0_white_image_width_140px_height_100px_resolution_144dpi.png"),
        (1, "1_work_items_width_140px_height_100px_resolution_144dpi.png"),
        (2, "2_work_items_1_blocker_width_239px_height_236px_resolution_96dpi.png"),
        (11, "11_work_items_width_640px_height_480px_resolution_96dpi.png"),
        (43, "full_board_width_808px_height_959px_resolution_96dpi.png"),
        (72, "full_board_width_1490px_height_1784px_resolution_144dpi.png"),
    ],
)
def test_(expected, filename):
    image = cv2.imread(str(FIXTURE_DIR / filename))
    work_items = WorkItems.parse_screenshot(image)
    assert work_items.count == expected
