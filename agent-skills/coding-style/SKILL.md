---
name: coding-style
description: Apply the repository owner's preferred coding conventions when implementing, refactoring, or reviewing code. Functional core, imperative shell is the preferred design. Use for changes involving project structure, orchestration, dispatch, factories, imports, dependencies, typing, state, or placement of implementation logic.
---

# Coding Style

Follow existing repository conventions first when they are more specific. Apply
the preferences below to new code and touched code; do not churn unrelated code
solely to make it conform.

Central principle: use functions to express scientific logic and objects to
manage the systems that execute it. Favor explicit state, composable
transformations, and independently testable behavior over unnecessary
abstraction.

Keywords: MUST = mandatory. SHOULD = preferred; a different design needs a
reason. MAY = permitted exception when the condition is true.

## Functional Core, Imperative Shell

- Code SHOULD use pure functions and explicit data transformations, not
  stateful objects, and function composition, not class inheritance.
- Functional core: algorithms, mathematical operations, aggregation rules,
  synchronization policies, evaluation metrics, and data transformations. These
  functions SHOULD be pure and MUST be testable without files, network, GPU, or
  global state.
- Imperative shell: entry points, experiment orchestration, training loops,
  file I/O, distributed communication, GPU management, checkpointing, and
  logging. The shell calls the core and owns all side effects. It SHOULD
  contain no scientific logic.
- A rigid directory structure is not necessary. A module MAY contain both
  layers when the boundary is clear (pure functions first, `main()` last).
- Do not force functional style when it makes simple code more complex. Follow
  the framework convention when it gives a more natural design (for example
  `torch.nn.Module`, `torch.utils.data.Dataset`, Lightning callbacks).

## Separate Orchestration from Implementation

- Keep entry points and scripts focused on orchestration: parse configuration,
  select components, call implementation code, and handle top-level I/O.
- Put reusable logic, training or processing loops, metric accumulation, and
  domain behavior in importable source modules.
- Do not define helper functions inside an entry-point function.
- Do not add method-specific `run_<name>` wrappers merely to hide
  straightforward dispatch.
- Keep files outside the main source package orchestration-only unless the user
  or established repository structure requires otherwise.

## Functions and State

- Each function has one clear responsibility and explicit inputs and outputs.
  Keep functions short (ideally < 30-40 lines). Return early; avoid deep nesting.
- All inputs of a core function MUST come through parameters: no hidden reads
  of globals, environment variables, or files.
- Functions MUST NOT modify input arguments unless the mutation is the
  documented purpose of the function. Return new values instead.
- Make randomness explicit: pass a seed, a `numpy.random.Generator`, or a
  `torch.Generator`. Core functions do not use the global RNG.
- State transitions SHOULD be explicit (`next_state = update_state(state=state,
  batch=batch)`). Each mutable state MUST have one clear owner. No hidden global
  state.
- Configurations and experiment records SHOULD be immutable (frozen dataclass,
  tuple, frozenset).
- Performance-sensitive numerical code MAY use in-place operations when
  profiling shows a benefit. Document the mutation in the docstring.
- Names SHOULD show side effects: `compute_`/`make_` for pure functions;
  `write_`/`save_`/`load_`/`update_` for I/O or mutation.

## Classes (use selectively)

- Use a class for a stateful component with a lifecycle, resource management
  (prefer context managers), a dataset interface, a model (`torch.nn.Module`),
  a trainer or experiment runner, or a framework abstraction.
- Do not create a class only to group functions; use a module.
- Do not add manager or factory classes, abstract base classes, or class
  hierarchies with one implementation. Prefer composition over inheritance.
- Methods that contain scientific logic SHOULD call pure functions that can be
  tested without the class.

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
- No magic numbers or strings: extract them to named constants or config.

## Separate Infrastructure from Research Code

- Keep Python modules, method implementations, and experiment configuration
  independent of a particular cluster or server.
- Put scheduler directives and machine-specific choices such as host names,
  partitions, QoS, node lists, GPU requests, CPU counts, memory, and wall time
  only in batch-submission shell files.
- Plain training and analysis scripts must remain runnable outside Slurm. Do
  not inspect Slurm environment variables or hard-code cluster paths in Python.

