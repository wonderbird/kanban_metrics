from iterative_metrics.domain.work_items import WorkItems


class WorkItemsFound:
    def __init__(self, work_items: WorkItems) -> None:
        self.work_items = work_items

    def __str__(self) -> str:
        return f"{self.work_items.count} work items found"
