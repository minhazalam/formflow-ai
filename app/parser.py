"""
Module: parser.py

Description:
Parses OCR text lines into structured records.

Author: Minhaz Alam
Created: 2026-04-16
"""
def parse_line(line):
    parts = line.split()

    if len(parts) < 4:
        return None

    return {
        "record_id": parts[0],
        "fname": parts[1],
        "lname": parts[2],
        "address": " ".join(parts[3:]),
        "status": "pending",
        "retry_count": 0
    }


def parse_lines(lines):
    """
    Convert raw text lines into structured records.

    Args:
        lines (list): List of text lines

    Returns:
        tuple: (records list, errors list)
    """
    records = []
    errors = []

    for line in lines:
        record = parse_line(line)

        if record:
            records.append(record)
        else:
            errors.append(line)

    return records, errors