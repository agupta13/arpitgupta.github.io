---
title: "The Paper Behind the Paper"
permalink: /blogs/the-paper-behind-the-paper.html
redirect_from:
  - /blog/the-paper-behind-the-paper.html
layout: single
author_profile: true
date: 2026-03-12
---

Every research paper has a shadow — the paper behind the paper. The published version gets cited and discussed. The shadow — the version histories, the abandoned drafts, the late-night rewrites, the feedback that changed everything — disappears the moment the camera-ready PDF ships. We keep the product and discard the process that made it.

Over the past few days, I did something I had been meaning to do for years. I took the full version histories of six research papers from my group — spanning five venues, eight total submissions, and over 7,600 tracked edits — and treated the writing process itself as data. I reconstructed every version, compared them sentence by sentence, cataloged every inline feedback marker, and tracked how each paper's identity evolved from first draft to final submission.

The central pattern in the data is this: research writing is primarily the iterative discovery of the right abstraction for the work, and only secondarily the refinement of prose. The patterns below — the ones that most consistently tracked paper outcomes in this sample — come from what the version histories show rather than what style guides prescribe. The longer first part is for graduate students; the shorter second part is a self-reflection on mentoring, written with the honesty that comes from reading your own editing patterns at scale. Everything is anonymized — papers are labeled A through F, students by role.

---

## The Dataset: Version Histories as a Research Instrument

Before findings, the method — because any group that uses version control for writing can replicate this analysis on their own projects, and the act of doing it is itself revealing.

Our group writes in Overleaf, which stores a complete edit history for every project — every keystroke, every save, every collaborator session. For each of the six papers, I extracted four categories of data.

**Version files.** Most of our papers use explicit version naming — `intro-v1.tex`, `intro-v2.tex`, `intro-v3.tex`, or suffixes that tag senior-author edits as distinct from student drafts. These are the fossils of the writing process. Each file is a snapshot of what the authors thought the paper should say at a given moment.

**Edit logs.** Overleaf's history view shows who edited what and when. I reconstructed timelines: which sections were written first, when the crunch started, how edits concentrated around deadlines.

**Feedback markers.** Our group uses inline LaTeX macros for feedback — things like `\advisor{this needs a stronger claim}` or `\student{should we include the ablation?}`. These conversations shape every decision in the final paper — and vanish from it entirely.

**Reviewer feedback.** For papers that went through peer review, I matched reviewer concerns to the specific sections and framing decisions they targeted.

Then I did sentence-level comparison across consecutive version files. For every pair — say, `intro-v2` vs. `intro-v3` — I compared each sentence to determine whether it survived, was modified, or was replaced entirely. The survival rate tells you whether a revision was a polish or a rethinking. I used an LLM to help with the sentence-level diffing and pattern extraction, which made the process feasible at scale. The core method is accessible to anyone willing to spend a weekend reading their own old drafts carefully. A companion document provides the exact extraction prompt so you can run this on your own projects.

The complete dataset:

| Metric | Value |
|--------|-------|
| Papers analyzed | 6 |
| Total submissions (including resubmissions) | 8 |
| Overleaf edits tracked | 7,600+ |
| Tex file versions compared | 100+ |
| Feedback markers cataloged | 80+ |
| Venues | 5 (across systems and ML) |
| Timeline span | 2+ years |
| Outcomes | 3 accepted, 1 rejected, 2 under review |

Any group using Overleaf — or GitHub, or any version-controlled writing workflow — has this data sitting in their project histories right now.

A caveat before the findings: six papers from a single research group, with one senior author's editorial style baked into every trajectory. The patterns below are strong and consistent across the sample, but they are hypotheses worth testing on other groups' data, not universal laws of research writing. The companion extraction prompt exists precisely so others can run the same analysis and see what replicates.

---

## Pillar 1: Identity Stability Tracks Acceptance

The strongest finding, and the one with the most consequence for students.

Across the dataset, **papers that had a stable identity before submission were accepted. Papers whose identity was still in flux at submission time were rejected.** In this small sample, the association was unusually strong.

An "identity crisis" is when a paper fundamentally changes what it claims to be about — a wholesale shift in the paper's core positioning. "We built a system for X" becomes "We discovered Y" becomes "We propose a framework for Z."

| Paper | Identity Shifts Before Submission | Resolved? | Outcome |
|-------|-----------------------------------|-----------|---------|
| Paper D | 0 (stable from start) | N/A | Accepted |
| Paper E | 1 (modest) | Yes | Accepted |
| Paper A | 3 (significant) | Yes — resolved in final 4 days | Accepted |
| Paper F | 1 (shift, but gap remained) | Partially | Rejected |
| Paper B | 3 (one per venue) | Still evolving at each submission | Rejected twice |

