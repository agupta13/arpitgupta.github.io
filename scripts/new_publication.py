#!/usr/bin/env python3
"""
Create a new publication record for the Jekyll site.

Usage (command-line flags):
  python scripts/new_publication.py \
    --title "Paper Title" \
    --authors "A. Author, B. Author" \
    --venue "ACM SIGCOMM, 2025" \
    --date 2025-08-01 \
    --url "https://example.com/paper.pdf" \
    --pdf "/pdfs/paper.pdf" \
    --award "Best Paper Award" \
    --link "Project Website|https://example.com" \
    --link "Press Release|https://news.example.com"

Usage (text prompt — pipe or pass as positional arg):
  python scripts/new_publication.py "
    title: Paper Title
    authors: A. Author, B. Author
    venue: ACM SIGCOMM, 2025
    date: 2025-08-01
    paperurl: https://example.com/paper.pdf
    award: Best Paper Award
    link: Project Website|https://example.com
  "

The script creates a file in _publications/ and prints its path.
"""

import argparse
import os
import re
import sys
import unicodedata
from datetime import date


PUBLICATIONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "_publications",
)


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80]


def parse_prompt(text: str) -> dict:
    """Parse a key: value text block into a dict."""
    data = {
        "title": "",
        "authors": "",
        "venue": "",
        "date": "",
        "paperurl": "",
        "pdf": "",
        "pubtype": "",
        "awards": [],
        "links": [],
    }
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r"^(\w+)\s*:\s*(.+)$", line)
        if not match:
            continue
        key, val = match.group(1).lower(), match.group(2).strip()
        if key == "title":
            data["title"] = val
        elif key == "authors":
            data["authors"] = val
        elif key == "venue":
            data["venue"] = val
        elif key == "date":
            data["date"] = val
        elif key in ("paperurl", "url"):
            data["paperurl"] = val
        elif key == "pdf":
            data["pdf"] = val
        elif key == "pubtype":
            data["pubtype"] = val
        elif key == "award":
            data["awards"].append(val)
        elif key == "link":
            if "|" in val:
                txt, url = val.split("|", 1)
                data["links"].append({"text": txt.strip(), "url": url.strip()})
            else:
                data["links"].append({"text": val, "url": val})
    return data


def build_front_matter(data: dict) -> str:
    """Build YAML front matter string."""
    lines = ["---"]
    lines.append(f'title: "{data["title"]}"')
    lines.append(f'authors: "{data["authors"]}"')
    lines.append(f'venue: "{data["venue"]}"')
    lines.append(f"date: {data['date']}")
    if data.get("paperurl"):
        lines.append(f'paperurl: "{data["paperurl"]}"')
    if data.get("pubtype"):
        lines.append(f'pubtype: "{data["pubtype"]}"')
    if data.get("pdf"):
        lines.append(f'pdf: "{data["pdf"]}"')
    if data.get("awards"):
        lines.append("awards:")
        for award in data["awards"]:
            lines.append(f'  - "{award}"')
    if data.get("links"):
        lines.append("links:")
        for link in data["links"]:
            lines.append(f"  - text: \"{link['text']}\"")
            lines.append(f"    url: \"{link['url']}\"")
    lines.append("---")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Create a new _publications/ record."
    )
    parser.add_argument("prompt", nargs="?", default=None,
                        help="Text prompt with key: value lines (alternative to flags)")
    parser.add_argument("--title", default="")
    parser.add_argument("--authors", default="")
    parser.add_argument("--venue", default="")
    parser.add_argument("--date", default="")
    parser.add_argument("--url", dest="paperurl", default="")
    parser.add_argument("--pdf", default="")
    parser.add_argument("--pubtype", default="",
                        help='"preprint" or "policy" (omit for peer-reviewed)')
    parser.add_argument("--award", action="append", default=[])
    parser.add_argument("--link", action="append", default=[],
                        help='"Link Text|https://url"')
    args = parser.parse_args()

    # If a prompt string is provided (positional or stdin), parse it
    if args.prompt:
        data = parse_prompt(args.prompt)
    elif not sys.stdin.isatty():
        data = parse_prompt(sys.stdin.read())
    else:
        # Use flag values
        data = {
            "title": args.title,
            "authors": args.authors,
            "venue": args.venue,
            "date": args.date,
            "paperurl": args.paperurl,
            "pdf": args.pdf,
            "pubtype": args.pubtype,
            "awards": args.award,
            "links": [],
        }
        for link_str in args.link:
            if "|" in link_str:
                txt, url = link_str.split("|", 1)
                data["links"].append({"text": txt.strip(), "url": url.strip()})
            else:
                data["links"].append({"text": link_str, "url": link_str})

    # Validate required fields
    missing = [f for f in ("title", "authors", "venue", "date") if not data.get(f)]
    if missing:
        print(f"Error: missing required fields: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    # Validate date format
    try:
        date_str = str(data["date"]).strip()
        parts = date_str.split("-")
        if len(parts) == 3:
            date(int(parts[0]), int(parts[1]), int(parts[2]))
        else:
            raise ValueError("expected YYYY-MM-DD")
        data["date"] = date_str
    except (ValueError, IndexError) as e:
        print(f"Error: invalid date '{data['date']}' — use YYYY-MM-DD: {e}",
              file=sys.stderr)
        sys.exit(1)

    # Build filename
    slug = slugify(data["title"])
    filename = f"{data['date']}-{slug}.md"
    filepath = os.path.join(PUBLICATIONS_DIR, filename)

    if os.path.exists(filepath):
        print(f"Error: file already exists: {filepath}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(PUBLICATIONS_DIR, exist_ok=True)
    content = build_front_matter(data)
    with open(filepath, "w") as f:
        f.write(content)

    print(f"Created: {filepath}")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
