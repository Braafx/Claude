"""Entry point for the daily art newsletter.

Usage:
    python -m tools.newsletter.run            # send today's newsletter
    python -m tools.newsletter.run --preview  # generate HTML file only (no email)
    python -m tools.newsletter.run --date 2026-03-25  # specific date
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from .content import generate
from .emailer import send
from .template import render


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and send daily art newsletter")
    parser.add_argument("--preview", action="store_true", help="Write HTML to file instead of emailing")
    parser.add_argument("--date", type=str, default=None, help="Date to generate for (YYYY-MM-DD)")
    args = parser.parse_args()

    target_date: date | None = None
    if args.date:
        target_date = date.fromisoformat(args.date)

    print("Generating content…")
    content = generate(for_date=target_date)
    html = render(content)

    output_dir = Path(__file__).parent.parent.parent / "newsletters"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{content.date}.html"
    output_file.write_text(html, encoding="utf-8")
    print(f"✓ Newsletter written to {output_file}")

    if args.preview:
        print(f"\nPreview mode — open {output_file} in your browser.")
        return

    try:
        subject = f"🎨 Daily Art Brief — {content.date}"
        send(subject=subject, html_body=html)
    except FileNotFoundError as e:
        print(f"\n⚠️  {e}", file=sys.stderr)
        print("The newsletter HTML has been saved locally. Set up config.json to enable email.")
        sys.exit(1)


if __name__ == "__main__":
    main()
