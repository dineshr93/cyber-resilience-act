#!/usr/bin/env python3
"""Verify a draft CRA answer against the primary source text.

Usage: verify-citations.py DRAFT.md [--self-test]
Extracts article/annex/date/fine citations from the draft, greps them
against sources/CELEX_02024R2847-20241120_EN_TXT.md, exits 1 if any
citation is not found. Deterministic: no LLM, no network.

ponytail: substring grep only — no article-body parsing. Upgrade to
per-article section checks if false positives matter.
"""
import calendar
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "sources" / "CELEX_02024R2847-20241120_EN_TXT.md"
MONTHS = dict(zip(calendar.month_abbr[1:], calendar.month_name[1:]))

ART_RE = re.compile(r"\bArt(?:icle)?\s+(\d{1,3})\b")
ANNEX_RE = re.compile(r"\bAnnex\s+([IVX]{1,3})\b")
DATE_RE = re.compile(r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})\b")
FINE_RE = re.compile(r"€(\d{1,3})M\b")


def extract(text):
    """Return list of (kind, raw, needle) tuples to look up in the source."""
    out = []
    for m in ART_RE.finditer(text):
        out.append(("article", m.group(0), f"Article {m.group(1)}"))
    for m in ANNEX_RE.finditer(text):
        out.append(("annex", m.group(0), f"ANNEX {m.group(1)}"))
    for m in DATE_RE.finditer(text):
        needle = f"{m.group(1)} {MONTHS[m.group(2)]} {m.group(3)}"
        out.append(("date", m.group(0), needle))
    for m in FINE_RE.finditer(text):
        out.append(("fine", m.group(0), f"{m.group(1)} 000 000"))
    return out


def verify(draft_text, src_text):
    failures = []
    for kind, raw, needle in extract(draft_text):
        if needle not in src_text:
            failures.append((kind, raw, needle))
    return failures


def self_test():
    assert ("article", "Art 13", "Article 13") in extract("Duties under Art 13 apply.")
    assert ("fine", "€15M", "15 000 000") in extract("Fines up to €15M.")
    assert ("date", "11 Sep 2026", "11 September 2026") in extract("Live from 11 Sep 2026.")
    assert ("annex", "Annex I", "ANNEX I") in extract("Annex I Part I.")
    # bogus citation must fail against a source that lacks it
    assert verify("Art 999 applies.", "Article 13 ...") != []
    assert verify("Article 13 applies.", "Article 13 ...") == []
    print("self-test ok")


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if not args:
        sys.exit("usage: verify-citations.py DRAFT.md [--self-test]")
    src_text = SRC.read_text()
    failures = verify(Path(args[0]).read_text(), src_text)
    for kind, raw, needle in failures:
        print(f"FAIL {kind}: '{raw}' -> '{needle}' not found in source")
    print(f"{len(failures)} failure(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
