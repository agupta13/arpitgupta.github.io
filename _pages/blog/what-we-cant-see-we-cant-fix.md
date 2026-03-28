---
title: "What We Can't See, We Can't Fix"
permalink: /blogs/what-we-cant-see-we-cant-fix.html
redirect_from:
  - /blog/what-we-cant-see-we-cant-fix.html
layout: single
author_profile: true
date: 2026-01-14
---

<p class="page__subtitle" style="font-size: 0.9em; color: var(--muted); margin-top: -0.5em; margin-bottom: 1em;">Originally published by the Benton Institute for Broadband &amp; Society (2026)</p>

As part of my fellowship with the Benton Institute for Broadband & Society, I had the opportunity to reflect on my journey toward bridging fundamental data gaps in broadband policymaking, and on the challenges and opportunities that lie ahead. This essay discusses what inspired the genesis of the Broadband-Plan Querying Tool (BQT), its evolution into BQT+, and our broader vision for building an independent and accessible broadband data infrastructure—one that is sufficiently extensive to support diverse current and future policy workloads, while remaining accessible with minimal technical expertise. This work would not have been possible without my students, Udit Paul and Laasya Koduru, and my collaborators Elizabeth Belding and Tejas N. Narechania, whose support and guidance have been invaluable.

I often start talks about broadband policy with a deceptively simple question: How do we really know who has access to affordable, reliable Internet?

It's a question that should be easy to answer in 2025—after all, broadband is the nervous system of modern life. Yet for all the billions of dollars spent to expand broadband availability, the truth is that we still don't have trustworthy, street-level data on who can connect, at what quality, and at what price. That absence of accurate information doesn't just limit research; it distorts how public money is spent and who that money ultimately serves.

For the past four years, our team at the University of California, Santa Barbara has tried to fix that. We built the Broadband-Plan Querying Tool, or BQT—a system that independently measures broadband availability and affordability by mimicking what any consumer can do: visit an Internet provider's website, enter an address, and record what plans, speeds, and prices appear. What started as a research prototype to verify the accuracy of provider claims has since evolved into a zero-code, machine-learning-driven platform that aspires to make broadband data collection accessible to everyone.

This post is about that journey—why we built BQT, what it revealed about the limitations of existing data, how it has informed federal and state policymaking, and why I believe the data infrastructure, enabled by tools like BQT, represents an essential public good.

## The Policy Paradox

