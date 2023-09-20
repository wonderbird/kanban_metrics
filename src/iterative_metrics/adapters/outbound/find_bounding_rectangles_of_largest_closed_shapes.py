import cv2 as cv

from iterative_metrics.domain.rectangle import Rectangle


def find_bounding_rectangles_of_largest_closed_shapes(boxes):
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

    return bounding_rectangles
