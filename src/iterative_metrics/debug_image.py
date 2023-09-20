import cv2 as cv


DEBUG = True


def debug_show_rectangles_in_image(image, rectangles):
    if not DEBUG:
        return

    for rect in rectangles:
        cv.rectangle(
            image,
            (rect.x, rect.y),
            (rect.x + rect.width, rect.y + rect.height),
            (0, 0, 255),
            2,
        )

    cv.imshow("Debugging", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
