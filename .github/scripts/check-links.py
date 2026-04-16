#!/usr/bin/env python3
"""
check-links.py — Internal link validator for Snyk user-docs.

Checks that every relative markdown link in docs/ resolves to an
existing file. Reports missing targets and exits non-zero if any
broken links are found.

Usage:
    python3 .github/scripts/check-links.py [--internal-only] [--path docs/]
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

DOCS_ROOT = Path(__file__).parent.parent.parent / "docs"

# Matches [text](target) and [text](target "title") — excludes http(s)
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')

# Matches ![alt](src)
IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')


def is_external(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https", "mailto", "ftp")


def is_gitbook_special(url: str) -> bool:
    """GitBook snippet syntax like {% ... %} or anchors-only."""
    return url.startswith("{%") or url.startswith("#")


def resolve_link(source_file: Path, target: str) -> Optional[Path]:
    """Return the resolved Path for a relative link, or None if external/special."""
    # Strip anchors
    target = target.split("#")[0].strip()
    # Strip title attributes: target "title"
    target = target.split('"')[0].strip().split("'")[0].strip()

    if not target:
        return None  # anchor-only link
    if is_external(target) or is_gitbook_special(target):
        return None

    resolved = (source_file.parent / target).resolve()
    return resolved


def check_file(md_file: Path, docs_root: Path) -> list[dict]:
    errors = []
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception as e:
        return [{"file": str(md_file), "line": 0, "target": "", "error": str(e)}]

    for line_num, line in enumerate(content.splitlines(), 1):
        for pattern in (LINK_RE, IMAGE_RE):
            for match in pattern.finditer(line):
                raw_target = match.group(2)
                resolved = resolve_link(md_file, raw_target)
                if resolved is None:
                    continue
                if not resolved.exists():
                    errors.append({
                        "file": str(md_file.relative_to(docs_root.parent)),
                        "line": line_num,
                        "target": raw_target,
                        "error": "File not found",
                    })
    return errors


def main():
    parser = argparse.ArgumentParser(description="Check internal markdown links.")
    parser.add_argument("--internal-only", action="store_true",
                        help="Only check internal (relative) links (default behaviour).")
    parser.add_argument("--path", default=str(DOCS_ROOT),
                        help="Root path to scan (default: docs/)")
    args = parser.parse_args()

    scan_root = Path(args.path)
    if not scan_root.exists():
        print(f"ERROR: Path does not exist: {scan_root}", file=sys.stderr)
        sys.exit(1)

    md_files = list(scan_root.rglob("*.md"))
    print(f"Scanning {len(md_files)} markdown files in {scan_root}...")

    all_errors: list[dict] = []
    for md_file in sorted(md_files):
        errors = check_file(md_file, DOCS_ROOT)
        all_errors.extend(errors)

    if all_errors:
        print(f"\n❌ Found {len(all_errors)} broken internal link(s):\n")
        for err in all_errors:
            print(f"  {err['file']}:{err['line']} → {err['target']}  [{err['error']}]")
        print()
        sys.exit(1)
    else:
        print(f"✅ All internal links valid ({len(md_files)} files checked).")
        sys.exit(0)


if __name__ == "__main__":
    main()
