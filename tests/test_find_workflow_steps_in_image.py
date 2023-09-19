from pathlib import Path
import pytest

from iterative_metrics.find_workflow_steps_in_image import find_workflow_steps_in_image


FIXTURE_DIR = Path(__file__).parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        (0, "0_white_image_width_140px_height_100px_resolution_144dpi.png"),
        (1, "1_workflow_step_width_151px_height_910px_resolution_96dpi.png"),
        (2, "2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"),
    ],
)
def test_find_workflow_steps_in_image(expected, filename):
    workflow_steps = find_workflow_steps_in_image(FIXTURE_DIR / filename)
    actual = len(workflow_steps)
    assert expected == actual


@pytest.mark.parametrize(
    "expected, filename",
    [
        (
            2,
            "2_workflow_steps_with_artifact_width_240px_height_910px_resolution_96dpi.png",
        ),
    ],
)
def test_find_workflow_steps_in_image_with_artifact(expected, filename):
    workflow_steps = find_workflow_steps_in_image(FIXTURE_DIR / filename)
    actual = len(workflow_steps)
    assert expected == actual
