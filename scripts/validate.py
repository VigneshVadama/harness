#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "harness"


def fail(message: str) -> NoReturn:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    content = read(path)
    if not content.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
    parts = content.split("---\n", 2)
    if len(parts) != 3:
        fail(f"{path.relative_to(ROOT)} frontmatter must be closed")

    fields: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if line.startswith(" "):
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields, parts[2]


def validate_skill(path: Path) -> None:
    require_file(path / "SKILL.md")
    fields, body = parse_frontmatter(path / "SKILL.md")
    if fields.get("name") != path.name:
        fail(f"{path.relative_to(ROOT)} skill name must match folder name")
    if not fields.get("description"):
        fail(f"{path.relative_to(ROOT)} description must be non-empty")
    if not body.strip():
        fail(f"{path.relative_to(ROOT)} body must be non-empty")
    for rel in [
        "references/handoff-schema.md",
        "references/missions.md",
        "references/validator-rubric.md",
        "references/checklist.md",
        "references/checklist-examples.md",
        "references/communication.md",
        "references/delivery.md",
        "examples/code-change.md",
        "examples/document-knowledge-extraction.md",
    ]:
        require_file(path / rel)
    for text in ["MUST", "RFC 2119", "checklist", "communication"]:
        if text not in body:
            fail(f"{path.relative_to(ROOT)} SKILL.md must mention {text}")
    skill_bytes = len((path / "SKILL.md").read_bytes())
    if skill_bytes > 3200 or len(fields["description"]) > 400:
        fail(
            f"{path.relative_to(ROOT)} SKILL.md over budget: {skill_bytes} bytes (max 3200), description max 400 chars"
        )
    validate_checklist_examples(path)


def validate_checklist_examples(path: Path) -> None:
    checklist = read(path / "references" / "checklist.md")
    examples = read(path / "references" / "checklist-examples.md")
    needed = set(re.findall(r"- \[ \] `([^`]+)`.*see examples", checklist))
    present = set(re.findall(r"^## `([^`]+)`", examples, flags=re.MULTILINE))
    if needed != present:
        fail(
            f"checklist examples mismatch: missing {sorted(needed - present)}, orphaned {sorted(present - needed)}"
        )


def validate_docs() -> None:
    readme = read(ROOT / "README.md")
    for text in [
        "npx skills add VigneshVadama/harness",
        "python3 scripts/validate.py",
        "uvx ruff check",
        "uvx ruff format --check",
        "uvx ty check",
        "agentskills validate skills/harness",
    ]:
        if text not in readme:
            fail(f"README missing {text}")
    if "missions/" not in read(ROOT / ".gitignore"):
        fail(".gitignore must ignore missions/")


def main() -> int:
    validate_skill(SKILL)
    validate_docs()
    print("OK: harness validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
