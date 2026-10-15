param(
    [Parameter(Mandatory)][ValidateRange(1,5)][int]$Exercise,
    [string]$Extra = ""
)
$root = Split-Path $PSScriptRoot -Parent
$target = @{1="exercises/exercise_1_confidence.py";2="exercises/exercise_2_hitl.py";3="exercises/exercise_3_escalation.py";4="exercises/exercise_4_audit.py";5="app.py"}[$Exercise]
$heading = if ($Exercise -eq 5) { "Exercise 5" } else { "Exercise $Exercise" }
$prompt = @"
Complete $target. Read the '$heading' section of README.md (and the 'Confidence routing' table) and implement every # TODO in that file.
Exercise 5 (app.py) must reuse the exercise 4 graph builder. Verify with: uv run python tools/check.py $target
$Extra
"@
$env:AGENT_TEAM_CHILD = "1"
# model/effort: defaults from ~/.codex/config.toml (low effort = cheap); override with -c if needed
$prompt | codex exec -C $root --sandbox workspace-write --skip-git-repo-check -
