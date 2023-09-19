from pathlib import Path
import pytest

from iterative_metrics.find_work_items_by_workflow_steps import (
    find_work_items_by_workflow_steps,
)

FIXTURE_DIR = Path(__file__).parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        ([], "0_white_image_width_140px_height_100px_resolution_144dpi.png"),
        ([2], "1_workflow_step_width_151px_height_910px_resolution_96dpi.png"),
        #        ([0, 2], "2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"),
    ],
    ids=[
        "0 workflow steps wit 0 work items",
        "1 workflow step with 2 work items",
        # "2 workflow steps with 0 and 2 work items",
    ],
)
def test_when_(expected, filename):
    actual = find_work_items_by_workflow_steps(FIXTURE_DIR / filename)
    assert expected == actual
