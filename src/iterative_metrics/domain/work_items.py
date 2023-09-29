from typing import List

import numpy as np

from iterative_metrics.adapters.outbound.find_work_items_in_image import (
    find_work_items_in_screenshot,
)
from iterative_metrics.domain.work_item import WorkItem


class WorkItems:
    def __init__(self, work_items: List[WorkItem]) -> None:
        self.work_items = work_items

    @staticmethod
    def parse_screenshot(screenshot: np.ndarray) -> "WorkItems":
        work_items = find_work_items_in_screenshot(screenshot)
        return WorkItems(work_items)

    @property
    def count(self) -> int:
        return len(self.work_items)
