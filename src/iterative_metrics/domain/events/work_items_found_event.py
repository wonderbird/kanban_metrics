from iterative_metrics.domain.work_items import WorkItems


class WorkItemsFoundEvent:
    def __init__(self, work_items: WorkItems) -> None:
        self.work_items = work_items
