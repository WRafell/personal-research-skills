---
name: asd-ste100
description: Apply ASD-STE100 Simplified Technical English principles to technical documentation. Use explicitly when the user asks to write, rewrite, review, simplify, or check technical text according to ASD-STE100 / Simplified Technical English (STE).
version: 1.0
---

# ASD-STE100 Simplified Technical English

## Purpose

Use this skill to write or revise technical documentation so that it follows the principles of **ASD-STE100 Simplified Technical English (STE)**.

The primary goals are:

- Make technical text clear and unambiguous.
- Use one word for one meaning whenever possible.
- Use short, direct sentence structures.
- Reduce vocabulary and grammatical variation.
- Make instructions easy to understand for international readers.
- Preserve the exact technical meaning of the source text.

This skill is an operational guide for an AI agent. It is **not a replacement for the official ASD-STE100 standard**. For formal compliance, use the current official standard, the applicable project terminology, and human technical review.

The current official reference is **ASD-STE100, Issue 9 (2025)** unless the user or project specifies another issue.

---

# 1. Activation

Apply this skill only when the user explicitly asks for one of the following:

- ASD-STE100
- Simplified Technical English
- STE-compliant writing
- STE review
- STE rewrite
- STE terminology check

Do not automatically apply STE to ordinary academic, business, conversational, or creative writing.

When this skill is active, prioritize STE rules over stylistic elegance.

---

# 2. Core Principle

Always optimize for the reader, not for the writer.

The preferred text is:

> technically correct + explicit + concise + structurally simple + difficult to misinterpret

Do not make a sentence more elegant if this makes it less precise.

Do not change the technical meaning to obtain simpler language.

If simplification and technical accuracy conflict, preserve technical accuracy and flag the problem.

---

# 3. Source of Authority

Use the following order of authority:

1. The technical facts and safety requirements of the source material.
2. The current official ASD-STE100 standard.
3. The project's approved terminology or terminology database.
4. Company or industry technical nouns and technical verbs.
5. This skill.

If this skill conflicts with the official standard, the official standard wins.

Do not claim that text is "ASD-STE100 compliant" unless the vocabulary and applicable rules have been checked against the official standard and project terminology.

If a complete lexical check is not possible, say:

> Revised according to ASD-STE100 principles; vocabulary compliance was not fully verified against the official dictionary.

---

# 4. Vocabulary Rules

## 4.1 Prefer approved STE vocabulary

Use words from the ASD-STE100 controlled dictionary when possible.

Use an approved word only:

- with its approved meaning;
- as its approved part of speech;
- in an approved grammatical form.

Do not assume that a familiar English word is permitted in every meaning or grammatical role.

Example principle:

- Prefer **start** when STE specifies it for the intended meaning.
- Avoid unnecessary synonyms such as *commence*, *initiate*, or *begin* when the approved term is **start**.

## 4.2 Use one term for one concept

After you select a technical term, use the same term throughout the document.

Do not alternate synonyms for style.

Bad:

- device
- unit
- equipment
- apparatus

if all four refer to the same item.

Better:

- Use the approved technical noun consistently, for example **unit**.

## 4.3 Technical nouns

A word that is not in the STE dictionary can be necessary as a technical noun.

Use technical nouns for:

- components;
- materials;
- systems;
- tools;
- locations;
- documents;
- technical concepts;
- domain-specific items.

Use technical nouns that are accepted in the applicable company, industry, product, or subject field.

Prefer technical nouns that are short, precise, and familiar to the intended reader.

Do not invent unnecessary synonyms for technical nouns.

Do not use slang, informal terminology, or local jargon unless it is an officially approved technical term.

## 4.4 Technical verbs

Use a domain-specific technical verb only when it is necessary and accepted in the applicable field or project terminology.

Use technical verbs consistently.

Do not convert technical verbs into nouns merely for stylistic variation.

## 4.5 American English spelling

Use American English spelling unless the project has an official requirement to use another spelling convention.

Examples:

- color, not colour
- center, not centre

Do not alter official product names, trademarks, identifiers, quoted text, or source-code elements.

---

# 5. Sentence Construction

## 5.1 Write short sentences

Prefer one main idea per sentence.

Split a sentence when it contains multiple independent actions, conditions, results, or explanations.

As an agent heuristic:

- Aim for approximately 20 words or fewer in procedural sentences when practical.
- Aim for approximately 25 words or fewer in descriptive sentences when practical.

These are working heuristics, not a substitute for the exact limits and exceptions in the applicable ASD-STE100 issue.

## 5.2 Use simple sentence structure

Prefer:

**subject + verb + object**

