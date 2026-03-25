import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import fitz  # PyMuPDF

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"


def ensure_directories():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def get_pdf():
    pdf_files = list(INPUT_DIR.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF found in input folder.")
        print(f"Place a PDF in: {INPUT_DIR}")
        return None

    return pdf_files[0]


def split_by_ranges(pdf_path):
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    print(f"\nPDF has {total_pages} pages")

    ranges = input(
        "Enter page ranges (example: 1-4,5-7,8-10): "
    ).strip()

    parts = ranges.split(",")

    for part in parts:
        start, end = part.split("-")
        start = int(start)
        end = int(end)

        writer = PdfWriter()

        for page in range(start - 1, end):
            writer.add_page(reader.pages[page])

        output_file = OUTPUT_DIR / f"split_{start}_{end}.pdf"

        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"Saved: {output_file}")


def pdf_to_images(pdf_path, output_dir):
    """Convert entire PDF into images"""

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()

        output_file = output_dir / f"page_{page_num+1}.png"
        pix.save(output_file)

        print(f"Saved: {output_file}")

    print("\nAll pages converted to images.")


def extract_page_as_image(pdf_path, output_dir):
    """Extract a specific page as image"""

    doc = fitz.open(pdf_path)

    total_pages = len(doc)
    print(f"\nPDF has {total_pages} pages")

    page_num = int(input("Enter page number to extract: "))

    if page_num < 1 or page_num > total_pages:
        print("Invalid page number")
        return

    page = doc.load_page(page_num - 1)
    pix = page.get_pixmap()

    output_file = output_dir / f"page_{page_num}.png"
    pix.save(output_file)

    print(f"Saved: {output_file}")


def main():
    print("\n=== PDF Splitter & Extractor ===\n")

    ensure_directories()

    pdf_path = get_pdf()

    if not pdf_path:
        return

    print("\nOptions:\n")
    print("1. Split PDF by page ranges")
    print("2. Convert entire PDF to images")
    print("3. Extract specific page as image")

    choice = input("\nSelect option: ").strip()

    if choice == "1":
        split_by_ranges(pdf_path)

    elif choice == "2":
        pdf_to_images(pdf_path, OUTPUT_DIR)

    elif choice == "3":
        extract_page_as_image(pdf_path, OUTPUT_DIR)

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()