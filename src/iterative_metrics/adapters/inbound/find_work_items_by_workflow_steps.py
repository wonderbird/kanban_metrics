import cv2

from iterative_metrics.adapters.outbound.find_work_items_in_image import (
    find_work_items_in_screenshot,
)
from iterative_metrics.adapters.outbound.find_workflow_steps_in_image import (
    find_workflow_steps_in_image,
)


def find_work_items_by_workflow_steps(image_file):
    image = cv2.imread(str(image_file))
    work_items = find_work_items_in_screenshot(image)
    workflow_steps = find_workflow_steps_in_image(image_file)

    if len(workflow_steps) == 0:
        return []

    result = [0] * len(workflow_steps)

    for work_item in work_items:
        for i, workflow_step in enumerate(workflow_steps):
            if workflow_step.contains(work_item):
                result[i] += 1
                break

    return result


if __name__ == "__main__":
    print(find_work_items_by_workflow_steps("../../../../client-data/kanban_board.png"))
