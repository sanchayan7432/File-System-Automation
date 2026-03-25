import pytesseract
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ensure_directories():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def get_images():
    extensions = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.tiff"]

    images = []
    for ext in extensions:
        images.extend(INPUT_DIR.glob(ext))

    if not images:
        print("❌ No images found in input folder.")
        print(f"Place images in: {INPUT_DIR}")
        return []

    return images


def extract_text_from_images(images):
    for img_path in images:
        print(f"\nProcessing: {img_path.name}")

        img = Image.open(img_path)

        text = pytesseract.image_to_string(img)

        output_file = OUTPUT_DIR / f"{img_path.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved: {output_file}")


def main():
    print("\n=== Image Text Extractor (OCR) ===\n")

    ensure_directories()

    images = get_images()

    if not images:
        return

    extract_text_from_images(images)

    print("\n✅ Text extraction complete.")


if __name__ == "__main__":
    main()