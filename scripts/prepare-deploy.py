#!/usr/bin/env python3
"""Build index.html for GitHub Pages from code-edited.html."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "code-edited.html"
DST = ROOT / "index.html"

FILE_URL_PATTERN = re.compile(
    r'file:///[^"\']+/assets/image/([^"\'?]+)',
    re.IGNORECASE,
)


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    html, count = FILE_URL_PATTERN.subn(r"assets/image/\1", html)
    DST.write_text(html, encoding="utf-8")
    print(f"Wrote {DST.name}: replaced {count} local file:// image paths.")


if __name__ == "__main__":
    main()