Paper A is instructive. It went through three identity crises — from survey to framework to systems paper — and all three were resolved before submission. Paper B had three identity shifts too, but each was triggered by a rejection rather than resolved proactively. At each submission point, the paper was still under construction.

Reviewers detect unresolved identity crises even when they lack the vocabulary for the diagnosis. The symptoms appear as "the paper tries to do too much," "the framing is unclear," "the contribution is hard to pin down." These are symptoms of a paper that has yet to find what it is.

Two secondary patterns help explain why identity crises persist. The data reveals a consistent writing order during the final crunch: **evaluation → design → introduction.** The final introduction — the one that ships — gets written last, after the evaluation is settled, because the introduction makes promises ("we show X, we achieve Y") and those promises can only be honest when the authors already know exactly what the evaluation delivers. Papers that submitted with an introduction still in scaffold mode — making promises it could not yet keep — got into trouble. Paper F's introduction promised breadth ("across domains, from finance to healthcare") while the evaluation delivered results on a single domain. Reviewers flagged "narrow applicability." Paper B's first submission promised "domain adaptation" while the evaluation delivered infrastructure. The introduction had outrun the evidence — another symptom of unresolved identity.

A deeper pattern from the data: measurement papers ("what we found") have naturally stable identities because the research questions provide structure. Systems papers ("what we built") must *discover* their identity through writing — the contribution has to be constructed by finding the right abstraction level for the actual technical work. This means systems papers inherently require more writing iterations. In this sample, every systems-paper introduction required multiple full rewrites before stabilizing.

> **The clearest pattern in this dataset:** Identity stability at submission time tracked acceptance more closely than any other variable I measured. Resolve the identity crisis before investing in anything else — everything downstream depends on it.

---

## Pillar 2: Framing Is the Highest-Repair-Cost Mistake

Pillar 1 established the outcome: papers with stable identities got accepted; papers still searching got rejected. The next question is *how* identity gets discovered — and in this data, the answer is framing.

The single most striking number in the dataset: **the median sentence survival rate between major versions is 0%.** When a section goes from version 2 to version 3, essentially zero sentences from v2 appear in v3.

| Paper | Section Transition | Survival Rate |
|-------|-------------------|---------------|
| Paper A | intro v2 → v3 | ~0% |
| Paper A | eval v1 → v2 → v3 | 0% at each step |
| Paper B | intro across 7 versions | ~0% per transition |
| Paper C | system design: student → senior edit | 0% (0 of 54 sentences) |
| Paper C | background: student → senior edit | 3% (3 of 89) |
| Paper D | intro v1 → v2 | ~0% |
| Paper E | framework v1 → v2 | 5% (3 of 55) |
| Paper F | intro v1 → final | 0% (0 of 18) |

Why does the survival rate collapse? Because major revisions are framing changes — and framing changes rewrite everything. The old prose is reference material. The new version is constructed from scratch. Writing is iterative rethinking, and framing is the variable that triggers each cycle.

The finding challenged my own self-image. I had always thought of my editing as sharpening student drafts. What I actually do — what the version histories prove — is absorb the student's evidence and intent and write an entirely new version. The student's draft is essential: it contains the raw material and the reasoning that makes the rewrite possible. But the rewrite itself is where the narrative gets constructed, and it is almost always a framing change.

Reviewer feedback across all papers confirms the same hierarchy from a different angle:

| Concern Type | Severity | What It Means |
|-------------|----------|---------------|
| **Framing** | Most damaging | Reviewers struggle to identify the contribution |
| **Design** | Damaging | The technical contribution has a flaw |
| **Scope** | Manageable | Clear paper, reviewers want more evidence |
| **Rigor** | Most manageable | Sound paper, needs calibration |

Paper B was rejected twice with framing concerns ("elusive writing," "unclear delta"). Paper A was accepted despite scope concerns ("limited evaluation"). Framing problems require rethinking the paper's identity — the kind of change that produces 0% sentence survival. Scope problems require adding an experiment to an existing framework. The gap in repair cost is enormous, and most students invest their anxiety on the wrong side of it.

> **Where students invest:** scope. **Where this data points:** framing. Every framing change produces 0% sentence survival — that is the repair cost of getting framing wrong late. Getting it right early is the strongest writing-side signal in this dataset.

**The concrete test:** Show your introduction to someone outside your subfield and ask them to state, in one sentence, what the paper contributes. If their answer misses yours, or diverges from it, you have a framing problem — and that is more valuable to fix than any amount of evaluation polishing.

---

## Pillar 3: Expand First, Compress Later

If framing instability is the costliest mistake, premature compression is its most common partner. Every paper in the dataset follows the same arc: the draft gets longer before it gets shorter.

