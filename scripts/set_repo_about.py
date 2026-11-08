#!/usr/bin/env python3
"""Apply the repository "About" metadata from repo-about.json.

GitHub does not store the About section in a file in the repository; it is
repository metadata. This script keeps the desired values under version control
and applies them with the GitHub CLI.

Usage:
    python scripts/set_repo_about.py
    python scripts/set_repo_about.py --dry-run
    python scripts/set_repo_about.py --repo owner/name

Requires:
    - gh CLI installed and authenticated (`gh auth login`)
    - write access to the repository
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "repo-about.json"

TOPIC_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_config() -> dict:
    if not CONFIG.is_file():
        fail(f"missing {CONFIG.relative_to(ROOT)}")
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {CONFIG.relative_to(ROOT)}: {exc}")

    description = data.get("description", "")
    homepage = data.get("homepage", "")
    topics = data.get("topics", [])

    if not isinstance(description, str) or not description.strip():
        fail("description must be a non-empty string")
    if len(description) > 350:
        fail(f"description is {len(description)} chars; GitHub allows up to 350")
    if not isinstance(homepage, str):
        fail("homepage must be a string")
    if homepage and not homepage.startswith(("http://", "https://")):
        fail("homepage must be empty or start with http:// or https://")
    if not isinstance(topics, list) or not all(isinstance(t, str) for t in topics):
        fail("topics must be a list of strings")
    if len(topics) > 20:
        fail(f"{len(topics)} topics; GitHub allows up to 20")
    for topic in topics:
        if len(topic) > 50:
            fail(f"topic too long: {topic!r}")
        if not TOPIC_RE.match(topic):
            fail(f"invalid topic {topic!r}; use lowercase letters, numbers and hyphens")

    return {"description": description, "homepage": homepage, "topics": topics}


def infer_repo() -> str:
    try:
        result = subprocess.run(
            ["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        fail("gh CLI not found; install it from https://cli.github.com/")
    except subprocess.CalledProcessError as exc:
        fail(f"could not infer repository: {exc.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply repo About metadata from repo-about.json")
    parser.add_argument("--repo", help="target repository as owner/name (default: infer from git remote)")
    parser.add_argument("--dry-run", action="store_true", help="validate and print the payload without applying it")
    args = parser.parse_args()

    config = load_config()
    repo = args.repo or infer_repo()

    payload = {
        "description": config["description"],
        "homepage": config["homepage"],
        "topics": config["topics"],
    }

    print(f"repository: {repo}")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    if args.dry_run:
        print("dry-run: not applying")
        return 0

    try:
        subprocess.run(
            ["gh", "api", "--method", "PATCH", f"repos/{repo}", "--input", "-"],
            cwd=ROOT,
            input=json.dumps(payload),
            text=True,
            check=True,
            capture_output=True,
        )
        if payload["topics"]:
            subprocess.run(
                ["gh", "api", "--method", "PUT", f"repos/{repo}/topics", "--input", "-"],
                cwd=ROOT,
                input=json.dumps({"names": payload["topics"]}),
                text=True,
                check=True,
                capture_output=True,
            )
    except FileNotFoundError:
        fail("gh CLI not found; install it from https://cli.github.com/")
    except subprocess.CalledProcessError as exc:
        fail(f"gh api failed: {exc.stderr.strip()}")

    print(f"About updated for {repo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
