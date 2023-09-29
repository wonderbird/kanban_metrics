from iterative_metrics.domain.workflow_steps import WorkflowSteps


class BoardStatusDetermined:
    def __init__(self, workflow_steps: WorkflowSteps) -> None:
        self.workflow_steps = workflow_steps

    def __str__(self):
        work_items_per_step = [
            step.number_of_work_items for step in self.workflow_steps
        ]
        return "board status: [" + ", ".join(map(str, work_items_per_step)) + "]"
