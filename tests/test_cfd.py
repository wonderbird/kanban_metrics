from .context import src
from src import iterative_metrics
from iterative_metrics.cfd import cfd


def test_cfd():
    assert cfd() is None
