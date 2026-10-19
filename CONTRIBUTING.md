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

## Commit messages

This organization uses [Conventional Commits](https://www.conventionalcommits.org/).
Every commit message MUST start with a type and optional scope:

    <type>(<scope>): <description>

Types: `feat` | `fix` | `docs` | `ci` | `chore` | `refactor` | `test` | `perf`

### Scope

The scope is optional. If a scope is used, it MUST be one of the scopes
defined in the repository's root file `SCOPES.md`. Using an undefined
scope is not allowed — define it in `SCOPES.md` first, in the same or
an earlier commit.

`SCOPES.md` structure:

    # Scopes

    <general description of what a scope of this repository can be —
    the dimensions or areas of the codebase that commits may target>

    ## <scope>

    <short description of what this scope covers>

## Commit authorship

The user requesting the work is the author of all commits, including
commits made on their behalf by AI agents. Agents must not appear as
author, committer, or co-author in the git history. In particular, do
NOT use `Co-authored-by` trailers to credit an agent — GitHub turns
those into contributor attribution.

When a commit was made on behalf of the user by an AI agent, the
commit message MUST end with a footer line in this format:

    Assisted by <Agent Name> - <model>

For example:

    Assisted by Mistral Vibe - mistral large

The footer is plain text, not a git trailer, so it creates no
contributor attribution. The agent name and model must be stated
truthfully.

## Skills

Skills are reusable procedures for AI agents, stored in this
repository as `skills/<name>/SKILL.md` and usable in every repository
of the organization. They are organization-agnostic and can be used in
any repository.

To add a new skill:

1. Create the directory `skills/<name>/SKILL.md`.
2. Prefix the skill name with `cs-` — in both the directory name and
   the `name` field of the frontmatter — so skills from this
   organization cannot conflict with skills from other sources.
3. Keep the skill generic: it must not mention this organization or
   assume its repositories.
4. Write the skill in simple technical English, as a procedure the
   agent runs step by step.

## Installing the skills

Install the skills of this repository for your agents with one command:

    npx skills add crystal-system/conventions -g -y

The `-g` flag installs them at the user level, for every project, so
nothing is added to or committed in the repositories you work on. The
CLI detects the agents installed on your machine and installs the
skills into each of them. Run `npx skills update` after changes to the
skills to refresh your installation.
