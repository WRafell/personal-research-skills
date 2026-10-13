---
name: research-digest
description: On request, turn the handoff log and dated research notes (and the records they cite) into one self-contained Markdown or LaTeX document with tables and figures (in its own folder docs/digests/<YYYYMMDD>-<slug>/ with an assets/ subfolder) and no references to internal files, paths, hosts, or job IDs, written to scientific-writing practice. Use when the user asks for a digest, summary document, write-up, progress report, or shareable account of the project or of one topic or period.
---

# Research digest

The handoff log and the research notes are working records: dated,
append-only, and full of locators (paths, run IDs, job IDs). They stay as they
are. A digest is a separate document, written only when the user asks, that a
person or an agent can read with no access to the project files.

## Request

Fix these before writing; ask only for what the request does not say:

- **Scope:** the whole project, one topic, or a period (dates).
- **Format:** Markdown (default) or LaTeX.
- **Reader:** for example the team, a supervisor, a new member, or a public
  reader. This sets the level of detail and the background to explain.
- **Order:** by topic (default: question, method, results, decisions) or by
  date.

Give each digest its own folder, unless the project names another place:

```text
docs/digests/<YYYYMMDD>-<slug>/
    digest.md          (or digest.tex for LaTeX)
    assets/            figures and other files that the document shows
```

The folder is complete by itself: it can be copied, zipped, or shared as it
is. Never edit the handoff log, the notes, or the reports to make the digest.

## Sources

- Read every handoff entry and research note in scope, and the reports they
  name.
- Take each number from the saved result record, not from the log text; when
  a log and a record disagree, use the record and say in the reply which
  entry was wrong.
- Give each result its state at the digest date: planned, running, completed,
  or failed. A job that a log calls running may have ended; check its record
  or ask.
- Later entries correct earlier ones. Use the corrected fact and do not
  repeat the error.

## Self-contained and self-referenced

The digest refers only to itself and to published literature.

- **No internal locators:** no file paths, folder names, host or cluster
  names, user names, job IDs, commit hashes, or links to project files.
- **No "see":** never send the reader elsewhere for content. State the method,
  the numbers, and the decision in the text.
- **Translate identifiers into descriptions.** "Run 261009-110827-82ab"
  becomes "the Hibou-L ABMIL model (seed 0, 512-pixel patches at 20x)". If
  runs must be told apart, give them short labels defined in the document
  (for example "model H512"), and list them in a table of conditions.
- **Define every term and abbreviation at first use,** including project
  names of methods and operating points (for example "C_weak_q0.999" becomes
  "a threshold on the raw attention logit at the 99.9th percentile of the
  training negative slides").
- **Internal cross-references only:** sections, tables, figures, and
  equations of the digest itself (`\cref` in LaTeX, section links in
  Markdown).
- **Literature citations are permitted** and follow `scientific-writing`:
  verified against the DOI or the source, with a full reference list.
- **Figures:** embed only images in the digest's own `assets/` folder, linked
  with a relative path (`assets/<name>.png`); never link to another project
  path.

## Content

Follow `scientific-writing` (claims and evidence, statistics, structure,
figures) and the report contract in `research-notes`. A default outline:

1. **Summary.** The current answer and the main numbers, in one paragraph.
2. **Background and aim.** The problem and the questions, for the chosen
   reader.
3. **Data and methods.** Datasets and splits with counts, preprocessing,
   models, training, evaluation metrics, statistical tests, and the
   conditions that were compared.
4. **Results.** One subsection per question: the comparison, a table of
   numbers with uncertainty, and the state of each result. Include null and
   adverse results.
5. **Decisions and their reasons.** What changed in the plan, and why.
6. **Limitations and open questions.**
7. **Next steps.**
8. **Appendix (optional).** A dated timeline of the main events, a glossary,
   and the full table of conditions.

## Tables and figures

A digest MUST have tables and figures; a digest of prose only is not
complete.

- **Tables** are in the document itself (Markdown tables, or `booktabs` in
  LaTeX), not images of tables. At minimum: a table of conditions (the
  defined labels with their settings), and one results table for each
  question with each metric, its uncertainty, n, and the state.
- **Figures:** at least one figure for each main result (for example a
  comparison plot with intervals, a paired plot, or example images with their
  color legend). Copy existing figures from the project reports when they fit
  the reader; otherwise make new ones from the records with a script, and
  keep that script in the project, not in the digest folder.
- Store each figure in the digest's `assets/` folder with a short
  descriptive name (for example `dice_by_encoder.png`). Compress large images
  (for example JPEG for photographs, PNG or PDF for plots).
- Number every table and figure, refer to each one in the text, and give each
  one a caption that stands alone (what is shown, n, units, the meaning of
  error bars and colors, and the main point). Follow the figure rules in
  `scientific-writing`.
- Image content must not show internal paths, host names, or job IDs (check
  titles, axis labels, and legends).

Write in the project's style standard for documents (for example ASD-STE100
when the project requires it), unless the user asks for paper prose.

## Before delivery

- [ ] Scan the text for paths (`/`, `~`, file extensions), host names, user
      names, job IDs, run IDs, commit hashes, and "see"; remove or translate
      each one.
- [ ] Every term and label is defined; every number matches its record and
      has its state.
- [ ] Every cross-reference resolves inside the document; every literature
      citation is verified.
- [ ] Tables and figures: a table of conditions, a results table for each
      question, a figure for each main result; each one numbered, cited in
      the text, and captioned; every image is in
      the digest's `assets/` folder and loads by a relative path; nothing
      outside the digest folder is needed.
- [ ] LaTeX: the document compiles.
- [ ] In the reply, list the sources read, any log errors found, and any
      result whose state could not be confirmed.
