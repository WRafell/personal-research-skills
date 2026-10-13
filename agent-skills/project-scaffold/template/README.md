# __project__

__question__

## Setup

```bash
conda create -y -n __environment__ python=__python__
conda activate __environment__
pip install -e ".[dev]"
```

The package runs as `python -m __package__.main`. Checks before each change is done: `ruff format`, `ruff check`, `pyrefly check`, `pytest`.

## Run

```bash
python -m __package__.main --config configs/example.json
```

Each run writes `local/runs/<run_id>/record.json`.
