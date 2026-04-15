from typing import Dict, List


def search_word(index: Dict, word: str) -> Dict:
    """
    Return all documents containing the word.
    """
    word = word.lower()
    return index.get(word, {})


def search_multiple_words(index: Dict, words: List[str]) -> List[int]:
    """
    Return document IDs that contain ALL words.
    """
    result_sets = []

    for word in words:
        word = word.lower()
        if word in index:
            result_sets.append(set(index[word].keys()))
        else:
            return []

    if not result_sets:
        return []

    return list(set.intersection(*result_sets))
