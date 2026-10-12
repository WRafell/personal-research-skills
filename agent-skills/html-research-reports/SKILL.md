---
name: html-research-reports
description: Create or revise source-backed HTML research reports and project briefings in pages/. Use for scientific status pages, experiment summaries, mechanism explainers, and decision workspaces.
---

# HTML research reports

Build a readable research workspace from recorded evidence. Match the established pages in `pages/` when working in this repository; adapt the structure to the report's question.

## Evidence and content

- Read the source report, completed settings, result records, and dated status entries needed for each claim. Treat plans, running jobs, completed runs, and interpretations as distinct states. Do not present an old snapshot as live status.
- Put the answer or current conclusion near the top. For project status, show objective, milestones, work queue, evidence, risks, and decision gates. For a scientific explanation, move from question and mechanism to controlled comparison, result, and limit.
- Use short headings, direct labels, compact paragraphs, and tables for comparable results. Define symbols and units. State sample size, conditions, and uncertainty when they affect interpretation. Show the snapshot date. Link to the supporting source files only on internal pages (see Shareable pages).
- A visual must answer a question. Prefer a small timeline, table, sparkline, or labeled mechanism diagram over decorative charts. Identify approximate or illustrative values.

## Structure over time

- Keep one **Overview** for the current state (answer, objective, evidence, queue, risks, gates). When the history spans many days, add one tab for each month (`YYYYMM`). Each month starts with a monthly overview (summary, results of the month, what was produced, open items), followed by one section for each working day (`YYYYMMDD`) with the work, the record IDs of that day, and links back to the related Overview sections. Do not add empty days.
- Give each month and day an element ID equal to its date, so that an address such as `#YYYYMM` or `#YYYYMMDD` opens the right tab and scrolls to the day; a section address opens the Overview. List the months and their days in the navigation rail.
- Build tabs as accessible ARIA tabs (`role="tablist"`, `tab`, `tabpanel`, `aria-selected`, arrow-key movement). Change tabs through `location.hash`; `history.pushState` fails on `file://` pages. Without JavaScript and in print, show all views one after another.

## Images and color legends

- Copy every image that the page shows into `pages/assets/<topic>/`, compressed (for example JPEG with trimmed margins), so that the page folder is self-contained.
- Choose example images with a rule that was fixed before (for example the cases selected by the analysis), not by eye, and give per-image values next to each image.
- Each image that uses color to encode data needs a legend next to it: a short key under the image, and a full legend once for the section. Take the colors and value ranges from the plotting code, not from the appearance; check colormap end colors with the plotting library.
- Say what the scale means: absolute or relative to each image, the range, and any transparency rule. When a monotone transform (for example a softmax or a per-image min–max) exaggerates small differences, say so, and name the panel that is correct for comparisons.
- Write the color name in words, in parentheses, after each swatch or ramp, for example "■ (dark red) positive class", so that the text is correct when the swatches do not show.

## Shareable pages

- Write each page as if it can be shared publicly unless the user says otherwise: no local or server paths, host or storage names, scheduler job IDs, user names, private repository names, or links outside the pages folder. Record IDs and dataset names are acceptable. Keep the evidence trail in the project records, not in the page.
- Check the license of any dataset image before a page is published.

## Visual system

- Follow the existing light Swiss/editorial style: a warm bone-paper surface (`#fdfcf3`), ink text (`#202624`), readable gray secondary text (`#4b565a`), cool 1px dividers (`#c7d1d3`), and one muted teal accent (`#21696e`). Use restrained semantic colors for validated, running, warning, and blocked states. Keep status words alongside color.
- Use a compact navigation rail and an aligned main column. Prefer dense rows, table/list hybrids, and native `<details>` for optional detail. Keep generous margins around sections without making the data sparse. Avoid bento grids, floating cards, giant KPI figures, gradients, shadows, and decorative icons.
- Use a legible sans serif for prose and monospace with tabular numerals for dates, experiment IDs, settings, and metrics. Start around 17px body text and 15px table text; do not shrink essential data to fit. Use restrained heading sizes and clear section rules.
- The shared `pages/paper-grain.svg` can add faint texture. Preserve contrast and legibility. Use teal text selection, visible keyboard focus, and compact tags and progress marks only where they encode information.

## Diagrams and interaction

- Use the **diagram-design plugin** for a substantive scientific or system diagram if it is available and suits the task. If unavailable, draw with accessible inline SVG or native HTML/CSS. Do not require the plugin or install it solely for a report.
- Label diagram elements and relationships directly; provide a text equivalent or accessible name. Keep line weights, color, and type consistent with the page. Make interactive controls change a meaningful comparison, and explain the selected state in text.
- Prefer semantic HTML and small, local JavaScript. Keep tables horizontally scrollable on narrow screens, convert the sidebar to compact navigation on mobile, and provide a usable print view. Use external libraries only when the report needs them, such as MathJax for equations.
- Make the page survive restrictive viewers (previews that block inline styles or remove empty elements): put all styles in the stylesheet, not in `style` attributes; draw swatches as colored characters (■, or □ for white) with classes, not as empty colored boxes; use native elements such as `<meter>` and `<details>`; draw textures without SVG filters or transparency (for example small dots in colors pre-mixed with the background).

## Before delivery

Check each displayed number, status, date, source link, and derived comparison against its record. Confirm that the page remains readable at desktop and phone widths and that diagrams, tables, and controls remain understandable without color alone.

- When a script edits the page, make each replacement check its anchor and fail if the anchor is missing; a silent miss can remove or skip a whole block of styles.
- Check the structure (balanced tags, unique IDs, every in-page link has a target, every local file exists inside the pages folder) and scan the text for the items in Shareable pages.
- Test the behavior (tabs, addresses, keyboard) and the computed styles (each component and swatch gets its style) with a DOM test such as jsdom; a test of visibility alone does not find lost styles.
- Look at the rendered page in a real browser at desktop and phone widths when one is available. If none is available, say so; do not claim a visual check that was not made.
