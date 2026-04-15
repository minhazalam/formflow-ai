# 🚀 FormFlow AI
🚧 Currently under active development — more features coming soon.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/Automation-Playwright-green)
![OCR](https://img.shields.io/badge/OCR-Tesseract-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

> **Human-in-the-loop OCR-powered form automation system**
> Extract data from images → auto-fill forms → validate in real UI → submit → repeat.

---

## ✨ Overview

FormFlow AI is designed to automate repetitive data entry workflows while keeping humans in control.

It extracts structured data from images using OCR, processes it into records, and assists users in entering the data into web forms. Users review and correct data directly in the target application before submission.

---

## 🧠 How It Works

```text id="flow-final"
Images → OCR → Parsing → Records Queue → Auto-fill Form → Human Review → Submit → Next Record
```

---

## 🔥 Key Features

* 📸 OCR-based data extraction using Tesseract
* 🧩 Structured parsing with normalization and validation
* 🔁 Retry mechanism with logging and error handling
* 🧑 Human-in-the-loop validation inside the actual web application
* 🔗 Config-driven field mapping (no code changes required)
* ⚡ Lightweight and local-first design
* 💻 CLI support for modular pipeline execution

---

## 🧰 Tech Stack

* Python
* Tesseract OCR
* Playwright

---

## 📁 Project Structure

```text id="struct-final"
app/        # OCR, parser, automation
utils/      # logging, file handling
config/     # form and parsing configurations
data/       # input images and runtime data
cli.py      # CLI interface
main.py     # entry point
```

---

## ⚙️ Setup & Run

### 1. Create Virtual Environment

```bash id="venv-final"
python -m venv venv
```

Activate:

* **Mac/Linux**

```bash id="mac-final"
source venv/bin/activate
```

* **Windows**

```bash id="win-final"
venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash id="deps-final"
pip install -r requirements.txt
playwright install
```

---

### 3. Install Tesseract OCR

* **Mac (Homebrew)**

```bash id="mac-tess-final"
brew install tesseract
```

* **Ubuntu / Linux**

```bash id="linux-tess-final"
sudo apt update
sudo apt install tesseract-ocr
```

* **Windows**

1. Download installer from:
   https://github.com/tesseract-ocr/tesseract
2. Install it
3. Add to PATH:

   ```
   C:\Program Files\Tesseract-OCR
   ```

> ⚠️ Verify installation:

```bash id="verify-final"
tesseract --version
```

---

### 4. Run the Application

FormFlow AI supports a **basic CLI interface** for modular execution.

#### ▶️ Run Full Pipeline (Default)

```bash
python main.py
```
Runs: OCR → Parsing → Automation

## 🧪 Example Workflow

```bash
# Step 1: Extract records
python main.py extract

# Step 2: Run automation
python main.py run
```

---

## 🧪 Example Input

```text id="example-final"
xt1234 john doe california
xt5678 alice smith new york
```

---

## 🚀 Use Cases

* Data entry automation
* Back-office workflows
* OCR-based ingestion pipelines
* Form processing systems

---

## 🛣️ Roadmap

* Streamlit-based review dashboard
* Multi-form support
* AI-assisted parsing fallback
* Batch processing enhancements

---

## 📜 License

MIT License © 2026 Minhaz Alam

---

## 👤 Author

**Minhaz Alam**
