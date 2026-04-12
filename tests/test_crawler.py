from src.crawler import parse_quotes_page


def test_parse_quotes_page_extracts_quote_data():
    sample_html = """
    <html>
        <body>
            <div class="quote">
                <span class="text">“Life is about making an impact, not making an income.”</span>
                <small class="author">Kevin Kruse</small>
                <div class="tags">
                    <a class="tag">life</a>
                    <a class="tag">inspirational</a>
                </div>
            </div>
        </body>
    </html>
    """

    results = parse_quotes_page(sample_html, "http://quotes.toscrape.com/page/1/")

    assert len(results) == 1
    assert results[0]["author"] == "Kevin Kruse"
    assert "life" in results[0]["tags"]
    assert results[0]["page_url"] == "http://quotes.toscrape.com/page/1/"


def test_parse_quotes_page_returns_empty_list_when_no_quotes():
    sample_html = "<html><body><p>No quotes here.</p></body></html>"

    results = parse_quotes_page(sample_html, "http://quotes.toscrape.com/page/1/")

    assert results == []
