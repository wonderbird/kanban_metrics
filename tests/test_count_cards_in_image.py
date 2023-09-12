from pathlib import Path
import pytest

from .context import src
from src import iterative_metrics
from iterative_metrics.count_cards_in_image import count_cards_in_image


FIXTURE_DIR = Path(__file__).parent.resolve() / "data"


FILE_WITH_0_KANBAN_CARDS = (
    "0_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_0_KANBAN_CARDS)
def test_count_cards_in_image_0(datafiles):
    assert 0 == count_cards_in_image(datafiles / FILE_WITH_0_KANBAN_CARDS)


FILE_WITH_1_KANBAN_CARDS = (
    "1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_1_KANBAN_CARDS)
def test_count_cards_in_image_1(datafiles):
    assert 1 == count_cards_in_image(datafiles / FILE_WITH_1_KANBAN_CARDS)


FILE_WITH_2_KANBAN_CARDS = (
    "2_kanban_cards_1_blocker_width_239px_height_236px_resolution_96dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_2_KANBAN_CARDS)
def test_count_cards_in_image_2(datafiles):
    assert 2 == count_cards_in_image(datafiles / FILE_WITH_2_KANBAN_CARDS)


FILE_WITH_11_KANBAN_CARDS = (
    "11_kanban_cards_width_640px_height_480px_resolution_96dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_11_KANBAN_CARDS)
def test_count_cards_in_image_11(datafiles):
    assert 11 == count_cards_in_image(datafiles / FILE_WITH_11_KANBAN_CARDS)


FILE_WITH_43_KANBAN_CARDS = (
    "full_kanban_board_width_808px_height_959px_resolution_96dpi.png"
)


@pytest.mark.datafiles(FIXTURE_DIR / FILE_WITH_43_KANBAN_CARDS)
def test_count_cards_in_image_43(datafiles):
    assert 43 == count_cards_in_image(datafiles / FILE_WITH_43_KANBAN_CARDS)