Example:

> The controller sends the signal to the actuator.

Avoid unnecessary embedding, long subordinate structures, and distant dependencies.

Bad:

> The controller, which receives information from the sensor that is installed near the valve, subsequently sends a signal to the actuator.

Better:

> The sensor is near the valve. The controller receives data from the sensor. The controller then sends a signal to the actuator.

## 5.3 State actions directly

In procedures, tell the reader exactly what to do.

Prefer the imperative form.

Example:

> Remove the cover.

Avoid:

> The cover should then be removed.

## 5.4 Avoid passive voice in procedural instructions

Use active voice for actions that the reader must perform.

Bad:

> The valve must be closed.

Better:

> Close the valve.

Passive voice can be acceptable in descriptive text when the actor is unknown, irrelevant, or not necessary for understanding. Use it only when it improves technical clarity and the applicable STE rule permits it.

## 5.5 Put conditions before actions

When an action depends on a condition, state the condition first when practical.

Better:

> If the pressure is more than 50 psi, close the valve.

Avoid making the reader perform an action before discovering the condition that controls it.

## 5.6 Make references explicit

Avoid vague pronouns when the antecedent can be unclear.

Bad:

> Remove the filter from the housing and clean it.

Ambiguous: What does *it* refer to?

Better:

> Remove the filter from the housing. Clean the filter.

Use the technical noun again when repetition improves clarity.

---

# 6. Verb Rules

## 6.1 Prefer simple verb forms

Use the simplest tense that accurately expresses the meaning.

Prefer simple present for descriptions and general technical facts.

Example:

> The pump supplies fuel to the engine.

Use imperative verbs for procedural steps.

Example:

> Disconnect the cable.

## 6.2 Avoid unnecessary continuous forms

Do not use an **-ing** form when a simpler approved construction communicates the same meaning.

Bad:

> Before removing the panel, disconnect the power supply.

Prefer a direct condition or instruction structure when appropriate:

> Before you remove the panel, disconnect the power supply.

or split the sequence:

> Disconnect the power supply. Then remove the panel.

Do not mechanically remove all **-ing** forms. Check the official rule and the grammatical function before changing the text.

## 6.3 Avoid nominalization when a direct verb is clearer

Bad:

> Perform an inspection of the cable.

Better, if the approved vocabulary permits it:

> Inspect the cable.

Do not apply this transformation if the resulting verb is not approved or if it changes the technical meaning.

---

# 7. Procedure Rules

For procedural text:

1. Give one primary action per step when practical.
2. Put required conditions before the action.
3. Put warnings and cautions before the action that creates the hazard.
4. Use imperative verbs for reader actions.
5. Specify the object of the action.
6. Specify limits, values, locations, and tools when necessary.
7. Put actions in the order in which the reader must do them.
8. Do not hide an action inside descriptive text.
9. Do not combine optional and mandatory actions ambiguously.
10. Keep consequences close to the action or condition that causes them.

Example:

Bad:

> After checking that the power is disconnected, the cover should be carefully removed so that damage to the wiring does not occur.

Better:

> Make sure that the power is off.
> Remove the cover carefully.
> Do not damage the wires.

---

# 8. Descriptive Text Rules

For descriptive or explanatory technical text:

- State one main topic per paragraph.
- Put the main idea first.
- Keep related information together.
- Prefer explicit logical connections.
- Avoid rhetorical language.
- Avoid metaphors unless they are established technical terms.
- Avoid unnecessary adjectives and adverbs.
- Avoid subjective words such as *easy*, *obvious*, *clearly*, *simply*, or *very* unless technically necessary.
- Do not use stylistic variation as a goal.

Bad:

> The highly sophisticated controller seamlessly manages a wide variety of different operational conditions.

Better:

> The controller controls the system in different operating conditions.

---

# 9. Ambiguity Control

Actively search for ambiguity.

Check:

- pronouns with multiple possible antecedents;
- modifiers that can attach to more than one phrase;
- words with multiple meanings;
- omitted subjects;
- omitted objects;
- unclear sequence;
- unclear scope of a condition;
- unclear scope of a warning;
- unclear units;
- unclear references such as *above*, *below*, *previous*, *following*, *former*, or *latter*;
- inconsistent component names;
- inconsistent abbreviations;
- unexplained acronyms.

When ambiguity exists, repeat the technical noun instead of relying on a pronoun.

---

# 10. Numbers, Units, and Data

Preserve technical values exactly unless the user asks for conversion.

Do not silently change:

- quantities;
- tolerances;
- ranges;
- dimensions;
- units;
- part numbers;
- model numbers;
- software versions;
- commands;
- filenames;
- parameter names;
- variable names;
- equations;
- identifiers.

