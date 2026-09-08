---
name: paper-writing
description: Edit or review LaTeX research manuscripts while preserving concise scientific prose and the repository's source-formatting conventions.
---

# Paper Writing

Apply the following source-formatting rules to LaTeX manuscripts:

- Keep each prose paragraph on one physical source line. Do not insert source
  line breaks in the middle of a paragraph.
- Use blank lines to separate paragraphs and major structural blocks.
- Keep titles, headings, labels, display environments, list items, captions,
  table rows, and similar LaTeX structure on their own source lines.
- Indent the contents of equations, lists, tables, and other nested environments
  with one literal tab per nesting level. Keep `\\begin{...}` and
  `\\end{...}` aligned at the same level.
- Keep each list item and caption on one physical line unless it contains a
  nested display environment.
- Treat formatting-only cleanup as semantics-preserving: do not rewrite prose or
  mathematics unless the user also requests content changes. Verify that only
  whitespace changed, and compile the manuscript when the environment permits.

After a manuscript edit, follow the repository instructions for its revision
log and status log.
