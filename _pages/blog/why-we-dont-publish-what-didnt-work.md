---
title: "Why we don't publish what didn't work"
permalink: /blogs/why-we-dont-publish-what-didnt-work.html
redirect_from:
  - /blog/why-we-dont-publish-what-didnt-work.html
layout: single
author_profile: true
date: 2026-08-17
published: false
---

<p class="page__subtitle" style="font-size: 0.9em; color: var(--muted); margin-top: -0.5em; margin-bottom: 1em;">Draft notes for a panel at NetNeg, the ACM Workshop on Negative Results in Network Measurements (SIGCOMM 2026)</p>

Research fields publish what works. What does not work usually stays unwritten. It lives in the memory of the people who ran the failed experiment, and it is lost when they move on. The next group starts the same experiment from scratch, pays the same cost to learn the same lesson, and loses it in turn. I think this is a mistake, and it is getting more expensive. I want to explain why, using a negative result from my own group. I also want to be honest that I helped bury that result.

<figure style="margin: 1.5em 0; text-align: center;">
  <img src="{{ base_path }}/images/blog/negatives-iceberg.jpg" alt="An Arctic iceberg with its large underwater mass visible through clear water." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.85em; color: var(--muted); margin-top: 0.5em;">Most of an iceberg sits below the waterline. Photo: Andreas Weith, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:Iceberg_in_the_Arctic_with_its_underside_exposed.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

## A negative result from my own group

A few years ago we tried to detect short-lived congestion events across a campus network. These are the brief episodes, lasting a second or two, that make a video call freeze and then recover before any monitoring system notices. We wanted to find them passively, by watching the traffic that already passes a single vantage point, instead of injecting our own test probes.

The effort rested on one hypothesis. The applications that suffer most from these events, like video calls, run over UDP, which gives an outside observer almost no timing signal. But those calls share the same links as ordinary downloads, which run over TCP, and TCP does leave a timing signal you can read passively. We reasoned that the TCP flows sitting next to a video call, on the same bottleneck, would tell us what the call was experiencing. We would measure the neighbors and infer the state of the flow we could not see.

We could not confirm it, for two reasons.

The first was precision. Estimating an accurate round-trip time from passive traces, across billions of packets, is much harder than the literature suggests. Our pipeline produced a usable latency sample from about one packet in seven, and it could not separate the campus portion of the path from the rest. The events we cared about are brief, which is the regime where an imprecise estimate is least reliable. We also had no independent record of when a real congestion event occurred, so a spike we flagged could be a true event or an artifact of our own thresholds. We had no way to distinguish the two.

The second reason was more fundamental. Our central question was whether the neighboring TCP flows are a faithful proxy for the video call. That question cannot be answered from passive traces at all, however many we collect. To check whether the proxy is good, you need to know what the video call actually experienced, and passive traces do not record that. The data that raised the question could not answer it.

That is the finding: you cannot validate a passive inference method using passive data alone. It is a real and general result about a common style of measurement. It does not look like the results we publish, so we did not publish it.

## Most research runs on results that didn't work

Set that project aside, because the pattern is general. Empirical work rarely moves in a straight line from question to answer. It cycles through four activities: you reproduce a published result, you push it until it breaks, you diagnose and fix what broke, and you establish something new. Two of those four are negative results. Finding the break and diagnosing it are how you learn what is actually true. Papers sometimes do report these intermediate negatives, but writing a paper is mostly compression, and a clean, linear story leaves little room for them. So the published version usually keeps the endpoint and drops the path that led there, even though that path carries much of what was learned.

<figure style="margin: 1.5em 0; text-align: center;">
  <img src="{{ base_path }}/images/blog/research-vs-paper.svg" alt="Left: a straight arrow from Question to Result, labeled how the paper tells it. Right: a tangled scribble from Question to Result, labeled how the research actually went." style="max-width: 100%; height: auto;" />
  <figcaption style="font-size: 0.85em; color: var(--muted); margin-top: 0.5em;">The published paper reports a straight path from question to result. The research that produced it rarely looks like that.</figcaption>
</figure>

## Two kinds of negative result

It helps to separate two things. An intermediary negative is a step inside a larger effort, such as finding that a method breaks under load or that a baseline is stronger than expected. A terminal null is a finished answer, such as finding that an effect is absent or that an approach cannot establish what you set out to establish. My congestion result is a terminal null of an awkward kind: it does not show the phenomenon is absent, only that this instrument cannot settle whether it is there. Both kinds are worth publishing. The first saves others the weeks it takes to rediscover a blocked path. The second tells everyone working on a problem where its boundary lies.

## Why we bury them

The burial is not laziness. It follows from three reasons.

First, we often cannot tell a real negative from an inconclusive one. If the instrument is imprecise, an absent signal might mean the effect is not there, or that we could never have seen it. Without ground truth, those two cases look identical, and a negative you cannot trust reads as no result. My congestion measurements sat in exactly this ambiguity.

