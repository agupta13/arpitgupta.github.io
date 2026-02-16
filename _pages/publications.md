---
permalink: /publications/
title: "Publications"
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
{% for pub in sorted_pubs %}
{% include pub-entry.html pub=pub %}
{% endfor %}

{% include base_path %}
{% assign total = site.data.publications | size %}
{% assign num = total %}
{% for pub in site.data.publications %}
{{ num }}. [{{ pub.title }}]({{ pub.url }}){% if pub.badge %} <span class="pub-badge pub-badge--{{ pub.badge }}">{% if pub.badge == 'policy' %}Policy{% elsif pub.badge == 'preprint' %}Preprint{% endif %}</span>{% endif %}\
{{ pub.authors }}\
{{ pub.venue }}, {{ pub.year }}{% if pub.extra %}

{{ pub.extra | markdownify }}{% endif %}

{% assign num = num | minus: 1 %}
{% endfor %}

<!-- List sourced from _data/publications.yml (same data used on Students page for paper links). -->
