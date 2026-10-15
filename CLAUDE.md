# HITL PR Review Agent — agent workflow (low cost, high yield)

Goal: finish every `# TODO:` in `exercises/exercise_{1..4}_*.py` and `app.py` exactly as `README.md` describes. README is the spec; don't edit `common/`, `audit/`.

## Roles (cheapest that works)
| Who | Does | Cost |
|---|---|---|
| Claude main (Sonnet) | plan, read README, review diff, talk to user | low |
| Codex (`tools/codex_task.ps1`) | writes code for ONE exercise per call | uses Codex quota, not Claude's |
| `tools/check.py` | deterministic gate: compile, lint, imports, thresholds, no TODO left | free |
| advisor (Opus) | only: final check before "done", or stuck after 2 failures | rare |

No evaluator/tester/brainstorm agents by default; the gate + one diff read by Claude replaces them.

## Loop (per exercise, in order 1→4, then app.py — each builds on the previous)
1. `uv run python tools/check.py <file>` → see remaining TODOs (free).
2. `pwsh tools/codex_task.ps1 -Exercise N` — Codex implements it (prompt is built from README section + file; self-contained).
3. `git diff -- <file>`; Claude reads the diff once. Run `tools/check.py`.
4. Live run needs `.env` keys (OPENROUTER_API_KEY, GITHUB_TOKEN): run the README command only with the user's OK (it calls LLM and, on commit, posts a real GitHub comment — external side effect, confirm first).
5. Fail twice on the same error → advisor with a brief. Otherwise fix inline.
6. Commit only when the user asks.

## Cost rules
- Never paste whole files into prompts; Codex reads the repo itself.
- One exercise per Codex call; don't parallelize (each depends on the previous).
- Don't re-run live LLM demos to "check" — use `tools/check.py` and a mocked/imports-only test first.
- Never print `.env`.
