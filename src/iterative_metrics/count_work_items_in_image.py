from .find_work_items_in_image import find_work_items_in_image


def count_work_items_in_image(image_file):
    work_items = find_work_items_in_image(image_file)
    return len(work_items)


if __name__ == "__main__":
    images = [
        "../../tests/data/1_work_items_width_140px_height_100px_resolution_144dpi.png",
        "../../tests/data/2_work_items_1_blocker_width_239px_height_236px_resolution_96dpi.png",
        "../../tests/data/11_work_items_width_640px_height_480px_resolution_96dpi.png",
        "../../tests/data/full_board_width_808px_height_959px_resolution_96dpi.png",
    ]

    for image in images:
        result = count_work_items_in_image(image)
        print(f"{image} contains {result} work items")
