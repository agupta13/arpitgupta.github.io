---
layout: archive
title: "Students"
permalink: /students/
author_profile: true
---

{% include base_path %}

<div class="students-page">

  {% include students_summary.html %}

  <h2 id="current-students">Current Students</h2>

  <h3>PhD Students</h3>
  <div class="student-cards">
    {% for student in site.data.students.current_phd %}
    <div class="student-card">
      <div class="student-card__image-wrap">
        <img src="{{ base_path }}/images/students/{{ student.image }}" alt="{{ student.name }}" class="student-card__image" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22%3E%3Crect fill=%22%23666%22 width=%22120%22 height=%22120%22/%3E%3C/svg%3E';">
      </div>
      <div class="student-card__body">
        <h4 class="student-card__name">
          {% if student.website and student.website != '#' %}
            <a href="{{ student.website }}" target="_blank" rel="noopener">{{ student.name }}</a>
          {% else %}
            {{ student.name }}
          {% endif %}
        </h4>
        <span class="student-card__meta-line"><strong>Years:</strong> {{ student.years }}</span>
        <span class="student-card__meta-line"><strong>Affiliation:</strong> {{ student.affiliation }}</span>
        <p class="student-card__topic"><strong>Topic:</strong> {{ student.topic }}</p>
        {% if student.honors and student.honors.size > 0 %}
          <p class="student-card__honors"><strong>Honors:</strong>
            {% for h in student.honors %}
              {% if h.text %}
                {% if h.url %}<a href="{{ h.url }}" target="_blank" rel="noopener">{{ h.text }}</a>{% else %}{{ h.text }}{% endif %}
              {% else %}
                {{ h }}
              {% endif %}{% unless forloop.last %} {% endunless %}
            {% endfor %}
          </p>
        {% endif %}
        {% if student.internships and student.internships.size > 0 %}
          <p class="student-card__internships"><strong>Internships:</strong> {{ student.internships | join: ", " }}</p>
        {% endif %}
        {% assign paper_count = student.papers | size %}
        {% if paper_count > 0 %}
          <details class="student-card__papers">
            <summary>Papers ({{ paper_count }})</summary>
            <ul>
              {% for pid in student.papers %}
                {% for pub in site.data.publications %}
                  {% if pub.id == pid %}
                    <li><a href="{{ pub.url }}">{{ pub.title }}</a></li>
                    {% break %}
                  {% endif %}
                {% endfor %}
              {% endfor %}
            </ul>
          </details>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>

  <h3>MS Students</h3>
  <div class="table-responsive">
    <table class="students-table">
      <thead>
        <tr>
          <th class="students-table__name">Name</th>
          <th class="students-table__years">Years</th>
          <th class="students-table__project">Project</th>
          <th class="students-table__type">Type</th>
          <th class="students-table__affiliation">Affiliation</th>
        </tr>
      </thead>
      <tbody>
        {% for s in site.data.students.current_ms %}
        <tr>
          <td class="students-table__name">{{ s.name }}</td>
          <td class="students-table__years">{{ s.years }}</td>
          <td class="students-table__project">{{ s.project }}</td>
          <td class="students-table__type">{{ s.type }}</td>
          <td class="students-table__affiliation">{{ s.affiliation }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

  <h3>BS/MS Students</h3>
  <div class="table-responsive">
    <table class="students-table">
      <thead>
        <tr>
          <th class="students-table__name">Name</th>
          <th class="students-table__years">Years</th>
          <th class="students-table__project">Project</th>
          <th class="students-table__type">Type</th>
          <th class="students-table__affiliation">Affiliation</th>
        </tr>
      </thead>
      <tbody>
        {% for s in site.data.students.current_bsms %}
        <tr>
          <td class="students-table__name">{{ s.name }}</td>
          <td class="students-table__years">{{ s.years }}</td>
          <td class="students-table__project">{{ s.project }}</td>
          <td class="students-table__type">{{ s.type }}</td>
          <td class="students-table__affiliation">{{ s.affiliation }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

  <hr>

  <h2 id="alumni">Alumni</h2>

  <h3>PhD Alumni</h3>
  <div class="student-cards">
    {% for student in site.data.students.alumni_phd %}
    <div class="student-card">
      <div class="student-card__image-wrap">
        <img src="{{ base_path }}/images/students/{{ student.image }}" alt="{{ student.name }}" class="student-card__image" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22%3E%3Crect fill=%22%23666%22 width=%22120%22 height=%22120%22/%3E%3C/svg%3E';">
      </div>
      <div class="student-card__body">
        <h4 class="student-card__name">
          {% if student.website %}
            <a href="{{ student.website }}" target="_blank" rel="noopener">{{ student.name }}</a>
          {% else %}
            {{ student.name }}
          {% endif %}
        </h4>
        <span class="student-card__meta-line"><strong>Years:</strong> {{ student.years }}</span>
        <span class="student-card__meta-line"><strong>Affiliation:</strong> {{ student.affiliation }}</span>
        <p class="student-card__topic"><strong>Thesis:</strong> <a href="{{ student.thesis_url }}">{{ student.thesis_title }}</a></p>
        <p class="student-card__placement"><strong>Placement:</strong> {{ student.placement }}</p>
        {% if student.honors and student.honors.size > 0 %}
          <p class="student-card__honors"><strong>Honors:</strong>
            {% for h in student.honors %}
              {% if h.text %}
                {% if h.url %}<a href="{{ h.url }}" target="_blank" rel="noopener">{{ h.text }}</a>{% else %}{{ h.text }}{% endif %}
              {% else %}
                {{ h }}
              {% endif %}{% unless forloop.last %} {% endunless %}
            {% endfor %}
          </p>
        {% endif %}
        {% assign paper_count = student.papers | size %}
        {% if paper_count > 0 %}
          <details class="student-card__papers">
            <summary>Papers ({{ paper_count }})</summary>
            <ul>
              {% for pid in student.papers %}
                {% for pub in site.data.publications %}
                  {% if pub.id == pid %}
                    <li><a href="{{ pub.url }}">{{ pub.title }}</a></li>
                    {% break %}
                  {% endif %}
                {% endfor %}
              {% endfor %}
            </ul>
          </details>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>

  <h3>Postdoc Alumni</h3>
  <div class="student-cards">
    {% for student in site.data.students.alumni_postdoc %}
    <div class="student-card">
      <div class="student-card__image-wrap">
        <img src="{{ base_path }}/images/students/{{ student.image }}" alt="{{ student.name }}" class="student-card__image" onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22120%22 height=%22120%22%3E%3Crect fill=%22%23666%22 width=%22120%22 height=%22120%22/%3E%3C/svg%3E';">
      </div>
      <div class="student-card__body">
        <h4 class="student-card__name">
          {% if student.website %}
            <a href="{{ student.website }}" target="_blank" rel="noopener">{{ student.name }}</a>
          {% else %}
            {{ student.name }}
          {% endif %}
        </h4>
        <span class="student-card__meta-line"><strong>Years:</strong> {{ student.years }}</span>
        <span class="student-card__meta-line"><strong>Affiliation:</strong> {{ student.affiliation }}</span>
        <p class="student-card__placement"><strong>Placement:</strong> {{ student.placement }}</p>
      </div>
    </div>
    {% endfor %}
  </div>

  <h3>Others</h3>
  <p>BS/MS and high-school project alumni.</p>
  <div class="table-responsive">
    <table class="students-table">
      <thead>
        <tr>
          <th class="students-table__name">Name</th>
          <th class="students-table__years">Years</th>
          <th class="students-table__project">Project</th>
          <th class="students-table__type">Type</th>
          <th class="students-table__affiliation">Affiliation</th>
        </tr>
      </thead>
      <tbody>
        {% assign sorted_others = site.data.students.alumni_bsms | sort: "exit_year" | reverse %}
        {% for s in sorted_others %}
        <tr>
          <td class="students-table__name">{{ s.name }}</td>
          <td class="students-table__years">{{ s.years }}</td>
          <td class="students-table__project">{{ s.project }}</td>
          <td class="students-table__type">{{ s.type }}</td>
          <td class="students-table__affiliation">{{ s.affiliation }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

</div>
