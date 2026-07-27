"""
Updates the "Latest Repositories" section of README.md with the five
most recently pushed-to, non-fork public repositories for GH_USERNAME.

Runs inside the `update-readme.yml` workflow. Requires:
    GH_TOKEN     - a token with public read access (the default
                   GITHUB_TOKEN is sufficient)
    GH_USERNAME  - the GitHub username to inspect (defaults to sanan011)
"""

import os
import sys
from datetime import datetime, timezone

import requests

USERNAME = os.environ.get("GH_USERNAME", "sanan011")
TOKEN = os.environ.get("GH_TOKEN")
README_PATH = "README.md"
START_MARKER = "<!--START_SECTION:repos-->"
END_MARKER = "<!--END_SECTION:repos-->"
MAX_REPOS = 5

API_URL = f"https://api.github.com/users/{USERNAME}/repos"


def fetch_repos() -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    response = requests.get(
        API_URL,
        headers=headers,
        params={"per_page": 100, "sort": "pushed", "direction": "desc"},
        timeout=30,
    )
    response.raise_for_status()
    repos = response.json()

    return [
        repo
        for repo in repos
        if not repo.get("fork") and not repo.get("archived")
    ][:MAX_REPOS]


def format_table(repos: list[dict]) -> str:
    if not repos:
        return "_No public repositories found._"

    header = "| Repository | Language | Last Updated |\n|---|---|---|\n"
    rows = []
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        language = repo.get("language") or "—"
        pushed_at = repo.get("pushed_at")
        if pushed_at:
            date = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
            date_str = date.strftime("%b %d, %Y")
        else:
            date_str = "—"
        rows.append(f"| [{name}]({url}) | {language} | {date_str} |")

    return header + "\n".join(rows)


def update_readme(table: str) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        print("Markers not found in README.md — nothing to update.")
        sys.exit(0)

    new_content = (
        content[: start + len(START_MARKER)]
        + "\n"
        + table
        + "\n"
        + content[end:]
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main() -> None:
    repos = fetch_repos()
    table = format_table(repos)
    update_readme(table)
    print(f"Updated Latest Repositories section with {len(repos)} repositories.")


if __name__ == "__main__":
    main()
