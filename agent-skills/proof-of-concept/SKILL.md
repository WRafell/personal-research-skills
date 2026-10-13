---
name: proof-of-concept
description: Keep a proof of concept (POC) self-contained in poc/<YYMMDD>-<slug>/ with a one-way dependency on the main code, a README with question, success criterion, and time limit, and a required end (promote into the main code, or archive in a research note and delete). Use when the user or the agent wants to prototype, try out, spike, quickly test, or check the feasibility of an idea outside the main pipeline.
---

# Proof of concept

A proof of concept (POC) answers one question quickly. It may be rough inside
its folder, but nothing outside depends on it, and it always ends. Use
`experiment-management` instead when the work is a real experiment on the
main pipeline whose results will go into a report.

## Folder

- Put each POC in `poc/<YYMMDD>-<slug>/` (the date it starts and a short
  name, for example `poc/261013-pin-board-figure/`). Keep all of its code,
  configs, notebooks, and its `README.md` there.
- Write outputs only to `poc/<id>/out/`, and add `poc/*/out/` to `.gitignore`.
  Large inputs stay where they are; read them, do not copy them.
- Do not add POC files to `src/`, `configs/`, `scripts/`, or the experiment
  run root (`local/<stage>/`).

## One-way dependency

- A POC MAY import from the main code (`src/`, packages).
- The main code, scripts, configs, and tests MUST NOT import from or call
  anything in `poc/`. Check with a search for `poc` in imports and paths
  before handoff.
- Do not change the main code to suit a POC. If the main code must change,
  the POC is ready to promote (see below).

## README first

Write `poc/<id>/README.md` before the code:

1. **Question.** One sentence.
2. **Success criterion.** What result answers the question yes or no, with a
   number where possible.
3. **Time limit.** For example 3 days from the start date.
4. **How to run.** The command, the environment, and the inputs.

At the end, add **Outcome**: what was done and the result in sentences with
raw numbers, following the report contract in `research-notes`.

## Standards inside a POC

- The coding style, tests, and run records of the main code are optional
  inside the folder. Keep the README current and the run command working.
- POC numbers are exploratory. Label them "POC" wherever they appear. They
  are not evidence for a report until the idea is promoted and reproduced.

## End: promote or archive

Every POC ends in one of two ways, by its time limit or earlier:

- **Promote.** Rewrite the idea in the main code with tests and configs (do
  not copy the POC files), run it with normal run records, and reproduce the
  POC result through the main pipeline. Then delete the POC folder.
- **Archive.** Write the outcome in a dated research note (question, method,
  result with numbers, decision), name the git commit that contains the POC
  code, and delete the folder. The code stays in the git history.

A POC past its time limit is listed in the handoff entry; ask the user to
promote, extend, or archive it. Do not delete a POC folder without either a
promotion that reproduced the result or a research note.

## Before handoff

- [ ] Each open POC has a README with question, criterion, time limit, and run
      command.
- [ ] No file outside `poc/` imports from or calls a POC.
- [ ] POC outputs are only in `poc/<id>/out/`.
- [ ] Each ended POC was promoted (and reproduced) or archived in a research
      note before its folder was deleted.
- [ ] POCs past their time limit are named in the handoff entry.
