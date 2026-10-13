---
name: scientific-writing
description: Draft, revise, or review scientific manuscripts (LaTeX papers, abstracts, theses, rebuttals) so that every claim traces to a saved result, statistics are reported completely, citations are verified, the structure and figures follow good practice, and the LaTeX source keeps the repository's formatting conventions. Use for any paper writing, editing, review, or pre-submission check.
---

# Scientific writing

A manuscript makes claims; each claim needs evidence that a reviewer can
check. This skill covers the content (claims, statistics, structure,
citations, figures) and the LaTeX source format. Results come from the
project's run records (see `experiment-management`); the report contract in
`research-notes` applies to every number.

## Claims and evidence

- Trace each claim to a saved result record or to a cited source. Keep a
  claim no stronger than its evidence: association is not cause, one dataset
  is not "general", a POC result is not evidence (see `proof-of-concept`).
- Generate the numbers in the text and tables from the records, for example a
  `results.tex` file of `\newcommand` macros written by a script, so that a
  rerun updates the paper. Do not type a result by hand.
- Report null, mixed, and adverse results that bear on the claims. Do not
  select metrics, operating points, or subsets after seeing the results
  without saying so.
- Separate results (what was measured) from discussion (what it means).
  Label post-hoc analyses and unmeasured mechanisms as such.

## Statistics

For each reported comparison give: the population and split; n and the unit
of analysis (for example slides, not patches); the metric and its exact
definition; the estimate with its 95% confidence interval; the named test and
whether it is paired; the p-value; the correction for multiple comparisons;
the primary endpoint fixed before the results; and the number of seeds or
runs, with their spread. Prefer effect sizes with intervals to p-values
alone.

## Reporting guideline

Choose the checklist that fits the study and the venue at the start, and
fill it before submission. Examples: CLAIM or TRIPOD+AI for medical-imaging
AI and prediction models, STARD for diagnostic accuracy, CONSORT-AI or
SPIRIT-AI for trials, and the venue's reproducibility checklist (for example
NeurIPS, MICCAI). Map each item to the section that answers it.

## Structure and style

- Use the venue's structure; by default introduction, methods, results,
  discussion (with limitations), conclusion. State the contributions as a
  short list at the end of the introduction.
- The abstract gives the problem, the method, the main numbers with their
  uncertainty, and the main limitation or scope.
- One idea per paragraph, with a topic sentence first. Use past tense for
  what was done and present tense for what the results show and for
  established facts.
- Define each acronym at first use in the abstract and again in the body.
  Use one term for one concept everywhere (for example do not switch between
  "patch", "tile", and "instance").
- Write a real limitations paragraph: data, labels, generalization, compute,
  and what was not tested.
- Follow the project's style standard. If a project applies a controlled
  language (for example ASD-STE100) to its documentation, ask before
  applying it to manuscript prose.

## Citations

- Verify every reference against its DOI, the publisher page, arXiv, or the
  PDF before it enters the bibliography. Never cite a paper from memory alone;
  if it cannot be found, say so and leave a `% TODO verify` mark.
- Cite what a source actually says; check page or section for specific
  claims. Prefer the archival version over a preprint when both exist.
- Describe related work fairly, including results that compete with the
  claims.

## Figures and tables

- Each caption stands alone: what is shown, n, units, what error bars or
  shaded areas mean, and the main point.
- Use colorblind-safe palettes, label axes with units, and keep the same
  color for the same condition across figures. Export vector graphics where
  possible.
- Use `booktabs` for tables and `siunitx` for numbers and units; align
  decimals; bold only by a rule that the caption states.
- Use `\cref` (cleveref) or `\ref` for every cross-reference; do not write
  figure or table numbers by hand.

## Availability, ethics, and licenses

- Add data and code availability statements that match what will really be
  released.
- Check the license and terms of use of each dataset and pretrained model
  (for example CAMELYON16, TCGA, gated model weights) and state them.
- Add ethics approval, consent, or the statement that it is not required,
  as the venue requires. Declare funding and conflicts of interest.

## LaTeX source format

- Keep each prose paragraph on one physical source line. Do not insert source
  line breaks in the middle of a paragraph.
- Use blank lines to separate paragraphs and major structural blocks.
- Keep titles, headings, labels, display environments, list items, captions,
  table rows, and similar LaTeX structure on their own source lines.
- Indent the contents of equations, lists, tables, and other nested
  environments with one literal tab per nesting level. Keep `\begin{...}` and
  `\end{...}` aligned at the same level.
- Keep each list item and caption on one physical line unless it contains a
  nested display environment.
- Treat formatting-only cleanup as semantics-preserving: do not rewrite prose
  or mathematics unless the user also requests content changes. Verify that
  only whitespace changed, and compile the manuscript when the environment
  permits.

## Before submission (and after each major revision)

- [ ] Every number in the text, tables, and figures matches its record (or
      comes from the generated macros); recompile after regenerating them.
- [ ] Each claim has its evidence; limitations are stated.
- [ ] Statistics are complete for each comparison (n, unit, CI, test,
      correction, primary endpoint, seeds).
- [ ] The reporting checklist is filled and mapped to sections.
- [ ] Every reference is verified; no `% TODO verify` remains.
- [ ] Captions stand alone; cross-references resolve; the PDF compiles
      without undefined references or overfull warnings that matter.
- [ ] Availability, license, ethics, funding, and conflict statements are
      present.
- [ ] Optional: an independent review by the other agent (`agents-collab`).

After a manuscript edit, follow the repository instructions for its revision
log and status log.
