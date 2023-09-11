from pathlib import Path
import pytest

from .context import src
from src import iterative_metrics
from iterative_metrics.count_cards_in_image import count_cards_in_image


FIXTURE_DIR = Path(__file__).parent.resolve() / "data"
FILE_WITH_0_KANBAN_CARDS = (
    "0_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
)
FILE_WITH_1_KANBAN_CARDS = (
    "1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_0_KANBAN_CARDS)
def test_count_cards_in_image_0(datafiles):
    assert 0 == count_cards_in_image(datafiles / FILE_WITH_0_KANBAN_CARDS)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_1_KANBAN_CARDS)
def test_count_cards_in_image_1(datafiles):
    assert 1 == count_cards_in_image(datafiles / FILE_WITH_1_KANBAN_CARDS)
