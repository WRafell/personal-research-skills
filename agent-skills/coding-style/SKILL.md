---
name: coding-style
description: Apply the repository owner's preferred coding conventions when implementing, refactoring, or reviewing code. Use for changes involving project structure, orchestration, dispatch, factories, imports, dependencies, or placement of implementation logic.
---

# Coding Style

Follow existing repository conventions first when they are more specific. Apply
the preferences below to new code and touched code; do not churn unrelated code
solely to make it conform.

## Verify Dependencies

- Before importing a new third-party package, verify that it is available in the
  active environment or declared in the project's dependency manifest.
- If the package is genuinely required, add it to the appropriate dependency
  manifest in the same change.
- Fail clearly when a required dependency is missing. Do not add a silent
  `try`/`except` fallback that skips or degrades requested behavior.

## Separate Orchestration from Implementation

- Keep entry points and scripts focused on orchestration: parse configuration,
  select components, call implementation code, and handle top-level I/O.
- Put reusable logic, training or processing loops, metric accumulation, and
  domain behavior in importable source modules.
- Do not define helper functions inside an entry-point function.
- Do not add method-specific `run_<name>` wrappers merely to hide straightforward
  dispatch.
- Use classes for stateful models, trainers, or components whose behavior and
  state belong together. Use functions for high-level orchestration.
- Keep files outside the main source package orchestration-only unless the user
  or established repository structure requires otherwise.

## Keep Research Code Configuration-Driven

- Python method implementations expose reusable algorithmic arguments. Name
  arguments for the behavior they control, not for a paper, campaign, dataset,
  machine, or one experiment arm.
- Keep independently meaningful controls independently configurable. Do not
  introduce a campaign switch whose value silently changes several trainer
  behaviors at once.
- Let the main entry point accept a configuration file and optional explicit
  CLI overrides. Persist the fully resolved configuration, including inherited
  values, before training starts.
- Put experiment- and campaign-specific values in configuration files and
  launch scripts. A new campaign should normally add or compose configuration,
  not add a campaign branch to Python.
- A provenance label may be recorded by orchestration, but it must not be
  passed into a trainer or used to select algorithm behavior.

## Separate Infrastructure from Research Code

- Keep Python modules, method implementations, and experiment configuration
  independent of a particular cluster or server.
- Put scheduler directives and machine-specific choices such as host names,
  partitions, QoS, node lists, GPU requests, CPU counts, memory, and wall time
  only in batch-submission shell files.
- Plain training and analysis scripts must remain runnable outside Slurm. Do
  not inspect Slurm environment variables or hard-code cluster paths in Python.

## Dispatch by Name

- Select configurable datasets, models, backbones, strategies, and similar
  components through a name-based dispatcher rather than hardcoding a concrete
  implementation in the entry point.
- Use explicit `if`/`elif` branches when the set of choices is small and
  repository conventions favor them.
- Raise a clear `ValueError` or `NotImplementedError` for unsupported names.
- Place imports lazily inside dispatch branches when implementations are
  optional, expensive, or method-specific.

## Construct Shared Components with Factories

- Centralize construction of shared configurable components in factory
  functions, preferably in an appropriate utility or source module.
- Pass configuration into the owning component and let it construct its own
  internals when that preserves encapsulation.
- Avoid constructing low-level models or datasets directly in the top-level
  entry point when a project dispatcher or factory exists.

## Format Python Consistently

- Prefer submodule imports such as `from torch import nn` over aliases such as
  `import torch.nn as nn`.
- In orchestration scripts, use uppercase string blocks as visual section
  dividers when sections improve readability:

```python
""" PARSE ARGS """

""" LOAD DATA """

""" TRAINING """
```

- Keep dispatch visible in the entry point when it expresses the program's
  high-level control flow.

## Preserve Supporting Documentation

- When behavior, configuration wiring, component contracts, or randomness
  changes, locate and update any repository documentation that maps those
  concerns.
- Edit the relevant section in place rather than appending a changelog entry,
  unless the repository explicitly uses an append-only log.

## Protect Active Runs

- Before editing code, configuration, launchers, or scripts, check whether a
  local or scheduled job is using the affected working tree. Do not infer that
  no job is active merely because it was started from another terminal or agent.
- Treat every file an active job may read, import, execute, or update as frozen.
  An apparently safe edit can mix code versions through lazy imports or corrupt
  a shell script that is being read incrementally.
- Continue work during a run only when the change is demonstrably outside its
  dependency and state paths, or in an isolated worktree or clone that shares no
  mutable inputs or outputs with the running job.
- Do not cancel, restart, or resubmit a user's job without authorization. When an
  authorized fix requires interruption, record the run as interrupted, inspect
  its artifacts, make the change, and launch a new traceable run rather than
  treating mixed-state output as valid.

## Review Before Handoff

Confirm that:

1. Every new third-party import is installed or declared.
2. Entry points contain orchestration rather than implementation loops.
3. Configurable components use dispatchers or factories instead of hardcoding.
4. Unsupported configuration values fail clearly.
5. Relevant architecture or state documentation remains synchronized.
6. Active jobs and their dependency paths were checked before editing.
7. Method arguments describe independent reusable behavior, while campaign
   values live in configuration and launch files.
8. Server and scheduler details appear only in batch-submission shell files.
