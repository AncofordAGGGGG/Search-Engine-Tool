# Search-Engine-Tool

## Overview
This project implements a simple search engine for the website:
http://quotes.toscrape.com

It includes:
- Web crawler
- Inverted index
- Search functionality

## Features
- Crawl quotes from multiple pages
- Build inverted index (word → documents)
- Search for a single word
- Search for multiple words

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Build index

```bash
python -m src.main build 
```

### Search a word

```bash
python -m src.main print life
```

### Search multiple words

```bash
python -m src.main find life good
```

## Project Structure

```
src/
  crawler.py
  indexer.py
  search.py
  main.py

tests/
data/
```

## Testing

Run tests using:
```bash
pytest
```