| Paper | Section | Peak → Final | Compression |
|-------|---------|-------------|-------------|
| Paper A | Middle sections | 95K → 59K chars | 38% |
| Paper B | Background | 57K → 19.5K chars | 65% |
| Paper C | Background | 89 → 42 sentences | 53% |
| Paper F | Method | 25K → 11K chars | 56% |

The normal range is 30–50% compression in the final pass. Paper B's 65% represents crisis compression — cutting material because the framing changed fundamentally between venues.

The mistake that costs the most time: compressing before the framing stabilizes. A student sees a page limit, gets anxious about length, and starts cutting from the first draft. Compression before identity resolution means cutting blind — the framing has yet to reveal what matters. The discipline is to stay in expansion mode until the identity is stable, then switch. The question changes from "what should I include?" to "what can I remove while preserving the argument?"

> **The takeaway:** Compression before identity resolution means cutting blind. After every paragraph in a final pass, ask: does this serve one of the paper's explicit claims? A paragraph may be interesting, well-written, and true — and still earn deletion if it serves zero claims.

---

## Pillar 4: Naming Is How Contributions Become Legible

Across every paper in the dataset, a consistent edit pattern: vague terms get replaced by specific ones. This is the single most frequent operation in revision histories, observed at every maturity level.

| Before (student draft) | After (final version) |
|------------------------|----------------------|
| "heuristics" | Four named algorithms with version-specific thresholds |
| "data-driven approach" | "two-stage ML framework with configurable accuracy-cost trade-off" |
| "evaluation framework" | A capitalized proper name that became the paper's citable contribution |
| "problem formulation" | Two coined terms, each naming a specific technical operation |
| "data generation" | Two named processes describing distinct pipeline stages |

The operation works at two levels. Existing concepts must be named specifically — write the four specific methods, the three specific metrics, the two specific systems. And novel contributions must be named — a proper term that becomes citable.

A pattern in the data: the key named abstractions that define each paper always appear in the *final* version, not the first. In every case, the term that became the paper's citable contribution — the phrase reviewers would later quote back — was discovered through writing, during the back-and-forth between results and story, usually in the final compression pass when the authors finally understood what the paper's core insight was.

**The test:** If a phrase could describe any paper in your field, it belongs in someone else's paper. "Novel data-driven approach" matches thousands of papers. The named abstraction that captures your specific insight matches exactly one.

> **The takeaway:** Specificity is the most frequent edit operation in every revision history. Name the four methods, name the core abstraction, replace every phrase that could describe any paper in the field.

---

## Pillar 5: Rejection Forces Abstraction

Paper B's journey — three different venues, rejected from the first two, under review at the third — is the most instructive trajectory in the dataset. The system itself barely changed between submissions. The argument for why it matters changed completely.

| Submission | Opening Frame | Core Change |
|-----------|---------------|-------------|
| Venue 1 (rejected) | "Recent advances in [technique] are transforming..." | Led with technique novelty; 12K chars of formal math |
| Venue 2 (rejected) | "Operational bottlenecks in [domain]..." | Cut the math; led with the practical problem |
| Venue 3 (under review) | "[Specific domain phenomenon] at [specific infrastructure]..." | Led with domain insight; background compressed 65% |

Each rejection forced the authors to find a higher level of abstraction. The paper went from technical novelty to operational need to fundamental insight. Edit intensity decreased 14× across submissions — from 92 edits/day to 7 — because the evidence was stable. Only the framing needed revision.

A reviewer who writes "the contribution is unclear" is saying the argument for why the work matters has yet to find the right altitude. The research may be sound. The story has yet to reach the level at which it communicates. The productive response is to rethink the framing at a higher level — the kind of change that feels like starting over but actually keeps the technical work intact while repositioning it.

> **The takeaway:** Each rejection is a signal to find a higher abstraction level. The technical work stays. The argument for why it matters must climb until it reaches the altitude at which it communicates.

---

> **The five patterns compress to one question:** Does the paper know what it is? Identity stability, framing cost, the expand-compress arc, naming, rejection as abstraction — each is a different lens on the same underlying variable. A paper that knows what it is can withstand narrower evaluation than students often fear. A paper still searching for its identity will struggle even when the technical work is strong.

---

## What Students Can Do From the First Draft

*If you are a graduate student reading this: what can you act on before your next deadline?*

Three habits follow directly from the data.

**Stress-test identity early.** Write three different one-paragraph summaries of what the paper is about. If they diverge, the paper has an identity crisis — and resolving it is worth more than any amount of sentence-level revision. Once the identity is stable, write a scaffold introduction that defines contributions and gives the evaluation a target. The scaffold is a planning document; the final introduction — the one that ships — gets written after results are settled, so every promise has evidence behind it.

**Delay compression until the contribution stabilizes.** Treat the first draft as knowledge transfer — a way to show your advisor everything you know, every piece of evidence you have, and every connection you see in the data. Include everything. Compression comes later, and it can only happen after someone understands the full picture. Cutting before the framing stabilizes means cutting blind.

