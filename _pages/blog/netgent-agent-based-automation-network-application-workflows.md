---
title: "NetGent: Agent-based automation of network application workflows"
permalink: /blog/netgent-agent-based-automation-network-application-workflows.html
layout: single
author_profile: true
date: 2026-02-05
---

<p class="page__subtitle" style="font-size: 0.9em; color: var(--muted); margin-top: -0.5em; margin-bottom: 1.5em;">Originally published on the <a href="https://blog.apnic.net/2026/02/05/netgent-agent-based-automation-of-network-application-workflows/">APNIC Blog</a> (February 5, 2026). Guest post with Jaber Daneshamooz. <a href="https://blog.apnic.net/2026/02/05/netgent-agent-based-automation-of-network-application-workflows/">Read the original post on APNIC →</a></p>

*The following is republished here in full from the [APNIC Blog](https://blog.apnic.net/2026/02/05/netgent-agent-based-automation-of-network-application-workflows/).*

---

Imagine running a measurement study to understand how an application behaves under different network conditions, or generating data for supervised learning problems that require ground-truth labels collected under controlled settings. You log into Instagram, scroll through several reels, generate video traffic, and observe how performance shifts as latency or bandwidth changes. Everything works today. But the next day, the workflow stalls on a slightly altered login screen. A few days later, a new cookie banner appears, a button moves, or a dialogue loads differently — and the automation you relied on collapses.

Whether the goal is to conduct a rigorous measurement study or to collect labelled data for a supervised learning problem, the underlying issue is the same — we need application workflows that behave consistently, even as the applications themselves evolve continuously. Traditional browser automation tools break frequently. Scripted interactions do not generalize across apps or layouts. And while agent-based approaches are more flexible, they depend on repeated LLM inference, which is too slow, too expensive, and too unstable for large-scale experimentation across diverse network conditions.

This fragility is more than an inconvenience. It limits our ability to collect representative data, reproduce experiments, train models that generalize, and understand application behaviour in realistic environments. As applications iterate weekly and deploy UI changes continuously, the gap between what researchers need and what existing automation tools can provide grows wider.

**NetGent was created to close this gap by rethinking how application workflows should be generated, maintained, and executed for networking research.**

## Why data generation needs a new approach

High-quality data sits at the foundation of nearly every modern networking study — congestion control evaluation, Quality of Experience (QoE) inference, anomaly detection, application fingerprinting, and many others. Yet much of the data used today comes from brittle scripts, narrow single-purpose workflows, or manually curated traces. These approaches make data generation fragile and unscalable, and they hinder reproducibility across testbeds, operators, and research groups.

A more robust solution requires treating data generation itself as a structured system component. When we disaggregate intents from execution, that is, separate **what** a workflow is intended to do from **how** it is executed, workflows become portable and stable. When execution is decoupled from UI details, workflows can be regenerated as applications evolve. And when workflows can run deterministically under many network conditions, researchers gain the ability to build consistent, diverse datasets that support meaningful comparisons and aid the development of generalizable Machine Learning (ML) models.

This architectural view — a thin-waist 'data-generation substrate' — is the motivation behind NetGent. It represents the workflow layer of this substrate, designed specifically to automate application behaviour in a way that is stable, repeatable, and efficiently scalable for networking research.

## Why application workflows are so difficult

Application workflows encode human intent through multi-step tasks: Logging in, navigating menus, scrolling feeds, watching videos, posting content, or joining calls. These workflows include conditional logic, asynchronous events, transitional states, and UI elements that change frequently as applications evolve. Traditional automation tools are tightly coupled to these UI details, so even small interface adjustments break the workflow and require manual repair.

Agent-based approaches offer greater flexibility but introduce new problems. They depend on LLM inference at runtime, which is costly and slow. They introduce nondeterminism that makes it difficult to compare runs across network conditions. And they are impractical for experiments that need to repeat workflows hundreds or thousands of times to capture meaningful diversity in traffic or to train high-quality models.

These limitations reveal a structural need for change. Workflows should be defined abstractly so they survive UI changes. They should execute deterministically so that results can be compared across different network conditions. And they should scale efficiently so they can be used to generate large, diverse datasets. **NetGent was designed around these requirements from the ground up.**

## How NetGent works

NetGent addresses the core challenge of producing realistic, repeatable application workflows by disaggregating the *intent* of a workflow from the *mechanics* of how it is executed. Instead of requiring researchers to write brittle scripts tied to specific UI elements, NetGent allows workflow logic to be expressed directly in natural language. A workflow may be described with a few trigger–action rules such as 'if on login page, enter credentials', 'if a cookie banner appears, accept it', or 'if reels are visible, watch several of them'. These descriptions capture what the workflow should accomplish without binding it to the specific layout or structure of any particular interface.

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/netgent-figure1.png" alt="Figure 1 — NetGent runtime loop progresses from the initial to end state." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">Figure 1 — NetGent runtime loop progresses from the initial to end state.</figcaption>
</figure>

Internally, NetGent converts these high-level rules into an **abstract non-deterministic finite automaton (NFA)** that encodes the logical structure of the workflow: The states a user might encounter, the conditions that trigger transitions, and the actions to be taken in response. Unlike traditional finite-state automation frameworks, this NFA supports multiple possible transitions, mirroring the unpredictable nature of modern applications where pop-ups, notifications, or intermediate screens may appear unexpectedly.

From this abstract representation, NetGent's **State Synthesis module** generates a set of **concrete states**, each equipped with application-specific detectors — based on Document Object Model (DOM) elements, text patterns, URLs, or other contextual cues — and the executable code for performing the required actions. The synthesis process is guided by the abstract rules but results in fully executable workflows. Once generated, these workflows are cached and executed by a lightweight **State Executor** that runs deterministically and does not require any LLM inference. This makes execution fast, robust, and inexpensive, while ensuring consistent behaviour across runs and network conditions.

If an application's UI changes, NetGent regenerates only the affected states instead of rebuilding the entire workflow. This architecture dramatically reduces maintenance overhead while preserving workflow fidelity and repeatability. In effect, NetGent combines the flexibility of language-driven workflow specification with the efficiency and stability of compiled execution, offering a workflow substrate on which diverse, complex, and human-like application behaviours can be generated and reproduced reliably.

## Example: Instagram login and reels exploration

To illustrate how NetGent works in practice, consider generating realistic Instagram traffic, such as browsing a feed or watching reels. The workflow can be expressed in a handful of high-level rules: 'if on login page, enter username and password', 'if on the home feed, scroll several times', 'if reels are present, watch them', and 'if a consent dialogue appears, accept it'.

NetGent converts these descriptions into an abstract Nondeterministic Finite Automata (NFA) that captures the logical flow of the interaction, including optional transitions like cookie banners or privacy prompts. From this, it synthesizes a concrete state machine with detectors for identifying the relevant UI elements and executable code for logging in, scrolling, clicking, and interacting with reels.

Once compiled, this workflow can be executed as many times as needed under different network conditions. It produces traffic patterns that match real user behaviour far more closely than traditional scripted approaches. Just as importantly, if Instagram changes its interface — whether by adjusting the login layout or inserting a new dialogue — NetGent can quickly regenerate just the parts of the workflow that need updating.

This capability is especially powerful for tasks like QoE inference or fingerprinting, where consistency across runs is essential. Yet it is equally valuable for measurement studies, benchmarking, or cross-traffic generation in controlled environments. The same workflow can be used repeatedly without reengineering the automation layer.

## Why NetGent matters

NetGent fills a critical gap in networking research: The ability to generate **realistic, repeatable, and diverse application traffic** at scale. By decoupling workflow intent from execution, it makes it possible to build libraries of reusable workflows for a wide range of applications — social media, video streaming, e-commerce, conferencing, messaging, and more.

For researchers, this reduces the barrier to creating complex datasets, enables controlled comparison across network conditions, and improves reproducibility across platforms and testbeds. For operators, NetGent offers a tool for diagnosing application behaviour under specific network impairments or evaluating how performance-sensitive applications interact with real-world traffic patterns. For both communities, it provides a foundation for producing the kind of high-quality data needed to evaluate networking systems and ML models responsibly.

NetGent is open source and available on GitHub. It includes a Python package, a Docker container, and a collection of pre-generated workflows that require no API keys and no interaction with external models. Users can extend these workflows or create new ones with only a few natural-language descriptions.

## Looking ahead

NetGent addresses one half of the data-generation challenge — application behaviour. But realistic experiments also depend on the **network environments** in which these applications run. Variations in latency, jitter, loss, burstiness, and wireless conditions play a major role in shaping application traffic.

In the next post, we will introduce **NetReplica**, a complementary system that models diverse network conditions programmatically. Together, NetGent and NetReplica form the initial components of a broader data-generation substrate — a foundation for building reproducible, scalable, and realistic datasets for networking research and ML systems.

Read more details in our paper *NetGent: Agent-Based Automation of Network Application*.

---

*Jaber Daneshamooz is a fourth-year PhD student in the Systems & Networking Lab at UC Santa Barbara, where his research focuses on developing programmable data-generation substrates for networking research and machine learning. He works on systems such as NetGent, NetReplica, and NetUnicorn that aim to make realistic, reproducible network experimentation accessible at scale.*

*This work was conducted in collaboration with Eugene Vuong, Laasya Koduru, Sanjay Chandrasekaran, and Arpit Gupta.*

---

<p style="font-size: 0.9em; color: var(--muted); margin-top: 1.5em;"><strong>Original source:</strong> <a href="https://blog.apnic.net/2026/02/05/netgent-agent-based-automation-of-network-application-workflows/">NetGent: Agent-based automation of network application workflows</a> — APNIC Blog (February 5, 2026)</p>
