from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

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


def create_watermark(text):
    packet = BytesIO()

    c = canvas.Canvas(packet, pagesize=letter)

    c.setFont("Helvetica", 40)
    c.setFillGray(0.5, 0.5)

    c.drawCentredString(300, 400, text)

    c.save()

    packet.seek(0)

    return PdfReader(packet)


def add_watermark(pdf_path, watermark_text):

    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    output_file = OUTPUT_DIR / f"{pdf_path.stem}_watermarked.pdf"

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"\n✅ Watermarked PDF saved: {output_file}")


def main():
    print("\n=== PDF Watermark Adder ===\n")

    ensure_directories()

    pdf_path = get_pdf()

    if not pdf_path:
        return

    watermark_text = input("Enter watermark text: ")

    add_watermark(pdf_path, watermark_text)


if __name__ == "__main__":
    main()