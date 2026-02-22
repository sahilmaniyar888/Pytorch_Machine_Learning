from __future__ import annotations

import os

VALID_EXTENSIONS = (".jpg", ".png", ".jpeg")


def filter_valid_images(image_paths: list[str]) -> list[str]:
    """Return only valid image paths (.jpg/.png/.jpeg), case-insensitive."""
    return [path for path in image_paths if path.lower().endswith(VALID_EXTENSIONS)]


def get_image_files(folder: str) -> list[str]:
    """Return full paths of valid images in a folder using list comprehension."""
    if not os.path.isdir(folder):
        return []
    all_files = os.listdir(folder)
    return [
        os.path.join(folder, file_name)
        for file_name in all_files
        if file_name.lower().endswith(VALID_EXTENSIONS)
    ]


def create_label_dict(labels: list[str]) -> dict[str, int]:
    """Map sorted unique class labels to integer IDs."""
    unique_labels = sorted(set(labels))
    return {label: idx for idx, label in enumerate(unique_labels)}


def count_images_per_class(image_paths: list[str]) -> dict[str, int]:
    """
    Count images per class from file names like 'cat_001.jpg'.
    Class is inferred from the first token before '_' in each basename.
    """
    valid_paths = filter_valid_images(image_paths)
    classes = [
        os.path.basename(path).rsplit(".", maxsplit=1)[0].split("_", maxsplit=1)[0].lower()
        for path in valid_paths
        if "_" in os.path.basename(path)
    ]
    unique_classes = sorted(set(classes))
    return {class_name: classes.count(class_name) for class_name in unique_classes}


def image_generator(image_paths: list[str]):
    """Yield one image path at a time to keep memory usage low."""
    for path in image_paths:
        print(f"Loading {path}...")
        yield path


if __name__ == "__main__":
    sample_dir = "data/raw/sample_images"
    os.makedirs(sample_dir, exist_ok=True)

    sample_paths = [
        f"{sample_dir}/cat_001.jpg",
        f"{sample_dir}/cat_002.JPG",
        f"{sample_dir}/dog_001.png",
        f"{sample_dir}/bird_001.jpeg",
        f"{sample_dir}/notes.txt",
    ]

    for path in sample_paths:
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as file:
                file.write("demo")

    print("=== Filter Valid Images ===")
    print(filter_valid_images(sample_paths))

    print("\n=== List Comprehension: get_image_files ===")
    images = get_image_files(sample_dir)
    print(images)

    print("\n=== Dict Comprehension: create_label_dict ===")
    classes = ["cat", "dog", "cat", "bird", "dog"]
    print(create_label_dict(classes))

    print("\n=== Exercise: count_images_per_class ===")
    print(count_images_per_class(sample_paths))

    print("\n=== Generator (memory efficient) ===")
    for path in image_generator(filter_valid_images(sample_paths)):
        print("Processed:", path)
