---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

## Research Overview

I am a networking researcher committed to advancing digital equity through principled system design.

My north star is clear:

> Access to a secure, performant, and affordable Internet must become a durable infrastructure guarante--not a function of geography, income, or institutional capacity.

Realizing this goal requires more than faster protocols or incremental optimizations. It requires validated data systems that make digital infrastructure measurable, accountable, and intelligently operable.

My research develops the architectural foundations for this transformation — spanning public-interest broadband infrastructure and agentic, AI-powered network operations.

---

## Path I — Public-Interest Broadband Data Infrastructure

Digital equity demands decision-grade visibility into broadband markets.

My work advances both the intellectual foundations and the operational infrastructure required to measure affordability, competition, and performance at scale.

Central to this effort is:

**[Broadband Query Tool (BQT / BQT+)](https://address.cs.ucsb.edu/bqt/)** — an address-level broadband pricing and availability intelligence platform enabling reproducible analysis of market structure and affordability.

BQT has informed regulatory and policy discussions across states and agencies, shaping how competition and pricing are evaluated in large-scale funding and oversight decisions. The broader vision is articulated in:

- [What We Can't See, We Can't Fix](https://www.benton.org/blog/what-we-cant-see-we-cant-fix)

BQT+ advances this platform through agentic system design: decomposing complex ISP interaction processes into reusable, adaptive components that scale across providers while preserving methodological rigor.

BQT/BQT+ has enabled a series of research contributions grounded in rigorous measurement and statistical modeling:

- [Contextualizing Speed Test Measurements](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/speedtest.pdf) (IMC 2022, **Distinguished Paper Award**) — establishing principled modeling of user-perceived performance.
- [Decoding the Divide](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/bqt_sigcomm23.pdf) (SIGCOMM 2023) — introducing address-level broadband pricing measurement for rigorous market analysis.
- [Assessing the Efficacy of the Connect America Fund](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/caf-sigcomm24.pdf) (SIGCOMM 2024, **ANRP Award**) — scalable methodologies for extracting and synthesizing ISP plan data across heterogeneous interfaces.

We are extending this foundation through:

**NetVibe** — an evolving longitudinal latency intelligence platform that connects infrastructure-level performance measurements with user-level experience.

Together, this body of work establishes independent broadband data ecosystems grounded in statistical modeling, systems research, and reproducible infrastructure — capable of informing billion-dollar investment decisions and regulatory accountability.


## Path II — Agentic and AI-Powered Network Operations (AIOps)

Digital equity also requires operational intelligence: networks that adapt, generalize, and remain trustworthy under dynamic conditions.

My group advances agentic and AI-powered network operations grounded in controllable data generation, structured representation learning, and principled validation.

### Programmable Data Substrate

We are building a programmable experimentation infrastructure that enables scalable and verifiable network research:

- **[netUnicorn](https://netunicorn.cs.ucsb.edu/)** — distributed orchestration across heterogeneous environments.
- **[NetReplica](#arxiv-link)** — an evolving bottleneck-aware emulation framework for controlled experimentation.
- **[NetGent](#arxiv-link)** — an agentic workflow automation system that compiles high-level specifications into deterministic, reusable execution pipelines.

These systems share a central architectural insight: complex operational tasks become reliable and scalable when decomposed into smaller, verifiable components — a principle mirrored in BQT+.

### Network Foundation Models and Validation

Building on this substrate, we introduced:

- **[netFound](https://arxiv.org/abs/2310.17025)** — a domain-specific network foundation model that learns spatial, temporal, and hierarchical structure directly from packet-level telemetry.
- **[NetBurst](#arxiv-link)** — ongoing modeling of bursty, event-driven network dynamics for improved temporal abstraction and forecasting.
- **[Intrinsic Evaluation Framework](#arxiv-link)** (NeurIPS 2025) — a representation-level validation methodology decoupling embedding quality from downstream task artifacts.
- **[Trustee](https://trusteeml.github.io/)** (ANRP recognition) — advancing interpretability and structured introspection for learning-based network systems.

This program establishes validated foundations for agentic and AI-powered network operations that are robust, generalizable, and deployment-aware.

### Deployment and Engagement

We actively engage with the [Energy Sciences Network (ESnet)](https://www.es.net/) to explore how AIOps frameworks can support large-scale scientific infrastructure — advancing adaptive traffic management, scalable telemetry analysis, and AI-driven operational intelligence in production environments.


## A Unifying Architectural Thesis

My research advances a coherent and long-term position:

> Digital infrastructure must be measurable, intelligible, and agentically actionable.

Broadband markets and network operations are manifestations of the same systems problem: transforming large-scale, dynamic network environments into validated, decision-grade intelligence.

The architectural commitment is deliberate:

1. **Instrument** networks with granular, high-fidelity perception.
2. **Learn** structured representations that preserve hierarchy, causality, and temporal dynamics.
3. **Validate** models and workflows independently of downstream artifacts.
4. **Embed** intelligence into systems capable of adaptive action.

In broadband policy, this architecture enables transparency, accountability, and evidence-driven investment. In network operations, it enables adaptive, reliable, and deployable AIOps.

This thesis defines the trajectory of my work: **build agentic, validated data systems that elevate digital infrastructure from reactive management to accountable, intelligent operation.** From BQT+ and NetVibe to netFound, NetBurst, and emerging agentic platforms, each system advances this architectural transformation.


## Representative Systems

- [BQT / BQT+](https://address.cs.ucsb.edu/bqt/) — broadband plan querying tool
- NetVibe — evolving longitudinal latency intelligence platform
- [netUnicorn](https://netunicorn.cs.ucsb.edu/) — distributed orchestration platform
- [netFound](https://arxiv.org/abs/2310.17025) — network foundation model
- [NetBurst](#arxiv-link) — event-centric forecasting system
- [NetReplica](#arxiv-link) — evolving bottleneck-aware emulation framework
- [NetGent](#arxiv-link) — agentic workflow automation system
- [Intrinsic Evaluation Framework](#arxiv-link) — representation analysis for network foundation models
- [Trustee](https://trusteeml.github.io/) — interpretability framework for ML-based network systems

### Funding
The research in my group is supported by various government agencies, namely, the National Science Foundation (NSF), the Department of Energy (DoE), as well as different network/content service providers such as Google, Verizon Innovations, ViaSat, and vendors including Intel and Cisco.

<table style="width:100%; border-collapse:collapse; font-size:0.95em;">
  <thead>
    <tr style="border-bottom:2px solid #444;">
      <th style="text-align:left; padding:8px 10px;">Project</th>
      <th style="text-align:left; padding:8px 10px;">Funding Organization</th>
      <th style="text-align:left; padding:8px 10px;">Start</th>
      <th style="text-align:left; padding:8px 10px;">Amount</th>
      <th style="text-align:left; padding:8px 10px;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">Effectively Measuring Broadband Affordability in California</a></td>
      <td style="padding:8px 10px;">California Public Utilities Commission</td>
      <td style="padding:8px 10px;">Jan 2026</td>
      <td style="padding:8px 10px;">$275k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">Bridging the Representation–Semantics Gap for Production-Ready AI-Powered Network Operations</a></td>
      <td style="padding:8px 10px;">Cisco</td>
      <td style="padding:8px 10px;">Feb 2026</td>
      <td style="padding:8px 10px;">$75k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">AIOps Roadmap Development for ESnet</a></td>
      <td style="padding:8px 10px;">DoE</td>
      <td style="padding:8px 10px;">Jul 2025</td>
      <td style="padding:8px 10px;">$65k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://research.google/programs-and-events/research-scholar-program/recipients/">Low Infrastructure ML</a></td>
      <td style="padding:8px 10px;">Google</td>
      <td style="padding:8px 10px;">Jul 2025</td>
      <td style="padding:8px 10px;">$100k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://blog.google/products/google-cloud/ml-systems-junior-faculty-awards/">Network Foundation Model for Enabling AI-powered Network Operations (AIOps)</a></td>
      <td style="padding:8px 10px;">Google</td>
      <td style="padding:8px 10px;">Jul 2025</td>
      <td style="padding:8px 10px;">$60k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2443777">Developing Generalizable ML Models for Diverse Learning Problems in Network Operations</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">May 2025</td>
      <td style="padding:8px 10px;">$700k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">Characterizing Broadband Pricing in California</a></td>
      <td style="padding:8px 10px;">California Public Utility Commission</td>
      <td style="padding:8px 10px;">Jan 2025</td>
      <td style="padding:8px 10px;">$125k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://dls.virginia.gov/commissions/jcots/materials/broadband_report_nov_2025.pdf">Characterizing Barriers to Digital Inclusion in Virginia</a></td>
      <td style="padding:8px 10px;">Virginia JCOTS</td>
      <td style="padding:8px 10px;">Jan 2025</td>
      <td style="padding:8px 10px;">$30k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">Telemetry-driven Foundation Models for Self-Driving Networks</a></td>
      <td style="padding:8px 10px;">Cisco Research</td>
      <td style="padding:8px 10px;">Sep 2024</td>
      <td style="padding:8px 10px;">$90k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://arxiv.org/abs/2310.17025">netFound: Network Foundation Model</a></td>
      <td style="padding:8px 10px;">DoE</td>
      <td style="padding:8px 10px;">Sep 2024</td>
      <td style="padding:8px 10px;">—</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2323229">IMR: MT: NetFlex: A Flexible Scalable &amp; Privacy-Preserving Network Measurement Platform to Iteratively Collect Multi-modal Multi-view Network Data from Access Networks</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">Oct 2023</td>
      <td style="padding:8px 10px;">$600k</td>
      <td style="padding:8px 10px;">Active</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://nsf.gov/awardsearch/showAward?AWD_ID=2224687">IMR: RI-P: Programmable Closed-loop Measurement Platform for Last-Mile Networks</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">Oct 2022</td>
      <td style="padding:8px 10px;">$100k</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://address.cs.ucsb.edu/">IMR: MM-1A: ADDRESS: Augment, Denoise and Debias Crowdsourced Measurements for Statistical Synthesis of Internet Access Characterization</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">Oct 2022</td>
      <td style="padding:8px 10px;">$600k</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="#">The Estimation and Monitoring of Quality of Experience Delivered over Internet Services</a></td>
      <td style="padding:8px 10px;">ViaSat</td>
      <td style="padding:8px 10px;">Jan 2022</td>
      <td style="padding:8px 10px;">$200k</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126327">CC* Integration-Large: Democratizing Networking Research in the Era of AI/ML</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">Oct 2021</td>
      <td style="padding:8px 10px;">$1M</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126281">CC* Integration-Large: Bringing Code to Data: A Collaborative Approach to Democratizing Internet Data Science</a></td>
      <td style="padding:8px 10px;">NSF</td>
      <td style="padding:8px 10px;">Oct 2021</td>
      <td style="padding:8px 10px;">$1M</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2003257">MLWiNS: RL-based Self-driving Wireless Network Management System for QoE Optimization</a></td>
      <td style="padding:8px 10px;">NSF &amp; Intel</td>
      <td style="padding:8px 10px;">Jun 2020</td>
      <td style="padding:8px 10px;">$820k</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
    <tr style="border-bottom:1px solid #ddd;">
      <td style="padding:8px 10px;"><a href="https://www.verizon.com/about/news/verizon-advances-5g-network-and-cyber-security">Scaling Cybersecurity Infrastructure using Programmable Data Planes</a></td>
      <td style="padding:8px 10px;">Verizon</td>
      <td style="padding:8px 10px;">Sep 2019</td>
      <td style="padding:8px 10px;">$200k</td>
      <td style="padding:8px 10px;">Completed</td>
    </tr>
  </tbody>
</table>