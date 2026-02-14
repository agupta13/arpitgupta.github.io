---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

## Research Philosophy

In our modern world, the ability to access information and communication technology is not just a convenience but is increasingly seen as a crucial *human right*. This ability is vital for people around the world to derive socio-economical benefits from the Internet by engaging in activities such as education, healthcare, commerce, and civic participation. However, despite years of effort from various stakeholders, a significant *digital divide* persists that sharply separates those with seamless access to the Internet and cutting-edge communication technologies from those who remain underserved. The wide-ranging social and economic consequences of this divide cannot be overstated.

I am committed to pursuing a research agenda aimed at forging a path toward a more equitable digital future.

To this end, my research focuses on two key themes. First, I explore how to advance Artificial Intelligence (AI) and Machine Learning (ML) for cybersecurity, with a special emphasis on democratizing the development of **production-ready AI/ML artifacts**. This initiative primarily aims to lower the threshold for collecting the *right* data for training ML models. Such ML models would be especially beneficial in network environments with limited budgets, operational capacity, and technical expertise. These environments are poised to benefit greatly from AI and ML advancements but are challenged in tapping into these technologies due to the high thresholds for developing trustworthy and generalizable ML artifacts.

The second area concerns Internet measurement research, with an emphasis on enabling **data-driven policymaking**. This approach centers around providing policymakers with access to the *right* data, which aids in evaluating existing policies and informing the syntheses of new policies. This effort is crucial for optimizing the use of limited capital resources to benefit underprivileged communities, thereby addressing their specific needs more effectively.


### Production-ready ML for Networks --> Self-driving Networks

<!-- The two research themes complement each other as one helps identify underserved communities that require any policy interventions, and the second helps realize a subset of interventions (e.g., sustainable community networks).  -->



 <!-- **self-driving networks** that can run themselves with minimal intervention.
Given our group's focus on **digital equity** issues, we focus primarily on building self-driving network for **last-mile (community) networks**.
Our goal is to lower the cost of deploying and operating highly *available*, *reliable*, *performant*, and *secure* last-mile networks in under-served communities. -->
According to the report from the National Security Commission on AI, advancements in AI have empowered malicious actors, thereby increasing the vulnerability of our digital ecosystems to various cyber threats. To counter this rising threat, we need an AI-enabled cybersecurity stack equipped with numerous intelligent modules or bots. Their collective input should enable the extraction of subtle trends in data, identify diverse attack vectors and workflows, and assist in synthesizing appropriate defense policies to neutralize these threats. Moreover, it is crucial to democratize access to this AI-enabled cybersecurity stack, which we refer to as **self-driving networks**.

The goal is to develop an AI-enabled stack that keeps the network secure and performant while requiring minimal human interventions. Specifically, we explore how to leverage machine learning (ML) and software-defined networks (SDN) to lower the cost of deploying and operating highly *available*, *reliable*, *performant*, and *secure* last-mile and enterprise networks.

