"""Free deterministic gate: python tools/check.py [files...] (default: all exercise files + app.py)."""
import py_compile
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = sorted((ROOT / "exercises").glob("exercise_*.py")) + [ROOT / "app.py"]


def main() -> int:
    files = [ROOT / a for a in sys.argv[1:]] or FILES
    bad = 0
    for f in files:
        try:
            py_compile.compile(str(f), doraise=True)
        except py_compile.PyCompileError as e:
            print(f"FAIL compile {f.name}: {e}")
            bad += 1
            continue
        todos = [i for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1) if re.search(r"#\s*TODO", l)]
        print(f"{'TODO' if todos else 'ok  '} {f.name}" + (f" ({len(todos)} left: lines {todos[:8]})" if todos else ""))
        bad += bool(todos)
    ruff = subprocess.run([sys.executable, "-m", "ruff", "check", "--select", "F,E9", *map(str, files)], capture_output=True, text=True)
    if ruff.returncode and "No module named" not in ruff.stderr:
        print(ruff.stdout)
        bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
