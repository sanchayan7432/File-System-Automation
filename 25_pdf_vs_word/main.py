from pathlib import Path
from pdf2docx import Converter
from docx2pdf import convert

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"


def ensure_directories():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def get_files(extension):
    return list(INPUT_DIR.glob(f"*{extension}"))


# -------------------------------
# PDF → DOCX
# -------------------------------
def pdf_to_docx():

    pdf_files = get_files(".pdf")

    if not pdf_files:
        print("❌ No PDF found in input folder.")
        print(f"Place a PDF in: {INPUT_DIR}")
        return

    for pdf in pdf_files:

        output_file = OUTPUT_DIR / f"{pdf.stem}.docx"

        print(f"\n🔄 Converting: {pdf.name}")

        try:
            converter = Converter(str(pdf))
            converter.convert(str(output_file))
            converter.close()

            print(f"✅ Saved: {output_file}")

        except Exception as e:
            print(f"❌ Failed to convert {pdf.name}")
            print("Error:", e)


# -------------------------------
# DOCX → PDF
# -------------------------------
def docx_to_pdf():

    docx_files = get_files(".docx")

    if not docx_files:
        print("❌ No DOCX file found in input folder.")
        print(f"Place a DOCX file in: {INPUT_DIR}")
        return

    for docx in docx_files:

        output_file = OUTPUT_DIR / f"{docx.stem}.pdf"

        print(f"\n🔄 Converting: {docx.name}")

        try:
            convert(str(docx), str(output_file))

            if output_file.exists():
                print(f"✅ Saved: {output_file}")
            else:
                print("❌ Conversion failed.")

        except Exception as e:

            print("\n❌ DOCX → PDF conversion failed.")
            print("This feature requires Microsoft Word installed and registered.")
            print("\nPossible Fix:")
            print("Run this command once in PowerShell:")
            print("winword /regserver\n")

            print("Technical error:", e)


# -------------------------------
# MAIN MENU
# -------------------------------
def main():

    print("\n=== PDF ↔ Word Converter ===\n")

    ensure_directories()

    print("Options:\n")
    print("1. PDF → DOCX")
    print("2. DOCX → PDF")

    choice = input("\nSelect option: ").strip()

    if choice == "1":
        pdf_to_docx()

    elif choice == "2":
        docx_to_pdf()

    else:
        print("❌ Invalid option")


if __name__ == "__main__":
    main()