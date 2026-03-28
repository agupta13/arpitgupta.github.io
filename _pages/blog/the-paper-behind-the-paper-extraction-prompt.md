---
title: "The Extraction Prompt — Replicate This on Your Own Papers"
permalink: /blogs/the-paper-behind-the-paper-extraction-prompt.html
redirect_from:
  - /blog/the-paper-behind-the-paper-extraction-prompt.html
layout: single
author_profile: true
date: 2026-03-12
---

*Companion to [The Paper Behind the Paper]({{ site.baseurl }}/blogs/the-paper-behind-the-paper.html)*

---

The analysis behind the blog post required extracting and comparing version histories at scale. The prompt below is written for Overleaf projects specifically, but the method generalizes. If your group writes on GitHub — or any version-controlled repository with commit histories and diff access — the same seven-phase structure applies. Replace the Overleaf API calls with `git log`, `git diff`, and file-tree traversal, and the rest of the analysis is identical. The core questions (sentence survival, edit concentration, identity evolution) are properties of the writing process itself — platform-independent.

The prompt is designed to be run with an LLM that has access to browse Overleaf projects. You can paste your own Overleaf project URLs at the end and run the same analysis on your own group's papers.

The prompt produces: (1) a version inventory with character counts for every tex file, (2) sentence-level survival rates between consecutive versions, (3) an edit timeline showing who edited what and when, (4) a catalog of inline feedback markers, and (5) a structural evolution analysis showing how the paper's identity changed across versions.

You can upload the resulting data as a companion to any blog post, course, or workshop where you discuss the writing process.

---

## The Prompt

