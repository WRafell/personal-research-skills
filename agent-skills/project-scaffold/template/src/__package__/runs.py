"""Run identifiers and run records."""

import json
import secrets
from datetime import datetime
from pathlib import Path


def new_run_id(now: datetime) -> str:
    """Return a run ID in the form YYMMDD-HHmmss-xxxx."""
    return f"{now:%y%m%d-%H%M%S}-{secrets.token_hex(2)}"


def start_record(run_dir: Path, run_id: str, settings: dict) -> Path:
    """Write the record with the resolved settings before the work starts."""
    run_dir.mkdir(parents=True, exist_ok=False)
    record_path = run_dir / "record.json"
    record = {"run_id": run_id, "status": "running", "settings": settings}
    record_path.write_text(json.dumps(record, indent=2))
    return record_path


def finish_record(record_path: Path, *, results: dict | None = None, error: str | None = None) -> None:
    """Add the results, or the error, to the record."""
    record = json.loads(record_path.read_text())
    record |= {"status": "failed", "error": error} if error else {"status": "completed", "results": results}
    record_path.write_text(json.dumps(record, indent=2))
