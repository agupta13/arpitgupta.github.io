# How to update the Students page

## Data

- **Edit `_data/students.yml`** for all student content:
  - **Current PhD** (`current_phd`): name, years, topic, affiliation, website, image filename, honors, internships, `papers` (list of publication ids from `_data/publications.yml`).
  - **BS/MS** (`bsms_ersp`, `bsms_cal_bridge`, `bsms_other`): name, years, topic, affiliation.
  - **Alumni PhD** (`alumni_phd`): same as current PhD plus `thesis_title`, `thesis_url`, `placement`.
  - **Postdoc alumni** (`alumni_postdoc`): name, years, placement, website.
  - **BS/MS alumni** (`alumni_bsms`): name, years, topic, affiliation.

## Images

- Add headshots under **`images/students/<slug>.jpg`** (e.g. `sanjay-chandrasekaran.jpg`). Use the `slug` or `image` value from `_data/students.yml`.
- If a headshot is missing, the page shows a gray placeholder automatically.
- Optional: add `images/students/placeholder.jpg` for a custom default image.

## Papers

- Publication list is in **`_data/publications.yml`**. Each entry has an `id` (e.g. `netgent`, `caf-sigcomm24`).
- In `_data/students.yml`, set **`papers: [id1, id2, ...]`** for each PhD/alias student so the "Papers (N)" section shows the correct links. Use the same ids as in `_data/publications.yml`.

## TODOs in YAML

- **Placement unknown:** use `placement: "TBD"` (or a TODO comment) and update when known.
- **Internships unknown:** leave `internships: []` or omit; the page does not show an internships line when empty.
- **Headshot missing:** add `# headshot_todo: true` in the student entry if you want to track it; the page will still use the gray placeholder until you add the image file.

## Build

Run from the repo root:

```bash
bundle exec jekyll build --config _config.yml,_config.dev.yml
```

To preview locally:

```bash
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Then open the Students page at `/students/`.
