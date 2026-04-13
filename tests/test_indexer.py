from src.indexer import tokenize, build_inverted_index


def test_tokenize_converts_text_to_lowercase_words():
    text = "Hello, World! Python is FUN."
    tokens = tokenize(text)

    assert tokens == ["hello", "world", "python", "is", "fun"]


def test_build_inverted_index_counts_words_and_positions():
    documents = [
        {"text": "Life is short life is good"},
        {"text": "Good things take time"}
    ]

    index = build_inverted_index(documents)

    assert "life" in index
    assert 0 in index["life"]
    assert index["life"][0]["count"] == 2
    assert index["life"][0]["positions"] == [0, 3]

    assert "good" in index
    assert index["good"][0]["count"] == 1
    assert index["good"][1]["count"] == 1


def test_build_inverted_index_returns_empty_dict_for_empty_documents():
    documents = []

    index = build_inverted_index(documents)

    assert index == {}
