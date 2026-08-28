#!/usr/bin/env python3
"""Validate ENDGAME's required repository structure and metadata."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "VERSION",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "templates/acceptance-gates.md",
    "examples/usage.md",
)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty: {relative}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not re.match(r"^---\n.*?^name: endgame\n.*?^description: .+\n---\n", skill, re.M | re.S):
        errors.append("SKILL.md frontmatter is missing or invalid")

    metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$endgame" not in metadata:
        errors.append("agents/openai.yaml default_prompt must invoke $endgame")
    if "allow_implicit_invocation: false" not in metadata:
        errors.append("ENDGAME must remain explicit-only")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "GPL-3.0-or-later" not in readme:
        errors.append("README.md must declare GPL-3.0-or-later")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("ENDGAME skill repository is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

