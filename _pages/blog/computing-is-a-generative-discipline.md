---
title: "Computing Is a Generative Discipline"
permalink: /blog/computing-is-a-generative-discipline.html
layout: single
author_profile: true
date: 2026-02-28
---

A familiar question is circulating through universities, funding agencies, and public discourse: Will AI subsume computer science? The question reveals a misunderstanding — one worth correcting, because the answer reshapes how we think about education in this field for the decades ahead.

Computing is a generative discipline. I use "computing" deliberately here — broader than "computer science" as a department label, it names the intellectual enterprise of creating, composing, and reasoning about computational abstractions. The generative claim is about that enterprise, not any particular institutional structure.

Computing produces the abstractions from which entirely new problem spaces emerge. AI is one of those problem spaces — among the most powerful and visible — but it is a *product* of computing's generative capacity. Recognizing this changes the conversation entirely. The real question is how computing education must evolve to reflect what the discipline has always been: the intellectual engine that creates successive waves of innovation.

## The Generative Pattern

The claim that computing is generative is empirical and historical. Across decades, computing has repeatedly produced abstraction layers from which entire intellectual domains emerged.

Packet switching, developed in the 1960s, created networking as a new intellectual domain — one with its own theory, its own design principles, and its own research community. Van Jacobson's seminal work on congestion control, presented at SIGCOMM in 1988,<sup>1</sup> formalized an entirely new class of distributed resource allocation problems that shaped decades of systems research and practice. MapReduce, introduced by Dean and Ghemawat at OSDI in 2004,<sup>2</sup> generated a new computational paradigm that reconstituted how an entire generation of researchers and practitioners thought about scalable computation. (I realize I'm leaning hard on networking examples here — occupational hazard — but the pattern generalizes well beyond my corner of the field.)

A computing abstraction opens a new problem space — with its own questions, methods, and communities — that did not exist before. That is the generative pattern.

The institutional record reinforces this. Carnegie Mellon established its School of Computer Science in 1988,<sup>3</sup> and AI has remained one of several pillars housed within that broader computing vision ever since — the Machine Learning Department, the Robotics Institute, and the Language Technologies Institute all sit under SCS today. MIT merged its Laboratory for Computer Science and its AI Lab into CSAIL in 2003,<sup>4</sup> an integration under the computing umbrella. UC Berkeley established the College of Computing, Data Science, and Society (CDSS) in 2023<sup>5</sup> — its first new college in over fifty years — pulling statistics, data science, and computational biology into a computing-centered structure. Cornell elevated its Faculty of Computing and Information Science to a full College in 2020.<sup>6</sup> And UT Austin announced a new School of Computing in February 2026,<sup>7</sup> uniting computer science, statistics and data sciences, and the School of Information into a single entity. Why did each of these institutions make this structural choice? Because computing keeps absorbing the fields it generates. It expands and reconstitutes itself.

## From LLMs to Agentic Systems: A Real-Time Case Study

The generative pattern is playing out right now. Just two years ago, the dominant narrative held that large language models would subsume everything — coding, writing, reasoning, entire professions.

Today, the frontier has already moved. The current wave centers on agentic systems: architectures where AI models are embedded within larger computational frameworks that plan, use tools, maintain state, and interact with external environments. At a high level, LLMs and agentic systems appear similar — both involve AI performing complex tasks. Yet they are fundamentally different in the computing abstractions they require.

LLMs draw primarily on statistical learning, optimization, and parallel computation. Agentic systems draw on a different and broader cross-section of computing: distributed systems, planning and control, program synthesis, security and sandboxing, formal verification of tool use, and the design of reliable multi-component software architectures. The shift from one paradigm to the next happened in under two years, and it demanded entirely different foundational knowledge.

Whatever follows agentic systems will emerge from computing abstractions, and it will require a different combination of them than the current paradigm does. The value of computing lives in the discipline's capacity to produce, recombine, and extend these abstractions. Ground your strategy in computing's foundations, and you adapt naturally. Lock it to "AI" as a fixed destination, and you are obsolete the moment the paradigm shifts.

## From Discipline to Education

If education should teach anything, it's how to operate with abstractions themselves — because that's what computing as a discipline does best. Students need to recognize when paradigms shift and map enduring principles onto new problem spaces.

