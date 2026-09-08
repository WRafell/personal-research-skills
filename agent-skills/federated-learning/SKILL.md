---
name: federated-learning
description: Build and maintain reproducible federated-learning experiments with consistent trainer lifecycles, client sampling, aggregation hooks, evaluation metrics, result records, and method dispatch. Use when implementing or modifying FL algorithms, federated training rounds, client/server behavior, data distributions, evaluation, experiment tracking, or FL-related notebook prototypes.
---

# Federated Learning

Follow the repository's current structure where it is already established. Use
these contracts when extracting notebook experiments into source modules or
introducing a reusable FL framework.

## Preserve the FL Objective

- Represent training as client-local optimization followed by server
  aggregation.
- Weight aggregation by client sample counts unless the algorithm explicitly
  specifies another rule.
- Keep data local to clients. Communicate only the payload required by the
  selected FL method.
- Record intentional deviations from the reference algorithm or paper.

## Use a Shared Trainer Lifecycle

Centralize behavior common to all FL methods in a base trainer. Let the base
trainer own:

- model construction through the project's backbone factory;
- the communication-round loop;
- client sampling through an object-scoped RNG;
- global evaluation;
- per-round history;
- the final results dictionary.

Give method subclasses two narrow hooks:

```python
def _local_train(client_set) -> tuple[payload, float, int]:
    """Return the method payload, average loss, and sample count."""

def _aggregate(payloads, sizes) -> None:
    """Update the global model and server state in place."""
```

Treat `payload` as opaque to the base trainer. Allow each method to return the
state it needs, such as a model state dictionary or model-plus-optimizer state.

- Keep the communication-round and client minibatch loops out of the entry
  point.
- Give subclasses keyword-only method-specific constructor arguments.
- Forward shared arguments with `super().__init__(**kwargs)`.
- Keep server-side optimizer or momentum state on the trainer that owns it.

## Add an FL Method Consistently

When introducing a method:

1. Add its canonical lowercase name to the experiment configuration or CLI
   choices.
2. Implement a subclass of the shared FL base trainer in the source package.
3. Override the local-training and aggregation hooks.
4. Add an explicit method-dispatch branch at the orchestration layer.
5. Pass method-specific hyperparameters by name.
6. Test local payload construction, sample weighting, global-state updates, and
   a short multi-client round.
7. Document algorithm assumptions and known deviations.

Method constructors and shared trainer interfaces must be campaign-agnostic.
Expose each algorithmic decision as an independently settable argument at the
narrowest owner that implements it: shared lifecycle controls belong on the FL
base, while optimizer- or method-specific controls belong on that method.
Never pass a campaign or arm name into a trainer to select behavior. Compose
named arms in experiment configuration files from ordinary method arguments.

Do not create a separate `run_<method>` wrapper merely to hide the dispatch.

## Make Data Distribution Explicit

- Configure datasets by name through the project data loader rather than
  importing a concrete dataset in the entry point.
- Record the client partition strategy and all its parameters, including IID or
  non-IID mode, number of clients, seed, class restrictions, sample counts, and
  participation rate.
- Use an explicit RNG or generator for deterministic partitions and client
  sampling.
- Keep test data construction separate from client training partitions.
- Distinguish independent client training from federated training. Do not call an
  experiment FedAvg unless communication and server aggregation actually occur.

## Track Every Experiment

Generate an experiment ID at run start with format `YYMMDD-HHmmss`.

Write a settings record before training begins. Include:

- all resolved configuration or CLI arguments;
- experiment ID and device;
- dataset and partition specification;
- FL method, backbone, client count, rounds, local-training configuration, and
  participation rate;
- random seeds.

On success, add `results` to the same record. On failure, add an `error` object
containing the exception type, message, and traceback. Keep `results` and `error`
mutually exclusive.

Maintain an append-only experiment index with one concise entry per successful
run. Include the experiment ID, method, dataset, backbone, distribution, client
and round counts, participation rate, result-record path, total and per-round
time, and primary final metrics. Do not add failed runs to the success index.

Use the repository's established paths when available. If none exist yet,
prefer:

```text
local/experimental_settings/{exp_id}.json
local/exp_log/experiments.md
```

## Standardize Evaluation

Return at least:

```python
{"loss", "acc", "f1", "auc"}
```

- Compute macro-F1.
- Compute macro one-vs-rest ROC-AUC from class probabilities.
- Return `NaN` for AUC when it is mathematically undefined; do not substitute a
  misleading score.
- Store `test_acc`, `test_f1`, and `test_auc` for every evaluated round.
- Store corresponding final values in the results dictionary.
- Use final values, not cherry-picked intermediate values, in the experiment
  index unless the field is explicitly labeled as best.

Add engram-specific metrics alongside this common evaluation contract rather
than replacing it.

## Protect Randomness and Observational Neutrality

- Keep client sampling on a trainer-owned RNG.
- Give independent stochastic consumers independent generators when practical.
- Ensure engram extraction, evaluation probes, visualization, and logging do not
  perturb the RNG sequence used by real training.
- Save and restore every affected RNG state around observational code when
  isolation cannot be achieved structurally.
- Document new or moved RNG consumers in the repository's stochastic-state
  documentation when such a map exists.

## Follow the Repository Logging Contract

When work changes client/server payloads, synchronization, lazy delivery,
state versions, or communication accounting, read and follow
`md_docs/fl_logging_checklist.md`. Treat its named schemas as the canonical
field contract and keep `scripts/analysis/check_logging_contract.py` enforcing
the active schema.

- Version a new schema so completed records remain readable under the contract
  they declared.
- Log actual recipients and bytes; do not substitute scheduled or estimated
  communication.
- Keep method-specific field lists in the checklist, not in every experiment
  instruction. Instructions should reference the schema and list only genuine
  experiment-specific additions or exceptions.
- Update the checklist and checker together when the contract changes.

## Review Before Handoff

Confirm that:

1. The experiment is accurately described as independent, federated, or
   centrally trained.
2. The base trainer owns shared lifecycle behavior.
3. The method hooks preserve payload and aggregation semantics.
4. Client partitioning, sampling, and seeds are recorded.
5. Aggregation weighting matches the intended algorithm.
6. Required evaluation metrics are computed and persisted.
7. Success and failure records are unambiguous.
8. FL method and architecture documentation remains synchronized.
9. No trainer behavior depends on a campaign, dataset, machine, or scheduler
   label, and independently meaningful controls remain independently settable.
