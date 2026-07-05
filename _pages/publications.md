---
permalink: /publications/
title: "Publications"
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
{% capture newline %}
{% endcapture %}

{% comment %} Sections in display order: key|Heading {% endcomment %}
{% assign sections = "policy|Policy Briefs & Reports,conference|Conference & Journal Papers,preprint|Under Review & Preprints,workshop|Workshops & Short Papers" | split: "," %}

<nav class="pub-toc">
  <strong>Jump to:</strong>
  {% for section in sections %}
    {% assign parts = section | split: "|" %}
    {% assign key = parts[0] %}
    {% assign heading = parts[1] %}
    {% assign count = 0 %}
    {% for pub in site.data.publications %}{% if pub.category == key %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
    <a href="#{{ key }}">{{ heading }}</a> ({{ count }}){% unless forloop.last %} &middot; {% endunless %}
  {% endfor %}
</nav>

{% for section in sections %}
  {% assign parts = section | split: "|" %}
  {% assign key = parts[0] %}
  {% assign heading = parts[1] %}

<h2 id="{{ key }}" class="pub-section-title">{{ heading }}</h2>
<ol class="publications-list">
{% for pub in site.data.publications %}
  {% if pub.category == key %}
  <li class="pub-item">
    <div class="pub-line pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a>{% if pub.badge %} <span class="pub-badge pub-badge--{{ pub.badge }}">{% if pub.badge == 'policy' %}Policy{% elsif pub.badge == 'preprint' %}Preprint{% endif %}</span>{% endif %}</div>
    <div class="pub-line pub-authors">{{ pub.authors }}</div>
    {% capture venue_display %}{% include venue_display.html venue=pub.venue %}{% endcapture %}
    <div class="pub-line pub-venue">{{ venue_display | strip }}, {{ pub.year }}</div>
{% if pub.extra %}
    {% assign extra_lines = pub.extra | split: newline %}
    {% comment %}1. Project website / workshop website first{% endcomment %}
    {% for line in extra_lines %}
      {% assign trimmed = line | strip %}
      {% if trimmed != "" %}{% if trimmed contains "Project Website" or trimmed contains "Workshop Website" %}
    <div class="pub-line pub-extra-line pub-project">{{ trimmed | markdownify }}</div>
      {% endif %}{% endif %}
    {% endfor %}
    {% comment %}2. Awards (no extra space){% endcomment %}
    {% for line in extra_lines %}
      {% assign trimmed = line | strip %}
      {% if trimmed != "" %}{% if trimmed contains "🏆" or trimmed contains "Award" or trimmed contains "Prize" or trimmed contains "Honorable Mention" or trimmed contains "Best Paper" or trimmed contains "Distinguished Paper" %}
    <div class="pub-line pub-extra-line pub-award">{{ trimmed | markdownify }}</div>
      {% endif %}{% endif %}
    {% endfor %}
    {% comment %}3. Misc (other links, etc.){% endcomment %}
    {% for line in extra_lines %}
      {% assign trimmed = line | strip %}
      {% if trimmed != "" %}
        {% assign is_project = false %}
        {% if trimmed contains "Project Website" or trimmed contains "Workshop Website" %}{% assign is_project = true %}{% endif %}
        {% assign is_award = false %}
        {% if trimmed contains "🏆" or trimmed contains "Award" or trimmed contains "Prize" or trimmed contains "Honorable Mention" or trimmed contains "Best Paper" or trimmed contains "Distinguished Paper" %}{% assign is_award = true %}{% endif %}
        {% if is_project == false and is_award == false %}
    <div class="pub-line pub-extra-line pub-misc">{{ trimmed | markdownify }}</div>
        {% endif %}
      {% endif %}
    {% endfor %}
{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ol>
{% endfor %}
<!-- List sourced from _data/publications.yml; grouped by the `category` field (policy | conference | preprint | workshop). -->
