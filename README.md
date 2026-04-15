# 🚀 FormFlow AI

**Human-in-the-loop OCR-powered form automation tool**

---

## 🧠 Overview

FormFlow AI extracts structured data from images and assists users in entering it into web forms with human validation.

Instead of blindly automating data entry, it keeps the user in control:

* Auto-fills form fields
* User reviews & edits in the actual web app
* User clicks **Save/Update**
* System moves to next record

---

## ⚙️ Workflow

```
Images → OCR → Parsing → Records Queue → Auto-fill Form → Human Review → Submit → Next Record
```

---

## 🔥 Features

* 📸 OCR-based data extraction (Tesseract)
* 🧠 Smart parsing with error handling
* 🔁 Retry mechanism for failed records
* 🧑 Human-in-the-loop validation (in browser)
* 🔗 Config-driven field mapping
* 📝 Logging & resumable execution

---

## 🧰 Tech Stack

* Python
* Tesseract OCR
* Playwright

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
playwright install
python main.py
```

Install Tesseract:

```bash
brew install tesseract
```

---

## 📁 Project Structure

```
app/        # core logic (OCR, parser, automation)
utils/      # helpers (logger, file handler)
config/     # form + parsing configs
data/       # images + output
```

---

## 🚀 Use Cases

* Data entry automation
* Back-office operations
* Form filling workflows
* Manual-to-digital conversion

---

## ⚡ Future Improvements

* Dashboard UI
* Multi-form support
* AI-based parsing fallback
* Bulk processing

---

## 👤 Author

Minhaz Alam
