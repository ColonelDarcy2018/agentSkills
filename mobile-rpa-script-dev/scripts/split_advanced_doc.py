#!/usr/bin/env python3
"""
Split a large markdown doc into smaller section files for AI-friendly retrieval.

Usage:
  split_advanced_doc.py --source <source_md> --out <out_dir>
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List, Tuple


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`~!@#$%^&*()+=|{}':;',\\[\\].<>/?，。！？、：；（）【】《》‘’“”\"\\s]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "section"


def parse_sections(markdown: str) -> List[Tuple[str, List[str]]]:
    lines = markdown.splitlines()
    sections: List[Tuple[str, List[str]]] = []

    current_title = "00-overview"
    current_body: List[str] = []

    for line in lines:
        if line.startswith("## ") or line.startswith("# "):
            if current_body:
                sections.append((current_title, current_body))
            title = line.lstrip("#").strip()
            current_title = title
            current_body = [line]
        else:
            current_body.append(line)

    if current_body:
        sections.append((current_title, current_body))

    return sections


def write_sections(sections: List[Tuple[str, List[str]]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    toc_lines = ["# Split Index", ""]

    for idx, (title, body) in enumerate(sections, start=1):
        filename = f"{idx:02d}-{slugify(title)}.md"
        path = out_dir / filename
        path.write_text("\n".join(body).strip() + "\n", encoding="utf-8")
        toc_lines.append(f"- `{filename}`: {title}")

    toc_lines.append("")
    toc_lines.append(f"Total sections: {len(sections)}")

    (out_dir / "00-index.md").write_text("\n".join(toc_lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Split large markdown into smaller files")
    parser.add_argument("--source", required=True, help="Path to source markdown")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    source = Path(args.source)
    out_dir = Path(args.out)

    if not source.exists():
        raise FileNotFoundError(f"source not found: {source}")

    text = source.read_text(encoding="utf-8")
    sections = parse_sections(text)
    write_sections(sections, out_dir)

    print(f"split done: {len(sections)} sections -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