```
You are a research writing analyst. Your task is to perform a forensic analysis
of the writing process behind research papers by extracting and comparing version
histories from Overleaf projects.

For each Overleaf project URL provided below, perform the following analysis:

═══════════════════════════════════════════════════════════════════════════════════
PHASE 1: PROJECT INVENTORY
═══════════════════════════════════════════════════════════════════════════════════

1. Access the Overleaf project and extract the complete file tree.
   - Use the Overleaf entities API: GET /project/{PROJECT_ID}/entities
   - Download the project zip: GET /project/{PROJECT_ID}/download/zip
   - Extract all .tex files from the zip.

2. For each .tex file, record:
   - File name and path
   - Character count (total characters)
   - Sentence count (approximate, splitting on period-space patterns)
   - Whether the file appears to be a version file (contains v1, v2, v3, rev1,
     _old, _final, or similar version markers in the filename)
   - The section type (intro, background, design/method, evaluation, conclusion,
     appendix, related work)

3. Produce a VERSION INVENTORY TABLE:

   | File | Section Type | Version Tag | Characters | Sentences | Notes |
   |------|-------------|-------------|------------|-----------|-------|

═══════════════════════════════════════════════════════════════════════════════════
PHASE 2: SENTENCE-LEVEL VERSION COMPARISON
═══════════════════════════════════════════════════════════════════════════════════

For each pair of consecutive version files (e.g., intro-v1.tex vs intro-v2.tex,
or section_old.tex vs section_final.tex):

4. Extract all sentences from both versions.

5. Compare sentence by sentence. For each sentence in the EARLIER version,
   classify it as:
   - SURVIVED: Appears verbatim (or with only trivial punctuation changes) in
     the later version
   - MODIFIED: A recognizable descendant exists in the later version (same core
     claim, reworded)
   - REPLACED: No recognizable descendant — the sentence was deleted and new
     content was written

6. Compute:
   - Survival rate: (SURVIVED / total sentences in earlier version) × 100%
   - Modification rate: (MODIFIED / total) × 100%
   - Replacement rate: (REPLACED / total) × 100%

7. Produce a SURVIVAL TABLE:

   | Transition | Sentences (v1) | Survived | Modified | Replaced | Survival % |
   |-----------|----------------|----------|----------|----------|------------|

═══════════════════════════════════════════════════════════════════════════════════
PHASE 3: EDIT TIMELINE AND CONTRIBUTOR ANALYSIS
═══════════════════════════════════════════════════════════════════════════════════

8. From the Overleaf edit history (if accessible) or from file metadata and
   version timestamps, reconstruct:
   - Total edit count per contributor
   - Edit concentration: what percentage of total edits occurred in the final
     14 days before the submission deadline?
   - Writing order during the crunch period: which sections were finalized first,
     second, third?

9. Produce an EDIT TIMELINE TABLE:

   | Contributor | Total Edits | Crunch Edits (final 14 days) | Crunch % |
   |------------|-------------|------------------------------|----------|

   And a WRITING ORDER analysis:
   "During the final crunch, sections were written in this order: [eval] →
   [design] → [intro], based on [evidence]."

═══════════════════════════════════════════════════════════════════════════════════
PHASE 4: FEEDBACK MARKER CATALOG
═══════════════════════════════════════════════════════════════════════════════════

10. Search all .tex files for inline feedback macros. Common patterns include:
    - \advisor{...}, \student{...}, \todo{...}
    - Custom macros like \advisor{...}, \studentA{...}, \studentB{...}, or any \xxxnote{...}
    - LaTeX comments (lines starting with %) that contain feedback language

11. For each marker found, record:
    - The macro name (anonymize if needed: "advisor marker," "student marker")
    - The content of the marker
    - The file and approximate location
    - Classification: framing feedback, technical feedback, structural feedback,
      scope feedback, or logistical feedback

12. Produce a FEEDBACK SUMMARY:

    | Marker Type | Count | Most Common Category | Example (anonymized) |
    |------------|-------|---------------------|---------------------|

═══════════════════════════════════════════════════════════════════════════════════
PHASE 5: IDENTITY EVOLUTION ANALYSIS
═══════════════════════════════════════════════════════════════════════════════════

13. For each version of the introduction (or the main paper file if no separate
    intro exists), extract:
    - The opening sentence
    - The stated contributions (usually a bulleted or numbered list)
    - The title (if it changed between versions)

14. Track identity shifts:
    - Did the paper's core positioning change between versions?
    - How many distinct "identities" did the paper have?
    - At what point did the identity stabilize?

15. Produce an IDENTITY EVOLUTION TABLE:

    | Version | Opening Sentence (first 20 words) | # Contributions | Core Identity |
    |---------|----------------------------------|-----------------|---------------|

═══════════════════════════════════════════════════════════════════════════════════
PHASE 6: CROSS-VERSION STRUCTURAL COMPARISON
═══════════════════════════════════════════════════════════════════════════════════

16. For the earliest and latest versions of the paper, compare:
    - Total character count (expansion or compression?)
    - Section proportions (what percentage of the paper is background vs.
      evaluation vs. method?)
    - Named abstractions: what coined terms appear in the final version that
      were absent in the first?
    - Heading evolution: did section headings change from descriptive
      ("Background") to argumentive ("Why existing approaches fail")?

17. Produce a STRUCTURAL COMPARISON TABLE:

    | Dimension | Earliest Version | Latest Version | Change |
    |-----------|-----------------|----------------|--------|

═══════════════════════════════════════════════════════════════════════════════════
PHASE 7: SYNTHESIS
═══════════════════════════════════════════════════════════════════════════════════

18. Summarize the key findings for this project:
    - Median sentence survival rate across version transitions
    - Total compression ratio (peak size vs. final size)
    - Number of identity shifts
    - Writing order (which section was finalized first/last)
    - Number and nature of feedback markers
    - Any named abstractions that appeared only in the final version

19. Flag any patterns that match these known writing principles:
    - 0% sentence survival between major versions (iterative reconceptualization)
    - Evaluation finalized before introduction (evaluation-first ordering)
    - 30-50% compression in the final pass (expand-then-compress arc)
    - Vague terms replaced by specific named terms (named-over-vague)
    - Section headings evolving from descriptive to argumentative
    - Identity stabilizing before submission (identity resolution)


═══════════════════════════════════════════════════════════════════════════════════
OVERLEAF PROJECT URLS TO ANALYZE
═══════════════════════════════════════════════════════════════════════════════════

Paste your Overleaf project URLs below (one per line). For papers with multiple
submissions, include all project URLs and note which venue each corresponds to.

Project 1: [PASTE OVERLEAF URL HERE]
  - Venue: [e.g., SIGCOMM 2026]
  - Outcome: [e.g., accepted / rejected / under review]
  - Lead student: [optional, for contributor analysis]

Project 2: [PASTE OVERLEAF URL HERE]
  - Venue:
  - Outcome:
  - Lead student:

Project 3: [PASTE OVERLEAF URL HERE]
  - Venue:
  - Outcome:
  - Lead student:

(Add as many projects as needed.)
```

---

## What the Prompt Produces

For each project, you get a structured dataset: version inventories, sentence survival rates, edit timelines, feedback catalogs, and identity evolution traces. Across multiple projects, cross-paper patterns emerge — the same patterns described in the blog post. The threshold I used: a pattern must appear in at least two papers with different lead authors to qualify as a group-level finding rather than a student-specific habit.

The data from my own analysis — anonymized and aggregated — is available as a companion file [here]. If you run this on your own projects, I want to hear whether the patterns replicate. The 0% survival rate, the expansion-compression arc, the identity stability association — these may be properties of my group's writing process, or they may be structural features of how research papers get written. More data points will tell.
