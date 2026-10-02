---
title: "Making the \"Net\" Work in the Agentic Era"
permalink: /blogs/making-the-net-work-in-the-agentic-era.html
redirect_from:
  - /blog/making-the-net-work-in-the-agentic-era.html
layout: single
author_profile: true
date: 2026-10-02
---

<div class="tex2jax_ignore" markdown="1">

On September 29, I spoke at [AI in Action: Conversations with UCSB Researchers](https://www.library.ucsb.edu/events-exhibitions/events/ai-in-action), a speaker series the UCSB Library started this year. The series is co-led by the UCSB Library and the UCSB AI Community of Practice's AI for Research Special Interest Group. Its goal is an open, interdisciplinary community exploring how AI can "deepen understanding, expand access to knowledge, and inspire new forms of scholarship." Each session pairs short talks by UCSB researchers with a moderated discussion, and the events are free and open to the public.

I shared the [fourth session](https://www.library.ucsb.edu/events-exhibitions/ai-action-miguel-eckstein-arpit-gupta) with Miguel Eckstein, whose talk, "Why We Look Where We Look," showed how building human visual traits into an AI agent helped explain how we move our eyes. My talk was about networks: how my group uses AI to inform broadband policy, to accelerate networking research, and to move toward networks that run themselves. This post is the written version of that talk.

{% include base_path %}
*You can also step through the talk itself: the [annotated slides]({{ base_path }}/annotated-talks/making-the-net-work-in-the-agentic-era/) pair each slide, build by build, with what I said.*

## Who can make a difference?

The Internet is the foundation of our modern digital lives. We rely on it for governance, education, healthcare, finance, and work. But unfortunately, it does not work for all. So my research focuses on one question: how do we make secure and performant Internet access affordable for all?

When we say affordable, someone has to bear the cost: the cost of building networks and the cost of operating them. So who can make a difference? There are three key players: users, service providers, and policymakers. Service providers include both Internet service providers (ISPs) and content providers like Google and Amazon.

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-stakeholders.svg" alt="Three key players: policymakers, service providers, and users. Policymakers lower the cost of building networks; service providers lower the cost of operating them." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">The three key players. Each of my two research thrusts targets one of the two costs.</figcaption>
</figure>

Policymakers can lower the capital expense through data-driven policymaking, so that federal dollars go where networks are not profitable to deploy. Service providers, in turn, can lower the operational expense through self-driving networks that run themselves with minimal human intervention. Both of these efforts depend on better data.

## Data-driven policymaking

### How do we know if these programs are really working?

Let me start with policymakers and the cost of building networks. We have invested more than 100 billion dollars in the past 30 years to subsidize broadband in rural, hard-to-serve areas. But how do we know if these programs are really working?

To answer that, we need data. In most cases, the data policymakers have is self-reported by the ISPs: data about availability, quality, and cost. The problem is that this data is known to be unreliable and noisy. ISPs have admitted to misreporting it, intentionally or unintentionally. So the question is, how do we reduce our reliance on self-reported data from ISPs?

### Readily available information

About five years ago, our team observed that ISPs already give this information to every potential customer. If you enter your address on an ISP's website, it tells you whether broadband is available at your address, at what speed, and at what cost. So the question we had was: this information is available, but can we collect it at population scale?

That motivated our work on [BQT](https://bqt.cs.ucsb.edu/), the Broadband-Plan Querying Tool. It queries ISP websites the way a real user would and extracts the advertised plans. We describe it in [Decoding the Divide](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/bqt_sigcomm23.pdf) and its successor, [BQT+](https://arxiv.org/abs/2602.16969). So far it has queried more than 1.5 million addresses across more than 100 ISPs. It is now the go-to tool for most state broadband offices, as well as for federal agencies.

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-twopaths.svg" alt="Today, policymakers rely on self-reported ISP data. With BQT, they get the plans ISPs advertise to customers, collected address by address." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">Two ways to learn what an ISP offers at an address.</figcaption>
</figure>

### Auditing the Connect America Fund

With this capability, we wanted to know whether the existing 100 billion dollar programs work. So we focused on the Connect America Fund (CAF), a 10 billion dollar program. It subsidized ISPs to serve around 6 million hard-to-serve rural addresses at 10 Mbps download and 1 Mbps upload. At the end, ISPs certified the addresses they served and the speeds they offered. We asked two questions. Are ISPs truthful? And are ISPs compliant? What do you guess?

This 10 billion dollar program failed miserably. ISPs served only about 55 percent of the addresses they certified, and only 33 percent of addresses got 10 Mbps. Today's broadband standard is much higher than that. Zooming in on Georgia, the areas where serviceability is relatively high sit close to the metro areas. The areas left out are the remote rural regions this program primarily targeted. The full audit is in our [SIGCOMM 2024 paper](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/caf-sigcomm24.pdf).

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-caf.svg" alt="Connect America Fund audit: of the addresses ISPs certified as served, about 55 percent were served and about 33 percent were offered 10 Mbps or more." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">The CAF audit, a 10 billion dollar program for more than 6 million mostly rural addresses.</figcaption>
</figure>

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-georgia.jpg" alt="Map of Georgia showing serviceability rate across CAF areas. Darker green areas, where serviceability is high, cluster near Atlanta and other metro areas; light areas across the remote rural south and east have low serviceability." style="max-width: 520px; width: 100%; height: auto; display: block; margin: 0 auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">Serviceability across Georgia's CAF areas. Darker green means higher serviceability; it clusters near the metro areas.</figcaption>
</figure>

### How can AI help?

This reinforces our belief that we need public-good infrastructure like BQT operating at scale. So how can AI help? First, it lowers the entry barrier. We built BQT-SaaS, where policymakers ask in natural language and our agents answer from the data we have or start new queries on BQT. Second, it lowers the engineering overhead of collecting data at scale and maintaining the software.

### Grand challenge: measure broadband quality at scale

But BQT only measures what ISPs advertise. It does not measure what users actually experience. Measuring what users experience has been a holy grail problem in network measurement for 30 years. AI now makes it possible to try. Can we take low-quality measurement signals, synthesize the quality of experience across a wide range of applications, attribute the reasons when it is poor, and do all of this with minimal overhead?

## Self-driving networks

So far, I have talked about where networks get built and whether the federal dollars get there. Once a network is built, someone has to operate it, and that cost falls on the service providers. That brings me to the second thrust: self-driving networks.

In a typical network today, a human operator monitors telemetry data and makes control decisions. The idea with self-driving networks is to replace that loop with production-ready machine learning models. This is critical in lowering the cost of operating secure and performant networks.

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-loop.svg" alt="Today a human operator sits between monitoring and control. In a self-driving network, production-ready machine learning models replace the human in that loop." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">A self-driving network replaces the human in the monitor-and-control loop with machine learning models.</figcaption>
</figure>

### Generalizability problem

However, the fundamental problem is that these models fail to generalize. In most cases they are underspecified: they learn shortcuts, fail on out-of-distribution samples, or pick up strong but wrong relationships in the data. [Our own work](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf) showed that most models in networking fail to generalize. The reason is that we train them on underspecified data, and we lack access to the right data.

### Data generation challenge

So my research agenda has focused on the data generation challenge. Past efforts are fragmented: for every learning problem, people build their own data pipeline. As a community, we need a thin waist that can generate data for any intent from any network.

Building this thin waist is the goal my research group has worked on for the past five years. [NetUnicorn](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/netUnicorn.pdf), [NetGent](https://arxiv.org/abs/2509.00625), and [NetReplica](https://arxiv.org/abs/2507.13476) each disaggregate a different part of the data generation stack. Together, they let us generate data for any intent from any network. As with BQT, running this as a reliable public infrastructure is hard.

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-thinwaist.svg" alt="Fragmented: each learning problem has its own data pipeline. Thin waist: one shared data generation layer, built from NetGent, NetUnicorn, and NetReplica, serves any intent on any network." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">From one pipeline per learning problem to a thin waist for data generation.</figcaption>
</figure>

### How can AI help?

So again, how can AI help? In the same two ways. We built [Pramana](https://arxiv.org/abs/2607.26352), the subject of our upcoming HotNets paper. It lowers the entry barrier for researchers, who can express data generation intents for any infrastructure and any problem. And it takes on the engineering overhead, so this runs as a reliable and sustainable public-good infrastructure at scale. Pramana also supports AI-powered research beyond network management: it grounds the new ideas and hypotheses that AI can now generate in real network data.

### Grand challenge: break the trilemma barrier

With better data, we can build models that generalize. But letting these models run a network on their own raises a harder question, and that is our second grand challenge. Some of you have already heard of the AI agent trilemma, a term coined by Arvind Narayanan in his [ICML 2026 keynote](https://www.cs.princeton.edu/~arvindn/talks/icml-2026-annotated-slides/#s16): a system can be general-purpose, automated, or trusted with high-stakes decisions, and you only get two at a time. A self-driving network needs all three. So the question is, can we build self-driving networks that break the AI trilemma barrier?

{% include base_path %}
<figure style="margin: 1.5em 0;">
  <img src="{{ base_path }}/images/blog/making-the-net-work-in-the-agentic-era-trilemma.svg" alt="The AI agent trilemma: general-purpose, high-stakes, automated. Today you only get two of the three. BQT-SaaS is general-purpose and high-stakes, so a person approves its plans. A self-driving network needs all three." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.9em; color: var(--muted); margin-top: 0.5em;">The AI agent trilemma, a term coined by Arvind Narayanan (ICML 2026 keynote, slide 16).</figcaption>
</figure>

Until we do, we need to prepare for systems with a human in the loop. Even in BQT-SaaS, the agent asks the user to approve before it runs anything. And those people need to reason about what AI produces.

## Teaching in the agentic era

That forces us to rethink how we train students for such human-in-the-loop systems, and it brings me to a question that bothers me a lot: what and how should we teach in the agentic era? The premium has shifted from producing stuff to reasoning about it, and we all agree that students need critical thinking. The question is how we develop it.

I have been working on two lines of effort. First, a [first principles framework](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/a4ne-networking-education.pdf), presented at a SIGCOMM 2026 workshop, that rethinks how we teach networking. I am also developing it into a book, [A First-Principles Approach to Networked Systems](https://sites.cs.ucsb.edu/~arpitgupta/first-principles-networking/) (a work in progress). It gives students a way to decompose existing or AI-proposed solutions and to synthesize new ones of their own. Second, an experiential learning framework that lowers the threshold for students to experiment with data and build their own understanding of networking concepts. Our upcoming SIGCSE paper, *Facilitating Experiential Learning in Networking Education*, describes how we use it in class.

### How can AI help?

The same Pramana we built for researchers helps here too: the research accelerator is also a teaching accelerator. Pramana lowers the entry barrier for students to get their hands dirty with real network data, and it lowers our engineering overhead of running this infrastructure for a whole class.

## Takeaways

The Internet should be viewed as a public utility, and we need to make secure and performant Internet access affordable for all. My research works toward this through two thrusts. In data-driven policymaking, better data enables effective decision-making. In self-driving networks, better data enables machine learning models that generalize. AI helps in two ways: it lowers the entry barrier for people who are not technical experts, and it lowers the engineering overheads of running public-good infrastructure. And to teach in the AI era, we need a first principles framework and experiential learning.

## Papers

- Broadband plans: [Decoding the Divide: Analyzing Disparities in Broadband Plans Offered by Major US ISPs](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/bqt_sigcomm23.pdf); [Robust and Extensible Measurement of Broadband Plans with BQT+](https://arxiv.org/abs/2602.16969); [Enabling Data-Driven Policymaking Using Broadband-Plan Querying Tool (BQT+)](https://arxiv.org/abs/2511.05838)
- CAF audit: [The Efficacy of the Connect America Fund in Addressing US Internet Access Inequities](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/caf-sigcomm24.pdf), ACM SIGCOMM 2024
- Generalizability: [AI/ML for Network Security: The Emperor has no Clothes](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf), ACM CCS 2022
- Data generation: [In Search of netUnicorn](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/netUnicorn.pdf), ACM CCS 2023; [NetGent: Agent-Based Automation of Network Application Workflows](https://arxiv.org/abs/2509.00625); [NetReplica: A Programmable Substrate for Bottleneck-Centric Network Data Generation](https://arxiv.org/abs/2507.13476)
- Pramana: [Pramana: A Composable, Domain-Specific Backend for Empirical Networking Research](https://arxiv.org/abs/2607.26352), upcoming at HotNets 2026
- The series: [AI in Action: Conversations with UCSB Researchers](https://www.library.ucsb.edu/events-exhibitions/events/ai-in-action), UCSB Library
- AI agent trilemma: Arvind Narayanan, [What will be left for us to work on?](https://www.cs.princeton.edu/~arvindn/talks/icml-2026-annotated-slides/), ICML 2026 keynote (slide 16)
- Teaching: [A First-Principles Framework for Networking Education](https://sites.cs.ucsb.edu/~arpitgupta/pdfs/a4ne-networking-education.pdf), ACM SIGCOMM 2026 workshop; *Facilitating Experiential Learning in Networking Education*, upcoming at SIGCSE TS 2027; the book in progress, [A First-Principles Approach to Networked Systems](https://sites.cs.ucsb.edu/~arpitgupta/first-principles-networking/)

</div>
