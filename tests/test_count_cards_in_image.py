from pathlib import Path
import pytest

from .context import src
from src import iterative_metrics
from iterative_metrics.count_cards_in_image import count_cards_in_image


FIXTURE_DIR = Path(__file__).parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        (0, "0_kanban_cards_width_140px_height_100px_resolution_144dpi.png"),
        (1, "1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"),
        (2, "2_kanban_cards_1_blocker_width_239px_height_236px_resolution_96dpi.png"),
        (11, "11_kanban_cards_width_640px_height_480px_resolution_96dpi.png"),
        (43, "full_kanban_board_width_808px_height_959px_resolution_96dpi.png"),
    ],
)
def test_count_cards_in_image(expected, filename):
    actual = count_cards_in_image(FIXTURE_DIR / filename)
    assert expected == actual
