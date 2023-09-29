import cv2

from iterative_metrics.domain.work_items import WorkItems
from iterative_metrics.domain.workflow_steps import WorkflowSteps


def find_work_items_by_workflow_steps(image_file):
    image = cv2.imread(str(image_file))
    work_items = WorkItems.parse_screenshot(image)
    workflow_steps = WorkflowSteps.parse_screenshot(image)

    if workflow_steps.count == 0:
        return []

    result = [0] * workflow_steps.count

    for work_item in work_items:
        for i, workflow_step in enumerate(workflow_steps):
            if workflow_step.contains(work_item):
                result[i] += 1
                break

    return result


if __name__ == "__main__":
    print(find_work_items_by_workflow_steps("../../../../client-data/kanban_board.png"))
