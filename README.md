# Pulse & Vitality — health education

112 health education articles: 83 in-depth bilingual articles and 29 independent Vietnamese guides to WHOOP metrics. The WHOOP collection was added on 27 October 2026, using rewritten explanations, source links, licensed illustrative images and reviewed original SVGs. Its English UI explicitly identifies the Vietnamese edition. **Clinical sign-off has not been recorded.** Source organizations have not endorsed the website.

The audit found unrelated canonical PubMed identifiers in at least 29 articles, unsupported wearable-to-hormone interpretations, and images that did not match captions. This edition develops the original topic outlines from revision `f68c786` into full articles, with corrected mechanisms and research interpretation. It replaces the overly brief summaries introduced in the first audit. Original texts remain in Git history; local workbook and JSON backups are in the workspace audit directory.

Production: [test-repo-y1wb.onrender.com](https://test-repo-y1wb.onrender.com/). Render tracks the existing GitHub repository `HandQ2212/test-repo`, branch `main`.

WHOOP collection: [29 guides](https://test-repo-y1wb.onrender.com/?collection=whoop&lang=vi). Individual article links use `/posts/WHOOP-ART-01.html?lang=vi` through `/posts/WHOOP-ART-29.html?lang=vi`. These are independently written educational articles, not copies of WHOOP articles or statements endorsed by WHOOP.

## Edit and rebuild

- `data/editorial_articles.tsv`, `editorial_women.tsv`, `editorial_men.tsv`: 83 editorial records in both languages.
- `data/longform_*.tsv`, `longform_tables.json`, `longform_research.json`: bilingual explanations, technical examples, article-specific situations, comparison tables and research notes.
- `build_longform.py`: combines these materials with the baseline topic outlines and produces `data/longform_articles.json`.
- `data/image_selections.json`, `image_curation.py`: reviewed image assets, frozen source metadata, bilingual captions and visible author/licence credits.
- `data/image_research_batches.json`: six sessions. Batch 01 covers 10 articles with 19 image placements; batch 02 covers 15 articles with 29 placements from 24 source images; batch 03 covers 15 articles with 25 placements from 24 source images; batch 04 covers 15 articles with 28 placements from 26 source images; batch 05 covers 15 articles with 23 placements from 21 source images; final batch 06 covers 13 articles with 19 placements from 18 source images. Each batch after batch 01 covers up to 15 articles. See `docs/Image_Research_Progress.md` and the six completed `docs/Image_Research_Batch_XX.html` galleries.
- `data/editorial_sources.tsv`: 82 source titles, URLs, types and support scopes. Manufacturer documentation explains a product; it is not clinical efficacy evidence. One retracted paper is cited solely to explain why its testosterone claim is excluded.
- `rebuild_editorial.py`: rebuild article JSON/JS, Markdown, master workbook, roadmaps, workbook copies in `docs/`, and all standalone HTML.
- `generate_posts.py`: regenerate standalone HTML from the current JSON only.
- `data/whoop_article_records.json`, `whoop_sources.json`, `whoop_image_manifest.json`: portable snapshot of the 29 Vietnamese WHOOP education records, source register and original diagram provenance.
- `sync_whoop_articles.py`: merge the WHOOP snapshot into the published catalog, retaining the 83 original records. The full editorial rebuild calls this before generating posts. Use `--import-research /absolute/path/to/WHOOP_Content_Research` only when importing an updated research edition from the workspace.
- `validate_whoop_publication.py`: check all 29 records, citations, page paths, language labels, licensed hero assets and diagram hashes.
- `article_figures.js`: show captions after image loading succeeds, discard broken inline figures, and remove retired summary figures embedded in article HTML.
- `validate_editorial.py`: coverage, references, images, bibliographic identity and parity across outputs.

With Python 3, `openpyxl` and `markdown` installed:

```sh
python3 rebuild_editorial.py
python3 validate_editorial.py
python3 validate_whoop_publication.py
node --check app.js
node --check articles_data.js
node server.js
```

The server runs at `http://localhost:3000`. HTML, article data, scripts and workbook responses use `Cache-Control: no-store`; missing file paths return 404 rather than the SPA HTML. The renderer also rejects retired `images/editorial/` text cards if stale article metadata is supplied. Rebuild uses the sibling `Fitness IOS` directory when present, otherwise the workbooks in `docs/`. Do not use historical batch builders or reference-upgrade scripts in `Fitness IOS/data` to rebuild this edition; they contain superseded drafts.

## Evidence and image provenance

Each article lists clickable sources and their support scopes. The master workbook adds `Editorial_Audit`, `Source_Register` and `Link_Audit`. The roadmaps include `Reviewed_Content` and updated source fields.

An HTTP success does not prove claim support. A 403, PubMed challenge or HTTP 203 is recorded separately from a missing page. Research identities were checked against primary/indexed records, including Europe PMC bibliographic metadata. This is an editorial audit, not a new systematic review or medical certification.

Image research is performed in sessions of up to 15 articles, starting with batch 02; completed batch 01 retains its original 10 articles. All 83 articles now have 143 reviewed image placements, each with a source page, author, reuse terms and a topic-specific caption. Relevant anatomy and device images may be reused with the same attribution; placement counts are not counts of unique photographs. A second image is added only when it serves the article. Batch 02 includes actual LH strips, a basal thermometer, a CPET setup, cervical mucus and male pelvic-floor anatomy. Batch 03 adds female perineal anatomy, vaginal microscopy, an appropriate groin-stretch position, menstrual products, everyday communication and recording scenes. Batch 04 adds pregnancy tests, venous blood collection and a documented iron-deficiency blood smear, prenatal care, walking in pregnancy and with a stroller, uterine enlargement, PCOS and endometriosis schematics, midlife care and example meals. Batch 05 adds clinical consultation, blood collection, blood-pressure measurement, penile cross-section anatomy, everyday communication and shared chores, a readable supplement label and human sperm microscopy. The supplement label is an example for checking ingredients and dose, not a dosage recommendation; a sperm micrograph does not establish fertility. Stock models are not assigned diagnoses, cycle phases or hormone levels. Batch 06 adds prepared meals, drinking during exercise, waking and running scenes, focused testicular anatomy, everyday planning, sleep arrangements and conversation among older adults; suitable sleep, laboratory and anatomy images are reused with their original credits. All 83 articles have completed the image review sessions. An inconsistent hormone-diagram label and a micrograph showing azoospermia were rejected for these placements. The master workbook includes `Image_Register` and per-article attribution metadata. Text-only summary cards stay excluded; broken images leave no caption or empty frame. Source metadata and visible subject checks do not imply medical certification or endorsement.

See [the audit report](docs/Health_Content_Audit_2026-10-26.md) for findings and validation scope.
