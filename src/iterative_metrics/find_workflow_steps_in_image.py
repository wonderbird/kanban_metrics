import cv2 as cv
import numpy as np

from iterative_metrics.rectangle import Rectangle
from iterative_metrics.workflow_step import WorkflowStep

DEBUG = False


def find_workflow_steps_in_image(image_file):
    # TODO fix problems reported by PyCharm

    # read HSV image
    bgr_input = cv.imread(image_file.__str__())
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    image = hsv_input
    image = cv.inRange(hsv_input, (0, 0, 200), (0, 0, 255))

    # remove the text and other small artifacts
    kernel = np.ones((3, 3), np.uint8)
    image = cv.erode(image, kernel, iterations=2)
    image = cv.dilate(image, kernel, iterations=2)

    # identify the borders in the image
    image = cv.Canny(image, 50, 200)

    # identify outer contours to count number of boxes
    contours, _ = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # identify bounding rectangles
    bounding_rectangles = []
    for index, contour in enumerate(contours):
        polygon = cv.approxPolyDP(contour, 3, True)
        bounding_rectangle = cv.boundingRect(polygon)
        bounding_rectangles.append(
            Rectangle(
                bounding_rectangle[0],
                bounding_rectangle[1],
                bounding_rectangle[2],
                bounding_rectangle[3],
            )
        )

    # for overlapping bounding rectangles, only keep the larger one
    sorted_rectangles = sorted(
        bounding_rectangles, key=lambda rectangle: rectangle.area, reverse=True
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
    largest_rectangles = sorted(largest_rectangles, key=lambda rectangle: rectangle.x)

    # convert largest rectangles to workflow steps
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
