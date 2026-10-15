# Contributing

These are the organization-wide conventions for all repositories in
the crystal-system organization. Every contributor must follow them.

## Branch naming

Branches MUST match: `<type>/<issue-number>-<short-description>`

- type: `f` (Feature) | `b` (Bug) | `t` (Task) — matches the GitHub issue type
- issue-number: the GitHub issue number, e.g. `123` (not `#123`)
- short-description: lowercase kebab-case, ≤ 5 words

Examples: `f/123-add-login-form`, `b/456-crash-on-save`, `t/78-update-ci-runner`

The branch type MUST match the issue's type. If the task has no issue
yet, create one first and set its type before branching.

Branch names are enforced by CI on every pull request via the reusable
workflow in this repository (`.github/workflows/branch-name.yml`).

## Commit authorship

The user requesting the work is the author of all commits, including
commits made on their behalf by AI agents. Agents must not appear as
author, committer, or co-author in the git history. In particular, do
NOT use `Co-authored-by` trailers to credit an agent — GitHub turns
those into contributor attribution. If agent assistance should be
noted, mention it in prose in the commit message body (e.g. "Assisted
by an AI agent."), which carries no attribution.
