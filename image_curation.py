"""Apply reviewed image choices without changing the health article prose."""
import json
import html
from pathlib import Path

BASE = Path(__file__).resolve().parent


def selections():
    path = BASE / 'data/image_selections.json'
    return json.loads(path.read_text())['assets'] if path.exists() else []


def apply_image_selections(records):
    for article in records.values():
        article.update(hero_caption='', hero_caption_vi='', hero_image_fit='cover',
                       image_attributions=[], image_review_batch=0,
                       image_review_status='Pending image research session')
    for asset in selections():
        article = records[asset['article_id']]
        role = asset['role']
        article[role + '_image'] = asset['asset']
        article[role + '_image_source_url'] = asset['source_page']
        article[role + '_caption'] = asset['caption_en']
        article[role + '_caption_vi'] = asset['caption_vi']
        if role == 'hero':
            article['thumbnail'] = asset['asset']
            article['hero_image_fit'] = asset['fit']
        article['image_attributions'].append({k: v for k, v in asset.items() if k != 'source_metadata'})
        article['image_review_batch'] = asset.get('batch', 1)
        article['image_review_status'] = f"Subject, source and licence checked — batch {article['image_review_batch']:02d}"
        article['image_provenance'] = f"Image research batch {article['image_review_batch']:02d}: visible subject, source metadata and reuse terms checked. See image_attributions for each asset."


def write_review_docs(articles):
    assets = selections()
    if not assets:
        return
    by_id = {a['id']: a for a in articles}
    path = BASE / 'data/image_research_batches.json'
    progress = json.loads(path.read_text())
    covered = {a['article_id'] for a in assets}
    lines = ['# Tiến độ nghiên cứu hình ảnh', '',
             f"Từ phiên 02, mỗi phiên xử lý tối đa {progress['batch_size']} bài. Phiên 01 đã hoàn tất 10 bài được giữ nguyên. Trạng thái dưới đây là tiến độ chọn và kiểm tra ảnh; trạng thái triển khai Render được kiểm tra riêng.", '',
             '| Đợt | Số bài | Trạng thái | Content ID |', '|---|---:|---|---|']
    for batch in progress['batches']:
        done = all(aid in covered for aid in batch['article_ids'])
        batch['status'] = 'image research completed' if done else 'pending'
        lines.append(f"| {batch['batch']:02d} | {len(batch['article_ids'])} | {'Đã chọn và đối chiếu ảnh' if done else 'Chưa thực hiện'} | {', '.join(batch['article_ids'])} |")
        if not done:
            continue
        chunks = []
        for aid in batch['article_ids']:
            cards = []
            for asset in [a for a in assets if a['article_id'] == aid]:
                e = html.escape
                cards.append(f'''<figure class="article-inline-diagram">
                  <img src="../{e(asset['asset'])}" alt="{e(asset['alt_vi'])}" loading="lazy">
                  <figcaption><strong>{e(asset['caption_vi'])}</strong><br>{e(asset['caption_en'])}
                  <span class="image-attribution"><a href="{e(asset['source_page'])}">{e(asset['author'])}</a> · <a href="{e(asset['license_url'])}">{e(asset['license'])}</a> · {e(asset['modifications_vi'])}</span>
                  <p>{e(asset['relevance_vi'])}</p></figcaption></figure>''')
            title = html.escape(by_id[aid]['title_vi'])
            chunks.append(f'<section><h2><a href="../posts/{aid}.html?lang=vi">{aid} — {title}</a></h2><div class="image-grid">'+''.join(cards)+'</div></section>')
        document = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Đợt {batch['batch']:02d}: ảnh đã đối chiếu cho {len(batch['article_ids'])} bài</title><link rel="stylesheet" href="../styles.css?v=image-review-1">
          <script src="../article_figures.js?v=figure-load-1"></script>
          <style>body{{max-width:1200px;margin:auto;padding:28px;font-family:system-ui,sans-serif}}h1{{font-size:30px}}h2{{font-size:22px;margin-top:40px}}.image-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:24px}}.article-inline-diagram{{margin:0}}.article-inline-diagram img{{height:340px;object-fit:contain}}figcaption p{{margin-top:12px}}a{{color:#2443a0}}</style></head>
          <body><h1>Đợt {batch['batch']:02d}: bộ ảnh cho {len(batch['article_ids'])} bài</h1><p>Ảnh và sơ đồ được đối chiếu về chủ thể, nguồn và giấy phép. Bấm tiêu đề để đọc bài; mỗi hình có tác giả, giấy phép và lý do chọn.</p>{''.join(chunks)}</body></html>'''
        (BASE/'docs'/f"Image_Research_Batch_{batch['batch']:02d}.html").write_text(document,encoding='utf-8')
    galleries = ', '.join(f"[Đợt {b['batch']:02d}](Image_Research_Batch_{b['batch']:02d}.html)"
                          for b in progress['batches'] if b['status'] == 'image research completed')
    lines += ['', f'Đã chọn {len(assets)} vị trí hình cho {len(covered)}/83 bài. Một số hình giải phẫu/dụng cụ được dùng lại khi phù hợp, với nguồn và giấy phép giữ nguyên. Các bài còn lại giữ trạng thái chưa rà soát trong quy trình này.', '',
              f'Nguồn và metadata: `data/image_selections.json`. Bảng Excel: sheet `Image_Register`. Bộ xem trước: {galleries}.', '',
              'Ảnh tóm tắt chỉ có chữ không được đưa trở lại. Ảnh không tải được không hiển thị khung hoặc chú thích. Không suy chẩn đoán, hormone, điểm số hay cường độ vận động từ một bức ảnh.']
    (BASE/'docs/Image_Research_Progress.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
