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
            if workflow_step.contains(work_item):
                result[i] += 1
                break

    return result


if __name__ == "__main__":
    print(find_work_items_by_workflow_steps("../../client-data/kanban_board.png"))
