---
layout: single
title: "Annotated Talks"
permalink: /annotated-talks/
author_profile: true
---

{% include base_path %}

Talks I have given, written up as slides with an edited transcript. Each page steps through the slides build by build, with what I said beside each one. The full list of talks is on the [Talks]({{ base_path }}/talks/) page.

<ul class="annotated-talks-list" style="list-style: none; padding-left: 0; display: grid; gap: 1.75em;">
{% for t in site.data.annotated_talks %}
  <li style="display: grid; grid-template-columns: minmax(0, 220px) minmax(0, 1fr); gap: 1.1em; align-items: start;">
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
@media (max-width: 600px) {
  .annotated-talks-list li { grid-template-columns: minmax(0, 1fr) !important; }
}
</style>
