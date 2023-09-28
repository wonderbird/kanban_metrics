from pathlib import Path

import cv2
import numpy as np

from iterative_metrics.domain.ports.board_screenshot_storage import (
    BoardScreenshotStorage,
)


class BoardScreenshotFile(BoardScreenshotStorage):
    def __init__(self, screenshot_path: Path) -> None:
        self.screenshot_path = screenshot_path

    def read_screenshot(self) -> np.ndarray:
        return cv2.imread(str(self.screenshot_path))
