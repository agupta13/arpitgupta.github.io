---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: true
---

{% include base_path %}

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
