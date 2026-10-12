---
name: research-notes
description: Create or append dated project research notes in docs/research-notes without overwriting existing notes.
---

# Research notes

Use this skill when the user asks to document research findings, experiments,
validation results, or implementation decisions, and after each completed
experiment (see `experiment-management`).

Write notes to `docs/research-notes/YYYY-MM-DD.md` using the current date.
Create the directory and file when absent; append to the existing file when it
already exists. Preserve all existing content.

Each entry starts with a heading `## [YYYYMMDD-HH:mm:ss] <short title>` (local
time from `date +%Y%m%d-%H:%M:%S`). Then write short paragraphs in this order:
the question or decision, the method and configuration (run IDs, settings),
the result with its evidence (paths, job IDs, metrics with intervals), and the
limits or follow-up.

Keep entries concise and evidence-based. Do not invent results or rewrite
historical entries. To correct an entry, append a new entry.
