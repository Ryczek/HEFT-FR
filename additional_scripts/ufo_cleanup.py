#!/usr/bin/env python3
"""Remove duplicate UFO Parameter definitions with same variable name."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PARAM_START_RE = re.compile(r"^([A-Za-z_]\w*)\s*=\s*Parameter\(")


def dedupe_parameter_blocks(text: str) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    seen: set[str] = set()
    i = 0
    removed = 0

    while i < len(lines):
        match = PARAM_START_RE.match(lines[i].strip())
        if not match:
            out.append(lines[i])
            i += 1
            continue

        name = match.group(1)
        block: list[str] = [lines[i]]
        i += 1

        while i < len(lines):
            block.append(lines[i])
            if lines[i].strip().endswith(")"):
                i += 1
                break
            i += 1

        if name in seen:
            removed += 1
            continue

        seen.add(name)
        out.extend(block)

    return "".join(out), removed


def main() -> int:
    parser = argparse.ArgumentParser(description="Deduplicate UFO parameters.py")
    parser.add_argument("parameters_py", type=Path, help="Path to UFO parameters.py")
    args = parser.parse_args()

    path = args.parameters_py
    if not path.exists():
        print(f"[UFO cleanup] File not found: {path}")
        return 1

    original = path.read_text(encoding="utf-8")
    cleaned, removed = dedupe_parameter_blocks(original)
    if removed > 0:
        path.write_text(cleaned, encoding="utf-8")
    print(f"[UFO cleanup] Removed {removed} duplicate parameter block(s) from {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
