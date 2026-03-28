# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic personal website for Arpit Gupta (UCSB CS), built with Jekyll 4.3+ on a customized Minimal Mistakes theme. Deployed via rsync to UCSB servers.

## Build & Serve Commands

```bash
# Install dependencies
bundle install

# Local development (serves at http://localhost:4000/~arpitgupta)
bundle exec jekyll serve

# Build for production
bundle exec jekyll build

# Deploy to UCSB server
./deploy.sh   # runs jekyll build + rsync to linux.engr.ucsb.edu
```

Development uses `_config.dev.yml` overrides (disables analytics, uses localhost URL, expanded SCSS).

## Content Architecture

Content lives in three layers:

1. **Data files (`_data/`)** - Structured YAML driving publications, students, and navigation:
   - `publications.yml` - Canonical publication list with metadata, badges (policy/preprint), awards
   - `students.yml` - Student roster (PhD, MS, postdoc, alumni) with photos, honors, internships, paper associations
   - `navigation.yml` - Site navigation menu

2. **Collections** - Markdown files with YAML front matter:
   - `_publications/` - Individual publication records (filename format: `YYYY-MM-DD-slug.md`)
   - `_talks/` - Talk/seminar entries
   - `_pages/blog/` - Blog posts

3. **Templates (`_layouts/`, `_includes/`)** - Liquid/HTML templates:
   - Key custom includes: `pub-entry.html` (publication rendering), `students_summary.html` (student display)
   - Layouts extend `default.html` -> `single.html` for most pages

## Adding Publications

Use the helper script:
```bash
python scripts/new_publication.py \
  --title "Paper Title" \
  --authors "A. Author, B. Author" \
  --venue "ACM SIGCOMM, 2025" \
  --date 2025-08-01 \
  --url "https://example.com/paper.pdf" \
  --award "Best Paper Award"
```

## Theme Customizations

- **Dark/light toggle**: CSS in `_sass/_theme-toggle.scss`, JS in `assets/js/theme-toggle.js`
- **Skin**: Set to "dark" in `_config.yml` (`minimal_mistakes_skin: "dark"`)
- **Blog posts**: Use `page--blog-post` CSS class for blog-specific styling
- **SCSS**: All custom styles in `_sass/`, compiled via `assets/css/main.scss`

## Key Conventions

- Blog posts go in `_pages/blog/` (not the standard Jekyll `_posts/` directory); they are served under `/blogs/`
- PDFs (papers, etc.) go in `pdfs/`
- Images go in `images/`
- The site's `baseurl` is `/~arpitgupta` (important for local link testing)
- MathJax is available but can be disabled per-page with `tex2jax_ignore` wrapper class
