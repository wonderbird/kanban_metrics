from typing import List
from collections.abc import Iterator

import cv2
import numpy as np

from iterative_metrics.adapters.outbound.debug_image import (
    debug_show_rectangles_in_image,
)
from iterative_metrics.adapters.outbound.find_bounding_rectangles_of_largest_closed_shapes import (
    find_bounding_rectangles_of_largest_closed_shapes,
)

from iterative_metrics.domain.work_item import WorkItem


class WorkItems:
    def __init__(self, work_items: List[WorkItem]) -> None:
        self.work_items = work_items

    @staticmethod
    def parse_screenshot(screenshot: np.ndarray) -> "WorkItems":
        hsv_input = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

        # identify the metrics area (green box)
        lower_boundary = np.array([35, 50, 50])
        upper_boundary = np.array([70, 255, 255])
        boxes_with_text = cv2.inRange(hsv_input, lower_boundary, upper_boundary)

        # remove the text and other small artifacts
        boxes = boxes_with_text

        # Close cracked borders of boxes
        kernel = np.ones((3, 3), np.uint8)
        boxes = cv2.dilate(boxes, kernel, iterations=1)
        # Remove small artifacts, e.g. checkboxes, wrong colored pixels
        kernel = np.ones((5, 5), np.uint8)
        boxes = cv2.erode(boxes, kernel, iterations=2)

        # Remove text from inside boxes
        kernel = np.ones((11, 11), np.uint8)
        boxes = cv2.dilate(boxes, kernel, iterations=1)
        bounding_rectangles = find_bounding_rectangles_of_largest_closed_shapes(boxes)

        # convert bounding rectangles to work items
        work_items = []
        for bounding_rectangle in bounding_rectangles:
            work_items.append(WorkItem(bounding_rectangle))
        debug_show_rectangles_in_image(screenshot, bounding_rectangles)

        return WorkItems(work_items)

    @property
    def count(self) -> int:
        return len(self.work_items)

    def __iter__(self) -> Iterator[WorkItem]:
        return iter(self.work_items)
