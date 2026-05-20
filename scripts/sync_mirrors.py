#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "orchestrator-worker-validator"

SKILL_MIRRORS = [
    ROOT
    / "templates"
    / "claude-code"
    / ".claude"
    / "skills"
    / "orchestrator-worker-validator",
    ROOT
    / "templates"
    / "github-copilot"
    / ".github"
    / "skills"
    / "orchestrator-worker-validator",
]

AGENT_MIRRORS = [
    (
        ROOT / "agents" / "orchestrator.md",
        ROOT / "templates" / "claude-code" / ".claude" / "agents" / "orchestrator.md",
    ),
    (
        ROOT / "agents" / "worker.md",
        ROOT / "templates" / "claude-code" / ".claude" / "agents" / "worker.md",
    ),
    (
        ROOT / "agents" / "validator.md",
        ROOT / "templates" / "claude-code" / ".claude" / "agents" / "validator.md",
    ),
    (
        ROOT / "github-copilot" / "agents" / "orchestrator.agent.md",
        ROOT
        / "templates"
        / "github-copilot"
        / ".github"
        / "agents"
        / "orchestrator.agent.md",
    ),
    (
        ROOT / "github-copilot" / "agents" / "worker.agent.md",
        ROOT
        / "templates"
        / "github-copilot"
        / ".github"
        / "agents"
        / "worker.agent.md",
    ),
    (
        ROOT / "github-copilot" / "agents" / "validator.agent.md",
        ROOT
        / "templates"
        / "github-copilot"
        / ".github"
        / "agents"
        / "validator.agent.md",
    ),
]


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> int:
    for mirror in SKILL_MIRRORS:
        copy_tree(SKILL, mirror)

    for src, dst in AGENT_MIRRORS:
        copy_file(src, dst)

    print("synced mirrors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