In the United States, broadband has long been treated as both a private market and a public necessity. This tension between those identities shapes an enduring broadband policy problem: how to ensure that the private market provides this public necessity to everyone. Over the past few decades, programs such as the [Connect America Fund (CAF)](https://www.fcc.gov/general/connect-america-fund-caf), the [Rural Digital Opportunity Fund (RDOF)](https://www.usac.org/high-cost/funds/rural-digital-opportunity-fund/), and now the [Broadband Equity, Access, and Deployment (BEAD)](https://broadbandusa.ntia.gov/funding-programs/broadband-equity-access-and-deployment-bead-program) Program have poured more than $100 billion into expanding broadband availability. Yet millions of households remain unserved or priced out.<sup>1</sup>

A paradox lies in the quality of data used to make funding decisions. More concretely, every one of these funding initiatives depends on knowing where broadband exists and the quality of service in those locations. Yet most decisions about where to fund new and improved infrastructure have historically been guided by the Federal Communications Commission's Form 477, which relied almost entirely on self-reported "private" data from Internet service providers (ISPs), lacked independent validation, and contained known errors. FCC's Form 477 data reported at census block granularity contributed to the overassessment of broadband availability in a region. For example, if an ISP were serving a single household in a census block, it could report the entire block as "served."

This historical problem was addressed by the creation of the national fabric and the national broadband map through the [FCC's Broadband Data Collection](https://www.fcc.gov/BroadbandData) program, established by the [Broadband Data Act](https://www.congress.gov/bill/116th-congress/senate-bill/1822). ISPs now report the availability of broadband and the top advertised speed at street address granularity—addressing Form 477's critical limitation. However, there is no independent verification of the ISPs' claims, leaving a data infrastructure built on trust rather than evidence.<sup>2</sup> Over the years, journalists and local officials have repeatedly caught inaccuracies—addresses reported as "served" where no service exists<sup>3</sup> and unexplained flips in technology types.<sup>4</sup> Consequently, when the FCC published its new National Broadband Map, state broadband offices across the country filed thousands of challenges to dispute ISPs' claims. The fundamental problem remained: public programs were being guided by private data.

Moreover, these efforts to map broadband only focus on reporting service availability and quality (top speeds). The resulting data offers no insight into the state of broadband affordability. Assessing broadband affordability requires understanding different speed tiers and prices that an ISP offers, none of which is reported to the FCC.

## Building an Independent Mirror

In 2021, my student, [Udit Paul](https://u-paul.github.io/), and I began wondering if we could bypass these ISP self-reports entirely. The idea was simple: why not collect data the same way consumers see it?

That question served as the foundation for the Broadband-Plan Querying Tool (BQT). Instead of asking providers for data, we asked their websites. We automated the process of entering a residential address into a provider's "check availability" page and recording the resulting plans, speeds, and prices.

Technically, it was messy. Each ISP website had its own layout and interface logic; some websites relied on dynamically loaded content or CAPTCHA-style defenses. But with patience and a small team of capable students, we built scripts that could replicate a user's clicks and keystrokes. Over time, we scaled those scripts to millions of addresses.

What emerged was an independent, reproducible picture of broadband availability and affordability—one drawn directly from ISPs' publicly advertised offerings.

## What We Found

Led jointly with Tejas Narechania and my UCSB colleague Elizabeth Belding, the first large-scale analysis using BQT, [Decoding the Divide](https://dl.acm.org/doi/pdf/10.1145/3603269.3604831) (SIGCOMM 2023), examined plan data from major U.S. providers across dozens of markets. The results were sobering. We observed that cable providers offered nearly identical "bad deals" when competing with DSL providers—behaving effectively as monopolies—but priced their plans approximately 30 percent lower when competing with fiber providers.

In essence, the study demonstrated that markets are not competitive just because of the presence of more than one provider in a region. Instead, the technology used by competing providers determines whether the benefits of competition are passed on to end users, thereby improving broadband affordability. These patterns suggest a possible policy intervention for affordability: if fiber competition improves affordability, encouraging fiber deployment could drive down prices. Current policy initiatives primarily fund the entry of a single ISP into underserved locations, creating a regulated monopoly that may improve broadband availability in a region but not necessarily affordability. An expensive service may ultimately lead to poor adoption and market failures.

The [next study](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/caf-sigcomm24.pdf) we conducted asked: Did prior federal programs deliver what they promised? The [Connect America Fund](https://www.fcc.gov/general/connect-america-fund-caf), launched in 2011, allocated roughly $10 billion to subsidize broadband in high-cost, mostly rural regions. ISPs that received funding to build and offer broadband service self-certified the addresses they served and what speeds they offered. Yet those certifications were never independently verified. Using BQT, we audited more than half a million CAF-funded addresses across 15 states.<sup>5</sup>

Our findings were striking: only 55 percent of ISP-certified addresses could actually obtain service, and just 33 percent met the FCC's speed and price requirements. Many rural areas—especially those targeted for subsidy—still lacked the service ISPs claimed to provide.

These findings are timely, as the federal government is investing billions of dollars in broadband infrastructure through the BEAD Program. More concretely, the study of CAF retrospectively shows that the previous $10 billion effort to improve broadband availability in rural America failed to achieve its intended goals. Our research underscores the urgent need to develop an open, transparent data infrastructure to establish a baseline for the BEAD Program and proactively track changes in broadband availability and affordability in BEAD-eligible regions. Such a data infrastructure would ensure we have the data needed to monitor BEAD's progress and support timely interventions, thereby increasing the likelihood that the program reaches its intended objectives.

Our results were impactful beyond academia. They appeared at legislative hearings, in press briefings, and eventually in an [amicus curiae brief to the U.S. Supreme Court in Wisconsin Bell v. United States](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4973313), a case involving broadband fraud under the False Claims Act. For the first time, independent data collected through automation informed both legal and policy accountability.

But BQT also revealed its own limitations.

## The Fragility of First-Generation Tools

Every time an ISP redesigned its website, BQT's scripts broke. Adding a new ISP for data collection required days of manual coding. For policymakers or community advocates without technical backgrounds, it would be impossible to run the tool.

This fragility underscored a deeper challenge: how to make broadband data collection democratic, not just independent. We needed a system that could evolve as websites changed, adapt to additional ISP sites, and be usable by people with no programming experience.

That realization motivated our team to pursue an additional goal: lowering the barrier to making BQT extensible to new ISPs and robust to changes in currently supported ISPs, thereby paving the way for the next‑generation iteration of BQT, which we refer to as BQT+

## From BQT to BQT+: Learning to Imitate Humans

BQT+ re-imagines data collection as a learning problem rather than a set of static scripts. At its core, the system treats each ISP's website as a finite-state machine—a sequence of states (enter address, confirm location, view plans) and transitions (click, scroll, submit). By recording a small number of human interactions, BQT+ "learns" this workflow automatically.

To interpret pages that change dynamically, we incorporated optical character recognition (OCR)—the same technology used in document scanners—to detect the position of buttons and text on the screen. The tool then uses a lightweight automation engine (PyAutoGUI) to move the cursor, click, and type as a human would.

This design makes BQT+ far more resilient. If an ISP updates its website layout or changes a button label, the system can often adapt without manual re-coding. Integrating a new ISP now takes hours rather than days. We built caching and verification layers so that identical inputs (the same address) always yield identical outputs. That repeatability is crucial for any policy dataset and transformed BQT+ from a research prototype into a measurement instrument.

This was a massive undertaking, but my student, [Laasya Koduru](https://lmkoduru.github.io/), embraced it wholeheartedly. She saw not just the technical challenge, but the bigger opportunity: turning BQT into something that could truly democratize access to broadband data.

## Putting BQT+ to Work

With BQT+ ready, we began tackling the next frontier: evaluating BEAD, the largest broadband funding program in U.S. history. Our vision is to create a data infrastructure that first establishes a baseline for BEAD-eligible locations—specifically, to understand whether, and what types of, plans are currently offered to these locations, thereby providing an assessment of their existing broadband quality and price. This initial effort helps determine whether BEAD funds are targeting the right places and, more importantly, establishes a baseline before any BEAD-induced changes in broadband quality and affordability occur. Subsequently, collecting this data iteratively to track changes will allow us to quantify the impact of BEAD funding in achieving its intended goals.

To this end, in partnership with USC Annenberg Professors [Hernan Galperin](https://annenberg.usc.edu/faculty/hernan-galperin) and [Francois Bar](https://annenberg.usc.edu/faculty/fran%C3%A7ois-bar), and with support from the [Pew Charitable Trusts](https://www.pewtrusts.org/), we used BQT+ to establish a baseline of broadband service in BEAD-eligible census block groups across California, Michigan, Oklahoma, and Virginia—covering approximately 63,000 residential addresses in total.

The results helped characterize the current state of broadband quality and affordability in BEAD-eligible areas of these four states. Many regions lacked access to 100/20 Mbps plans, and the low-cost options available were unaffordable for most low-income households. More concretely, the share of BEAD-eligible census blocks without access to a 100 Mbps plan ranged from about 20 percent in California to 85 percent in Oklahoma. Similarly, the share of blocks with unaffordable offerings—defined as plans priced above an income-based affordability threshold —ranged from 65 percent in California to 85 percent in Michigan. Note that the affordability threshold is computed by relating advertised monthly broadband prices to local household income distributions, following long-standing federal policy guidance<sup>6</sup> that treats broadband as affordable only if subscription costs constitute a small, bounded fraction of household income for low-income households. Under this framework, plans that may appear inexpensive in absolute terms can still be unaffordable in low-income regions once income constraints are taken into account.

These observations underscore persistent affordability challenges across BEAD-eligible regions and indicate that the program's funds are indeed targeted at the right areas. Importantly, these findings also bring the role of pricing oversight into sharper focus. While BEAD does not impose traditional retail price regulation, prior federal broadband programs operationalized affordability through income-based benchmarks and low-cost service expectations for subsidized networks. The National Telecommunications and Information Administration's [June 2025 policy notice](https://www.ntia.gov/sites/default/files/2025-06/bead-restructuring-policy-notice.pdf) limits states' ability to impose such price-related conditions on BEAD-funded deployments. In the absence of comparable mechanisms, BEAD investments may expand availability and improve service quality while still failing to translate into affordable offerings for low-income households, ultimately jeopardizing adoption and equity objectives.

Our results have also given policymakers a powerful way to track progress over time—to compare broadband availability and pricing before and after BEAD funding flows. For the first time, the baseline measurement itself is built from independently verifiable data, not provider declarations.

At the state level, we partnered with the [Virginia Joint Commission on Technology and Science (JCOTS)](https://dls.virginia.gov/commissions/jcots/materials/broadband_report_nov_2025.pdf) to show how BQT+ can transform broadband policymaking from a reactive exercise into an evidence-driven process. By systematically querying ISP websites across ten Virginia localities, representative of the state's geographical, demographic, and socioeconomic diversities, BQT+ generated the Commonwealth's first independently verifiable dataset on broadband affordability and availability at the street-address level. This analysis revealed clear regional disparities—particularly between rural and suburban areas—and provided a concrete foundation for policy design.

The data enabled JCOTS to craft several targeted recommendations to improve affordability and equity. Among them were calls to ensure that low-cost broadband plans are more visible and accessible to the public, and to establish a baseline affordability standard that requires providers to offer at least one 100 Mbps (download speed) plan for $30 per month or less. The study also highlighted the need for targeted tax incentives to sustain near-universal affordability and for a dedicated state grant program to fill gaps in broadband affordability left by BEAD and the termination of Digital Equity Act funding.

Taken together, these insights illustrate how independent, verifiable data can enable states to move beyond making policy with data that has known limitations and quality concerns, toward prescriptive, data-informed policymaking grounded in datasets that better reflect on-the-ground realities—where broadband access and affordability are not merely measured, but meaningfully improved.

## Data as Infrastructure

Through these studies, one conviction has grown stronger for me: independent broadband data is itself infrastructure.

We often think of infrastructure as physical—fiber, towers, routers—but data infrastructure underpins every policy decision about where to build and whom to serve. When that data is inaccurate or proprietary, public programs become guesswork.

BQT+ demonstrates that it's possible to build an independent data infrastructure that is transparent, verifiable, and accessible. By automating what consumers already do and presenting the results in aggregate, we can hold providers accountable while minimizing the data collection cost, both in terms of the manual effort it entails as well as the networking and computing overheads.

## Making Independence Accessible

Still, independence alone isn't enough. For broadband measurement to truly serve the public interest, it must be accessible.

Our journey from BQT to BQT+ lowers the threshold for the programming know-how needed to extend BQT to additional ISPs and make it robust to changes on ISPs' websites. However, we have a long way to go to make BQT truly accessible to a broader set of stakeholders with minimal technical expertise. To this end, our long-term vision for BQT is to evolve from a research system into a Software-as-a-Service (SaaS) platform—a zero-code web interface that enables state agencies, nonprofits, and community organizations to select regions, run queries, and download standardized data without writing a single line of code.

Imagine a local broadband office being able to verify, in real time, what plans residents in a given ZIP code actually see online, or a journalist comparing advertised prices across counties with a few clicks. That's the future we're building toward.

But building a public-facing service that operates responsibly takes time and resources. BQT interacts with live ISP websites, so we must ensure that every automated query is rate-limited to avoid overwhelming ISPs' websites with excessive querying. We also have to develop interfaces that make complex data intuitive without oversimplifying it.

Right now, my team is piloting controlled deployments to refine these workflows. BQT+ is not yet publicly available, and for good reason: we want to ensure that when it is, it genuinely empowers users rather than burdening them with technical or ethical pitfalls. Our priority is to make the system meaningfully accessible—reliable in what it measures, easy to use, and sustainable in operation.

## The Broader Vision

When I step back, I see BQT as part of a larger movement to democratize digital measurement. In networking research, we've spent decades building tools that test speed or reliability. But those tools often stop at the network's edge; they tell us how fast a connection is, not whether people can afford it. BQT fills that gap by linking measurement to lived experience. BQT captures the marketplace as consumers see it—what choices they actually have and at what cost. That perspective is essential for accountability.

Independent broadband data also creates opportunities for collaboration between disciplines. Our work with Tejas Narechania has shown how computer scientists and legal scholars can combine methods: technical automation, validating policy claims, and legal analysis, shaping data governance. Together, we can craft not only better measurements but better mechanisms for oversight.

## Why Independent Data Is a Public Good

At its core, the debate over broadband data mirrors the debate over broadband itself. Access to high-quality information about essential services should not depend on proprietary systems or corporate goodwill. When only providers can see the full picture, policymakers and the public are forced to take their word for it.

Treating broadband data as a public good means building and maintaining tools that anyone can use to verify claims, evaluate programs, and advocate for equity. It means funding not just fiber but facts.

Independent datasets, like those produced by BQT, complement rather than replace official FCC efforts. They provide a check—a mirror to keep the public record honest. In that sense, investing in data infrastructure is an act of democratic stewardship.

## A Call for Collaboration

As a Benton Fellow, I've had the privilege of working alongside advocates, researchers, and policymakers who share a common goal: making the Internet work for everyone. Tools like BQT+ can accelerate that mission only if they are built collaboratively.

We're now seeking partners—state broadband offices, community organizations, researchers, and philanthropic foundations—interested in supporting and piloting the zero-code, SaaS-based version of BQT. We welcome collaborations that help us test usability, expand ISP coverage, and align data outputs with policy needs.

The task ahead is both technical and civic. Building a trustworthy data infrastructure requires sustained investment, not one-off grants. But the payoff is transformative: a transparent, replicable system that ensures broadband investments reach the people who need them most.

Benton's role—as a convener, a bridge between research and policy—remains vital here. By fostering collaborations across academia, government, and civil society, we can turn independent data collection into a shared national asset.

## Looking Forward

As BQT continues to evolve into a SaaS platform, we plan to broaden its scope beyond fixed broadband to include all fixed-wireless and satellite ISPs, assess the state of broadband adoption at different granularities, and link our datasets with performance measurements of actual user experience.

Our ambition is simple but enduring: to create a transparent, sustainable data ecosystem that allows every policymaker, journalist, and citizen to see the broadband landscape clearly.

Reliable connectivity is now as fundamental as electricity or water. Ensuring its equitable distribution requires reliable data. Independent measurement tools like BQT+—built through collaboration, guided by accountability, and shared as public infrastructure—are how we get there.

---

*Arpit Gupta is an Associate Professor of Computer Science at the University of California, Santa Barbara, a Faculty Scientist at Berkeley Lab, and a Benton Institute Fellow.*

## Notes

1. [FCC-16-38A1](https://docs.fcc.gov/public/attachments/FCC-16-38A1.pdf), [Pew: Is broadband affordable for middle-class families?](https://www.pew.org/en/research-and-analysis/articles/2023/08/30/is-broadband-affordable-for-middle-class-families)
2. CAF's goal was to bring service to more than 6 million addresses.
3. [SIGCOMM 2024](https://dl.acm.org/doi/pdf/10.1145/3646547.3688441)
4. [IMC 2020](https://dl.acm.org/doi/pdf/10.1145/3419394.3423652), [Broadband Breakfast: FCC fine for false broadband claims](https://broadbandbreakfast.com/fcc-imposes-10-000-fine-on-isp-for-false-broadband-claims/), [Consumer Reports: FCC broadband map](https://www.consumerreports.org/electronics/broadband/fcc-broadband-map-federal-funding-a598688349)
5. [The Broadband DATA Act (2020)](https://www.congress.gov/116/plaws/publ130/PLAW-116publ130.pdf) made it unlawful for providers to "willfully and knowingly, or recklessly, submit information or data that is materially inaccurate or incomplete" regarding broadband availability or quality. In addition, the law calls for "regular audits of information submitted to the Commission by providers." Nonetheless, FCC action against some providers demonstrates that there is misrepresentation.
6. [CAF](https://www.fcc.gov/consumers/guides/connect-america-fund-phase-ii-faqs) and [RDOF](https://www.usac.org/high-cost/funds/rural-digital-opportunity-fund/) Program requirements called for providers to "offer rates reasonably comparable to rates in urban areas." By law, BEAD-supported networks must offer low-cost service options, as determined by ISPs, for eligible low-income households.

<p class="page__content-source" style="font-size: 0.85em; color: var(--muted); margin-top: 2em;"><a href="https://www.benton.org/blog/what-we-cant-see-we-cant-fix">Originally published at Benton Institute for Broadband &amp; Society.</a></p>
