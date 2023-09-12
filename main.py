import src.iterative_metrics.cumulative_flow_diagram as diag
import src.iterative_metrics.count_cards_in_image as img


if __name__ == "__main__":
    img.count_cards_in_image(
        "tests/data/1_kanban_cards_width_140px_height_100px_resolution_144dpi.png"
    )
    diag.cumulative_flow_diagram()
