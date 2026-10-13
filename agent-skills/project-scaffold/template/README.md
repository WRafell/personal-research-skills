# __project__

__question__

## Setup

Environment: __environment__ (for example `conda create -n __project__ python=3.11`).
Then, in the project folder: `pip install -e .` (the package runs as `python -m __package__.main`).

## Run

```bash
python -m __package__.main --config configs/example.json
pytest
```

Each run writes `local/runs/<run_id>/record.json`.
