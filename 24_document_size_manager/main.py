from pathlib import Path
import zipfile
from PIL import Image
import fitz
import os

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"


def ensure_directories():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def get_files():
    files = list(INPUT_DIR.glob("*"))

    if not files:
        print("❌ No files found in input folder.")
        print(f"Place files in: {INPUT_DIR}")
        return []

    return files


def format_size(size):
    """Convert bytes to KB/MB"""
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size/1024:.2f} KB"
    else:
        return f"{size/(1024*1024):.2f} MB"


# IMAGE COMPRESSION
def compress_images(files):

    print("\n=== Image Compression ===\n")

    for file in files:

        if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        before = os.path.getsize(file)

        img = Image.open(file)

        output_file = OUTPUT_DIR / f"{file.stem}_compressed.jpg"

        img.save(output_file, optimize=True, quality=40)

        after = os.path.getsize(output_file)

        print(f"\nFile: {file.name}")
        print(f"Before: {format_size(before)}")
        print(f"After : {format_size(after)}")


# IMAGE ENLARGEMENT
def enlarge_images(files):

    print("\n=== Image Enlargement ===\n")

    scale = int(input("Enter scale factor (example 2 = double size): "))

    for file in files:

        if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        before = os.path.getsize(file)

        img = Image.open(file)

        width, height = img.size
        img = img.resize((width * scale, height * scale))

        output_file = OUTPUT_DIR / f"{file.stem}_enlarged.png"

        img.save(output_file)

        after = os.path.getsize(output_file)

        print(f"\nFile: {file.name}")
        print(f"Before: {format_size(before)}")
        print(f"After : {format_size(after)}")


# PDF COMPRESSION
def compress_pdf(files):

    print("\n=== PDF Compression ===\n")

    for file in files:

        if file.suffix.lower() != ".pdf":
            continue

        before = os.path.getsize(file)

        doc = fitz.open(file)

        output_file = OUTPUT_DIR / f"{file.stem}_compressed.pdf"

        doc.save(output_file, garbage=4, deflate=True)

        after = os.path.getsize(output_file)

        print(f"\nFile: {file.name}")
        print(f"Before: {format_size(before)}")
        print(f"After : {format_size(after)}")


# GENERIC ZIP COMPRESSION
def zip_files(files):

    print("\n=== ZIP Compression ===\n")

    zip_path = OUTPUT_DIR / "compressed_archive.zip"

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:

        for file in files:
            z.write(file, file.name)

    print(f"ZIP archive created: {zip_path}")


def main():

    print("\n=== Document Size Manager ===\n")

    ensure_directories()

    files = get_files()

    if not files:
        return

    print("\nOptions:\n")

    print("1. Compress Images")
    print("2. Enlarge Image Quality")
    print("3. Compress PDF")
    print("4. Compress Any File (ZIP)")

    choice = input("\nSelect option: ").strip()

    if choice == "1":
        compress_images(files)

    elif choice == "2":
        enlarge_images(files)

    elif choice == "3":
        compress_pdf(files)

    elif choice == "4":
        zip_files(files)

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()