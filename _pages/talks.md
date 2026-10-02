---
layout: archive
title: "Talks"
permalink: /talks/
redirect_from:
  - /annotated-talks/
author_profile: true
---

{% include base_path %}

{% if site.data.annotated_talks.size > 0 %}
<h2 id="annotated" class="archive__subtitle">Annotated talks</h2>
<p style="font-size: 0.95em;">Talks written up as slides with an edited transcript. Each page steps through the slides build by build, with what I said beside each one.</p>
<ul class="annotated-talks-list" style="list-style: none; padding-left: 0; display: grid; gap: 1.5em; margin-bottom: 2em;">
{% for t in site.data.annotated_talks %}
  <li style="display: grid; grid-template-columns: minmax(0, 200px) minmax(0, 1fr); gap: 1.1em; align-items: start;">
    <a href="{{ base_path }}/annotated-talks/{{ t.slug }}/" aria-label="{{ t.title }}">
      <img src="{{ base_path }}/{{ t.thumbnail }}" alt="" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid rgba(127,127,127,.35);" loading="lazy" />
    </a>
    <div style="min-width: 0;">
      <a href="{{ base_path }}/annotated-talks/{{ t.slug }}/"><strong>{{ t.title }}</strong></a>
      <p style="margin: 0.25em 0 0; font-size: 0.9em; color: var(--muted);">{{ t.event }}, {{ t.venue }} · {{ t.date | date: "%B %-d, %Y" }} · {{ t.slides }} slides</p>
      <p style="margin: 0.4em 0 0; font-size: 0.95em;">{{ t.summary }}</p>
      {% if t.blog %}<p style="margin: 0.4em 0 0; font-size: 0.9em;"><a href="{{ base_path }}/{{ t.blog }}">Read the blog post</a></p>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
<style>
@media (max-width: 600px) { .annotated-talks-list li { grid-template-columns: minmax(0, 1fr) !important; } }
</style>
{% endif %}

{% assign talk_years = "" | split: "," %}
{% assign sorted_talks = site.talks | sort: "date" | reverse %}
{% for talk in sorted_talks %}
  {% assign year = talk.date | date: "%Y" %}
  {% unless talk_years contains year %}
    {% assign talk_years = talk_years | push: year %}
  {% endunless %}
{% endfor %}

{% for year in talk_years %}
  <h2 id="{{ year }}" class="archive__subtitle">{{ year }}</h2>
  <ol class="talks-list">
  {% for post in sorted_talks %}
    {% assign post_year = post.date | date: "%Y" %}
    {% if post_year == year %}
      {% include archive-single-talk.html %}
    {% endif %}
  {% endfor %}
  </ol>
{% endfor %}
