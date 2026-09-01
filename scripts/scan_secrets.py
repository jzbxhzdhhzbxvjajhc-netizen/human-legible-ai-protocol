#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""Fail closed on common secrets in files, Git history, and release ZIPs."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path


PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub classic token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "Google API key": re.compile(r"\bAIza[A-Za-z0-9_-]{30,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "Stripe live secret": re.compile(r"\bsk_live_[A-Za-z0-9]{20,}\b"),
    "embedded URL password": re.compile(r"https?://[^\s/:]+:[^\s/@]{8,}@"),
    "assigned secret": re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password)\b"
        r"\s*[:=]\s*[\"']?([A-Za-z0-9_./+=-]{16,})"
    ),
    "personal email": re.compile(
        r"(?i)\b[A-Z0-9._%+-]+@(?:gmail\.com|qq\.com|163\.com|126\.com|outlook\.com|hotmail\.com)\b"
    ),
}

PLACEHOLDERS = (
    "your_",
    "your-",
    "example",
    "placeholder",
    "replace_me",
    "replace-me",
    "redacted",
    "dummy",
    "sample",
)
def run_git(*args: str, cwd: Path) -> bytes:
    return subprocess.check_output(["git", *args], cwd=cwd, stderr=subprocess.DEVNULL)


def scan_text(label: str, text: str) -> list[str]:
    findings: list[str] = []
    for name, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            value = match.group(1) if match.lastindex else match.group(0)
            lowered = value.lower()
            if any(marker in lowered for marker in PLACEHOLDERS):
                continue
            line = text.count("\n", 0, match.start()) + 1
            findings.append(f"{label}:{line}: possible {name}")
    return findings


def decode(data: bytes) -> str | None:
    if b"\x00" in data[:4096]:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan_current(repo: Path) -> tuple[list[str], int]:
    findings: list[str] = []
    count = 0
    listing = run_git("ls-files", "-z", "--cached", "--others", "--exclude-standard", cwd=repo)
    for raw_path in listing.decode("utf-8", errors="surrogateescape").split("\x00"):
        if not raw_path:
            continue
        path = repo / raw_path
        if not path.is_file():
            continue
        text = decode(path.read_bytes())
        if text is None:
            continue
        count += 1
        findings.extend(scan_text(f"current:{raw_path.replace(chr(92), '/')}", text))
    return findings, count


def scan_history(repo: Path) -> tuple[list[str], int]:
    findings: list[str] = []
    seen_blobs: set[str] = set()
    count = 0
    commits = run_git("rev-list", "--all", cwd=repo).decode().splitlines()
    for commit in commits:
        listing = run_git("ls-tree", "-r", commit, cwd=repo).decode().splitlines()
        for row in listing:
            meta, separator, path = row.partition("\t")
            if not separator:
                continue
            parts = meta.split()
            if len(parts) < 3 or parts[1] != "blob":
                continue
            blob = parts[2]
            if blob in seen_blobs:
                continue
            seen_blobs.add(blob)
            data = run_git("cat-file", "-p", blob, cwd=repo)
            text = decode(data)
            if text is None:
                continue
            count += 1
            findings.extend(scan_text(f"history:{commit[:8]}:{path}", text))
    return findings, count


def scan_git_metadata(repo: Path) -> tuple[list[str], int]:
    """Scan commit and annotated-tag identities/messages, not only file blobs."""
    findings: list[str] = []
    count = 0

    log_data = run_git(
        "log",
        "--all",
        "--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%B%x00",
        cwd=repo,
    )
    log_text = log_data.decode("utf-8", errors="replace")
    commit_records = [record for record in log_text.split("\n\n") if record.strip()]
    count += len(commit_records)
    findings.extend(scan_text("git-metadata:commits", log_text))

    tag_data = run_git(
        "for-each-ref",
        "refs/tags",
        "--format=%(refname)%00%(taggername)%00%(taggeremail)%00%(contents)%00",
        cwd=repo,
    )
    tag_text = tag_data.decode("utf-8", errors="replace")
    tag_records = [record for record in tag_text.split("\n") if record.strip()]
    count += len(tag_records)
    findings.extend(scan_text("git-metadata:tags", tag_text))

    return findings, count


def scan_archives(paths: list[Path]) -> tuple[list[str], int]:
    findings: list[str] = []
    count = 0
    for path in paths:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                data = archive.read(info)
                text = decode(data)
                if text is None:
                    continue
                count += 1
                findings.extend(scan_text(f"archive:{path.name}:{info.filename}", text))
    return findings, count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).parents[1])
    parser.add_argument("--zip", dest="archives", action="append", type=Path, default=[])
    args = parser.parse_args()
    repo = args.repo.resolve()

    findings, current_count = scan_current(repo)
    history_findings, history_count = scan_history(repo)
    findings.extend(history_findings)
    metadata_findings, metadata_count = scan_git_metadata(repo)
    findings.extend(metadata_findings)
    archive_findings, archive_count = scan_archives([path.resolve() for path in args.archives])
    findings.extend(archive_findings)

    if findings:
        print("BLOCKED: possible secret or personal contact data found:")
        for finding in findings:
            print(f"- {finding}")
        print("Do not publish. Revoke exposed keys, remove them from history, and scan again.")
        return 1

    print(
        "OK: no common secrets or personal contact emails found; "
        f"current_files={current_count}; historical_blobs={history_count}; "
        f"git_metadata_records={metadata_count}; archive_files={archive_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
