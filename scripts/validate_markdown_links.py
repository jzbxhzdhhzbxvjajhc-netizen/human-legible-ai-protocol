#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Validate local Markdown links in the repository."""

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    checked = 0
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            for raw_target in LINK.findall(line):
                target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_part = unquote(target.split("#", 1)[0])
                if not path_part:
                    continue
                checked += 1
                resolved = (document.parent / path_part).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    failures.append(f"{document.relative_to(ROOT)}:{line_number}: link escapes repository: {target}")
                    continue
                if not resolved.exists():
                    failures.append(f"{document.relative_to(ROOT)}:{line_number}: missing target: {target}")

    if failures:
        print("BROKEN local Markdown links:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"OK: {checked} local Markdown links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
