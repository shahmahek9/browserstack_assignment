# El País Opinion Scraper – Selenium + BrowserStack

## Overview
This project demonstrates **end-to-end web automation, scraping, API integration, and cross-browser testing** using Selenium.  
The script scrapes articles from the *Opinion* section of the Spanish newspaper **El País**, translates article titles to English, performs text analysis, and executes tests locally and on BrowserStack across multiple environments.

This assignment showcases:
- Selenium automation
- Web scraping with BeautifulSoup
- API integration (Google Translate)
- Text processing & analysis
- Cross-browser cloud testing (BrowserStack)

---

## Features

### Web Automation & Scraping
- Opens El País homepage and ensures Spanish content.
- Navigates to the **Opinion** section.
- Extracts the first **5 articles**:
  - Title (Spanish)
  - Article content preview
  - Cover image (downloaded locally)

### Translation API Integration
- Uses **Google Translator (deep-translator)** to translate Spanish titles → English.

### Text Analysis
- Combines translated titles.
- Finds words repeated **more than twice**.
- Outputs frequency analysis.

### Cross-Browser Testing (BrowserStack)
Configured for execution across:
- Windows 11 – Chrome
- Windows 10 – Firefox
- macOS Sonoma – Safari
- iPhone 14 – Safari
- Samsung Galaxy S23 – Chrome

Architecture supports **parallel execution** using ThreadPoolExecutor.

---

## Project Structure

```

browserstack_elpias/
│
├── scraper/
│   ├── **init**.py
│   ├── scraper.py          # Selenium scraping + BrowserStack driver
│   ├── translator.py       # Google Translate integration
│   └── analyzer.py         # Word frequency analysis
│
├── tests/
│   └── test_browserstack.py
│
├── images/                 # Downloaded article images
├── main.py                 # Local execution script
├── run_browserstack_parallel.py
├── pytest.ini
└── README.md

````

---

## Installation

### 1. Clone repository
```bash
git clone <repo-url>
cd browserstack_elpias
````

### 2. Create virtual environment

```bash
python -m venv bsenv
bsenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Required packages:

```
selenium
beautifulsoup4
requests
deep-translator
pytest
```

---

## Local Execution

Run scraper locally:

```bash
python main.py
```

Output:

* Spanish article titles + content preview
* Downloaded images in `/images`
* Translated English titles
* Repeated word analysis

---

## BrowserStack Setup

### 1. Get credentials

Login → [https://automate.browserstack.com](https://automate.browserstack.com)
Account → Access Keys

### 2. Set environment variables (Windows)

```bat
set BROWSERSTACK_USERNAME=YOUR_USERNAME
set BROWSERSTACK_ACCESS_KEY=YOUR_ACCESS_KEY
```

Verify:

```bat
echo %BROWSERSTACK_USERNAME%
```

---

## Run on BrowserStack

Run cross-browser execution:

```bash
python run_browserstack_parallel.py
```

The runner executes the test across 5 environments sequentially.

### Note on Parallel Execution

The architecture supports **parallel execution via ThreadPoolExecutor**.
Due to BrowserStack trial plan concurrency limits, the demo runs sequentially.
With higher concurrency enabled, the script runs fully parallel.

---

## Expected Output

For each environment:

* Browser session appears on BrowserStack dashboard
* Titles printed in Spanish
* Images saved locally
* Titles translated to English
* Repeated words printed

---

## Example Analysis Output

```
TRANSLATED TITLES:
Politics and the future of Europe
The crisis of democracy
...

WORDS REPEATED MORE THAN TWICE:
europe 3
politics 3
```

---

## Security Note

Environment variables are used for BrowserStack credentials.
Do not commit credentials to version control.

---

## Tech Stack

* Python 3.11+
* Selenium 4
* BeautifulSoup
* Deep Translator API
* BrowserStack Automate
* PyTest

---

## Conclusion

This project demonstrates a complete workflow combining **automation, scraping, APIs, text analytics and cloud testing** in a production-style architecture.

```
```
