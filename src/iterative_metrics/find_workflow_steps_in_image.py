import cv2 as cv
import numpy as np

from iterative_metrics.rectangle import Rectangle

DEBUG = False


def find_workflow_steps_in_image(image_file):
    # read HSV image
    bgr_input = cv.imread(image_file.__str__())
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    image = hsv_input
    image = cv.inRange(hsv_input, (0, 0, 200), (0, 0, 255))

    kernel = np.ones((3, 3), np.uint8)
    image = cv.erode(image, kernel, iterations=2)
    image = cv.dilate(image, kernel, iterations=2)

    # identify the bounding borders of the filled boxes
    image = cv.Canny(image, 50, 200)

    contours, _ = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    bounding_rectangles = [None] * len(contours)
    areas = [(None, None)] * len(contours)
    for index, contour in enumerate(contours):
        polygon = cv.approxPolyDP(contour, 3, True)
        bounding_rectangle = cv.boundingRect(polygon)
        bounding_rectangles[index] = Rectangle(
            bounding_rectangle[0],
            bounding_rectangle[1],
            bounding_rectangle[2],
            bounding_rectangle[3],
        )
        areas[index] = (index, bounding_rectangles[index].area)

    debug_show_rectangles_in_image(bgr_input, bounding_rectangles)

    return len(bounding_rectangles)


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
