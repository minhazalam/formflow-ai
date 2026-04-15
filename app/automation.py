"""
Module: automation.py

Description:
Handles browser automation to fill forms using Playwright.

Author: Minhaz Alam
Created: 2026-04-16
"""
from playwright.sync_api import sync_playwright
from app.config_loader import load_config
from utils.file_handler import save_records
from utils.logger import get_logger

MAX_RETRIES = 3


def fill_form(page, record, config):
    for field, selector in config["fields"].items():
        value = record.get(field, "")
        page.fill(selector, value)


def run_automation(records):
    """
    Execute automation workflow to fill web forms.

    Args:
        records (list): List of records to process

    Returns:
        None
    """

    logger = get_logger()
    config = load_config()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-gpu", "--no-sandbox"]
        )

        page = browser.new_page()
        page.goto(config["url"])

        for record in records:

            if record["status"] == "done":
                continue

            if record["retry_count"] >= MAX_RETRIES:
                logger.error(f"❌ Max retries exceeded: {record}")
                record["status"] = "failed"
                save_records(records)
                continue

            try:
                logger.info(f"➡️ Processing record: {record}")

                fill_form(page, record, config)

                input("👉 Review → Click SAVE → Press Enter...")

                record["status"] = "done"
                logger.info(f"✅ Success: {record}")

            except Exception as e:
                record["retry_count"] += 1
                record["status"] = "pending"

                logger.error(f"❌ Error: {e} | Retry: {record['retry_count']} | Record: {record}")

            finally:
                save_records(records)

        browser.close()