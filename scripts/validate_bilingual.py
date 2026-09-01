#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Validate bilingual HLAI decision-parity cases."""

import json
import sys
from pathlib import Path


REQUIRED = {
    "id",
    "mode",
    "zh_input",
    "en_input",
    "invariants",
    "zh_plain_term",
    "en_plain_term",
}
MODES = {"START", "CONTROL", "EXPLAIN"}


def main() -> int:
    path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).parents[1] / "evals" / "bilingual-parity.jsonl"
    )
    ids: set[str] = set()
    counts = {mode: 0 for mode in MODES}

    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                case = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"line {line_number}: invalid JSON: {exc}") from exc

            missing = REQUIRED - case.keys()
            if missing:
                raise SystemExit(f"line {line_number}: missing fields: {sorted(missing)}")
            if case["mode"] not in MODES:
                raise SystemExit(f"line {line_number}: invalid mode: {case['mode']}")
            if case["id"] in ids:
                raise SystemExit(f"line {line_number}: duplicate id: {case['id']}")
            for field in ("zh_input", "en_input", "zh_plain_term", "en_plain_term"):
                if not isinstance(case[field], str) or not case[field].strip():
                    raise SystemExit(f"line {line_number}: {field} must be a non-empty string")
            if not isinstance(case["invariants"], list) or not case["invariants"]:
                raise SystemExit(f"line {line_number}: invariants must be a non-empty list")

            ids.add(case["id"])
            counts[case["mode"]] += 1

    if not all(counts.values()):
        raise SystemExit(f"each mode needs at least one parity case: {counts}")

    print(
        f"OK: {len(ids)} bilingual parity cases; "
        + ", ".join(f"{mode}={counts[mode]}" for mode in sorted(MODES))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
