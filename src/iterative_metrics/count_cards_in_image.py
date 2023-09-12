import cv2 as cv
import matplotlib.pyplot as plt


def count_cards_in_image(path):
    original_image = cv.imread(
        "../../tests/data/1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
    )

    hsv_image = cv.cvtColor(original_image, cv.COLOR_RGB2HSV)
    black_white_image = cv.inRange(hsv_image, (0, 0, 100), (0, 0, 255))
    plt.imshow(black_white_image, cmap="gray")
    plt.show()
    return 0


if __name__ == "__main__":
    count_cards_in_image("")
