from iterative_metrics.domain.workflow_steps import WorkflowSteps


class PotentialWorkflowStepsFoundEvent:
    def __init__(self, workflow_steps: WorkflowSteps) -> None:
        self.workflow_steps = workflow_steps

    def __str__(self):
        return f"{self.workflow_steps.count} potential workflow steps found"
