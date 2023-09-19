from iterative_metrics.find_work_items_in_image import find_work_items_in_image


def find_work_items_by_workflow_steps(image_file):
    work_items = find_work_items_in_image(image_file)

    if len(work_items) == 0:
        return []
    else:
        return [len(work_items)]
