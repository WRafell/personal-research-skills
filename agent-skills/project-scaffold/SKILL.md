---
name: project-scaffold
description: Create the standard skeleton and Python environment (conda or uv, chosen by the user) of a new research project or repository (src package with main.py and the __main__ guard, configs, tests, scripts, docs with handoff, research notes, run index, pages, digests, .gitignore, pyproject with ruff, pyrefly, and pytest, AGENTS.md and CLAUDE.md) from the template in this skill. Use when the user starts a new project, a new repository, or a new codebase. A new experiment inside an existing project is a config, not a new skeleton (see experiment-management).
---

# Project scaffold

Every new project starts from the same skeleton, so that the other skills
(`experiment-management`, `handoff`, `research-notes`, `research-digest`,
`html-research-reports`, `proof-of-concept`, `coding-style`) find the paths
they expect.

Use this skill only for a new project or repository. In an existing project,
a new experiment is a config file and a run of an existing entry point
(`experiment-management`, "Keep the Workspace Tidy"); never add a second
skeleton inside a project.

## Layout

```text
<project>/
    AGENTS.md, CLAUDE.md      skills and project values (AGENTS.md, the standard file); CLAUDE.md points to it
    README.md                 question, setup, run commands
    .gitignore                Python caches, local/, poc/*/out/, large files
    pyproject.toml            installable package; dev extra and settings for ruff, pyrefly, pytest
    src/<package>/
        __init__.py
        main.py               entry point: main() and the __main__ guard
        runs.py               run ID and run record helpers
    configs/                  experiment configs (configs/<stage>/<name>.json)
    scripts/                  batch submission files (allocation lives only here)
    tests/
        test_entry_points.py  guard check and a smoke run of main
    docs/
        handoff.md            append-only session log
        experiment_runs.md    append-only run index
        research-notes/       dated notes
        pages/                HTML pages
        digests/              research digests
        results/, figures/    copies of the records and figures that reports cite
    local/                    run outputs and scratch (not in git; made by runs)
    poc/                      proofs of concept (made only when needed)
```

## Entry points

- Each executable module has a `main(argv: list[str] | None = None)` function
  and ends with:

  ```python
  if __name__ == "__main__":
      main()
  ```

  Importing a module never starts work. `tests/test_entry_points.py` fails
  when a module defines `main()` without the guard (ruff and pyrefly do not
  check this).
- Run entry points as modules: `python -m <package>.main --config ...`.
- Keep the core pure (`run(settings) -> results`) and the shell in `main()`
  (arguments, files, records), as `coding-style` requires.

## Procedure

1. Ask the user whether to use conda or uv for the environment, unless the
   user already said which. This choice has no default. Check first which
   tools the machine has (`command -v conda uv`) and include that in the
   question. If the chosen tool is not installed, tell the user; do not install
   it without approval.
2. Get the project name, the package name (a valid Python identifier), the
   one-sentence question, the conda env name if the choice is conda (default:
   the project name), the Python version (default: 3.11), the machines that
   need the env (default: the workstation), the clusters, and the time zone.
   Ask only for what the user did not give; use `TBD` for the rest.
3. Do not write into a folder that has files, except an empty git repository.
4. Copy the template and fill the placeholders. Set `ENV_SETUP` and
   `ENV_SUMMARY` for the chosen tool only:

   ```bash
   SKILL=~/.claude/skills/project-scaffold   # or ~/.codex/skills/project-scaffold
   DEST=<project folder>
   export PKG=<package> PROJECT=<project> QUESTION='<question>' CLUSTERS='<clusters>' TIMEZONE='<time zone>'

   # conda
   export ENV_SETUP=$'conda create -y -n <env name> python=<python version>\nconda activate <env name>\npip install -e ".[dev]"'
   export ENV_SUMMARY='conda env `<env name>` (Python <python version>), installed with `pip install -e ".[dev]"`; run tools with `conda run -n <env name> ...` or in the activated env.'

   # uv
   export ENV_SETUP=$'uv venv --python <python version> .venv\nsource .venv/bin/activate\nuv pip install -e ".[dev]"'
   export ENV_SUMMARY='uv venv `.venv` (Python <python version>), installed with `uv pip install -e ".[dev]"`; run tools with `.venv/bin/<tool>` or in the activated env.'

   cp -r "$SKILL/template/." "$DEST/"
   mv "$DEST/gitignore" "$DEST/.gitignore"
   mv "$DEST/src/__package__" "$DEST/src/$PKG"
   grep -rlE '__(package|project|question|envsetup|envsummary|clusters|timezone)__' "$DEST" \
     | xargs perl -pi -e 's/__package__/$ENV{PKG}/g; s/__project__/$ENV{PROJECT}/g;
         s/__question__/$ENV{QUESTION}/g; s/__envsetup__/$ENV{ENV_SETUP}/g;
         s/__envsummary__/$ENV{ENV_SUMMARY}/g; s/__clusters__/$ENV{CLUSTERS}/g;
         s/__timezone__/$ENV{TIMEZONE}/g'
   ```

5. Create the environment on each machine that needs it.

   With conda, check first that the name is free (`conda env list`); if it
   exists, ask before using or replacing it.

   ```bash
   conda create -y -n <env name> python=<python version>
   conda run -n <env name> pip install -e "$DEST[dev]"
   ```

   With uv, the environment is the project's `.venv` (not in git, one per
   checkout).

   ```bash
   uv venv --python <python version> "$DEST/.venv"
   uv pip install --python "$DEST/.venv/bin/python" -e "$DEST[dev]"
   ```

   On a cluster, create the env as the cluster instructions say (installs on
   the login node are usually permitted; running code there is not).
6. Check: no placeholder is left (`grep -rn '__[a-z]*__' "$DEST"` shows only
   the `__name__`/`__main__`/`__init__`/`__doc__`/`__pycache__`/`__file__`
   names), and in the new env (`conda run -n <env name> ...` or
   `.venv/bin/<tool>`, on the workstation or a compute node, not a login node)
   these pass: `ruff format --check .`, `ruff check .`, `pyrefly check`,
   `pytest`, and `python -m <package>.main --config configs/example.json`.
7. `git init` if the folder is not a repository. Do not commit or push unless
   the user asks.
8. Append the first handoff entry: what was created, the environment tool, the
   env name and machines, the check results, the project values, and the open
   `TBD` values.

## Adapt, do not grow

Add a folder only when the project needs it (for example `packages/` for a
second installable package, or `requirements/` for several environments).
Remove the example config once a real config exists. Do not add folders "for
later".
