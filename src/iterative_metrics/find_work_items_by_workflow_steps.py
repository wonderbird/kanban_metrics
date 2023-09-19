from iterative_metrics.find_work_items_in_image import find_work_items_in_image
from iterative_metrics.find_workflow_steps_in_image import find_workflow_steps_in_image


def find_work_items_by_workflow_steps(image_file):
    work_items = find_work_items_in_image(image_file)
    workflow_steps = find_workflow_steps_in_image(image_file)

    if len(work_items) == 0:
        return []

    result = [0] * len(workflow_steps)
    result[-1] = len(work_items)
    return result
