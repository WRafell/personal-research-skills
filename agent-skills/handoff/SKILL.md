---
name: handoff
description: Keep an append-only handoff log so that the next agent session can continue the work. Read it at the start of a session; append one entry before the end of a session that changed code, data, jobs, or plans.
---

# Handoff

The handoff log is `docs/handoff.md` unless the project instructions name a
different file. The project instructions also give the time zone (default:
the local time of the workstation).

## At the start of a session

- Read the last entries of the handoff log before other work. Treat job states
  in old entries as possibly out of date; check them on the cluster.

## At the end of a session (or after a large step)

- Append one entry when the session changed code, data, jobs, or plans.
- Never edit or delete an earlier entry. To correct an entry, append a new
  entry that names the correction.
- Format: one paragraph, `[YYYYMMDD-HH:mm:ss] - {paragraph}`. Get the time with
  `date +%Y%m%d-%H:%M:%S`.
- Start with a bold one-line status (for example `**Copy is complete.**`).
- Record the facts that a future agent needs: what changed (files, functions),
  where (paths, hosts, snapshots, job IDs, run IDs), the current status
  (running, complete, failed, and why), the checks done, and the open items.
- Do not use shell substitution in text that contains backticks; write the
  entry with a quoted heredoc or a script.

## Relation to other records

- Results go to the dated research notes (`research-notes`) and the reports
  (`experiment-management`). The handoff entry links to them; it does not repeat
  the full results.
