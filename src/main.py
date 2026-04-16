import json
import sys

from src.crawler import crawl_quotes
from src.indexer import build_inverted_index
from src.search import search_word, search_multiple_words


INDEX_FILE = "data/index.json"


def build():
    print("Crawling data...")
    documents = crawl_quotes(max_pages=3)

    print("Building index...")
    index = build_inverted_index(documents)

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f)

    print("Index saved to", INDEX_FILE)


def load():
    with open(INDEX_FILE, "r") as f:
        return json.load(f)


def print_word(word):
    index = load()
    result = search_word(index, word)
    print(result)


def find_words(words):
    index = load()
    result = search_multiple_words(index, words)
    print(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [build|print|find]")
        return

    command = sys.argv[1]

    if command == "build":
        build()
    elif command == "print":
        if len(sys.argv) < 3:
            print("Usage: print <word>")
            return
        print_word(sys.argv[2])
    elif command == "find":
        if len(sys.argv) < 3:
            print("Usage: find <word1> <word2> ...")
            return
        find_words(sys.argv[2:])
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
