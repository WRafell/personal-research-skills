---
name: research-code-maps
description: Keep research documentation synchronized with implementation by maintaining algorithm, stochastic-state, control-flow, configuration, and trusted-result maps. Use when changing algorithms, method contracts, aggregation, data or parameter flow, CLI/config wiring, RNG creation or consumption, observational probes, or reference-result validity.
---

# Research Code Maps

Maintain concise maps that explain the parts of the research code most likely to
produce plausible but incorrect results. Update relevant sections in place; do
not turn these maps into changelogs.

Use existing documentation paths when available. If maps do not yet exist,
prefer descriptive files under `project_overview/` or the repository's
documentation directory.

## Map Algorithms and Deviations

Maintain an algorithm map that states:

- what each method and variant is intended to do;
- its authoritative paper, specification, or baseline;
- important equations or update rules;
- implementation assumptions;
- known divergences from the reference;
- comparability limits between variants or stored results.

Update it when adding a method or variant, changing algorithm behavior, or
discovering that implementation and reference differ.

Record a discovered divergence as a caveat before deciding whether to change the
code. Do not silently rewrite documentation to make an accidental implementation
look intentional.

## Map Stochastic State

Maintain a table of every meaningful RNG source and consumer. For each, record:

- construction or seeding location;
- RNG type and seed source;
- owning object or scope;
- consumers;
- whether its state is isolated from other code paths;
- save/restore behavior around observational code;
- known gaps.

Update the map whenever code adds or moves calls such as:

```text
manual_seed
default_rng
Generator(
.seed(
```

Also update it when adding engram extraction, evaluation probes, logging,
visualization, or other observation paths that run before or alongside real
training.

- Ensure observational paths preserve every RNG source they can affect.
- List a generator shared by logically separate code paths as a known gap even
  if the current task does not fix it.
- Distinguish deterministic partitioning, model initialization, client sampling,
  minibatch order, augmentation, and analysis sampling.

## Map Control and Data Flow

Maintain a structural overview covering:

- entry points and dispatch;
- model and dataset construction;
- client/server or trainer lifecycle;
- round, epoch, and minibatch loops;
- parameter and payload flow;
- aggregation weighting and blending;
- engram extraction and comparison flow;
- evaluation and result persistence.

Update it when changing:

- a round loop or lifecycle method contract;
- client-to-server or server-to-client payloads;
- aggregation inputs, weighting, or state updates;
- which outputs can be compared fairly;
- ownership of models, optimizers, statistics, or engrams.

Describe contracts at their boundaries: accepted inputs, returned outputs, state
mutations, and ordering constraints.

## Map Configuration Wiring

For each important CLI flag or configuration field, record:

- public name;
- type and default;
- validation or choices;
- constructor or function parameter receiving it;
- downstream behavior it changes;
- serialized result field when the name differs.

Update the map whenever a setting is added, renamed, removed, or rewired. Pay
special attention when CLI and constructor names differ.

Map configuration-file keys and inheritance/override precedence as well as CLI
flags. The map must make clear that campaign labels are provenance only and
that trainer behavior is selected by independent algorithmic settings. Record
server allocation only in the relevant batch-submission script; do not map it
as part of the method or experiment configuration.

## Map Trusted Results

Maintain a small registry of reference results used for comparisons. Record:

- experiment identifier and result path;
- code or notebook context;
- full configuration;
- metric definition;
- why the result is trusted;
- known limitations.

Invalidate or annotate a result immediately when it used wrong hyperparameters,
predates a correctness fix, came from stale notebook output, or lacks sufficient
provenance. Never continue presenting it as a baseline merely because later work
depends on it.

## Keep Maps Useful

- Edit the relevant row or section in place.
- Prefer tables for exact mappings and prose for contracts or caveats.
- Link to source files and experiment records instead of duplicating large code
  or result blobs.
- Describe current truth. Use the experiment index or version history for
  chronology.
- Add a new map only when it guards a distinct source of research error.

## Review Before Handoff

Determine whether the change affects:

1. algorithm intent or reference fidelity;
2. stochastic sources or consumers;
3. control, data, parameter, or payload flow;
4. configuration wiring;
5. trusted-result validity.

Update every affected map and verify that its statements match the current code,
not the intended future implementation.