Developing self-driving networks requires solving various fundamental research problems, which includes answering how we can
* Enable **accurate and flexible (streaming) analytics** over network data at scale (see [Sonata](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/sonata.pdf), [DynamiQ](https://arxiv.org/pdf/2106.05420.pdf), [Panakos](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/speedtest.pdf), [OpTel](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/OpTel_camera_ready.pdf));
* Lower the threshold to **curate high-quality datasets** for different learning problems from diverse network environments at scale (see [PINOT](https://pinot.cs.ucsb.edu/), [netUnicorn](https://netunicorn.cs.ucsb.edu/));
* Develop **production-ready ML artifacts** that can both accurately assess the network's state and take effective actions to keep networks performant and secure (see [netUnicorn](https://netunicorn.cs.ucsb.edu/), [Trustee](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf)); and
* **Establish trust** in ML-based artifacts so network operators feel confident enough to relinquish control to these artifacts in production settings (see [Trustee](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf)).
* ...

### Data-driven Policymaking
The goal here is to develop tools and infrastructures that enable collecting the *right* data that can inform policy interventions targeting digital equity, including consumer subsidy programs, rate regulations, infrastructure funding, etc.

Addressing the data problem for policymakers entails solving various fundamental research problems, which includes answering
* What broadband plans, which includes both speed and price, are available in a region? See our [SIGCOMM paper](ttps://sites.cs.ucsb.edu/~arpitgupta/pdfs/bqt_sigcomm23.pdf) for details.
* How to make the best use of noisy crowdsourced network measurement data? See our [IMC paper](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/speedtest.pdf) on this topic for more details.
* How to quantify the efficacy of different policy interventions (e.g., consumer subsidies, rate regulations, etc.)?
* ...

### Ongoing Projects
Some of the projects that provide a decent sample of ongoing research activities at SNL:

- [Trustee](https://trusteeml.github.io/): A framework that cracks open decision-making for black-box ML models (for networks) using high-fidelity, low-complexity, and stable decision trees.
- [BQT](https://address.cs.ucsb.edu/bqt/): A tool that queries broadband plan offerings from major ISPs in the US at street-level granularity.
- [PINOT](https://pinot.cs.ucsb.edu/): A programmable data-collection infrastructure at UCSB to collect fine-grained (labeled) network data at scale.
- [netUnicorn](https://netunicorn.cs.ucsb.edu/): A data-collection platform that simplifies collecting network data for different learning problems from diverse network environments.
- [netFound](https://arxiv.org/pdf/2310.17025.pdf): A foundation model for networking data that employs self-supervised learning techniques on abundant unlabeled network data, passively collected from production environment using [PINOT](https://pinot.cs.ucsb.edu/) for task-agnostic pre-training and smaller-scale labeled network data, actively collected using PINOT and [netUnicorn](https://netunicorn.cs.ucsb.edu/) for task-specific fine-tuning.



<!-- - [Trustee](https://trusteeml.github.io/): A framework that cracks open decision-making for black-box ML models (for networks) using high-fidelity, low-complexity, and stable decision trees.
- [PINOT](https://pinot.cs.ucsb.edu/): A programmable data-collection infrastructure at UCSB to collect fine-grained (labeled) network data at scale.
- [netUnicorn](https://netunicorn.cs.ucsb.edu/): A data-collection platform that simplifies collecting network data for different learning problems from diverse network environments. -->



<!-- ### Related Publications
Some of the recently published works that provide a sample of some of the ongoing activities at SNL:
- [AI/ML for Network Security: The Emperor has no Clothes](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf), ACM CCS, 2022.
- [The Importance of Contextualization of Crowdsourced Active Speed Test Measurements](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/speedtest.pdf), ACM IMC, 2022.
- [Detecting Ephemeral Optical Events with OpTel](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/OpTel_camera_ready.pdf), USENIX NSDI, 2022.
- [Internet Inequity in Chicago: Adoption, Affordability, and Availability](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/2022_tprc_chicago_digital_divide-submitted.pdf), TPRC, 2022.
- [DynamiQ: Planning for Dynamics in Network Streaming Analytics Systems](https://arxiv.org/pdf/2106.05420.pdf),
arXiv: Report 2106.05420, 2021.
- [An Effort to Democratize Networking Research in the Era of AI/ML](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/democratize_netai.pdf), ACM HotNets 2019. -->



<!-- machine learning (ML) and
programmable network data planes to develop *low-cost* last-mile networks that can provide highly *available*, *reliable*, *performant* and *secure* network connectivity to underrepresented and under-served communities.

<!-- The growing popularity of networked devices and applications imposes
increasingly stringent security- and performance-related requirements on the
underlying communication fabric. Satisfying these ever-increasing demands with
limited infrastructure and operational budgets are challenging for the network
operators. -->

<!-- My research combines the flexibility of **programmable data-plane targets** and
the intelligibility of **ML algorithms** to develop ML-based artifacts for
networking that bridge the fundamental gap between requirements and resources.
Additionally, my research focuses on ensuring that network operators can
**trust** these ML-based artifacts enough to deploy them in production
settings.  -->

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





<!-- ## Ongoing Projects

### Programmable Data-Collection Infrastructure/Platform(s)

### Flexible and Scalable Network Data Analytics System(s)

### ML Pipeline for Learning Problems in Networking -->


<!-- ## Past Projects -->

<!-- The proposed research will help catalyze adoption of ML-based solutions for network operations, which will form the intellectual foundation for future self-driving networks. My academic career to this point has prepared me to pursue this goal with an extensive experience in developing open-sourced networked systems, such as SDX~\cite{sdx}, iSDX~\cite{isdx}, Sonata~\cite{sonata-paper}, DynamiQ~\cite{dynamiq}, Optel~\cite{optel}, etc., that have been widely used in both academia and industry.  -->
