import cv2 as cv
import numpy as np

from iterative_metrics.adapters.outbound.debug_image import (
    debug_show_rectangles_in_image,
)
from iterative_metrics.find_bounding_rectangles_of_largest_closed_shapes import (
    find_bounding_rectangles_of_largest_closed_shapes,
)
from iterative_metrics.workflow_step import WorkflowStep


def find_workflow_steps_in_image(image_file):
    # read HSV image
    bgr_input = cv.imread(image_file.__str__())
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    # find the workflow step boxes
    lower_boundary = np.array([0, 0, 200])
    upper_boundary = np.array([0, 0, 255])
    boxes_with_text = cv.inRange(hsv_input, lower_boundary, upper_boundary)

    # remove the text and other small artifacts
    kernel = np.ones((3, 3), np.uint8)
    boxes = cv.erode(boxes_with_text, kernel, iterations=2)
    boxes = cv.dilate(boxes, kernel, iterations=2)

    bounding_rectangles = find_bounding_rectangles_of_largest_closed_shapes(boxes)

    # for overlapping bounding rectangles, only keep the larger one
    sorted_rectangles = sorted(
        bounding_rectangles, key=lambda rect: rect.area, reverse=True
    )
    largest_rectangles = []
    for rectangle in sorted_rectangles:
        if not any(
            [
                rectangle.intersects(large_rectangle)
                for large_rectangle in largest_rectangles
            ]
        ):
            largest_rectangles.append(rectangle)

    # sort rectangles from left to right
    largest_rectangles = sorted(largest_rectangles, key=lambda rect: rect.x)

    # convert rectangles to workflow steps
    workflow_steps = []
    for rectangle in largest_rectangles:
        workflow_steps.append(WorkflowStep(rectangle))

    debug_show_rectangles_in_image(bgr_input, largest_rectangles)

    return workflow_steps


if __name__ == "__main__":
    print(find_workflow_steps_in_image("../../../../client-data/kanban_board.png"))
