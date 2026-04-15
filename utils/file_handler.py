"""
Module: file_handler.py

Description:
Handles reading and writing of records to JSON storage.

Author: Minhaz Alam
Created: 2026-04-16
"""
import json
import os

DATA_PATH = "data/output/records.json"


def save_records(records):
    os.makedirs("data/output", exist_ok=True)

    with open(DATA_PATH, "w") as f:
        json.dump(records, f, indent=2)


def load_records():
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, "r") as f:
        return json.load(f)