The LLM-to-agentic transition is the case study. Students who learned only transformers and prompting are scrambling. Students trained in distributed systems, formal reasoning, and software architecture? They adapted within weeks. They didn't predict the shift, but their foundations carried them through it. The abstractions transferred. The specifics did not.

**Education should mirror the discipline's generative structure.** The same property that makes computing durable as a field should be the foundation of how we teach it. Build curriculum around the invariant intellectual core: abstraction, problem formulation, decomposition, critical evaluation, and first-principles reasoning. These are the competencies that carry a student from one paradigm to the next, just as the discipline itself moves.

## What AI Has Actually Revealed

The rapid automation of mechanistic tasks — code generation, boilerplate writing, pattern completion — has exposed a gap. We were assessing production: syntactically correct code, completed algorithms, plausible technical prose. When a tool can generate all of that, the assessments we relied on were, in retrospect, measuring the wrong thing.

AI forces a return to first principles. Every instructor must now ask: What do we really want students to learn? How should we assess transfer of critical skills rather than reproduction of known patterns?

I see what this looks like concretely in my own research group. When I was a PhD student, getting feedback from my advisor on a figure or analysis meant days of wrestling with matplotlib documentation to produce exactly what he wanted. Now, when I give my students similar feedback, they come back within minutes — "done." But here is what matters: these are PhD students who already understood the analysis before they touched the tool. They knew what the figure *should* show, why a particular visualization choice mattered, what the data meant. AI accelerated production of something they already knew how to reason about. That's the right use case.

Undergraduates are in a different position. Most of them are still building the conceptual scaffolding that makes critical judgment possible. They can't always tell where the legitimate use of AI ends and where it starts undermining their learning — because that boundary requires exactly the judgment they haven't yet developed. So how do you teach discrimination to students who don't yet have the expertise to exercise it?

The answers point toward assessment that probes understanding directly. Concretely: ask students to construct adversarial test cases that expose when an AI-generated solution fails on edge cases. Require proof obligations where a student must formally justify *why* an algorithm is correct, not just that it runs. Use "explain-then-implement" oral checks where a student walks through their reasoning before writing any code. These assessment patterns are harder to design and harder to grade. But they measure what actually matters.

## Decouple Goals from Mechanisms

Stop tying curriculum to whatever tool is trending. That's the core move.

The LLM-to-agentic shift is proof of why: in two years, the dominant paradigm, its tooling, and its workflows changed substantially. Curriculum built around any specific mechanism will require perpetual revision and never converge on a stable intellectual foundation.

The conceptual kernels that endure across paradigm shifts are well known: abstraction, problem formulation, critical discrimination, first-principles reasoning, the ability to reason about complexity and trade-offs. They let the discipline reconstitute itself each time — around networking, the web, cloud computing, now AI. They are what will carry it through whatever follows.

The goal of computing education is to teach students how problems evolve and how enduring principles map to new problem spaces. A student who understands decomposition, resource allocation, formal specification, and adversarial reasoning will navigate the next paradigm shift as capably as the current one — because they are operating at the level of the abstractions that *generate* paradigms.

## The Cost of Getting This Wrong (and Right)

I want to be honest about what curricular change actually costs, because I think the conversation often stays too abstract here.

