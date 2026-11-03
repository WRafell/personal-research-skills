# Skills

The shared skills are installed at user level (`~/.claude/skills`, `~/.codex/skills`). Follow them with the project values below:
`coding-style`, `experiment-management`, `proof-of-concept`, `handoff`, `research-notes`, `research-digest`, `html-research-reports`, `scientific-writing`, `cluster-ssh-execution`, `agents-collab`.

# Project values for the skills

- Question: __question__
- Package: `src/__package__/`; entry points run as `python -m __package__.<module>`; each has `main()` and the `__main__` guard.
- Configs: `configs/<stage>/`; runs: `local/<stage>/<run_id>/record.json`; scratch: `local/scratch/`; proofs of concept: `poc/<YYMMDD>-<slug>/`.
- Handoff log: `docs/handoff.md` (time zone: __timezone__). Research notes: `docs/research-notes/`. Run index: `docs/experiment_runs.md`. HTML pages: `docs/pages/`. Digests: `docs/digests/<YYYYMMDD>-<slug>/`. Report copies: `docs/results/`, `docs/figures/`.
- Environment: __envsummary__ Clusters: __clusters__.
- Checks before code is done (in the env, not on a login node): `ruff format`, `ruff check`, `pyrefly check`, `pytest`.

# Reports

- Keep the reports current unless the user says otherwise; research notes and the handoff log are append-only.
