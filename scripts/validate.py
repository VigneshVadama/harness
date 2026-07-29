#!/usr/bin/env python3
from __future__ import annotations

import json
import stat
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

import tomllib

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "orchestrator-worker-validator"


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
        "references/platform-packaging.md",
        "examples/code-change.md",
        "examples/document-knowledge-extraction.md",
    ]:
        require_file(path / rel)
    for text in ["MUST", "RFC 2119", "checklist", "communication"]:
        if text not in body:
            fail(f"{path.relative_to(ROOT)} SKILL.md must mention {text}")


def compare_dirs(left: Path, right: Path) -> None:
    result = subprocess.run(
        ["diff", "-qr", str(left), str(right)],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        fail(f"mirror drift between {left.relative_to(ROOT)} and {right.relative_to(ROOT)}")


def validate_json(path: Path) -> dict[str, object]:
    require_file(path)
    try:
        data = json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must be a JSON object")
    return data


def validate_plugins() -> None:
    codex = validate_json(ROOT / ".codex-plugin" / "plugin.json")
    if codex.get("name") != "harness" or codex.get("skills") != "./skills/":
        fail(".codex-plugin/plugin.json must expose ./skills/")

    claude = validate_json(ROOT / ".claude-plugin" / "plugin.json")
    if claude.get("name") != "harness":
        fail(".claude-plugin/plugin.json name mismatch")
    claude_skills = claude.get("skills")
    if not isinstance(claude_skills, list) or "./skills/orchestrator-worker-validator/" not in claude_skills:
        fail(".claude-plugin/plugin.json must expose the harness skill")
    claude_agents = claude.get("agents")
    if not isinstance(claude_agents, list):
        fail(".claude-plugin/plugin.json agents must be a list")
    for agent in [
        "./agents/orchestrator.md",
        "./agents/worker.md",
        "./agents/validator.md",
    ]:
        if agent not in claude_agents:
            fail(f".claude-plugin/plugin.json missing {agent}")

    copilot = validate_json(ROOT / "github-copilot" / "plugin" / "plugin.json")
    for key in ["agents", "skills"]:
        if key not in copilot:
            fail("github-copilot/plugin/plugin.json missing agents or skills")


def validate_claude_agents() -> None:
    expected = {
        "orchestrator.md": ("orchestrator", "inherit", "blue", "Task"),
        "worker.md": ("worker", "sonnet", "green", "Edit"),
        "validator.md": ("validator", "opus", "yellow", "Bash"),
    }
    for filename, (name, model, color, tool_hint) in expected.items():
        fields, body = parse_frontmatter(ROOT / "agents" / filename)
        if fields.get("name") != name:
            fail(f"agents/{filename} name mismatch")
        if fields.get("model") != model or fields.get("color") != color:
            fail(f"agents/{filename} model/color mismatch")
        if tool_hint not in fields.get("tools", ""):
            fail(f"agents/{filename} missing expected tool hint")
        if "orchestrator-worker-validator" not in body:
            fail(f"agents/{filename} must mention the skill")


def validate_github_agents() -> None:
    expected_tools = {
        "orchestrator.agent.md": "agent",
        "worker.agent.md": "edit",
        "validator.agent.md": "execute",
    }
    for filename, tool_hint in expected_tools.items():
        fields, body = parse_frontmatter(ROOT / "github-copilot" / "agents" / filename)
        if fields.get("target") != "github-copilot":
            fail(f"github-copilot/agents/{filename} must target github-copilot")
        if fields.get("model") != "GPT-5.4":
            fail(f"github-copilot/agents/{filename} must use GPT-5.4")
        if tool_hint not in fields.get("tools", ""):
            fail(f"github-copilot/agents/{filename} missing expected tool")
        if filename == "validator.agent.md" and "edit" in fields.get("tools", "").lower():
            fail("GitHub validator must not have edit tools")
        if "handoffs" in fields:
            fail("GitHub Copilot cloud agents must not use unsupported handoffs frontmatter")
        if "orchestrator-worker-validator" not in body:
            fail(f"github-copilot/agents/{filename} must mention the skill")


def validate_codex_templates() -> None:
    config = read(ROOT / "templates" / "codex" / ".codex" / "config.toml")
    if "max_depth = 1" not in config:
        fail("templates/codex/.codex/config.toml must cap max_depth at 1")

    for name in ["orchestrator", "worker", "validator"]:
        path = ROOT / "templates" / "codex" / ".codex" / "agents" / f"{name}.toml"
        data = tomllib.loads(read(path))
        if data.get("name") != name:
            fail(f"{path.relative_to(ROOT)} name mismatch")
        skill_configs = data.get("skills", {}).get("config", [])
        expected_skill_path = "./skills/orchestrator-worker-validator/SKILL.md"
        if not any(
            isinstance(item, dict)
            and item.get("enabled") is True
            and item.get("path") == expected_skill_path
            for item in skill_configs
        ):
            fail(f"{path.relative_to(ROOT)} must enable {expected_skill_path}")
    validator = tomllib.loads(read(ROOT / "templates" / "codex" / ".codex" / "agents" / "validator.toml"))
    if validator.get("sandbox_mode") != "read-only":
        fail("Codex validator template must be read-only")


def validate_managed_agent_templates() -> None:
    worker = read(ROOT / "templates" / "claude-managed-agents" / "worker.yaml")
    validator = read(ROOT / "templates" / "claude-managed-agents" / "validator.yaml")
    coordinator = read(ROOT / "templates" / "claude-managed-agents" / "coordinator.yaml")
    for name, content in {"worker": worker, "validator": validator, "coordinator": coordinator}.items():
        for text in ["skills:", "type: custom", "skill_id: $HARNESS_SKILL_ID", "version: latest"]:
            if text not in content:
                fail(f"{name}.yaml missing {text}")
    for text in ["agent_toolset_20260401", "multiagent:", "type: coordinator", "$WORKER_AGENT_ID", "$VALIDATOR_AGENT_ID"]:
        if text not in coordinator:
            fail(f"coordinator.yaml missing {text}")

    script = ROOT / "templates" / "claude-managed-agents" / "scripts" / "create-managed-agents.sh"
    require_file(script)
    mode = script.stat().st_mode
    if not mode & stat.S_IXUSR:
        fail("create-managed-agents.sh must be executable")
    content = read(script)
    if "--dry-run" not in content or "--apply" not in content:
        fail("create-managed-agents.sh must support dry-run and apply")
    result = subprocess.run(
        [str(script), "--dry-run"],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        fail("create-managed-agents.sh --dry-run must not require environment variables")
    for text in ["$HARNESS_SKILL_ID", "$WORKER_AGENT_ID", "$VALIDATOR_AGENT_ID"]:
        if text not in result.stdout:
            fail(f"create-managed-agents.sh --dry-run must preserve {text}")


def validate_mirrors() -> None:
    skill_mirrors = [
        ROOT / "templates" / "claude-code" / ".claude" / "skills" / SKILL.name,
        ROOT / "templates" / "github-copilot" / ".github" / "skills" / SKILL.name,
    ]
    for mirror in skill_mirrors:
        compare_dirs(SKILL, mirror)

    agent_pairs = [
        (ROOT / "agents" / "orchestrator.md", ROOT / "templates" / "claude-code" / ".claude" / "agents" / "orchestrator.md"),
        (ROOT / "agents" / "worker.md", ROOT / "templates" / "claude-code" / ".claude" / "agents" / "worker.md"),
        (ROOT / "agents" / "validator.md", ROOT / "templates" / "claude-code" / ".claude" / "agents" / "validator.md"),
        (
            ROOT / "github-copilot" / "agents" / "orchestrator.agent.md",
            ROOT / "templates" / "github-copilot" / ".github" / "agents" / "orchestrator.agent.md",
        ),
        (
            ROOT / "github-copilot" / "agents" / "worker.agent.md",
            ROOT / "templates" / "github-copilot" / ".github" / "agents" / "worker.agent.md",
        ),
        (
            ROOT / "github-copilot" / "agents" / "validator.agent.md",
            ROOT / "templates" / "github-copilot" / ".github" / "agents" / "validator.agent.md",
        ),
    ]
    for left, right in agent_pairs:
        if read(left) != read(right):
            fail(f"mirror drift between {left.relative_to(ROOT)} and {right.relative_to(ROOT)}")


def validate_docs() -> None:
    readme = read(ROOT / "README.md")
    for text in [
        "npx skills add VigneshVadama/harness",
        "claude --plugin-dir .",
        ".codex-plugin/plugin.json",
        "uvx ruff check .",
        "uvx pyright .",
        "templates/github-copilot/.github/",
        "templates/claude-managed-agents/scripts/create-managed-agents.sh --dry-run",
    ]:
        if text not in readme:
            fail(f"README missing {text}")
    if "missions/" not in read(ROOT / ".gitignore"):
        fail(".gitignore must ignore missions/")


def main() -> int:
    validate_skill(SKILL)
    validate_plugins()
    validate_claude_agents()
    validate_github_agents()
    validate_codex_templates()
    validate_managed_agent_templates()
    validate_mirrors()
    validate_docs()
    print("OK: harness validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
