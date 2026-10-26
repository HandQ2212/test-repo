# Pulse & Vitality — health education

83 bilingual health guides with references, evidence limitations and original editorial illustrations. Revised on 26 October 2026. **Clinical sign-off has not been recorded.** Source organizations have not endorsed the website.

The audit found unrelated canonical PubMed identifiers in at least 29 articles, unsupported wearable-to-hormone interpretations, and images that did not match captions. The revised edition uses shorter, bounded guidance and removes unsupported numerical prescriptions and treatment promises. Original texts remain in Git history; local workbook and JSON backups are in the workspace audit directory.

Production: [test-repo-y1wb.onrender.com](https://test-repo-y1wb.onrender.com/). Render tracks the existing GitHub repository `HandQ2212/test-repo`, branch `main`.

## Edit and rebuild

- `data/editorial_articles.tsv`, `editorial_women.tsv`, `editorial_men.tsv`: 83 editorial records in both languages.
- `data/editorial_sources.tsv`: 70 source titles, URLs, types and support scopes. Manufacturer documentation explains a product; it is not clinical efficacy evidence.
- `rebuild_editorial.py`: rebuild JSON, JS, 166 SVGs, Markdown, master workbook, roadmaps, workbook copies in `docs/`, and all standalone HTML.
- `generate_posts.py`: regenerate standalone HTML from the current JSON only.
- `validate_editorial.py`: coverage, references, images, bibliographic identity and parity across outputs.

With Python 3, `openpyxl` and `markdown` installed:

```sh
python3 rebuild_editorial.py
python3 validate_editorial.py
node --check app.js
node --check articles_data.js
node server.js
```

The server runs at `http://localhost:3000`. Rebuild uses the sibling `Fitness IOS` directory when present, otherwise the workbooks in `docs/`. Do not use historical batch builders or reference-upgrade scripts in `Fitness IOS/data` to rebuild this edition; they contain superseded drafts.

## Evidence and image provenance

Each article lists clickable sources and their support scopes. The master workbook adds `Editorial_Audit`, `Source_Register` and `Link_Audit`. The roadmaps include `Reviewed_Content` and updated source fields.

An HTTP success does not prove claim support. A 403, PubMed challenge or HTTP 203 is recorded separately from a missing page. Research identities were checked against primary/indexed records, including Europe PMC bibliographic metadata. This is an editorial audit, not a new systematic review or medical certification.

Displayed SVGs are original project assets labelled as editorial summaries, not anatomical illustrations, measured data or reproductions of cited figures. Legacy raster assets remain unused for traceability.

See [the audit report](docs/Health_Content_Audit_2026-10-26.md) for findings and validation scope.
