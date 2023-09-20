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
    assert actual == expected


def test_find_workflow_steps_in_image_with_artifact():
    workflow_steps = find_workflow_steps_in_image(
        FIXTURE_DIR
        / "2_workflow_steps_with_artifact_width_240px_height_910px_resolution_96dpi.png"
    )
    actual = len(workflow_steps)
    assert actual == 2


def test_result_should_be_sorted_from_left_to_right():
    workflow_steps = find_workflow_steps_in_image(
        FIXTURE_DIR / "2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"
    )
    assert (
        workflow_steps[0].bounding_rectangle.x
        + workflow_steps[0].bounding_rectangle.width
        < workflow_steps[1].bounding_rectangle.x
    )
