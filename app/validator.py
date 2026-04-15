def validate(record):
    errors = []

    if not record["record_id"].startswith("xt"):
        errors.append("Invalid record_id")

    if not record["fname"].isalpha():
        errors.append("Invalid fname")

    return errors