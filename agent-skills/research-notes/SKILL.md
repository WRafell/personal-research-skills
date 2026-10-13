---
name: research-notes
description: Create or append dated research notes in docs/research-notes. Each note is a self-contained record in full sentences of what was done, why, how, and the raw results with their numbers; links to files are supporting references only. Use after each experiment, analysis, validation, or research decision, and when the user asks to document findings.
---

# Research notes

A research note is the scientific record of the project. A reader MUST be able
to understand what was done, why, and what the numbers were, from the note
alone, without opening any other file. A list of links or file paths is not a
research note.

Use this skill when the user asks to document research findings, experiments,
validation results, or implementation decisions, and after each completed
experiment (see `experiment-management`). The session state (jobs, paths, what
to do next) goes to the handoff log (see `handoff`), not to the notes.

## Report contract

This contract is the same in `research-notes`, `html-research-reports`, and
`experiment-management`. It applies to every research report: a dated note, a
Markdown report, and an HTML page.

A report is a self-contained, source-backed record. A reader MUST understand
it without opening any other file. Write it in this order:

1. **Answer.** The current conclusion, or the short answer, first.
2. **Question and reason.** What was asked and why it matters.
3. **Method, in sentences.** The data and the sample counts, the conditions
   and the one factor that changed, the baseline, the main settings with their
   values, and the primary comparison with its statistical test, fixed before
   the results.
4. **Results with raw numbers.** Values read from saved records: each
   condition's metric, the paired difference with its 95% CI, the p-value, and
   counts such as "34 of 49 cases". Use a table when several conditions are
   compared. Give favorable, null, mixed, and adverse results the same detail.
5. **Interpretation.** Separate from the results. Label post-hoc analyses and
   unmeasured mechanisms as such.
6. **Limits and next step.**
7. **References last.** Record IDs, job IDs, and file paths support the text;
   they never replace the sentences or the numbers.

Rules:

- Label each result as planned, running, completed, or failed.
- Never write "improved", "works", or "similar" where a measured value exists.
- Keep reports current. When code, data, runs, or results change, update every
  affected report in the same session, unless the user says otherwise. Dated
  research notes and the handoff log are append-only; correct them with a new
  entry.
- HTML pages also follow `html-research-reports`: an Overview plus month
  (`YYYYMM`) and day (`YYYYMMDD`) sections; a legend for each color-coded
  image, with the color names in words; no internal paths, hosts, user names,
  or job IDs; and a DOM test before delivery, plus a look in a real browser
  when one is available.

Before you finish, check each item and say in your reply which checks you did:

- [ ] The answer is at the top; the question, method, and results are in full
      sentences.
- [ ] Each number agrees with its saved record; each result has its state.
- [ ] The interpretation and limits are separate from the results.
- [ ] References are last and replace no text.
- [ ] Every report that this change affects is updated.
- [ ] HTML only: legends, shareable text, DOM test, and the browser check (or
      a statement that no browser was available).

## File and heading

- Write to `docs/research-notes/YYYY-MM-DD.md` with the current date. Create
  the directory and the file when absent; append when the file exists. Keep
  all existing content. Never rewrite an earlier entry; to correct it, append
  a new entry that names the correction.
- Start each entry with `## [YYYYMMDD-HH:mm:ss] <short title>` (local time
  from `date +%Y%m%d-%H:%M:%S`). The title names the finding or decision, not
  the file (for example "Calibrated threshold doubles the Dice of top-k
  selection", not "Update report").

## Required content, in sentences

Write short paragraphs in full sentences, in this order. Each part is required
unless it is marked optional.

1. **Question and reason.** What was asked or tested, and why: the hypothesis,
   the problem it addresses, or the decision that the result informs.
2. **What was done.** The method in sentences: the data (dataset, split, number
   of samples or units), the conditions and the factor that changed, the
   baseline, the main settings with their values (for example seed, threshold,
   model, resolution), and the primary comparison with its statistical test.
   State what was not changed when that matters for the comparison.
3. **Results with raw numbers.** The measured values, read from the result
   records: the unit of analysis and its count, each condition's metric, the
   difference with its uncertainty (for example the 95% CI), the test statistic
   or p-value, and counts such as "34 of 49 cases". Use a Markdown table when
   several conditions or metrics are compared. Give units and keep the
   precision of the record. Report null, mixed, and adverse results with the
   same detail as favorable results.
4. **Interpretation.** One to three sentences on what the result supports and
   what it does not. Keep it separate from the raw results, and label
   post-hoc analyses and unmeasured mechanisms as such.
5. **Limits and next step.** Known limits (for example one seed, a small
   sample, an approximation, a check that was not made) and the next step or
   open question.
6. **References (optional, last).** Record IDs, job IDs, and file paths that
   hold the evidence. They support the note; they never replace the sentences
   or the numbers above.

## Not permitted

- An entry that is only links, file paths, or a list of changed files.
- "See <file>" or "results are in <folder>" in place of the numbers.
- Claims without numbers, such as "improved", "works", "is better", or "is
  similar", when a measured value exists.
- Numbers that were not read from a saved output, and numbers from a running
  or failed job presented as final. Say which state each result is in:
  planned, running, completed, or failed.
- Copying a whole report. Summarize the method and give the key numbers; the
  report keeps the full detail.

## Example of the form (generic, invented values)

```markdown
## [20250314-16:42:10] Calibrated threshold doubles the Dice of top-k selection

**Question and reason.** Top-k selection of model scores gave masks that
looked incomplete. We tested whether a score threshold calibrated on training
negatives gives better masks, because the answer decides whether a new
segmentation model is necessary.

**What was done.** We used the held-out test split (50 positive and 80
negative cases) and the trained model without changes. Method A keeps the top
10% of units by score in each case. Method C keeps units whose score is above
3.1, the 99.9th percentile of the scores of the training negative cases. The
primary comparison was fixed before the results: mean Dice on positive test
cases, paired by case, Wilcoxon signed-rank test.

**Results.**

| Method | Mean Dice (95% CI) | Median Dice |
|---|---|---|
| A, top 10% | 0.21 (0.14 to 0.28) | 0.07 |
| C, score > 3.1 | 0.51 (0.43 to 0.60) | 0.51 |

The paired difference is +0.30 (95% CI 0.24 to 0.36); 47 of 50 cases improve;
p = 2e-14. On negative cases, C flags 0.12 mm² per case on average.

**Interpretation.** The incomplete masks come mostly from the fixed budget,
not from regions that the model scores low. The result does not show that the
masks are accurate for small lesions.

**Limits and next step.** One training seed. Dice on the smaller half of the
cases is 0.23, which the unit size limits. Next: repeat with five seeds.

**References.** Run 250314-120501-a1b2; report docs/segmentation_report.md.
```

## Before saving

Read the entry as a person who has no access to the project files. If the
question, the reason, the method, or the main numbers are not in the text,
add them. Check every number against its record.
