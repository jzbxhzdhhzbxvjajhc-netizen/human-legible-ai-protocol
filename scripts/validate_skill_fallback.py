#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Dependency-free fallback for the official Skill quick validator.

The official validator remains preferred. This script covers the same rules
used by HLAI's simple two-field frontmatter when PyYAML is unavailable.
"""

import ast
import re
import sys
from pathlib import Path


ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}
MAX_SKILL_NAME_LENGTH = 64


def parse_scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value[0] in {"'", '"'}:
        parsed = ast.literal_eval(value)
        if not isinstance(parsed, str):
            raise ValueError("frontmatter values must be strings")
        return parsed
    return value


def main() -> int:
    skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1] / "skill" / "human-legible-ai"
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit("SKILL.md not found")

    content = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not match:
        raise SystemExit("Invalid frontmatter format")

    fields: dict[str, str] = {}
    for line_number, line in enumerate(match.group(1).splitlines(), 1):
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or not key.strip():
            raise SystemExit(f"frontmatter line {line_number}: expected key: value")
        key = key.strip()
        if key in fields:
            raise SystemExit(f"duplicate frontmatter key: {key}")
        try:
            fields[key] = parse_scalar(value)
        except (SyntaxError, ValueError) as exc:
            raise SystemExit(f"frontmatter line {line_number}: invalid string: {exc}") from exc

    unexpected = set(fields) - ALLOWED
    if unexpected:
        raise SystemExit(f"unexpected frontmatter keys: {sorted(unexpected)}")
    for required in ("name", "description"):
        if required not in fields:
            raise SystemExit(f"missing frontmatter key: {required}")

    name = fields["name"].strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise SystemExit("name must use lowercase letters, digits, and single hyphens")
    if len(name) > MAX_SKILL_NAME_LENGTH:
        raise SystemExit(f"name exceeds {MAX_SKILL_NAME_LENGTH} characters")

    description = fields["description"].strip()
    if not description:
        raise SystemExit("description must not be empty")
    if len(description) > 1024:
        raise SystemExit("description exceeds 1024 characters")
    if "<" in description or ">" in description:
        raise SystemExit("description must not contain angle brackets")
    if "[TODO:" in content:
        raise SystemExit("unfinished TODO placeholder found")

    for linked in re.findall(r"\[[^\]]+\]\((references/[^)]+)\)", content):
        if not (skill_dir / linked).exists():
            raise SystemExit(f"missing linked reference: {linked}")

    print(f"OK: valid Skill structure; name={name}; description={len(description)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
