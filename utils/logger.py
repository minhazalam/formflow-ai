"""
Module: logger.py

Description:
Configures and provides application-wide logging.

Author: Minhaz Alam
Created: 2026-04-16
"""
import logging
import os

LOG_DIR = "data/logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():
    return logging