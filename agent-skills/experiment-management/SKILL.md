---
name: experiment-management
description: Structure, run, and record reproducible research experiments with stable identifiers, resolved settings, results, failures, metrics, timing, and an append-only experiment index. Use when creating or modifying experiment entry points, training runs, evaluations, ablations, baselines, notebook-to-script migrations, result schemas, or experiment logs.
---

# Experiment Management

Use the repository's established experiment paths and schemas when they exist.
Introduce the defaults below when the project has no equivalent convention.

## Create an Experiment Identity

- Generate one experiment ID at run start in `YYMMDD-HHmmss-xxxx` — timestamp plus a 4-hex-char random suffix (using the "secret" library).
- Use the same ID for settings, outputs, checkpoints, plots, logs, and summary
  entries produced by that run.
- Generate the ID in a shared utility rather than reimplementing its format in
  every entry point.
- Avoid overwriting an existing experiment. Detect collisions or include a
  deterministic suffix when runs can start within the same second.

## Persist Resolved Settings Before Work Begins

Write the experiment record before expensive work starts. Capture resolved
values rather than only user-provided overrides.

Include:

- all CLI arguments or configuration values;
- experiment ID;
- device and relevant environment information;
- dataset, split, and sampling configuration;
- model or backbone;
- method and method-specific hyperparameters;
- random seeds;
- paths to inputs, outputs, and trusted checkpoints where applicable.

Prefer:

```text
local/experimental_settings/{exp_id}.json
```

when the repository has not established another location.

Treat versioned configuration files as the source of experiment composition.
The entry point should load a config, resolve inheritance/defaults, apply only
explicit CLI overrides, validate the result, and persist that resolved result.
Campaign names and arm labels are orchestration metadata; they must not choose
trainer behavior. Each arm is a normal method plus explicit reusable settings.

Keep machine allocation out of experiment configs. Scheduler, node, partition,
QoS, GPU, CPU, memory, and wall-time choices belong only in batch-submission
shell files, so the same config can run locally or on another cluster.

## Complete the Same Record

On success, add a `results` object to the existing settings record. Include:

- per-step, per-epoch, or per-round history;
- final metrics;
- explicitly labeled best metrics when useful;
- total runtime and a meaningful normalized runtime such as time per epoch or
  round;
- paths to material artifacts.

On failure, add:

```json
{
  "error": {
    "type": "ExceptionClass",
    "message": "Human-readable message",
    "traceback": "Full traceback"
  }
}
```

Keep `results` and `error` mutually exclusive. Preserve the original settings
even when execution fails.

## Maintain an Append-Only Experiment Index

Append one concise Markdown bullet for every successful run. Never overwrite
earlier entries or rewrite the file as a generated table.

Include:

- experiment ID;
- method and task;
- dataset and model;
- important distribution or ablation settings;
- scale, such as client count, rounds, epochs, or sample count;
- result-record path;
- total and normalized runtime;
- primary final metrics.

Prefer:

```text
local/exp_log/experiments.md
```

when no experiment index exists.

Do not add failed runs to the successful-run index. Their structured error
records are the source of truth.

## Write Evidence-First Experiment Reports

When writing an experiment overview, analysis, or dated experiment log:

- List the exact repository-relative path to every authoritative raw structured
  record used, normally `local/experimental_settings/{exp_id}.json`. Also list
  any diagnostic or result artifact paths used to compute reported values. Do
  not cite only a derived summary when the underlying records are available.
- Base numerical claims on completed settings records and saved artifacts.
  Identify incomplete, failed, stale, or excluded runs and state the selection
  rule.
- Prioritize resolved setup, run status, provenance, per-seed or per-run values,
  prespecified aggregates, and reproducibility limitations. Keep interpretation
  to the minimum needed to explain what was measured, and separate it from raw
  observations and calculations.
- Guard against confirmation and narrative bias. Report mixed, null, adverse,
  and hypothesis-inconsistent results with the same specificity as favorable
  results. Label post-hoc analyses, development-selected thresholds, and
  mechanisms that were not directly measured.
- Do not present association as mechanism, a matched comparison as proof of
  causality, absence of an observed difference as equivalence, or a descriptive
  pattern as statistically established without the corresponding design or
  analysis. Avoid evaluative terms such as "wins," "real effect," "promising,"
  or "preferable" when the raw measurements and stated uncertainty are enough.
- Do not add paper-style motivation, persuasive narrative, recommendations, or
  future-work priorities unless the user explicitly requests them.

## Maintain Public Report Mirrors Safely

When a repository maintains public copies of experiment documentation:

