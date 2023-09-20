from iterative_metrics.find_work_items_in_image import find_work_items_in_image
from iterative_metrics.find_workflow_steps_in_image import find_workflow_steps_in_image


def find_work_items_by_workflow_steps(image_file):
    work_items = find_work_items_in_image(image_file)
    workflow_steps = find_workflow_steps_in_image(image_file)

    if len(workflow_steps) == 0:
        return []

    result = [0] * len(workflow_steps)

    for work_item in work_items:
        for i, workflow_step in enumerate(workflow_steps):
            is_x_in_workflow_step = (
                workflow_step.bounding_rectangle.x
                <= work_item.bounding_rectangle.x
                <= workflow_step.bounding_rectangle.x
                + workflow_step.bounding_rectangle.width
            )
            is_y_in_workflow_step = (
                workflow_step.bounding_rectangle.y
                <= work_item.bounding_rectangle.y
                <= workflow_step.bounding_rectangle.y
                + workflow_step.bounding_rectangle.height
            )
            is_work_item_in_workflow_step = (
                is_x_in_workflow_step and is_y_in_workflow_step
            )

            if is_work_item_in_workflow_step:
                result[i] += 1
                break

    return result
