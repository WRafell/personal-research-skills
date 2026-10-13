"""Run one experiment from a config file and write its run record."""

import argparse
import json
from datetime import datetime
from pathlib import Path

from __package__.runs import finish_record, new_run_id, start_record


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True, help="JSON config of the experiment")
    parser.add_argument("--run-root", type=Path, default=Path("local/runs"), help="folder for run folders")
    return parser.parse_args(argv)


def run(settings: dict) -> dict:
    """Return the results for the resolved settings. Replace with the experiment."""
    return {"metrics": {}, "settings_seen": sorted(settings)}


def main(argv: list[str] | None = None) -> None:
    arguments = parse_arguments(argv)
    settings = json.loads(arguments.config.read_text())
    run_id = new_run_id(datetime.now())
    record_path = start_record(arguments.run_root / run_id, run_id, settings)
    try:
        results = run(settings)
    except Exception as error:
        finish_record(record_path, error=repr(error))
        raise
    finish_record(record_path, results=results)
    print(f"{run_id}: completed")


if __name__ == "__main__":
    main()
