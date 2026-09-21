# Publications backlog

Open gaps in `_data/publications.yml` and the CV bibliography, found during the
2026-09-16 audit (arXiv sweep + CV-bib diff + acceptance-mail check). Deferred —
nothing here is blocking, but each item is either a dead link on the live site or
a paper that exists somewhere and is missing somewhere else.

## 1. Publications with no URL (render as dead links)

These render as `<a href="">Title</a>` on the Publications page — clickable, goes
nowhere. All were added on title/venue at acceptance time, before a PDF existed.

| id | Paper | Venue |
|---|---|---|
| `sigcse27-experiential-learning` | Facilitating Experiential Learning in Networking Education | SIGCSE TS 2027 |
| `ntcr-loom` | NetReplica: A Bottleneck-Regime Substrate for Reproducible Network Data Generation | NTC-R 2026 |
| `ntcr-rethinking-nfm` | Rethinking Network Foundation Models: From Bigger Models to Better Data | NTC-R 2026 |
| `tprc26-affordability-convex` | From Measurement to Policy Design (BQT+ convex optimization) | TPRC 2026 |
| `prime-early-termination` | The Policy Implications of Early Termination in Internet Speed Testing | IMC PRIME '25 |

Fix: add `url:` (arXiv `/abs/` or a PDF under `pdfs/`) for each.

## 2. In the CV but never on the site

- **`stbias`** — "Analyzing Disparity and Temporal Progression of Internet Quality
  through Crowdsourced Measurements with Bias-Correction", arXiv:2310.16136
  (Lee, Paul, Gupta, Belding, Gu; 2023). Listed in `\nocitepreprints` in `cv.tex`,
  absent from `publications.yml`.

## 3. On the site but never in the CV

- **Pramana** — "Pramana: A Composable, Domain-Specific Backend for Empirical
  Networking Research", arXiv:2607.26352 (Jul 2026). Added to the site as a
  preprint; no entry in `cv/publications.bib`. `cv.tex` mentions the name only in
  student-assignment lines (Srish Nigam, Sthanav Murali).
- Also not linked from `_pages/research.md`, unlike the other named systems.

## 4. Naming — NetReplica and Loom

**Current decision (2026-09-21): Loom stays a separate artifact for now.**
The NTC-R paper keeps the name Loom; the arXiv paper is NetReplica. Two names,
two artifacts — this supersedes the 2026-09-16 "one name in the public domain"
position, which had briefly renamed the NTC-R paper to NetReplica.

History, because it explains the state of things:

- 2026-09-16 — arXiv 2507.13476 was found retitled to **NetForge** in v3. Arpit:
  an alias is fine for a blind submission, but the public arXiv release must not
  fork the name. Site and CV were set to NetReplica for both papers.
- Jaber's counterpoint, still worth keeping: reviewers found "Replica" confusing,
  since the system *generates* bottleneck regimes rather than replaying captured
  traffic. That objection has not gone away.
- 2026-09-17 — Jaber retitled arXiv to **NetReplica** (v4), abstract included.
  That half is settled and correct.
- 2026-09-17 — Jaber emailed the NTC-R chairs asking to rename the paper to
  NetReplica. **Given the 2026-09-21 decision, that request should be withdrawn**
  so the camera-ready stays Loom. Not yet confirmed either way.

| Where | Name | State |
|---|---|---|
| arXiv 2507.13476 | NetReplica (v4, 2026-09-17) | ✅ settled |
| NTC-R paper | Loom | ✅ site + CV reverted 2026-09-21 |
| GitHub repo | `SNL-UCSB/netforge` | left alone — renaming breaks links |

Keeping the two names also resolves what was a real problem while both were
called NetReplica: the titles were near-identical
("A Programmable Substrate for Bottleneck-Centric Network Data Generation" vs
"A Bottleneck-Regime Substrate for Reproducible Network Data Generation") and
read as duplicates on the Publications page.

They are genuinely different papers — arXiv argues a data-generation substrate
built on Cross-Traffic Profiles, evaluated via an ABR case study (47% gain on
Fugu); NTC-R argues experiments run at the level of *executions, not regimes*,
evidenced by a 66-paper corpus audit (255/387 experiments) and a
congestion-control-classifier reproduction.

If the one-name position is revisited later, the NTC-R subtitle should carry its
own reframing rather than restating the arXiv one.

## 5. Smaller items

- `netburst` uses `https://www.arxiv.org/pdf/...` — the only `www.arxiv.org` URL
  in the file; everything else is bare `arxiv.org`.
- `ntcr-loom` is now a misleading id (the paper is no longer called Loom). Renaming
  it cascades into three students' `papers:` lists in `students.yml`.
- **Biobib** (`~/Projects/misc/biobib`) not updated for any of the 2026-09-16
  additions: 3 IMC PRIME '25 workshop papers, 3 preprints (Pramana, Multifractal,
  BQT+), the PFFP congressional staff briefing, and the NetReplica renames. That
  repo has its own decision log (`DECISIONS_LOG_2026-09-14.md`,
  `FINAL_ENTRY_DECISIONS.md`) — work through those conventions rather than
  bulk-adding.

## 6. Gotcha, already fixed — don't regress

`_includes/venue_display.html` normalizes venues by substring. A venue containing
`"co-located with ACM IMC"` used to match a generic `contains "IMC"` branch and
render as plain **"ACM IMC"**, silently promoting the three PRIME workshop talks
to main-conference papers. Fixed by matching `PRIME` first (commit `7fbc2ec`).

The same trap applies to any future workshop whose venue string names the
conference it is co-located with. The NTC-R papers are safe only because no
top-level CoNEXT branch exists yet.

## Audit method (to re-run)

`scratchpad/arxiv_sweep.py` queries the arXiv API per group-member surname, keeps
hits with an exact `Arpit Gupta` author and ≤25 authors submitted 2024+, and diffs
against arXiv ids found in `publications.yml` + `_pages/*.md`. The 2024 cutoff is
why `stbias` (2023) surfaced only via the CV-bib diff — widen it to catch older
preprints the CV does not track either.
