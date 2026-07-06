---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

## Research Overview

My mission is to make a secure, performant, and affordable Internet accessible to everyone.

I pursue this mission along two paths, each of which requires bridging fundamental data gaps in how we measure and operate networks:

* **Path I — Data-Driven Policymaking:** building independent, decision-grade broadband data so that public investment in connectivity can be measured, audited, and held accountable.
* **Path II — Self-Driving Networks:** developing AI-powered network operations that let networks adapt, generalize, and stay trustworthy with limited infrastructure and operational resources.

Both paths turn on the same conviction: we cannot fix what we cannot measure, and we cannot safely automate what we cannot generate and reason about as data.

---

## Path I — Data-Driven Policymaking

Public investment in broadband runs into a fundamental data gap: we cannot tell whether tens of billions of dollars in funding actually reach the communities they target.

My work closes that gap, building the intellectual foundations and operational infrastructure to measure affordability, competition, and performance at scale.

Central to this effort is:

**[Broadband Query Tool (BQT / BQT+)](https://address.cs.ucsb.edu/bqt/)** — an address-level broadband pricing and availability intelligence platform enabling reproducible analysis of market structure and affordability.

BQT has informed regulatory and policy discussions across states and agencies, shaping how competition and pricing are evaluated in large-scale funding and oversight decisions, and is used by Cal Advocates, the Institute for Local Self-Reliance (ILSR), and Merit Network. The broader vision is articulated in:

* [What We Can't See, We Can't Fix](https://www.benton.org/blog/what-we-cant-see-we-cant-fix)

BQT+ advances this platform through agentic system design: decomposing complex ISP interaction processes into reusable, adaptive components that scale across providers while preserving methodological rigor.

BQT/BQT+ has enabled a series of research contributions grounded in rigorous measurement and statistical modeling:

* [Contextualizing Speed Test Measurements](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/speedtest.pdf) (IMC 2022, **Distinguished Paper Award**) — establishing principled modeling of user-perceived performance.
* [Decoding the Divide](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/bqt_sigcomm23.pdf) (SIGCOMM 2023) — introducing address-level broadband pricing measurement for rigorous market analysis.
* [Assessing the Efficacy of the Connect America Fund](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/caf-sigcomm24.pdf) (SIGCOMM 2024, **ANRP Award**) — scalable methodologies for extracting and synthesizing ISP plan data across heterogeneous interfaces.

We are extending this foundation through:

**NetVibe** — an evolving longitudinal latency intelligence platform that connects infrastructure-level performance measurements with user-level experience.

Together, this body of work establishes independent broadband data ecosystems grounded in statistical modeling, systems research, and reproducible infrastructure — capable of informing billion-dollar investment decisions and regulatory accountability.

## Path II — Self-Driving Networks (AI-Powered Network Operations)

Operating networks with limited infrastructure and expertise runs into a second data gap: the labeled, representative data needed to build trustworthy models is scarce, and the tools to generate it at scale are missing.

My group closes that gap through controllable data generation, structured representation learning, and principled evaluation, so that networks can adapt, generalize, and stay trustworthy under dynamic conditions.

### Programmable Data Substrate

We are building a programmable experimentation infrastructure that enables scalable and verifiable network research:

* **[netUnicorn](https://netunicorn.cs.ucsb.edu/)** — distributed orchestration across heterogeneous environments; adopted as a reproducibility substrate.
* **NetReplica** — an evolving bottleneck-aware emulation framework for controlled experimentation.
* **NetGent** — an agentic workflow automation system that compiles high-level specifications into deterministic, reusable execution pipelines.

These systems share a central architectural insight: complex operational tasks become reliable and scalable when decomposed into smaller, verifiable components — a principle mirrored in BQT+.

### Network Foundation Models and Validation

Building on this substrate, we introduced:

* **[netFound](https://arxiv.org/abs/2310.17025)** — a domain-specific network foundation model that learns spatial, temporal, and hierarchical structure directly from packet-level telemetry.
* **NetBurst** — ongoing modeling of bursty, event-driven network dynamics for improved temporal abstraction and forecasting.
* **Intrinsic Evaluation Framework** (NeurIPS 2025) — a representation-level validation methodology decoupling embedding quality from downstream task artifacts.
* **[Trustee](https://trusteeml.github.io/)** (ANRP recognition) — advancing interpretability and structured introspection for learning-based network systems.

netFound and NetBurst are in tech-transfer at ESnet and Google within the DOE Genesis Mission.

This program establishes foundations for agentic and AI-powered network operations that are robust, generalizable, and deployment-aware.

### Deployment and Engagement

We actively engage with the [Energy Sciences Network (ESnet)](https://www.es.net/) to explore how AIOps frameworks can support large-scale scientific infrastructure — advancing adaptive traffic management, scalable telemetry analysis, and AI-driven operational intelligence in production environments.

## Impact & Engagement

Our broadband data work informs regulatory, legislative, and community decisions beyond the research literature.

### Policy Briefs & Reports
* [Create Independent Broadband Data for Public Accountability](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/pffp-brief.pdf), Policy Brief, UC Presidential Faculty Fellows Program, 2026. Presented at the Congressional Staff Briefing "Building Trust in Public Institutions," Dirksen Senate Office Building, Washington DC, May 2026.
* [Broadband Affordability and the BEAD Program: Analysis and Policy Recommendations](https://arnicusc.org/wp-content/uploads/2026/02/Policy-Brief-BEAD-3.pdf), MEDIA Project Phase 3 Report, USC Annenberg, 2026.
* [Beyond Access: Broadband Affordability & Adoption](https://dls.virginia.gov/commissions/jcots/materials/broadband_report_nov_2025.pdf), Research Study, Virginia Joint Commission on Technology and Science (JCOTS), 2025.

### Amicus Briefs
* [Brief of Amici Curiae in Support of Respondents](https://www.supremecourt.gov/DocketPDF/23/23-1127/327232/20241001102442280_23-1127%20Amici%20Brief.pdf), *Wisconsin Bell v. U.S. ex rel. Heath* (No. 23-1127), Supreme Court of the United States, 2024.

### Op-Eds & Public Commentary
* [What We Can't See, We Can't Fix](https://www.benton.org/blog/what-we-cant-see-we-cant-fix), Benton Institute for Broadband & Society, 2026.
* [Measuring Broadband Policy Success](https://harvardlawreview.org/blog/2024/07/measuring-broadband-policy-success), Harvard Law Review Blog, 2024.
* [NetGent: Agent-based Automation of Network Application Workflows](https://blog.apnic.net/2026/02/05/netgent-agent-based-automation-of-network-application-workflows/), APNIC Blog, 2026.
* [Computing Is a Generative Discipline](https://sites.cs.ucsb.edu/~arpitgupta/blogs/computing-is-a-generative-discipline.html), 2026.
* [Systems for Agents, Agents for Systems](https://sites.cs.ucsb.edu/~arpitgupta/blogs/systems-for-agents-agents-for-systems.html), 2026.

### Data Contributions
* [Broadband Competition and Pricing Strategies in California's Urban Markets](https://www.publicadvocates.cpuc.ca.gov/-/media/cal-advocates-website/files/press-room/reports-and-analyses/260114-public-advocates-broadband-competition-and-pricing-strategies-in-california-urban-markets.pdf), California Public Advocates Office (Cal Advocates), CPUC, 2026. Competition and pricing analysis conducted using UCSB's Broadband Query Tool (BQT).
* [Dollars to Megabits: How We Uncovered Disparities in Internet Deals](https://themarkup.org/show-your-work/2022/10/19/how-we-uncovered-disparities-in-internet-deals), The Markup, 2022.

### Community & Policy Engagement
* **BEAD Challenge Process** (2024): provided evidence for Merit Network Inc. to challenge the FCC's National Broadband Map for underserved regions in Michigan.
* **City of Los Angeles** (2024): our data helped catalyze a motion empowering CHRED to act against digital discrimination.
* **#OaklandUndivided** (2023–): used the BQT tool to identify underserved addresses and bridge data gaps for policymaking in Oakland, CA.
* **Institute for Local Self-Reliance (ILSR)** (2023–): gathered BQT data to strengthen the case for community networks.
* **Affordable broadband for multi-dwelling units** (2023–): assessing broadband offerings in MDUs using the BQT tool.
* **Santa Barbara County** (2023): report on the state of broadband affordability shared with the county.

## Representative Systems

* [BQT / BQT+](https://address.cs.ucsb.edu/bqt/) — broadband plan querying tool
* NetVibe — evolving longitudinal latency intelligence platform
* [netUnicorn](https://netunicorn.cs.ucsb.edu/) — distributed orchestration platform
* [netFound](https://arxiv.org/abs/2310.17025) — network foundation model
* NetBurst — event-centric forecasting system
* NetReplica — evolving bottleneck-aware emulation framework
* NetGent — agentic workflow automation system
* Intrinsic Evaluation Framework — representation analysis for network foundation models
* [Trustee](https://trusteeml.github.io/) — interpretability framework for ML-based network systems

### Funding

The research in my group is supported by various government agencies, namely, the National Science Foundation (NSF), the Department of Energy (DoE), as well as different network/content service providers such as Google, Verizon Innovations, ViaSat, and vendors including Intel and Cisco.

| Project | Funding Organization | Start | Amount | Status |
| --- | --- | --- | --- | --- |
| Making Agentic AI Safe for DOE User Facilities | DOE / LBNL LDRD (Co-PI) | Oct 2026 | $250k | Active |
| [Effectively Measuring Broadband Affordability in California](#) | California Public Utilities Commission | Jan 2026 | $275k | Active |
| [Bridging the Representation–Semantics Gap for Production-Ready AI-Powered Network Operations](#) | Cisco | Winter 2026 | $75k | Active |
| [AIOps Roadmap Development for ESnet](#) | DoE | Jul 2025 | $65k | Active |
| [Low Infrastructure ML](https://research.google/programs-and-events/research-scholar-program/recipients/) | Google | Jul 2025 | $100k | Active |
| [Network Foundation Model for Enabling AI-powered Network Operations (AIOps)](https://blog.google/products/google-cloud/ml-systems-junior-faculty-awards/) | Google | Jul 2025 | $60k | Active |
| [Developing Generalizable ML Models for Diverse Learning Problems in Network Operations](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2443777) | NSF | May 2025 | $700k | Active |
| Measuring the Effectiveness of Digital Inclusion Approaches | Pew Charitable Trusts | 2025 | $42k | Active |
| [Characterizing Broadband Pricing in California](#) | California Public Utility Commission | Summer 2025 | $125k | Active |
| [Characterizing Barriers to Digital Inclusion in Virginia](https://dls.virginia.gov/commissions/jcots/materials/broadband%5Freport%5Fnov%5F2025.pdf) | Virginia JCOTS | Jan 2025 | $30k | Active |
| [Telemetry-driven Foundation Models for Self-Driving Networks](#) | Cisco Research | Sep 2024 | $90k | Active |
| [netFound: Network Foundation Model](https://arxiv.org/abs/2310.17025) | DoE | Sep 2024 | — | Active |
| [IMR: MT: NetFlex: A Flexible Scalable & Privacy-Preserving Network Measurement Platform to Iteratively Collect Multi-modal Multi-view Network Data from Access Networks](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2323229) | NSF | Oct 2023 | $600k | Active |
| [IMR: RI-P: Programmable Closed-loop Measurement Platform for Last-Mile Networks](https://nsf.gov/awardsearch/showAward?AWD_ID=2224687) | NSF | Oct 2022 | $100k | Completed |
| [IMR: MM-1A: ADDRESS: Augment, Denoise and Debias Crowdsourced Measurements for Statistical Synthesis of Internet Access Characterization](https://address.cs.ucsb.edu/) | NSF | Oct 2022 | $600k | Completed |
| [The Estimation and Monitoring of Quality of Experience Delivered over Internet Services](#) | ViaSat | Jan 2022 | $200k | Completed |
| [CC\* Integration-Large: Democratizing Networking Research in the Era of AI/ML](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126327) | NSF | Oct 2021 | $1M | Completed |
| [CC\* Integration-Large: Bringing Code to Data: A Collaborative Approach to Democratizing Internet Data Science](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2126281) | NSF | Oct 2021 | $1M | Completed |
| [MLWiNS: RL-based Self-driving Wireless Network Management System for QoE Optimization](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2003257) | NSF & Intel | Jun 2020 | $820k | Completed |
| [Scaling Cybersecurity Infrastructure using Programmable Data Planes](https://www.verizon.com/about/news/verizon-advances-5g-network-and-cyber-security) | Verizon | Sep 2019 | $200k | Completed |
