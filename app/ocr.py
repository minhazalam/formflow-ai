import pytesseract
from PIL import Image
import shutil


def get_tesseract_path():
    path = shutil.which("tesseract")

    if path is None:
        raise RuntimeError(
            "❌ Tesseract not found. Install using:\n"
            "brew install tesseract"
        )

    return path


def extract_lines(image_path):
    try:
        # Set path dynamically
        pytesseract.pytesseract.tesseract_cmd = get_tesseract_path()

        image = Image.open(image_path)

        # Improve OCR quality
        image = image.convert("L")
        image = image.resize((800, 800))

        text = pytesseract.image_to_string(image)

        print("\n🧠 RAW OCR TEXT:\n", text)   # 👈 DEBUG (IMPORTANT)

        lines = text.split("\n")

        cleaned = [line.strip() for line in lines if line.strip()]

        print("\n📄 CLEANED LINES:\n", cleaned)  # 👈 DEBUG

        return cleaned

    except Exception as e:
        print(f"OCR Error: {e}")
        return []