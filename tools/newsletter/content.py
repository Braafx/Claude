"""Newsletter content generation — picks daily content from curated JSON pools."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent.parent / "data"


@dataclass
class NewsletterContent:
    date: str
    tutorial: dict[str, Any]
    throwback: dict[str, Any]
    brush: dict[str, Any]
    coach_note: str
    bonus: dict[str, Any]
    reference_query: str
    reference_url: str


def _seeded_pick(items: list[Any], seed: str) -> Any:
    """Deterministic pick from a list based on a seed — same seed = same result."""
    index = int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(items)
    return items[index]


def _load(filename: str) -> list[Any]:
    return json.loads((DATA_DIR / filename).read_text(encoding="utf-8"))


def generate(for_date: date | None = None) -> NewsletterContent:
    """Generate newsletter content for the given date (defaults to today)."""
    today = for_date or date.today()
    ds = today.isoformat()

    tutorials = _load("tutorials.json")
    throwbacks = _load("throwbacks.json")
    brushes = _load("brushes.json")
    coach_notes = _load("coach_notes.json")
    bonuses = _load("bonuses.json")
    queries = _load("reference_queries.json")

    ref_query = _seeded_pick(queries, f"{ds}-ref")
    ref_url = (
        f"https://source.unsplash.com/1280x800/?{ref_query.replace(' ', ',')}"
    )

    return NewsletterContent(
        date=ds,
        tutorial=_seeded_pick(tutorials, f"{ds}-tutorial"),
        throwback=_seeded_pick(throwbacks, f"{ds}-throwback"),
        brush=_seeded_pick(brushes, f"{ds}-brush"),
        coach_note=_seeded_pick(coach_notes, f"{ds}-coach"),
        bonus=_seeded_pick(bonuses, f"{ds}-bonus"),
        reference_query=ref_query,
        reference_url=ref_url,
    )
