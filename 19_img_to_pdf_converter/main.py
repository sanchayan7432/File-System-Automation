import os
from pathlib import Path
from PIL import Image

# Directories
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

SUPPORTED_EXTENSIONS = [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"]


def ensure_directories():
    """Create input and output directories if they don't exist."""
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def get_images():
    """Collect all supported images from input folder."""
    images = []

    for file in INPUT_DIR.iterdir():
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            images.append(file)

    return sorted(images)


def convert_images_to_pdf(images):
    """Convert multiple images to a single PDF."""
    if not images:
        print("❌ No images found in input folder.")
        return

    image_list = []

    for img_path in images:
        try:
            img = Image.open(img_path)

            # Convert to RGB (required for PDF)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            image_list.append(img)

        except Exception as e:
            print(f"⚠ Could not process {img_path.name}: {e}")

    if not image_list:
        print("❌ No valid images to convert.")
        return

    output_pdf = OUTPUT_DIR / "converted_images.pdf"

    try:
        image_list[0].save(
            output_pdf,
            save_all=True,
            append_images=image_list[1:]
        )

        print(f"\n✅ PDF created successfully:")
        print(output_pdf)

    except Exception as e:
        print(f"❌ Failed to create PDF: {e}")


def main():
    print("\n=== Image to PDF Converter ===\n")

    ensure_directories()

    images = get_images()

    if not images:
        print("No images found.")
        print(f"Place images inside:\n{INPUT_DIR}")
        return

    print("Images detected:")
    for img in images:
        print(f"- {img.name}")

    confirm = input("\nConvert these images to PDF? (y/n): ").lower()

    if confirm != "y":
        print("Operation cancelled.")
        return

    convert_images_to_pdf(images)


if __name__ == "__main__":
    main()