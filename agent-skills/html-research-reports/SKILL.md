---
name: html-research-reports
description: Create or revise source-backed HTML research reports and project briefings in pages/. Use for scientific status pages, experiment summaries, mechanism explainers, and decision workspaces.
---

# HTML research reports

Build a readable research workspace from recorded evidence. Match the established pages in `pages/` when working in this repository; adapt the structure to the report's question.

## Evidence and content

- Read the source report, completed settings, result records, and dated status entries needed for each claim. Treat plans, running jobs, completed runs, and interpretations as distinct states. Do not present an old snapshot as live status.
- Put the answer or current conclusion near the top. For project status, show objective, milestones, work queue, evidence, risks, and decision gates. For a scientific explanation, move from question and mechanism to controlled comparison, result, and limit.
- Use short headings, direct labels, compact paragraphs, and tables for comparable results. Define symbols and units. State sample size, conditions, and uncertainty when they affect interpretation. Link to the supporting source files and show the snapshot date.
- A visual must answer a question. Prefer a small timeline, table, sparkline, or labeled mechanism diagram over decorative charts. Identify approximate or illustrative values.

## Visual system

- Follow the existing light Swiss/editorial style: a warm bone-paper surface (`#fdfcf3`), ink text (`#202624`), readable gray secondary text (`#4b565a`), cool 1px dividers (`#c7d1d3`), and one muted teal accent (`#21696e`). Use restrained semantic colors for validated, running, warning, and blocked states. Keep status words alongside color.
- Use a compact navigation rail and an aligned main column. Prefer dense rows, table/list hybrids, and native `<details>` for optional detail. Keep generous margins around sections without making the data sparse. Avoid bento grids, floating cards, giant KPI figures, gradients, shadows, and decorative icons.
- Use a legible sans serif for prose and monospace with tabular numerals for dates, experiment IDs, settings, and metrics. Start around 17px body text and 15px table text; do not shrink essential data to fit. Use restrained heading sizes and clear section rules.
- The shared `pages/paper-grain.svg` can add faint texture. Preserve contrast and legibility. Use teal text selection, visible keyboard focus, and compact tags and progress marks only where they encode information.

## Diagrams and interaction

- Use the **diagram-design plugin** for a substantive scientific or system diagram if it is available and suits the task. If unavailable, draw with accessible inline SVG or native HTML/CSS. Do not require the plugin or install it solely for a report.
- Label diagram elements and relationships directly; provide a text equivalent or accessible name. Keep line weights, color, and type consistent with the page. Make interactive controls change a meaningful comparison, and explain the selected state in text.
- Prefer semantic HTML and small, local JavaScript. Keep tables horizontally scrollable on narrow screens, convert the sidebar to compact navigation on mobile, and provide a usable print view. Use external libraries only when the report needs them, such as MathJax for equations.

## Before delivery

Check each displayed number, status, date, source link, and derived comparison against its record. Confirm that the page remains readable at desktop and phone widths and that diagrams, tables, and controls remain understandable without color alone.
