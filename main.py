from pathlib import Path

import src.iterative_metrics.cumulative_flow_diagram as diag
import src.iterative_metrics.count_cards_in_image as img


if __name__ == "__main__":
    input_image = Path(__file__).parent.resolve() / "client-data" / "kanban_board.png"
    if input_image.exists():
        number_of_cards = img.count_cards_in_image(input_image)
        print(f"{number_of_cards} cards identified in {input_image}")

    diag.cumulative_flow_diagram()
