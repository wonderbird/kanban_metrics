import numpy as np


class BoardScreenshotUpdatedEvent:
    def __init__(self, screenshot: np.ndarray) -> None:
        self.screenshot = screenshot
