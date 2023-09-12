import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def count_cards_in_image(path):
    # read HSV image
    bgr_input = cv.imread(path)
    hsv_input = cv.cvtColor(bgr_input, cv.COLOR_BGR2HSV)

    # remove non-title decorations - keep only black pixels with a value of 0
    title_box_with_text = cv.inRange(hsv_input, (0, 0, 0), (0, 0, 1))

    # remove text from title box
    kernel = np.ones((5, 5), np.uint8)
    title_box_enlarged = cv.dilate(title_box_with_text, kernel, iterations=1)
    title_box = cv.erode(title_box_enlarged, kernel, iterations=1)

    # display result
    plt.imshow(title_box, cmap="gray")
    plt.show()
    return 0


if __name__ == "__main__":
    count_cards_in_image(
        "../../tests/data/1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
    )
