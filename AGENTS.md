# AGENTS.md

AI agents MUST follow the organization's [contributing rules](CONTRIBUTING.md)
exactly as a human contributor would. Read them first.

The rules that apply to all contributors are defined in
[CONTRIBUTING.md](CONTRIBUTING.md) — currently branch naming, commit
messages (Conventional Commits with repository scopes), spec-driven
development, and commit authorship.

Additional guidance for agents:

- Before starting a task, check for an existing issue; if there is
  none, create one and set its type before branching.
- Derive the branch type from the issue type, not from your own
  judgement of the work.
- Reference the issue in the pull request with a closing keyword
  (e.g. `Closes #123`).
- Follow spec-driven development: before writing code, read the
  `SPEC.md` of every folder you touch and the specs it references. If
  your change alters what the code achieves, update the affected
  `SPEC.md` (or `<something>.SPEC.md`) FIRST, in the same pull
  request. Every folder you add that contains code files gets its
  `SPEC.md` in the same pull request, using the template in
  [templates/SPEC.md](templates/SPEC.md).
- Keep `README.md` and `AGENTS.md` user-facing: they document what
  the code does and how to use it, not how it is implemented.
  Implementation details belong in `SPEC.md`.
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