Use consistent number and unit formatting throughout the document.

If a conversion is necessary, keep the original value when required for traceability.

---

# 11. Abbreviations and Acronyms

Use only abbreviations that the intended reader can identify or that the project permits.

At first occurrence, give the full term unless the abbreviation is universally accepted in the applicable document set or the project rules state otherwise.

Example:

> Use the flight control computer (FCC) to do the test.

Then use **FCC** consistently.

Do not create multiple abbreviations for the same term.

---

# 12. Warnings, Cautions, and Safety Text

Never simplify safety text in a way that changes its meaning, severity, scope, trigger, or required action.

When revising safety information:

- preserve the hazard;
- preserve the condition that creates the hazard;
- preserve the consequence;
- preserve the required preventive action;
- preserve mandatory terminology required by the user's organization or standard.

Do not rewrite standardized warning or caution text when the governing documentation rules prohibit changes.

If compliance conflicts with approved safety wording, keep the approved safety wording and flag the conflict.

---

# 13. Formatting Principles

Use formatting to make information easy to scan.

Prefer:

- numbered steps for procedures;
- bullets for independent facts or requirements;
- tables for structured comparisons or repeated data;
- headings that identify the actual subject;
- notes only when the information is supplementary.

Do not use formatting to compensate for unclear sentences.

Keep each procedural step self-contained enough that the reader knows what action to perform.

---

# 14. Agent Rewrite Workflow

When the user asks you to rewrite text in STE, use this sequence.

## Step 1 — Preserve meaning

Identify:

- required actions;
- technical facts;
- conditions;
- limits;
- hazards;
- sequence;
- technical nouns;
- technical verbs;
- project-specific terminology.

Do not rewrite until you understand these elements.

## Step 2 — Build a terminology map

Create an internal mapping of concepts to preferred terms.

Example:

| Concept | Preferred term |
|---|---|
| equipment enclosure | housing |
| electrical connector | connector |
| removal action | remove |

Use one preferred term for each concept.

Do not show this table unless it helps the user.

## Step 3 — Simplify structure

For each sentence:

- identify the main action or statement;
- remove unnecessary subordinate clauses;
- split multiple ideas;
- make the subject explicit;
- make the object explicit;
- put conditions before dependent actions;
- change procedural actions to imperative voice.

## Step 4 — Control vocabulary

Check each important content word.

Classify it as:

- approved STE word;
- technical noun;
- technical verb;
- proper name;
- symbol or identifier;
- potentially unapproved vocabulary.

Replace potentially unapproved vocabulary when a verified approved alternative is available.

Never invent an STE-approved alternative from memory when lexical certainty is important.

## Step 5 — Check consistency

Check terminology, abbreviations, units, capitalization, and repeated references.

## Step 6 — Check ambiguity

Ask internally:

- Can a sentence have two meanings?
- Can a pronoun refer to more than one item?
- Can the reader misunderstand the action order?
- Can the scope of a condition be unclear?
- Can a warning be associated with the wrong step?

If yes, rewrite.

## Step 7 — Final compliance pass

Use the checklist in Section 17.

---

# 15. Review Mode

When the user asks for an STE review instead of a rewrite, do not silently rewrite the entire text unless requested.

Classify findings by severity:

### ERROR
A likely violation that can cause ambiguity, incorrect interpretation, or conflict with a core STE rule.

### WARNING
A construction that is probably not preferred in STE or requires verification against the official standard or dictionary.

### CONSISTENCY
A terminology, abbreviation, spelling, or formatting inconsistency.

### TECHNICAL CHECK
A sentence that cannot be safely revised without domain knowledge.

For each finding, provide:

- original text;
- problem;
- proposed revision;
- reason.

If the user requests only the corrected version, output only the corrected version plus any critical unresolved technical questions.

---

# 16. Do Not Do These Things

Do not:

- change technical meaning for readability;
- invent missing technical information;
- replace exact technical terminology with a vague common word;
- use synonyms only to avoid repetition;
- make procedures sound conversational;
- add rhetorical flourishes;
- add politeness words to procedural steps;
- use idioms;
- use slang;
- use humor in safety-critical instructions;
- use vague words such as *thing*, *stuff*, *somehow*, or *etc.* when exact information is available;
- hide uncertainty;
- claim formal STE compliance without sufficient verification.

---

# 17. Compliance Checklist

Before you return STE text, check all applicable items.

## Meaning

- [ ] The technical meaning is unchanged.
- [ ] No required action is missing.
- [ ] No condition, limit, hazard, or consequence is missing.
- [ ] Values, identifiers, and units are unchanged unless intentionally converted.

