import os
from pathlib import Path
from PIL import Image
from PyPDF2 import PdfMerger

# Base directories
BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

SUPPORTED_IMAGES = [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"]
SUPPORTED_PDF = ".pdf"


def ensure_directories():
    """Create input and output directories if missing."""
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def collect_files():
    """Collect all PDFs and images from input folder."""
    files = []

    for file in INPUT_DIR.iterdir():
        if file.suffix.lower() == SUPPORTED_PDF or file.suffix.lower() in SUPPORTED_IMAGES:
            files.append(file)

    return sorted(files)


def convert_image_to_pdf(image_path):
    """Convert image to temporary PDF."""
    try:
        img = Image.open(image_path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        temp_pdf = OUTPUT_DIR / f"{image_path.stem}_temp.pdf"

        img.save(temp_pdf)

        return temp_pdf

    except Exception as e:
        print(f"Failed converting image {image_path.name}: {e}")
        return None


def merge_files(files):
    """Merge PDFs and images into a single PDF."""
    merger = PdfMerger()
    temp_files = []

    for file in files:
        try:
            if file.suffix.lower() == ".pdf":
                merger.append(str(file))

            elif file.suffix.lower() in SUPPORTED_IMAGES:
                temp_pdf = convert_image_to_pdf(file)

                if temp_pdf:
                    merger.append(str(temp_pdf))
                    temp_files.append(temp_pdf)

        except Exception as e:
            print(f"Error processing {file.name}: {e}")

    output_file = OUTPUT_DIR / "merged_output.pdf"

    try:
        merger.write(str(output_file))
        merger.close()

        print("\n✅ PDF merged successfully!")
        print(f"Saved to: {output_file}")

    except Exception as e:
        print(f"Failed to merge files: {e}")

    # Clean temporary PDFs
    for temp in temp_files:
        try:
            os.remove(temp)
        except:
            pass


def main():
    print("\n=== PDF Merger Utility ===\n")

    ensure_directories()

    files = collect_files()

    if not files:
        print("❌ No PDF or image files found.")
        print(f"Place files in: {INPUT_DIR}")
        return

    print("Files detected:\n")

    for f in files:
        print(f"- {f.name}")

    confirm = input("\nMerge these files into a single PDF? (y/n): ").lower()

    if confirm != "y":
        print("Operation cancelled.")
        return

    merge_files(files)


if __name__ == "__main__":
    main()