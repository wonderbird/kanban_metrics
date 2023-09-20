from iterative_metrics.adapters.inbound.cumulative_flow_diagram import (
    cumulative_flow_diagram,
)


def test_cumulative_flow_diagram():
    assert cumulative_flow_diagram() is None