## Vocabulary

- [ ] One term is used for one concept.
- [ ] Approved STE vocabulary is used when verified and applicable.
- [ ] Technical nouns are necessary, precise, and consistent.
- [ ] Technical verbs are necessary and consistent.
- [ ] Words are not used in an uncertain STE meaning when lexical compliance is claimed.
- [ ] American English spelling is used unless another convention is required.

## Sentences

- [ ] Sentences contain one main idea when practical.
- [ ] Sentence structure is direct.
- [ ] Subjects and objects are explicit.
- [ ] Conditions are placed before dependent actions when practical.
- [ ] Procedural actions use the imperative form.
- [ ] Passive voice is not used unnecessarily in procedures.
- [ ] Unnecessary **-ing** constructions are removed or rewritten when appropriate.

## Ambiguity

- [ ] Pronouns have only one possible antecedent.
- [ ] Action sequence is clear.
- [ ] Condition scope is clear.
- [ ] Warning/caution scope is clear.
- [ ] References are explicit.

## Consistency

- [ ] Technical terms are consistent.
- [ ] Abbreviations are consistent.
- [ ] Units and number formats are consistent.
- [ ] Capitalization is consistent.

## Readability

- [ ] Paragraphs are short and focused.
- [ ] Procedures are in chronological order.
- [ ] Lists are used where they improve clarity.
- [ ] Decorative or rhetorical language is removed.

---

# 18. Output Modes

Use the output mode that best matches the request.

## Rewrite mode

Return the complete revised STE text.

Do not give a long explanation unless the user asks for one.

## Review mode

Return findings and recommended corrections.

Use a compact table when there are many findings.

## Strict mode

When the user asks for **strict ASD-STE100 compliance**:

1. Do not rely only on general STE principles.
2. Verify vocabulary against the applicable ASD-STE100 dictionary when the standard is available.
3. Check the applicable writing rules.
4. Check project-specific technical nouns and verbs.
5. Flag all items that cannot be verified.
6. Do not certify compliance unless the required references are available.

## Light mode

When the user asks to "make this more like STE" or "simplify using STE principles," apply the structural and vocabulary principles without claiming formal compliance.

---

# 19. Recommended Response Labels

When useful, use one of these labels:

- **STE rewrite** — when you rewrote the text.
- **STE review** — when you identified issues without fully replacing the text.
- **STE-principles rewrite** — when the official dictionary was not fully checked.
- **Requires terminology verification** — when project-specific or dictionary status is uncertain.

Do not add these labels when the user requests clean output only.

---

# 20. Examples

## Example 1 — Procedure

Original:

> Prior to commencing the removal of the access panel, it should be ensured that electrical power has been disconnected.

Preferred STE-style revision:

> Make sure that the electrical power is off. Then remove the access panel.

Why:

- shorter structure;
- direct action;
- no unnecessary passive construction;
- condition before dependent action;
- simpler vocabulary.

## Example 2 — Ambiguous pronoun

Original:

> Remove the sensor from the bracket and inspect it for damage.

Problem:

*It* can refer to the sensor or the bracket.

Preferred revision, if the sensor is the intended object:

> Remove the sensor from the bracket. Inspect the sensor for damage.

## Example 3 — Excessive synonyms

Original:

> The operator starts the pump. After the unit begins operation, monitor the device.

Preferred revision if all terms refer to the pump:

> Start the pump. When the pump operates, monitor the pump.

## Example 4 — Long descriptive sentence

Original:

> The control module, which receives pressure data from several sensors installed throughout the system, automatically adjusts the valve position when pressure variations occur.

Preferred revision:

> Several sensors measure the system pressure. The control module receives data from the sensors. If the pressure changes, the control module adjusts the valve position.

---

# 21. Agent Decision Rule

When uncertain, choose the version that has:

1. less ambiguity;
2. fewer meanings per word;
3. fewer concepts per sentence;
4. more explicit subjects and objects;
5. more consistent terminology;
6. the same technical meaning.

If uncertainty remains because of missing technical knowledge, do not guess. Mark the sentence for technical review.

---

# 22. Formal Compliance Notice

ASD-STE100 is a controlled natural language standard with both writing rules and a controlled dictionary. Correct application requires technical knowledge, linguistic judgment, and the applicable official reference.

An AI agent can assist with drafting, checking, and rewriting, but a plausible STE-style result is not automatically proof of formal ASD-STE100 compliance.

For safety-critical, regulated, contractual, aerospace, defense, maintenance, or certification documentation, require qualified human review before publication.