- Keep runtime records and working reports in their established authoritative
  locations. Copy them to the public tree; do not move or delete the sources.
- Publish the completed structured records actually used by each report, not
  the entire experiment directory. In the report, identify both the
  authoritative record path and the public-copy path.
- Treat the public JSON as an exact evidence copy. Before publishing, check it
  for credentials, private filesystem paths, identifying infrastructure
  metadata, and tracebacks. Do not silently sanitize a record: either omit it
  pending review or document any transformation explicitly.
- Refresh public copies from their sources after each requested update. Do not
  edit the two versions independently or allow the public mirror to become a
  second source of truth.

## Define Metrics Precisely

- Give each metric one stable name throughout evaluation, history, final
  results, tables, and logs.
- Document averaging mode and inputs for ambiguous metrics.
- For multiclass classification, prefer macro-F1 and macro one-vs-rest ROC-AUC
  computed from class probabilities.
- Return `NaN` when a metric is mathematically undefined. Do not silently replace
  it with zero.
- Distinguish final metrics from best metrics in both names and prose.
- Use final metrics in the experiment index unless it explicitly labels a value
  as best.
- Add task-specific metrics, such as engram retrieval or similarity, alongside
  common predictive metrics rather than overloading their names.

## Preserve Reproducibility

- Record every seed and stochastic data-partition parameter.
- Record the actual resolved device and important numerical settings.
- Do not let observational analysis silently consume the RNG stream used by the
  experiment.
- Store enough provenance to rerun the experiment without reconstructing choices
  from notebook state or terminal history.
- Treat stored results as trusted only when their configuration and code context
  are known.

## Do Not Touch Files a Running Job Depends On

While a job, campaign, or scheduled run is in flight, treat everything it reads
as frozen. This covers the entry point, the source modules it imports, the
scripts it executes, its configuration, and any manifest or state file it
writes.

Two distinct failure modes, both silent until they are expensive:

- **Shell and batch scripts are read incrementally, not loaded once.** Editing a
  script that a running job is executing shifts byte offsets under a live
  interpreter, so it resumes mid-file at the wrong position and dies on a
  syntax error that does not exist in the finished file. The edit can look
  correct and still destroy the run.
- **Interpreted source is imported lazily.** A module edited mid-run may be
  imported afterwards in its new form, silently mixing two code states inside
  one result.

Rules:

- Before editing, inspect active local and scheduled jobs and identify the files
  and mutable state they depend on. Do not assume another terminal or agent has
  no live work.
- Wait for a run to finish before editing one of its dependencies. Do not cancel,
  restart, or resubmit it without user authorization. If an authorized fix
  cannot wait, cancel the run, record it as interrupted, edit, then resubmit it
  under a new traceable identity.
- Concurrent work is safe only outside the run's dependency and state paths, or
  in an isolated worktree or clone with no shared mutable inputs or outputs.
- Keep provenance guards scoped to what actually affects results, so unrelated
  edits do not abort valid work. A guard that hashes a version-control pointer
  rather than file content will kill a campaign for a documentation commit.
- Never place a guard's own definition inside what it guards; a launcher that
  fingerprints its own tree invalidates its own campaign when repaired.
- Prefer per-worker files over shared ones for anything concurrent jobs write,
  so no process depends on a file another process is mutating.
- After an interrupted run, verify what actually completed before assuming the
  work is lost. A job that fails in its epilogue may hold complete, valid
  results.

## Keep Notebooks and Scripts Honest

- Treat notebooks as exploratory interfaces, not implicit experiment records.
- Move reusable experiment logic into source modules before relying on a
  notebook result as a baseline.
- Save notebook-derived metrics and settings through the same experiment schema
  used by scripts.
- Label partial, interrupted, manually altered, or stale-output notebook runs as
  untrusted.

## Review Before Handoff

Confirm that:

1. Settings are written before expensive execution.
2. A run has exactly one ID and one authoritative record.
3. Success and failure states cannot coexist.
4. Metric definitions and names are consistent.
5. Runtime and artifact paths are recorded.
6. Only successful runs enter the append-only index.
7. The record contains enough information to reproduce the run.
8. No file a running job depends on was edited while it was in flight.
9. Every report identifies its raw JSON records and other source artifacts.
10. Reported observations are separated from minimal, explicitly qualified
    interpretation, with confirmation and narrative bias checked.
11. Any public report mirror includes reviewed copies of its cited completed
   records and remains synchronized with the authoritative sources.
12. Campaign composition is expressed in configuration files without
    campaign-specific branches in Python.
13. Experiment configs are portable; server allocation is confined to batch
    submission scripts.