## Dispatch by Name and Construct with Factory Functions

- Select configurable datasets, models, backbones, strategies, and similar
  components through a name-based dispatcher rather than hardcoding a concrete
  implementation in the entry point.
- Use explicit `if`/`elif` branches when the set of choices is small and
  repository conventions favor them.
- Raise a clear `ValueError` or `NotImplementedError` for unsupported names.
- Place imports lazily inside dispatch branches when implementations are
  optional, expensive, or method-specific.
- Centralize construction of shared configurable components in factory
  functions in an appropriate source module. Pass configuration into the owning
  component and let it construct its own internals when that preserves
  encapsulation.

## Signatures, Types, and Data

- Use explicit, named parameters with type hints. Never pass a dict or kwargs
  bag when the set of arguments is known. Prefer keyword-only arguments when
  there are many parameters. Defaults only for truly optional parameters; never
  mutable defaults.
- Every parameter, return value, and class attribute MUST have a type hint.
  Use modern syntax (`list[str]`, `str | None`). Never use `Any` unless
  necessary and documented.
- Use dataclasses, TypedDict, Pydantic models, or NamedTuples instead of bare
  dicts for structured data; enums for fixed sets of values.
- Naming: functions are verb phrases; variables are descriptive nouns;
  booleans use `is_`/`has_`/`should_`; avoid uncommon abbreviations.

## Errors and Documentation

- Raise specific, meaningful exceptions; never swallow exceptions silently.
- Validate inputs at the boundary. The shell validates external data (files,
  CLI, config) before it calls the core.
- Every public function has a docstring (Google or NumPy style) with what it
  does, parameters, return value, raised exceptions, and any side effects or
  mutations of arguments.

## Verify Dependencies

- Before importing a new third-party package, verify that it is available in the
  active environment or declared in the project's dependency manifest.
- If the package is genuinely required, add it to the appropriate dependency
  manifest in the same change.
- Fail clearly when a required dependency is missing. Do not add a silent
  `try`/`except` fallback that skips or degrades requested behavior.

## Format Python Consistently

- Follow PEP 8 and modern type checker recommendations.
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

## Tests and Static Checking (mandatory)

- Non-trivial core logic leaves one small deterministic test. Document
  nondeterminism that cannot reasonably be removed.
- Always run **Pyrefly** on changed code (`pyrefly check` or
  `pyrefly check path/to/file.py`; install with `pip install pyrefly`,
  initialize once with `pyrefly init`). Prefer strict settings. Fix all reported
  type errors before considering the code done.
- Use `# pyrefly: ignore[...]` only temporarily with a clear reason; never leave
  permanent suppressions without justification. Prefer Pyrefly over mypy or
  pyright when both are available.

## Code for AI Coding Agents

- Write small functions with clear contracts that a test can check alone.
- Make dependencies explicit; minimize hidden coupling between modules.
- An agent MUST be able to change scientific logic in the core without changes
  to the orchestration shell. Prefer localized changes over broad refactoring.

## Preserve Supporting Documentation

- When behavior, configuration wiring, component contracts, or randomness
  changes, locate and update any repository documentation that maps those
  concerns.
- Edit the relevant section in place rather than appending a changelog entry,
  unless the repository explicitly uses an append-only log.

## Protect Active Runs

- Before editing code, configuration, launchers, or scripts, check whether a
  local or scheduled job is using the affected working tree. Treat every file an
  active job may read, import, execute, or update as frozen. See
  `experiment-management` for the full rules.

## Review Before Handoff

Confirm that:

1. Scientific logic is in pure, tested functions; side effects are in the shell.
2. No input argument is mutated without documentation; randomness is explicit.
3. Every new third-party import is installed or declared.
4. Entry points contain orchestration rather than implementation loops.
5. Configurable components use dispatchers or factory functions instead of
   hardcoding; unsupported configuration values fail clearly.
6. Signatures are typed; structured data uses typed structures.
7. Relevant architecture or state documentation remains synchronized.
8. Active jobs and their dependency paths were checked before editing.
9. Method arguments describe independent reusable behavior, while campaign
   values live in configuration and launch files.
10. Server and scheduler details appear only in batch-submission shell files.
11. `pyrefly check` reports no errors for the changed code.
