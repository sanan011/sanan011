"""
Updates two sections of README.md for GH_USERNAME:

  1. "Recent Activity"      — a plain-language list built from the user's
                               real public events (pushes, PRs, issues,
                               releases, new repos), pulled directly from
                               the GitHub Events API.
  2. "Latest Repositories"  — the five most recently pushed-to, non-fork
                               public repositories.

Runs inside the `update-readme.yml` workflow. Requires:
    GH_TOKEN     - a token with public read access (the default
                   GITHUB_TOKEN is sufficient)
    GH_USERNAME  - the GitHub username to inspect (defaults to sanan011)
"""

import os
from datetime import datetime, timezone

import requests

USERNAME = os.environ.get("GH_USERNAME", "sanan011")
TOKEN = os.environ.get("GH_TOKEN")
README_PATH = "README.md"

REPOS_START = "<!--START_SECTION:repos-->"
REPOS_END = "<!--END_SECTION:repos-->"
ACTIVITY_START = "<!--START_SECTION:activity-->"
ACTIVITY_END = "<!--END_SECTION:activity-->"

MAX_REPOS = 5
MAX_ACTIVITY = 5

REPOS_API_URL = f"https://api.github.com/users/{USERNAME}/repos"
EVENTS_API_URL = f"https://api.github.com/users/{USERNAME}/events/public"


def _headers() -> dict:
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return headers


def _format_date(iso_string: str) -> str:
    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )
    return date.strftime("%b %d, %Y")


# --------------------------------------------------------------------------
# Latest Repositories
# --------------------------------------------------------------------------


def fetch_repos() -> list[dict]:
    response = requests.get(
        REPOS_API_URL,
        headers=_headers(),
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


def format_repos_table(repos: list[dict]) -> str:
    if not repos:
        return "_No public repositories found._"

    header = "| Repository | Language | Last Updated |\n|---|---|---|\n"
    rows = []
    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        language = repo.get("language") or "—"
        pushed_at = repo.get("pushed_at")
        date_str = _format_date(pushed_at) if pushed_at else "—"
        rows.append(f"| [{name}]({url}) | {language} | {date_str} |")

    return header + "\n".join(rows)


# --------------------------------------------------------------------------
# Recent Activity
# --------------------------------------------------------------------------


def fetch_events() -> list[dict]:
    response = requests.get(
        EVENTS_API_URL,
        headers=_headers(),
        params={"per_page": 30},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def _describe_event(event: dict):
    """Return a single markdown bullet for a supported event, or None
    for event types that aren't shown (stars, forks, watches, etc.)."""

    repo_name = event["repo"]["name"]
    repo_url = f"https://github.com/{repo_name}"
    short_name = repo_name.split("/")[-1]
    date_str = _format_date(event["created_at"])
    payload = event.get("payload", {})
    event_type = event["type"]

    if event_type == "PushEvent":
        commits = payload.get("commits", [])
        if not commits:
            return None
        message = commits[-1]["message"].splitlines()[0].strip()
        count = payload.get("size", len(commits))
        commit_word = "commit" if count == 1 else "commits"
        return (
            f"- Pushed {count} {commit_word} to "
            f"[`{short_name}`]({repo_url}) — \"{message}\" · {date_str}"
        )

    if event_type == "CreateEvent" and payload.get("ref_type") == "repository":
        return f"- Created repository [`{short_name}`]({repo_url}) · {date_str}"

    if event_type == "PullRequestEvent":
        action = payload.get("action")
        if action not in ("opened", "closed"):
            return None
        pr = payload.get("pull_request", {})
        title = pr.get("title", "").strip()
        verb = "Merged" if pr.get("merged") else action.capitalize()
        return f"- {verb} pull request in [`{short_name}`]({repo_url}) — \"{title}\" · {date_str}"

    if event_type == "IssuesEvent":
        action = payload.get("action")
        if action not in ("opened", "closed"):
            return None
        issue = payload.get("issue", {})
        title = issue.get("title", "").strip()
        return f"- {action.capitalize()} issue in [`{short_name}`]({repo_url}) — \"{title}\" · {date_str}"

    if event_type == "ReleaseEvent":
        release = payload.get("release", {})
        tag = release.get("tag_name", "")
        return f"- Published release `{tag}` for [`{short_name}`]({repo_url}) · {date_str}"

    return None


def format_activity_list(events: list[dict]) -> str:
    lines: list[str] = []
    for event in events:
        line = _describe_event(event)
        if line:
            lines.append(line)
        if len(lines) >= MAX_ACTIVITY:
            break

    if not lines:
        return "_No recent public activity found._"

    return "\n".join(lines)


# --------------------------------------------------------------------------
# README patching
# --------------------------------------------------------------------------


def replace_section(content: str, start_marker: str, end_marker: str, body: str) -> str:
    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1:
        print(f"Markers {start_marker} / {end_marker} not found — skipping.")
        return content

    return (
        content[: start + len(start_marker)]
        + "\n"
        + body
        + "\n"
        + content[end:]
    )


def main() -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    repos = fetch_repos()
    content = replace_section(content, REPOS_START, REPOS_END, format_repos_table(repos))
    print(f"Updated Latest Repositories with {len(repos)} repositories.")

    events = fetch_events()
    content = replace_section(content, ACTIVITY_START, ACTIVITY_END, format_activity_list(events))
    print("Updated Recent Activity section.")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()
