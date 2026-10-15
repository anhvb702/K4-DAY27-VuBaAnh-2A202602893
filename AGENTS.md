# Codex instructions (this repo)
You are a delegated child executor (AGENT_TEAM_CHILD=1): do NOT run `.agent-team/run.py` or spawn a team.
- Spec = `README.md`. Implement only the exercise named in the prompt: replace its `# TODO:` markers, keep the skeleton's structure/signatures, remove the TODO comments you complete.
- Reuse earlier exercises (ex2 builds on ex1, etc.) and `common/`, `audit/`; do not modify those.
- Python: 4 spaces, snake_case, minimal code, no extra deps beyond pyproject.
- Do not read/print `.env`. Do not call live LLM/GitHub APIs; verify with `uv run python tools/check.py <file>` only.
- Finish with a 5-line summary: what changed, check result, open risks.
