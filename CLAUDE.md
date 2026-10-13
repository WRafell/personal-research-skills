# CLAUDE.md

## Skills

### Cluster SSH execution

For tasks that use managed servers or Slurm, read and follow
`agent-skills/cluster-ssh-execution/SKILL.md`. Keep Claude Code local; perform
remote work through one-shot SSH commands and the scheduler.

### Coding style

For implementation, refactoring, or code review, read and follow
`agent-skills/coding-style/SKILL.md`.

### Experiment management

For experiments, evaluations, ablations, baselines, result schemas, or
experiment logs, read and follow
`agent-skills/experiment-management/SKILL.md`.

### Proof of concept

For prototypes, spikes, quick tests, or feasibility checks outside the main
pipeline, read and follow `agent-skills/proof-of-concept/SKILL.md`. Each POC
lives in its own `poc/<YYMMDD>-<slug>/` folder, the main code never depends on
it, and it ends by promotion into the main code or by an archive note.

### Federated learning

For federated algorithms, client/server training, data partitioning,
aggregation, FL evaluation, or experiment tracking, read and follow
`agent-skills/federated-learning/SKILL.md`. Apply the coding-style and
experiment-management skills alongside it when relevant.

### Scientific writing

For drafting, revising, reviewing, or checking research manuscripts (claims
and evidence, statistics, reporting checklists, citations, figures, LaTeX
format), read and follow `agent-skills/scientific-writing/SKILL.md`.

### Research code maps

For changes to algorithms, stochastic state, control or data flow,
configuration wiring, method contracts, aggregation, or trusted results, read
and follow `agent-skills/research-code-maps/SKILL.md`.

### Handoff

Before work, read the project's handoff log; before ending a session that
changed code, data, jobs, or plans, append one entry. Read and follow
`agent-skills/handoff/SKILL.md`.

### Research notes

For dated research notes, read and follow `agent-skills/research-notes/SKILL.md`.
Each note is a self-contained record in full sentences: what was done, why,
how, and the raw results with their numbers. Links to files are supporting
references only, never the content of a note.

### HTML research reports

For HTML result pages and project briefings, read and follow
`agent-skills/html-research-reports/SKILL.md`.

### Agent collaboration

To use Codex and Claude Code as independent reviewers of each other, read and
follow `agent-skills/agents-collab/SKILL.md`.

### Writing standard (ASD-STE100)

When a project asks for Simplified Technical English, read and follow
`agent-skills/writing-skill/SKILL.md`. The skill is active only on explicit
request.

## Project-specific instructions

Define repository paths, report mirrors, environments, remote worktrees,
cluster aliases, and experiment conventions in the consuming project's own
instructions. Project-specific rules take precedence over these shared skills.
