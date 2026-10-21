# Web Scraping: Books to Scrape

## Project Overview

This project uses Python to scrape book information from [Books to Scrape](https://books.toscrape.com/), a practice website designed for web scraping exercises.

The scraper navigates through 50 catalogue pages, extracts book information, and exports the collected records to a CSV dataset for further analysis.

## Objectives

- Retrieve webpage content using Python.
- Parse HTML and extract structured information.
- Automate data collection across multiple pages.
- Store scraped information in a structured dataset.
- Export the results to CSV for data analysis.

## Technologies Used

- **Python** — programming and automation
- **Requests** — retrieving webpage content
- **BeautifulSoup** — parsing HTML and extracting information
- **Pandas** — organizing and exporting data

## Dataset Description

The resulting dataset contains 1,000 book records and four columns:

| Column | Description |
|---|---|
| Title | Name of the book |
| Price | Listed price in pounds sterling |
| Rating | Star rating represented as a word |
| Availability | Stock availability information |

**Output file:** `books_dataset.csv`

## Installation

Install the required libraries:

```bash
python -m pip install requests beautifulsoup4 pandas
```

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the scraper:

```bash
python main.py
```

4. The program will scrape the catalogue pages and generate `books_dataset.csv`.

## Learning Outcomes

This project demonstrates practical experience with HTTP requests, HTML parsing, CSS class selection, loops, pagination, structured data collection, and CSV export using Python.

## Data Source and Acknowledgment

Data source: [Books to Scrape](https://books.toscrape.com/)

This project was developed for educational purposes as part of a data analytics learning journey.

## Author

**Kaushik Arnob**

