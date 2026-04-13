#!/usr/bin/env python3
"""
PostToolUse hook for the `prr` Claude Code plugin.

Validates YAML frontmatter on files written by Write/Edit/MultiEdit when the
frontmatter declares `managed_by: prr`. Non-prr files are ignored — this hook
must never interfere with a user's own markdown.

Exit codes:
  0 = ok, or file is not managed by prr (skip silently)
  2 = validation failed; stderr is surfaced to Claude so it can self-correct

No third-party dependencies — stdlib only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ALLOWED_TYPES = {
    "roadmap",
    "theme",
    "roi-scorecard",
    "change-communication",
    "special-request-evaluation",
}

ALLOWED_TIMEFRAMES = {"Now", "Next", "Later"}

MANAGED_BY_VALUE = "prr"


def read_event() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def target_path(event: dict) -> str | None:
    tool = event.get("tool_name", "")
    inp = event.get("tool_input", {}) or {}
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        return inp.get("file_path")
    return None


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_frontmatter(text: str) -> str | None:
    m = FRONTMATTER_RE.match(text)
    return m.group(1) if m else None


def strip_comment_and_quotes(value: str) -> str:
    value = re.sub(r"\s+#.*$", "", value).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def scalar(fm: str, key: str) -> str | None:
    """Return the trimmed scalar after `key:` on a top-level frontmatter line."""
    pattern = rf"^{re.escape(key)}:\s*(.*?)$"
    m = re.search(pattern, fm, re.MULTILINE)
    if not m:
        return None
    return strip_comment_and_quotes(m.group(1))


def has_nonempty_list(fm: str, key: str) -> bool:
    """True if `key:` has a non-empty inline list [a, b] or block list (`- item`)."""
    inline = re.search(
        rf"^{re.escape(key)}:\s*\[(.*?)\]\s*(?:#.*)?$", fm, re.MULTILINE
    )
    if inline:
        return bool(inline.group(1).strip())
    block = re.search(
        rf"^{re.escape(key)}:\s*(?:#.*)?\n((?:[ \t]+-[ \t]+.+\n?)+)",
        fm,
        re.MULTILINE,
    )
    return bool(block)


def has_scalar_or_block(fm: str, key: str) -> bool:
    """True if `key:` is present with any non-empty value (scalar or folded block)."""
    val = scalar(fm, key)
    if val:
        return True
    # Folded / literal block scalar: `key: >` or `key: |` followed by indented lines.
    block = re.search(
        rf"^{re.escape(key)}:\s*[>|]\s*\n((?:[ \t]+.+\n?)+)", fm, re.MULTILINE
    )
    return bool(block)


def validate(text: str) -> list[str]:
    fm = extract_frontmatter(text)
    if fm is None:
        return []

    if strip_comment_and_quotes(scalar(fm, "managed_by") or "") != MANAGED_BY_VALUE:
        return []

    errors: list[str] = []
    artifact_type = scalar(fm, "type")
    if artifact_type not in ALLOWED_TYPES:
        errors.append(
            f"`type:` must be one of {sorted(ALLOWED_TYPES)}; got '{artifact_type}'."
        )
        return errors

    if artifact_type == "roadmap":
        for required in ("vision", "disclaimer"):
            if not has_scalar_or_block(fm, required):
                errors.append(
                    f"roadmap requires `{required}:` — missing or empty. "
                    "See skills/product-roadmaps/templates/roadmap.md."
                )
        if not has_nonempty_list(fm, "objectives"):
            errors.append(
                "roadmap requires non-empty `objectives:` list — a roadmap with no "
                "business objectives is a Roadmap Without Strategic Context anti-pattern."
            )

    elif artifact_type == "theme":
        if not has_nonempty_list(fm, "linked_objectives"):
            errors.append(
                "theme requires non-empty `linked_objectives:` — a theme with no "
                "objective link is an 'Orphaned Theme' anti-pattern. Link to at "
                "least one OBJ-* from the roadmap."
            )
        timeframe = scalar(fm, "timeframe")
        if timeframe not in ALLOWED_TIMEFRAMES:
            errors.append(
                f"theme `timeframe:` must be one of {sorted(ALLOWED_TIMEFRAMES)}; "
                f"got '{timeframe}'. Specific calendar dates are prohibited — use "
                "Now/Next/Later only."
            )
        confidence_raw = scalar(fm, "confidence")
        if confidence_raw is not None:
            try:
                c = int(confidence_raw)
                if c == 100:
                    errors.append(
                        "theme `confidence:` must be 0–99, never 100. No roadmap "
                        "item ships at 100% certainty — the future is uncertain."
                    )
                elif not 0 <= c <= 99:
                    errors.append(
                        f"theme `confidence:` must be an integer 0–99; got {c}."
                    )
            except ValueError:
                errors.append(
                    f"theme `confidence:` must be an integer 0–99; got '{confidence_raw}'."
                )
        if not scalar(fm, "customer_need"):
            errors.append(
                "theme requires `customer_need:` — a theme must describe a customer "
                "problem, not a solution or feature."
            )

    return errors


def main() -> int:
    event = read_event()
    path_str = target_path(event)
    if not path_str:
        return 0
    path = Path(path_str)
    if not path.exists() or not path.is_file():
        return 0
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return 0

    errors = validate(text)
    if not errors:
        return 0

    bullet = "\n  - "
    sys.stderr.write(
        f"[prr] Validation failed for {path}:{bullet}{bullet.join(errors)}\n"
        "Fix the frontmatter to match the templates under "
        "skills/product-roadmaps/templates/ in the prr plugin.\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
