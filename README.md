# Pulse & Vitality — health education

83 in-depth bilingual health articles with physiological explanations, comparison tables, practical situations and scoped references. Revised on 26 October 2026. **Clinical sign-off has not been recorded.** Source organizations have not endorsed the website.

The audit found unrelated canonical PubMed identifiers in at least 29 articles, unsupported wearable-to-hormone interpretations, and images that did not match captions. This edition develops the original topic outlines from revision `f68c786` into full articles, with corrected mechanisms and research interpretation. It replaces the overly brief summaries introduced in the first audit. Original texts remain in Git history; local workbook and JSON backups are in the workspace audit directory.

Production: [test-repo-y1wb.onrender.com](https://test-repo-y1wb.onrender.com/). Render tracks the existing GitHub repository `HandQ2212/test-repo`, branch `main`.

## Edit and rebuild

- `data/editorial_articles.tsv`, `editorial_women.tsv`, `editorial_men.tsv`: 83 editorial records in both languages.
- `data/longform_*.tsv`, `longform_tables.json`, `longform_research.json`: bilingual explanations, technical examples, article-specific situations, comparison tables and research notes.
- `build_longform.py`: combines these materials with the baseline topic outlines and produces `data/longform_articles.json`.
- `data/image_selections.json`, `image_curation.py`: reviewed image assets, frozen source metadata, bilingual captions and visible author/licence credits.
- `data/image_research_batches.json`: nine sessions of up to 10 articles; batch 01 covers the first 10, with 19 selected images. See `docs/Image_Research_Progress.md` and `docs/Image_Research_Batch_01.html`.
- `data/editorial_sources.tsv`: 82 source titles, URLs, types and support scopes. Manufacturer documentation explains a product; it is not clinical efficacy evidence. One retracted paper is cited solely to explain why its testosterone claim is excluded.
- `rebuild_editorial.py`: rebuild article JSON/JS, Markdown, master workbook, roadmaps, workbook copies in `docs/`, and all standalone HTML.
- `generate_posts.py`: regenerate standalone HTML from the current JSON only.
- `article_figures.js`: show captions after image loading succeeds, discard broken inline figures, and remove retired summary figures embedded in article HTML.
- `validate_editorial.py`: coverage, references, images, bibliographic identity and parity across outputs.

With Python 3, `openpyxl` and `markdown` installed:

```sh
python3 rebuild_editorial.py
python3 validate_editorial.py
node --check app.js
node --check articles_data.js
node server.js
```

The server runs at `http://localhost:3000`. HTML, article data, scripts and workbook responses use `Cache-Control: no-store`; missing file paths return 404 rather than the SPA HTML. The renderer also rejects retired `images/editorial/` text cards if stale article metadata is supplied. Rebuild uses the sibling `Fitness IOS` directory when present, otherwise the workbooks in `docs/`. Do not use historical batch builders or reference-upgrade scripts in `Fitness IOS/data` to rebuild this edition; they contain superseded drafts.

## Evidence and image provenance

Each article lists clickable sources and their support scopes. The master workbook adds `Editorial_Audit`, `Source_Register` and `Link_Audit`. The roadmaps include `Reviewed_Content` and updated source fields.

An HTTP success does not prove claim support. A 403, PubMed challenge or HTTP 203 is recorded separately from a missing page. Research identities were checked against primary/indexed records, including Europe PMC bibliographic metadata. This is an editorial audit, not a new systematic review or medical certification.

Image research is performed in sessions of about 10 articles. Batch 01 replaces images for the first 10 articles with 19 selected photographs, diagrams and recordings, each with a source page, author, reuse terms and a topic-specific caption. One WHOOP article uses one relevant photograph because a suitable additional openly reusable product graphic was not confirmed. The remaining 73 articles retain their prior assets and are explicitly marked pending image review. The master workbook includes `Image_Register` and per-article attribution metadata. Text-only summary cards stay excluded; broken images leave no caption or empty frame. Source metadata and visible subject checks do not imply medical certification or endorsement.

See [the audit report](docs/Health_Content_Audit_2026-10-26.md) for findings and validation scope.
