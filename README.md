# basic-scraper

## TLDR

This is a quick project that I coded to learn scraping and specifically start learning pagination.

## Description

This is a scraper that goes through all the pages at books.toscrape.com

it finds each book and writes its title, price and if it is available into a csv file then outputs it as books.csv

## Purpose

I am currently trying to code another project that incorporates scraping and wanted to use this project as a stepping stone for confidence and understanding as it has very few obstacles. I initially planned to learn scraping during the project, but when I got blocked by bot detection with walmart I decided to do this project before trying another supermarket scraper.

## How to Run it?

Make sure Python and Git are installed, then run:

```bash
git clone https://github.com/sammerdog516/basic-scraper.git
cd basic-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the scraper:

```bash
python scraper.py
```

Once the scraper finishes, it will create `books.csv` in the project directory. You can open this file using Excel, another spreadsheet program, a text editor, or any other CSV viewer.