"""Every module that defines main() runs it only under the __main__ guard."""

import ast
import json
from pathlib import Path

from __package__.main import main

SOURCE = Path(__file__).resolve().parents[1] / "src"


def has_main_guard(tree: ast.Module) -> bool:
    return any(
        isinstance(node, ast.If)
        and isinstance(node.test, ast.Compare)
        and isinstance(node.test.left, ast.Name)
        and node.test.left.id == "__name__"
        and any(isinstance(c, ast.Constant) and c.value == "__main__" for c in node.test.comparators)
        for node in tree.body
    )


def test_modules_with_main_have_guard() -> None:
    missing = []
    for path in SOURCE.rglob("*.py"):
        tree = ast.parse(path.read_text())
        defines_main = any(isinstance(node, ast.FunctionDef) and node.name == "main" for node in tree.body)
        if defines_main and not has_main_guard(tree):
            missing.append(str(path.relative_to(SOURCE)))
    assert not missing, f"main() without the __main__ guard: {missing}"


def test_main_writes_a_completed_record(tmp_path: Path) -> None:
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"seed": 0}))
    main(["--config", str(config), "--run-root", str(tmp_path / "runs")])
    (record_path,) = (tmp_path / "runs").glob("*/record.json")
    assert json.loads(record_path.read_text())["status"] == "completed"