Second, establishing a trustworthy negative is expensive. To claim that something does not hold, you usually need the same controlled setup you would need to show that it does. Ground truth is the costly ingredient, and most of us do not have it available.

Third, we treat negatives as private knowledge. They survive in the heads of the people who hit them and resurface, if at all, only as motivation for whatever those people build next. The knowledge is real, but it is never written where the field can use it.

## What the field loses

Consider what publishing a negative would save. It spares the next group the cost of rediscovering a dead end that someone already mapped. It exposes a weak or under-specified hypothesis to scrutiny early, while changing direction is still cheap, rather than after a student has spent years on it. And it gives others a result they can inspect and argue with instead of a silence they have to fill themselves. A field that circulates its negatives moves faster than one that keeps them. We have mature norms for sharing what worked and almost none for sharing what did not.

## What we built next: NetVibe

The congestion result did not end there. Learning that we could not validate passive inference with passive data is what led us to build the missing ingredient, and over time that work became NetVibe.

NetVibe is a broadband-quality monitoring tool we developed. It runs continuously on a user's machine and measures network latency in a lightweight way, using the audio channel of the WebRTC stack instead of flooding the link with a speed test. It measures upstream and downstream delay separately, at fine time resolution, at a cost low enough to run all day on millions of machines. From that latency signal, machine-learning models infer properties of the network the user cannot observe directly: how much competing traffic sits on the bottleneck link, where the bottleneck is, and how well applications like Zoom or YouTube would perform under the current conditions.

Those inference models are the point, and they work only because they are trained on controlled, labeled data. We generate that data by recreating network conditions in a controlled setting and running real application workloads under them, so we know the true network state that produced each latency trace. NetVibe grounds its passive signal in controlled data instead of asking that signal to validate itself, which is the step the congestion project could not manage.

So the negative did useful work. But it did that work only for us, and only for one question. The lesson stayed inside my group as engineering intuition. It never became a result other people could use, and the problem it points to is much larger than broadband monitoring.

## What would have to change

Two things.

The first is to make controlled, labeled data cheap to produce, because that is the ingredient every trustworthy negative needs and almost no one has. NetVibe solved this for one narrow question by generating ground truth for a single application setting. The general problem is that every study needs controlled data for its own question, and producing it from scratch each time is the real bottleneck in empirical networking research. Stating a hypothesis takes an afternoon, but generating the data that tests it takes months.

This is the problem my group is now trying to solve with Pramana. Pramana is a shared backend that takes a research intent, meaning a description of what data you need and under what conditions, and returns realistic data with the true conditions labeled. It is built to serve a wide range of intents rather than one hard-coded setting, by composing the controlled network conditions and the real application workloads that a study asks for. Its purpose is to bridge the gap between having an idea and having the data to test it, which is the lag that slows the whole field down. The bottleneck is the same whether a hypothesis holds or fails: you need trustworthy data to find out. A backend that supplies realistic labeled data on demand helps in both cases, and it makes a null result something you can establish and defend rather than an ambiguous failure.

The second change is to give negatives a place to be published, and to be deliberate about where that place is. This workshop, NetNeg, is a strong start. It signals that the community takes negative results seriously, and it gives people a room to present the lessons that flagship venues overlook. But I doubt that a single workshop for all of networking is the durable answer. A negative result has a niche audience. It is most useful to the people working on the exact problem it maps, and less legible to everyone else. Aggregating every subfield's negatives into one venue puts each result in front of mostly the wrong readers, which is hard to sustain year over year.

The durable path is to route negatives to where their audience already gathers. That means dedicated negative-results tracks at SIGCOMM, NSDI, and IMC, which carry the reach and the legitimacy that make people submit and cite. It also means reserving space for negatives inside topical, special-interest workshops such as NAIC and QuantNet, where the community that would act on a given negative is already present. Our community has created venues on purpose before. A few years ago the field added a dedicated replication track at IMC, with a publication home in CCR, after treating replication as derivative for years, and I helped push for and promote that track. Negatives deserve the same deliberate effort, placed where each kind of negative will actually be read.

## Why this matters now

For most of the field's history, burying negatives was a slow, quiet loss. That is changing. AI systems now propose plausible hypotheses far faster than anyone can test them. Ideation is becoming cheap, and validation is becoming the bottleneck. If our only response to a failed hypothesis is to bury it, we will rediscover the same dead ends across many groups at once, while the backlog of untested ideas grows. Pramana addresses one side of this by making the data to test an idea cheaper to produce. Publishing negatives addresses the other, by making a failed test teach the whole field instead of one lab. The gap between forming a hypothesis and testing it is paid for in someone's thesis or tenure clock. I have spent parts of my own career in that gap, on bets that did not work out, and I made those calls. The least we can do is make a failed bet something everyone learns from.
