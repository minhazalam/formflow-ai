"""
Module: cli.py

Description:
Provides command-line interface for running FormFlow AI pipeline.

Author: Minhaz Alam
Created: 2026-04-16
"""
import argparse
from main import process_images
from utils.file_handler import load_records
from app.automation import run_automation
from utils.logger import get_logger


def run_cli():
    parser = argparse.ArgumentParser(
        description="🚀 FormFlow AI CLI"
    )

    parser.add_argument(
        "command",
        nargs="?",  # 👈 makes it optional
        default="all",
        choices=["extract", "run", "all"],
        help="Command to execute"
    )

    args = parser.parse_args()
    logger = get_logger()

    logger.info("🚀 Starting FormFlow AI")

    if args.command == "extract":
        logger.info("📸 Running OCR + Parsing...")
        records = process_images()
        logger.info(f"✅ Extracted {len(records)} records")

    elif args.command == "run":
        logger.info("🤖 Running automation...")
        records = load_records()

        if not records:
            logger.warning("❌ No records found. Run 'extract' first.")
            return

        logger.info(f"✅ Loaded {len(records)} records")
        run_automation(records)

    elif args.command == "all":
        logger.info("🚀 Running full pipeline...")

        records = process_images()

        if not records:
            logger.warning("❌ No records found")
            return

        logger.info(f"✅ Total records: {len(records)}")
        run_automation(records)