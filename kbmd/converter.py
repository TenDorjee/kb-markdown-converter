# kbmd/converter.py
"""Convert my.opentext.com article API responses to Markdown."""

import json

from markdownify import markdownify


def convert_article(payload: dict) -> str:
    """Convert an article API response to Markdown (title + body only).

    Args:
        payload: JSON from /api/web/support/article/{id}.

    Returns:
        Markdown with an H1 title and the converted body.

    Raises:
        KeyError: If "response", "Title" or "Content" is missing.
    """
    article = payload["response"]
    body = markdownify(article["Content"], heading_style="ATX")  # "#" style headings
    return f"# {article['Title']}\n\n{body}"


if __name__ == "__main__":
    # Usage: python -m kbmd.converter <article.json>
    import sys

    with open(sys.argv[1], encoding="utf-8") as f:
        print(convert_article(json.load(f)))