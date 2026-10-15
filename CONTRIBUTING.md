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
