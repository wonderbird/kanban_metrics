from pathlib import Path

import cv2
import pytest

from iterative_metrics.domain.workflow_steps import WorkflowSteps

FIXTURE_DIR = Path(__file__).parent.parent.parent.resolve() / "data"


@pytest.mark.parametrize(
    "expected, filename",
    [
        (0, "0_white_image_width_140px_height_100px_resolution_144dpi.png"),
        (1, "1_workflow_step_width_151px_height_910px_resolution_96dpi.png"),
        (2, "2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"),
    ],
)
def test_given_ideal_screenshot(expected, filename):
    image = cv2.imread(str(FIXTURE_DIR / filename))
    workflow_steps = WorkflowSteps.parse_screenshot(image)
    assert workflow_steps.count == expected


def test_given_artifact_in_screenshot():
    image_path = (
        FIXTURE_DIR
        / "2_workflow_steps_with_artifact_width_240px_height_910px_resolution_96dpi.png"
    )
    image = cv2.imread(str(image_path))
    workflow_steps = WorkflowSteps.parse_screenshot(image)
    assert workflow_steps.count == 2


def test_result_should_be_sorted_from_left_to_right():
    image_path = (
        FIXTURE_DIR / "2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"
    )
    image = cv2.imread(str(image_path))
    workflow_steps = WorkflowSteps.parse_screenshot(image)

    left_x_coordinates = [step.bounding_rectangle.x for step in workflow_steps]
    assert left_x_coordinates == sorted(left_x_coordinates)


@pytest.mark.parametrize(
    "expected, filename",
    [
        (18, "full_board_width_808px_height_959px_resolution_96dpi.png"),
        (12, "full_board_width_1490px_height_1784px_resolution_144dpi.png"),
    ],
)
def test_given_realistic_full_board(expected, filename):
    image = cv2.imread(str(FIXTURE_DIR / filename))
    workflow_steps = WorkflowSteps.parse_screenshot(image)
    assert workflow_steps.count == expected
