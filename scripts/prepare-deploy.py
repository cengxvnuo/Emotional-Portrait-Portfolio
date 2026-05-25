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


PUBLIC_HIDE_EDIT_UI = """
<style id="portfolio-public-deploy">
#portfolioEditToggle,#portfolioImageEditor,.portfolio-edit-bar,.portfolio-section-tools,.portfolio-img-tools{display:none!important}
body.portfolio-editing .portfolio-section-tools,body.portfolio-editing .portfolio-img-tools{display:none!important}
</style>
"""

def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    html, count = FILE_URL_PATTERN.subn(r"assets/image/\1", html)
    if 'id="portfolio-public-deploy"' not in html:
        html = html.replace("</head>", PUBLIC_HIDE_EDIT_UI + "</head>", 1)
    DST.write_text(html, encoding="utf-8")
    print(f"Wrote {DST.name}: replaced {count} local file:// image paths.")


if __name__ == "__main__":
    main()
