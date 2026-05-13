import re
from collections import defaultdict
from typing import Dict, List


def tokenize(text: str) -> List[str]:
    """
    Convert text to lowercase and split into words.
    """
    text = text.lower() # Convert text to lowercase and extract words only
    words = re.findall(r"\b[a-z]+\b", text)
    return words


def build_inverted_index(documents: List[dict]) -> Dict:
    """
    Build an inverted index:
    word -> {
        doc_id: {
            "count": frequency,
            "positions": [pos1, pos2, ...]
        }
    }
    """
    index = defaultdict(dict) # Create inverted index structure

    for doc_id, doc in enumerate(documents):
        words = tokenize(doc.get("text", ""))

        for position, word in enumerate(words):
            if doc_id not in index[word]:
                index[word][doc_id] = {
                    "count": 0,
                    "positions": []
                } # Store word frequency and positions

            index[word][doc_id]["count"] += 1
            index[word][doc_id]["positions"].append(position)

    return dict(index)
