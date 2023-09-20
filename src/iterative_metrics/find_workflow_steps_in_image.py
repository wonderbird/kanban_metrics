import cv2 as cv
import numpy as np

from iterative_metrics.find_bounding_rectangles_of_largest_closed_shapes import (
    find_bounding_rectangles_of_largest_closed_shapes,
)
from iterative_metrics.rectangle import Rectangle
from iterative_metrics.workflow_step import WorkflowStep

DEBUG = False


def find_workflow_steps_in_image(image_file):
    # TODO fix problems reported by PyCharm

    # read HSV image
    bgr_input = cv.imread(image_file.__str__())
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    boxes_with_text = cv.inRange(hsv_input, (0, 0, 200), (0, 0, 255))

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


def debug_show_rectangles_in_image(image, bounding_rectangles):
    if not DEBUG:
        return

    for bounding_rectangle in bounding_rectangles:
        cv.rectangle(
            image,
            (bounding_rectangle.x, bounding_rectangle.y),
            (
                bounding_rectangle.x + bounding_rectangle.width,
                bounding_rectangle.y + bounding_rectangle.height,
            ),
            (0, 0, 255),
            2,
        )

    cv.imshow("Debugging", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    find_workflow_steps_in_image(
        "../../tests/data/2_workflow_steps_width_240px_height_910px_resolution_96dpi.png"
    )
