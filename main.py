import src
from src import iterative_metrics
from iterative_metrics.cumulative_flow_diagram import cumulative_flow_diagram
from iterative_metrics.count_cards_in_image import count_cards_in_image


if __name__ == "__main__":
    count_cards_in_image(
        "tests/data/1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
    )
    cumulative_flow_diagram()