Early in my career, as a tenure-track faculty member, I tried to build a completely new course on programmable networks for CS 176B. I was passionate about it — I genuinely believe that teaching should be empirical, that instructors should generate new content, and that the gap between research and education should be as narrow as we can make it. So I designed the course from scratch. The problem was that my TAs were not experts on writing P4 programs, I was simultaneously struggling to establish my research program, and the whole thing turned into a disaster. My worst teaching ratings — still sitting on [Rate My Professor](https://www.ratemyprofessors.com/professor/2615402), still findable, still discouraging — date to that quarter. I am grateful, in retrospect, that tenure committees do not consult Rate My Professor.

Meaningful curricular change demands resources that are rarely accounted for. Redesigning a course around new principles — changing the content, the programming assignments, the mode of delivery, the assessments — exceeds one quarter of preparation. It might take two. It might require one or two PhD students working full-time. The risk of failure is real, especially for junior faculty simultaneously building a research identity. My own experience teaches me that ambition without infrastructure produces burnout and bad evaluations, not better education.

This makes the proactive posture even more important. If change is necessary — and it is — we should reason deliberately about *what kind* of change, rather than scrambling reactively. What might AI capabilities stabilize into over the next five to ten years? What does that mean for specific courses, specific learning objectives, specific assessment strategies? We should be identifying the invariant skill set that students need across both the current transitional phase and the eventual steady state. We will not get this right on the first attempt — and that is fine. But principled iteration beats institutional whiplash.

## The Instructor's Position

Instructors should be at the frontier of AI — yet curriculum should remain rooted in enduring principles, not in specific AI mechanisms. These are complementary positions. Frontier knowledge enables instructors to recognize when paradigms are shifting, to update what they teach, and to teach discrimination effectively. An instructor who understands the limitations of current models can design assessments that probe understanding. An instructor who does not will end up designing around the tool rather than around the learning objective.

But here is the thing: instructors who actually learn this stuff start to see the leverage. Not immediately — there's a ramp-up cost that is real and should be stated plainly. Rethinking learning objectives, redesigning assessments, managing student use of AI — all of it is expensive, layered on top of existing teaching, research, and service demands. But the medium-term payoff is real for those who engage seriously. Effort first, then compounding returns.

Students, in turn, must develop discrimination as a first-class competency. The ability to evaluate AI-generated artifacts — to distinguish genuine insight from confident-sounding nonsense, to probe edge cases, to demand justification rather than accept plausibility — is an intellectual skill that computing education is uniquely positioned to develop, grounded as it is in formal reasoning, empirical testing, and principled skepticism.

## Governance and Institutional Design

Faculty governance must remain central to AI integration in education. The decisions being made now — which tools to adopt, how to assess student work, what constitutes academic integrity in an AI-saturated environment — will shape computing education for years. These decisions should be made by faculty who understand both the discipline and the pedagogy.

When individual instructors and students independently adopt whatever AI tools are fashionable, you get fragmentation: inconsistent expectations across sections of the same course, inequitable access, unexamined privacy risks, erosion of academic freedom. Institutionally governed AI services — privacy-preserving, opt-in, auditable — provide a principled alternative. They protect intellectual property, ensure equity of access, and create conditions for coherent pedagogical design.

Fairness demands particular attention. In multi-section courses, students should encounter consistent expectations around AI use. Access to tools should vary by pedagogical design, not by economic circumstance. A common institutional language around levels of AI integration — from prohibition to supervised use to open collaboration — gives instructors and students a shared framework for navigating what is, genuinely, new terrain.

## What Computing Owes the Next Generation

Computing has always been the discipline that creates the future — by producing the abstractions from which new fields, new industries, and new intellectual paradigms emerge. AI is the latest and most visible product of this generative capacity. It is evidence of computing's vitality.

Education in computing should embody this same generative confidence. Root CS education in the abstractions and first principles that have always given the discipline its durability. Decouple educational goals from transient mechanisms. Invest in the infrastructure that makes principled curricular change possible — the time, the people, the institutional support. Teach students to discriminate between what sounds right and what is right. And iterate deliberately, knowing that the path forward is principled adaptation.

The discipline that generated AI is the right one to educate whoever shapes what comes next.

---

*Arpit Gupta is an Associate Professor of Computer Science at the University of California, Santa Barbara, and a Faculty Scientist at Berkeley Lab.*

## Notes

1. V. Jacobson, "Congestion Avoidance and Control," *ACM SIGCOMM Computer Communication Review*, 1988.
2. J. Dean and S. Ghemawat, "[MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)," *OSDI*, 2004.
3. Carnegie Mellon's School of Computer Science was formally established December 22, 1988, with Nico Habermann as founding Dean. See [SCS History](https://www.cs.cmu.edu/scs25/history).
4. MIT CSAIL was formed July 1, 2003, merging the Laboratory for Computer Science (LCS) and the AI Laboratory. See [CSAIL Mission & History](https://www.csail.mit.edu/about/mission-history).
5. UC Berkeley's College of Computing, Data Science, and Society was approved by the UC Board of Regents on May 18, 2023. See [CDSS Announcement](https://cdss.berkeley.edu/news/uc-berkeley-college-computing-data-science-and-society-established).
6. Cornell's Ann S. Bowers College of Computing and Information Science was elevated to College status in December 2020.
7. The UT Austin School of Computing was approved by the UT System Board of Regents on February 19, 2026, with classes beginning Fall 2026. See [UT Austin Announcement](https://news.utexas.edu/2026/02/19/ut-launches-new-school-of-computing-uniting-computer-and-data-science-statistics-information-disciplines/).
