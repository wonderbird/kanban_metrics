from pathlib import Path

import iterative_metrics.adapters.inbound.cumulative_flow_diagram as diag
import iterative_metrics.adapters.inbound.count_work_items_in_image as img


if __name__ == "__main__":
    input_image = Path(__file__).parent.resolve() / "client-data" / "kanban_board.png"
    if input_image.exists():
        number_of_work_items = img.count_work_items_in_image(input_image)
        print(f"{number_of_work_items} work_items identified in {input_image}")

    diag.cumulative_flow_diagram()
