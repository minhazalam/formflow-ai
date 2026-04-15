"""
Module: main.py

Description:
Handles image processing pipeline including OCR extraction and parsing.
Acts as the core pipeline logic for FormFlow AI.

Author: Minhaz Alam
Created: 2026-04-16
"""
import os
from app.ocr import extract_lines
from app.parser import parse_lines
from utils.file_handler import save_records, load_records
from app.automation import run_automation
from utils.logger import get_logger

IMAGE_FOLDER = "data/images"


def process_images():
    """
    Process all images from the input folder and extract structured records.

    Performs OCR on images, parses extracted text into structured records,
    and stores them in the output file.

    Returns:
        list: List of extracted records
    """
    logger = get_logger()
    all_records = load_records()

    if not os.path.exists(IMAGE_FOLDER):
        logger.error("❌ Images folder not found")
        return []

    for file in os.listdir(IMAGE_FOLDER):

        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        path = os.path.join(IMAGE_FOLDER, file)

        logger.info(f"📸 Processing image: {file}")

        try:
            lines = extract_lines(path)
            records, errors = parse_lines(lines)

            if errors:
                logger.warning(f"⚠️ Parsing errors: {errors}")

            all_records.extend(records)
            save_records(all_records)

        except Exception as e:
            logger.error(f"❌ OCR failed for {file}: {e}")

    return all_records


if __name__ == "__main__":

    logger = get_logger()
    logger.info("🚀 Starting FormFlow AI")

    records = process_images()

    if not records:
        logger.warning("❌ No records found")
    else:
        logger.info(f"✅ Total records: {len(records)}")
        run_automation(records)