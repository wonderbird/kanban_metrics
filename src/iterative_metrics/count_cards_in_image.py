import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def count_cards_in_image(path):
    # read HSV image
    bgr_input = cv.imread(path.__str__())
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

    # Debugging aid - uncomment to display an image
    # plt.imshow(borders, cmap="gray")
    # plt.show()

    # identify outer contours to count number of boxes
    contours, _ = cv.findContours(borders, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    number_of_boxes = len(contours)

    # display result
    return number_of_boxes


if __name__ == "__main__":
    images = [
        "../../tests/data/1_kanban_cards_width_140px_height_100px_resolution_144dpi.png",
        "../../tests/data/2_kanban_cards_1_blocker_width_239px_height_236px_resolution_96dpi.png",
        "../../tests/data/11_kanban_cards_width_640px_height_480px_resolution_96dpi.png",
        "../../tests/data/full_kanban_board_width_808px_height_959px_resolution_96dpi.png",
    ]

    for image in images:
        number_of_cards = count_cards_in_image(image)
        print(f"{image} contains {number_of_cards} cards")
