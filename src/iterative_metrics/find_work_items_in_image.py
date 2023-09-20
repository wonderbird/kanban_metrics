import cv2 as cv
import numpy as np

from .rectangle import Rectangle
from .work_item import WorkItem


def find_work_items_in_image(image_file):
    bgr_input = cv.imread(image_file.__str__())
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    # identify the metrics area (green box)
    boxes_with_text = cv.inRange(hsv_input, (35, 50, 50), (70, 255, 255))

    # remove the text and other small artifacts
    boxes = boxes_with_text

    # Close cracked borders of boxes
    kernel = np.ones((3, 3), np.uint8)
    boxes = cv.dilate(boxes, kernel, iterations=1)

    # Remove small artifacts, e.g. checkboxes, wrong colored pixels
    kernel = np.ones((5, 5), np.uint8)
    boxes = cv.erode(boxes, kernel, iterations=2)

    # Remove text from inside boxes
    kernel = np.ones((11, 11), np.uint8)
    boxes = cv.dilate(boxes, kernel, iterations=1)

    # identify the bounding borders of the filled boxes
    borders = cv.Canny(boxes, 50, 200)

    # identify outer contours to count number of boxes
    contours, _ = cv.findContours(borders, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

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

    # convert bounding rectangles to work items
    work_items = []
    for bounding_rectangle in bounding_rectangles:
        work_items.append(WorkItem(bounding_rectangle))

    return work_items
