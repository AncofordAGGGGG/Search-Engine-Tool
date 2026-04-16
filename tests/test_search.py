from src.search import search_word, search_multiple_words


def test_search_word_returns_matching_documents():
    index = {
        "life": {
            0: {"count": 2, "positions": [0, 3]},
            2: {"count": 1, "positions": [5]}
        }
    }

    result = search_word(index, "life")

    assert 0 in result
    assert 2 in result
    assert result[0]["count"] == 2


def test_search_word_returns_empty_dict_for_missing_word():
    index = {
        "life": 
            0: {"count": 2, "positions": [0, 3]}
        }
    }

    result = search_word(index, "missing")

    assert result == {}


def test_search_multiple_words_returns_common_documents():
    index = {
        "life": {
            0: {"count": 2, "positions": [0, 3]},
            1: {"count": 1, "positions": [2]}
        },
        "good": {
            1: {"count": 1, "positions": [4]},
            2: {"count": 2, "positions": [1, 6]}
        },
        "is": {
            0: {"count": 1, "positions": [1]},
            1: {"count": 1, "positions": [3]}
        }
    }

    result = search_multiple_words(index, ["life", "is"])

    assert set(result) == {0, 1}


def test_search_multiple_words_returns_empty_list_when_no_overlap():
    index = {
        "life": {
            0: {"count": 2, "positions": [0, 3]}
        },
        "good": {
            1: {"count": 1, "positions": [4]}
        }
    }

    result = search_multiple_words(index, ["life", "good"])

    assert result == []
