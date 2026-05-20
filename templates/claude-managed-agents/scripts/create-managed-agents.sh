#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="dry-run"

if [[ "${1:-}" == "--apply" ]]; then
  MODE="apply"
elif [[ "${1:-}" == "--dry-run" || "${1:-}" == "" ]]; then
  MODE="dry-run"
else
  echo "usage: $0 [--dry-run|--apply]" >&2
  exit 2
fi

require_env() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    echo "missing required environment variable: $name" >&2
    exit 1
  fi
}

if [[ "$MODE" == "dry-run" ]]; then
  HARNESS_SKILL_ID="${HARNESS_SKILL_ID:-\$HARNESS_SKILL_ID}"
  WORKER_AGENT_ID="${WORKER_AGENT_ID:-\$WORKER_AGENT_ID}"
  VALIDATOR_AGENT_ID="${VALIDATOR_AGENT_ID:-\$VALIDATOR_AGENT_ID}"
  export HARNESS_SKILL_ID WORKER_AGENT_ID VALIDATOR_AGENT_ID
else
  require_env HARNESS_SKILL_ID
fi

render() {
  local file="$1"
  envsubst < "$ROOT_DIR/$file"
}

run_create() {
  local file="$1"
  if [[ "$MODE" == "dry-run" ]]; then
    echo "### $file"
    render "$file"
    return
  fi
  render "$file" | ant beta:agents create
}

run_create worker.yaml
run_create validator.yaml

if [[ "$MODE" == "dry-run" ]]; then
  echo "### coordinator.yaml"
  echo "Set WORKER_AGENT_ID and VALIDATOR_AGENT_ID before applying coordinator.yaml"
  render coordinator.yaml
else
  require_env WORKER_AGENT_ID
  require_env VALIDATOR_AGENT_ID
  render coordinator.yaml | ant beta:agents create
fi
