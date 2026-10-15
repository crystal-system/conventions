# AGENTS.md

AI agents MUST follow the organization's [contributing rules](CONTRIBUTING.md)
exactly as a human contributor would. Read them first.

The rules that apply to all contributors are defined in
[CONTRIBUTING.md](CONTRIBUTING.md) — currently branch naming, commit
messages (Conventional Commits with repository scopes), and commit
authorship.

Additional guidance for agents:

- Before starting a task, check for an existing issue; if there is
  none, create one and set its type before branching.
- Derive the branch type from the issue type, not from your own
  judgement of the work.
- Reference the issue in the pull request with a closing keyword
  (e.g. `Closes #123`).
- Write commit messages in Conventional Commits format:
  `<type>(<scope>): <description>`, with types feat | fix | docs | ci |
  chore | refactor | test | perf. The scope is optional; if used, it
  MUST be defined in the repository's `SCOPES.md`. If the task needs a
  new scope, add it to `SCOPES.md` first (structure defined in
  CONTRIBUTING.md).
- Commit as the requesting user. Never set the agent as author or
  committer, and never add a `Co-authored-by` trailer for the agent.
- When you make a commit on behalf of the user, end the commit
  message with a footer line in this format:

      Assisted by <Agent Name> - <model>

  State your actual agent name and the model you run on, truthfully.
  The footer is plain text, not a trailer, and must be the last line
  of the commit message.