**Name your core insight.** Give your central contribution a specific, two-to-four-word name that distinguishes it from everything else in the field. If the name could describe any paper in your area, the discovery process has further to go. As a diagnostic: show your draft to someone outside your subfield and ask them to state, in one sentence, what the paper contributes. If their answer diverges from yours, you have a framing problem — and in this dataset, that carried the highest repair cost of any mistake.

---

## What I Learned as a Mentor

*What does the data say about me — beyond the papers themselves?*

The second half of this analysis was harder to write, because the data exposed my own patterns — the ones I was teaching around until the data made them visible.

### The Late Intervention Pattern

Across all six papers, my editorial intervention arrives late and dominates the final product. In Paper A, 57% of all edits happened in the final 12 days before submission. In Paper D, my crunch-phase editing represented a 350× increase over my early involvement. The pattern is consistent: the student builds for months, and I rewrite in days.

The pattern works as a production system. I am less convinced it works as a pedagogy. A late rewrite can rescue a paper while skipping the step the student most needs: seeing the reasoning behind the rewrite. When I rewrite a section from scratch, the student receives the final product and misses the intermediate reasoning entirely. The version history captures *what* changed. The *why* — the reasoning behind each transformation — stays invisible.

One paper in the dataset offers a counterpoint. A student used 126 inline feedback markers — far more than any other student — engaging in explicit dialogue about framing decisions throughout the writing process. That student's drafts required progressively less rewriting across three submission cycles — a trajectory I did not observe with students who received my rewrites in silence.

> The dialogue was the teaching mechanism. The final product was an artifact of it.

Going forward, I want to make my editorial reasoning more visible. Instead of handing back a rewritten file, I want to annotate the reasoning: "I moved this paragraph because the claim needs to precede the evidence," "I cut this because it serves zero contributions listed in the introduction," "I renamed this because the old term could describe any paper in the field." The overhead is real. But if it accelerates the point at which a student can self-edit, the total cost over a PhD is lower.

### The Comprehensive Draft Is a Feature

Every student in the dataset produces an initial draft more comprehensive than the final version. I used to think this was a problem. The data changed my mind. The comprehensive draft is how the student transfers their understanding — what they know, what evidence exists, what connections they see. That information is essential for the rewrite.

The problem is the feedback loop. The 30–50% compression in the final pass represents editorial judgment about what earns its place — and that judgment is the skill students most need to develop. When I compress alone, the student sees the result but not the reasoning: why this paragraph stayed, why that one was cut, why two sections merged into one. I am now trying to make the compression pass collaborative: the student and I sit together, I narrate the cutting in real time, and the goal is to make the deletion logic visible so it becomes learned.

### Student-Venue Matching

One of the clearest signals in the data: measurement papers have naturally stable identities while systems papers require extensive identity discovery. Students whose first papers were measurement-oriented had smoother paths to acceptance. Students whose first papers were systems-oriented faced more identity crises, more rewrites, and more rejections.

This is a property of the writing task itself. A measurement paper's identity is determined by its research questions: "we measured X and found Y." A systems paper's identity must be *constructed*: "we built X, and the reason you should care is Y, framed as Z." That construction develops over time.

I am now more deliberate about matching paper type to student development stage. An early-career student benefits from leading a measurement or evaluation paper first — the identity is given by the questions, the writing task is more contained, and the student gets an acceptance that builds both skill and confidence. The systems paper, with its inherent identity discovery, is better suited for a student who has already absorbed the basics through a successful first paper.

---

> ### The Argument in Brief
>
> Version histories are data. Treated as data, they reveal structural patterns that style guides miss entirely: identity stability as the clearest acceptance-linked pattern, framing as the highest-repair-cost mistake, a consistent expand-then-compress arc, naming as the most frequent edit operation, and rejection as the mechanism that forces abstraction. For mentors, the data exposes where intervention helps and where it merely substitutes — and suggests that making editorial reasoning visible matters more than making editorial decisions alone.

---

## Replicating This Analysis

The full extraction prompt — seven phases, from version inventory through synthesis — is available as a [companion document]({{ site.baseurl }}/blogs/the-paper-behind-the-paper-extraction-prompt.html). It is written for Overleaf but generalizes to any version-controlled writing workflow; replace the API calls with `git log` and `git diff` and the rest is identical. The anonymized data from my own analysis is available as a companion file [here]. If you run this on your own papers, I want to hear whether the patterns replicate.

---

*Based on analysis of 6 papers, 8 submissions, 7,600+ Overleaf edits, and 100+ tex file versions from my research group at UC Santa Barbara. All papers and students are anonymized. AI tools assisted with sentence-level diffing and pattern extraction at scale; the analysis and interpretation are mine.*
