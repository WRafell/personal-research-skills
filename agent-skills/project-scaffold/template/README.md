# __project__

__question__

## Setup

```bash
__envsetup__
```

The package runs as `python -m __package__.main`. Checks before each change is done: `ruff format`, `ruff check`, `pyrefly check`, `pytest`.

## Run

```bash
python -m __package__.main --config configs/example.json
```

Each run writes `local/runs/<run_id>/record.json`.
