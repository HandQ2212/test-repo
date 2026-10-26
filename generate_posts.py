import json
import os
import re
import html
import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "articles.json"), "r", encoding="utf-8") as f:
    articles = json.load(f)

category_icons = {
    "Sleep": "🌙",
    "Recovery": "🔋",
    "Activity": "🏃",
    "Health & Wellness": "🌿",
    "Women's Health": "🌸",
    "Men's Health": "💪"
}

category_vi = {
    "Sleep": "Giấc ngủ",
    "Recovery": "Phục hồi",
    "Activity": "Vận động",
    "Health & Wellness": "Sức khỏe toàn diện",
    "Women's Health": "Sức khỏe Nữ giới",
    "Men's Health": "Sức khỏe Nam giới"
}

category_colors = {
    "Sleep": ("#EDE9FE", "#6D28D9", "#8B5CF6"),
    "Recovery": ("#ECFDF5", "#059669", "#10B981"),
    "Activity": ("#FEF3C7", "#D97706", "#F59E0B"),
    "Health & Wellness": ("#E0F2FE", "#0284C7", "#0EA5E9"),
    "Women's Health": ("#FCE7F3", "#DB2777", "#EC4899"),
    "Men's Health": ("#E0E7FF", "#4338CA", "#6366F1")
}

def resolve_post_img_path(path_str):
    if not path_str:
        return ""
    if path_str.startswith("images/"):
        return "../" + path_str
    return path_str

def render_article_markdown(md_text, inline_img_src, inline_caption, inline_source_url, lang="en"):
    body_html = markdown.markdown(
        md_text,
        extensions=['extra', 'tables', 'sane_lists']
    )
    # Convert mermaid code blocks into <div class="mermaid"> with decoded HTML entities
    def repl_mermaid(m):
        raw_code = html.unescape(m.group(1)).strip()
        return f'\n<div class="mermaid">\n{raw_code}\n</div>\n'

    body_html = re.sub(r'<pre><code class="(?:language-)?mermaid">([\s\S]*?)</code></pre>', repl_mermaid, body_html)

    if "article-inline-diagram" not in body_html and inline_img_src and not re.search(r'(^|/)images/editorial/', inline_img_src):
        src_label = "View figure ↗" if lang == "en" else "Xem hình và sơ đồ ↗"
        inline_diagram_html = f"""
        <figure class="article-inline-diagram">
          <img src="{inline_img_src}" alt="{inline_caption}" loading="lazy">
          <figcaption>📊 <strong>{inline_caption}</strong> <a href="{inline_source_url}" target="_blank" rel="noopener noreferrer" class="img-source-badge">({src_label})</a></figcaption>
        </figure>
        """
        if "</h2>" in body_html:
            parts = body_html.split("</h2>", 1)
            if "</p>" in parts[1]:
                p_parts = parts[1].split("</p>", 1)
                body_html = parts[0] + "</h2>" + p_parts[0] + "</p>" + inline_diagram_html + p_parts[1]
            else:
                body_html = parts[0] + "</h2>" + inline_diagram_html + parts[1]
        else:
            body_html = inline_diagram_html + body_html

    body_html = body_html.replace('src="images/', 'src="../images/')
    return body_html

posts_dir = os.path.join(BASE_DIR, "posts")
os.makedirs(posts_dir, exist_ok=True)

for i, art in enumerate(articles):
    cat = art["category"]
    cat_vi_name = category_vi.get(cat, cat)
    icon = category_icons.get(cat, "📄")
    bg_pill, text_pill, _ = category_colors.get(cat, ("#F1F5F9", "#334155", "#64748B"))

    title_en = art["title"]
    title_vi = art.get("title_vi", title_en)
    desc_en = art["description"]
    desc_vi = art.get("description_vi", desc_en)
    takeaway_en = art["takeaway"]
    takeaway_vi = art.get("takeaway_vi", takeaway_en)
    readtime_en = art["reading_time"]
    readtime_vi = art.get("reading_time_vi", readtime_en)
    caption_en = art.get("inline_caption", "")
    caption_vi = art.get("inline_caption_vi", caption_en)

    hero_img_src = resolve_post_img_path(art.get("hero_image", ""))
    hero_source_url = art.get("hero_image_source_url", hero_img_src)
    inline_img_src = resolve_post_img_path(art.get("inline_image", ""))
    inline_source_url = art.get("inline_image_source_url", inline_img_src)

    body_html_en = render_article_markdown(art["content"], inline_img_src, caption_en, inline_source_url, "en")
    body_html_vi = render_article_markdown(art.get("content_vi", art["content"]), inline_img_src, caption_vi, inline_source_url, "vi")

    prev_art = articles[i - 1] if i > 0 else None
    next_art = articles[i + 1] if i < len(articles) - 1 else None

    related = [a for a in articles if a["category"] == cat and a["id"] != art["id"]][:3]
    if len(related) < 3:
        others = [a for a in articles if a["id"] != art["id"] and a not in related]
        related.extend(others[:3 - len(related)])

    related_cards_en = ""
    related_cards_vi = ""
    for rel in related:
        rel_icon = category_icons.get(rel["category"], "📄")
        rel_bg, rel_text, _ = category_colors.get(rel["category"], ("#F1F5F9", "#334155", "#64748B"))
        rel_hero = resolve_post_img_path(rel.get("hero_image", ""))
        rel_cat_vi = category_vi.get(rel["category"], rel["category"])
        rel_title_vi = rel.get("title_vi", rel["title"])
        rel_desc_vi = rel.get("description_vi", rel["description"])

        related_cards_en += f"""
        <a href="{rel['id']}.html?lang=en" class="related-post-card">
          <div class="related-post-img" style="background-image: url('{rel_hero}');">
            <span class="related-post-badge" style="background: {rel_bg}; color: {rel_text};">
              {rel_icon} {rel['category']}
            </span>
          </div>
          <div class="related-post-info">
            <h4 class="related-post-title">{rel['title']}</h4>
            <p class="related-post-desc">{rel['description'][:90]}...</p>
            <div class="related-post-meta">
              <span>⏱ {rel['reading_time']}</span>
              <span>•</span>
              <span>{rel['type']}</span>
            </div>
          </div>
        </a>
        """
        related_cards_vi += f"""
        <a href="{rel['id']}.html?lang=vi" class="related-post-card">
          <div class="related-post-img" style="background-image: url('{rel_hero}');">
            <span class="related-post-badge" style="background: {rel_bg}; color: {rel_text};">
              {rel_icon} {rel_cat_vi}
            </span>
          </div>
          <div class="related-post-info">
            <h4 class="related-post-title">{rel_title_vi}</h4>
            <p class="related-post-desc">{rel_desc_vi[:90]}...</p>
            <div class="related-post-meta">
              <span>⏱ {rel.get('reading_time_vi', rel['reading_time'])}</span>
              <span>•</span>
              <span>{rel['type']}</span>
            </div>
          </div>
        </a>
        """

    prev_en = f"""
    <a href="{prev_art['id']}.html?lang=en" class="post-nav-btn prev">
      <span class="nav-direction">← Previous Article</span>
      <span class="nav-title">{prev_art['title']}</span>
    </a>""" if prev_art else '<div class="post-nav-placeholder"></div>'

    next_en = f"""
    <a href="{next_art['id']}.html?lang=en" class="post-nav-btn next">
      <span class="nav-direction">Next Article →</span>
      <span class="nav-title">{next_art['title']}</span>
    </a>""" if next_art else '<div class="post-nav-placeholder"></div>'

    prev_vi = f"""
    <a href="{prev_art['id']}.html?lang=vi" class="post-nav-btn prev">
      <span class="nav-direction">← Bài viết trước</span>
      <span class="nav-title">{prev_art.get('title_vi', prev_art['title'])}</span>
    </a>""" if prev_art else '<div class="post-nav-placeholder"></div>'

    next_vi = f"""
    <a href="{next_art['id']}.html?lang=vi" class="post-nav-btn next">
      <span class="nav-direction">Bài tiếp theo →</span>
      <span class="nav-title">{next_art.get('title_vi', next_art['title'])}</span>
    </a>""" if next_art else '<div class="post-nav-placeholder"></div>'

    html_page = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_vi} | {title_en}</title>
  <link rel="stylesheet" href="../styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body class="blog-post-page">
  <div class="reading-progress-container">
    <div id="reading-progress" class="reading-progress-bar"></div>
  </div>

  <!-- Sticky Top Navigation with Bilingual Switcher -->
  <header class="navbar post-navbar">
    <div class="nav-container">
      <a href="../index.html" class="brand" style="text-decoration: none;">
        <div class="brand-logo">⚡</div>
        <div class="brand-text">
          <span class="brand-title">PULSE & VITALITY</span>
          <span class="brand-subtitle" id="post-brand-subtitle">Cẩm Nang Khoa Học Sức Khỏe & Thiết Bị Đeo</span>
        </div>
      </a>
      <div class="nav-actions">
        <div class="lang-switch-group" role="group" aria-label="Language Switcher">
          <button id="post-lang-vi" class="lang-btn active" onclick="switchPostLang('vi')">🇻🇳 Tiếng Việt</button>
          <button id="post-lang-en" class="lang-btn" onclick="switchPostLang('en')">🇬🇧 English</button>
        </div>
        <a href="../index.html" class="btn-back-hub" id="post-back-btn">
          ← Quay lại Danh sách
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================================= -->
  <!-- VIETNAMESE ARTICLE CONTAINER                              -->
  <!-- ========================================================= -->
  <main id="post-container-vi" class="article-page-container">
    <nav class="article-breadcrumb">
      <a href="../index.html?lang=vi">Trang chủ</a>
      <span class="sep">/</span>
      <a href="../index.html?lang=vi">{cat_vi_name}</a>
      <span class="sep">/</span>
      <span class="current">{art['sub_topic']}</span>
    </nav>

    <header class="article-page-header">
      <div class="article-badges-row">
        <span class="badge" style="background: {bg_pill}; color: {text_pill}; font-weight: 700;">
          {icon} {cat_vi_name}
        </span>
        <span class="badge badge-sub">{art['sub_topic']}</span>
        <span class="badge badge-type">{art['type']}</span>
        <span class="article-read-time">⏱ {readtime_vi}</span>
      </div>

      <h1 class="article-main-title">{title_vi}</h1>
      <p class="article-sapo-lead">{desc_vi}</p>

      <figure class="article-featured-hero">
        <img src="{hero_img_src}" alt="{title_vi}">
        <figcaption>{title_vi} • <a href="{hero_source_url}" target="_blank" rel="noopener noreferrer" class="img-source-badge">Xem ảnh lớn ↗</a></figcaption>
      </figure>

      <div class="article-metadata-card">
        <div class="meta-avatar">PV</div>
        <div class="meta-content">
          <div class="meta-author">Pulse & Vitality • Nội dung giáo dục sức khỏe</div>
          <div class="meta-details">
            <span>Nguồn tham khảo chính: <a href="{art['source_url']}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; font-weight: 700;">{art['source_name']} ↗</a></span>
            <span class="meta-dot">•</span>
            <span>Cập nhật: <strong>{art['source_checked_date']}</strong></span>
            <span class="meta-dot">•</span>
            <span>Duyệt lâm sàng: <strong>Chưa có xác nhận</strong></span>
          </div>
        </div>
      </div>
    </header>

    <section class="takeaway-banner-large">
      <div class="takeaway-banner-header">
        <span class="takeaway-icon-lg">💡</span>
        <span>Điểm Cốt Lõi & Hành Động Thực Tế</span>
      </div>
      <p>{takeaway_vi}</p>
    </section>

    <article class="article-rich-body">
      {body_html_vi}
    </article>

    <section class="canonical-citation-card">
      <div class="citation-icon">📚</div>
      <div class="citation-body">
        <h4>Nguồn tham khảo và giới hạn bằng chứng</h4>
        <p>Nguồn chính: <strong>{art['source_name']}</strong>. Các nguồn bổ sung và phạm vi hỗ trợ được liệt kê trong bài. Cập nhật 26/10/2026; chưa có xác nhận duyệt bởi bác sĩ.</p>
        <div class="citation-actions">
          <a href="{art['source_url']}" target="_blank" rel="noopener noreferrer" class="btn-canonical-study">
            Truy Cập Nguồn Gốc ({art['source_name'][:40]}...) ↗
          </a>
        </div>
      </div>
    </section>

    <nav class="post-pagination-nav">
      {prev_vi}
      {next_vi}
    </nav>

    <section class="related-articles-section">
      <div class="related-section-header">
        <h3>Bài viết liên quan thuộc chủ đề {cat_vi_name}</h3>
      </div>
      <div class="related-posts-grid">
        {related_cards_vi}
      </div>
    </section>

    <div class="return-hub-cta">
      <a href="../index.html?lang=vi" class="btn-return-hub">← Quay lại Trang chủ & Tìm kiếm</a>
      <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="btn-scroll-top">↑ Lên đầu trang</button>
    </div>
  </main>

  <!-- ========================================================= -->
  <!-- ENGLISH ARTICLE CONTAINER                                 -->
  <!-- ========================================================= -->
  <main id="post-container-en" class="article-page-container hidden">
    <nav class="article-breadcrumb">
      <a href="../index.html?lang=en">Knowledge Hub</a>
      <span class="sep">/</span>
      <a href="../index.html?lang=en">{cat}</a>
      <span class="sep">/</span>
      <span class="current">{art['sub_topic']}</span>
    </nav>

    <header class="article-page-header">
      <div class="article-badges-row">
        <span class="badge" style="background: {bg_pill}; color: {text_pill}; font-weight: 700;">
          {icon} {cat}
        </span>
        <span class="badge badge-sub">{art['sub_topic']}</span>
        <span class="badge badge-type">{art['type']}</span>
        <span class="article-read-time">⏱ {readtime_en} read</span>
      </div>

      <h1 class="article-main-title">{title_en}</h1>
      <p class="article-sapo-lead">{desc_en}</p>

      <figure class="article-featured-hero">
        <img src="{hero_img_src}" alt="{title_en}">
        <figcaption>{title_en} • <a href="{hero_source_url}" target="_blank" rel="noopener noreferrer" class="img-source-badge">View full image ↗</a></figcaption>
      </figure>

      <div class="article-metadata-card">
        <div class="meta-avatar">PV</div>
        <div class="meta-content">
          <div class="meta-author">Pulse & Vitality • Health education</div>
          <div class="meta-details">
            <span>Primary reference: <a href="{art['source_url']}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; font-weight: 700;">{art['source_name']} ↗</a></span>
            <span class="meta-dot">•</span>
            <span>Updated: <strong>{art['source_checked_date']}</strong></span>
            <span class="meta-dot">•</span>
            <span>Clinical review: <strong>Not recorded</strong></span>
          </div>
        </div>
      </div>
    </header>

    <section class="takeaway-banner-large">
      <div class="takeaway-banner-header">
        <span class="takeaway-icon-lg">💡</span>
        <span>Key Actionable Takeaway</span>
      </div>
      <p>{takeaway_en}</p>
    </section>

    <article class="article-rich-body">
      {body_html_en}
    </article>

    <section class="canonical-citation-card">
      <div class="citation-icon">📚</div>
      <div class="citation-body">
        <h4>References and evidence limits</h4>
        <p>Primary reference: <strong>{art['source_name']}</strong>. Additional sources and their scope appear in the article. Updated 26 October 2026; clinical sign-off has not been recorded.</p>
        <div class="citation-actions">
          <a href="{art['source_url']}" target="_blank" rel="noopener noreferrer" class="btn-canonical-study">
            Access Original Source ({art['source_name'][:40]}...) ↗
          </a>
        </div>
      </div>
    </section>

    <nav class="post-pagination-nav">
      {prev_en}
      {next_en}
    </nav>

    <section class="related-articles-section">
      <div class="related-section-header">
        <h3>Related Reads in {cat}</h3>
      </div>
      <div class="related-posts-grid">
        {related_cards_en}
      </div>
    </section>

    <div class="return-hub-cta">
      <a href="../index.html?lang=en" class="btn-return-hub">← Back to Knowledge Hub & Search</a>
      <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="btn-scroll-top">↑ Back to Top</button>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <p>© 2026 Pulse & Vitality Performance Engine • Evidence-Based Wearable Health Hub (EN / VI)</p>
    </div>
  </footer>

  <script>
    if (window.mermaid) {{
      mermaid.initialize({{
        startOnLoad: false,
        theme: 'neutral',
        fontFamily: 'Plus Jakarta Sans, sans-serif',
        securityLevel: 'loose',
        flowchart: {{
          useMaxWidth: true,
          htmlLabels: true,
          curve: 'basis'
        }}
      }});
    }}

    async function renderActiveMermaid() {{
      if (window.mermaid) {{
        try {{
          const activeContainer = document.querySelector('.article-page-container:not(.hidden)');
          if (activeContainer) {{
            const nodes = activeContainer.querySelectorAll('.mermaid:not([data-processed="true"])');
            if (nodes.length > 0) {{
              await mermaid.run({{ nodes: nodes }});
            }}
          }}
        }} catch (err) {{
          console.warn('Mermaid render warning:', err);
        }}
      }}
    }}

    function switchPostLang(lang) {{
      localStorage.setItem('pv_lang', lang);
      const viContainer = document.getElementById('post-container-vi');
      const enContainer = document.getElementById('post-container-en');
      const btnVi = document.getElementById('post-lang-vi');
      const btnEn = document.getElementById('post-lang-en');
      const brandSub = document.getElementById('post-brand-subtitle');
      const backBtn = document.getElementById('post-back-btn');

      if (lang === 'en') {{
        viContainer.classList.add('hidden');
        enContainer.classList.remove('hidden');
        btnVi.classList.remove('active');
        btnEn.classList.add('active');
        brandSub.textContent = 'Health & Human Performance Knowledge Hub';
        backBtn.textContent = '← Back to All Articles';
        backBtn.href = '../index.html?lang=en';
        document.documentElement.lang = 'en';
      }} else {{
        enContainer.classList.add('hidden');
        viContainer.classList.remove('hidden');
        btnEn.classList.remove('active');
        btnVi.classList.add('active');
        brandSub.textContent = 'Cẩm Nang Khoa Học Sức Khỏe & Thiết Bị Đeo';
        backBtn.textContent = '← Quay lại Danh sách';
        backBtn.href = '../index.html?lang=vi';
        document.documentElement.lang = 'vi';
      }}
      setTimeout(renderActiveMermaid, 50);
    }}

    (function initLang() {{
      const params = new URLSearchParams(window.location.search);
      const qLang = params.get('lang');
      const saved = qLang || localStorage.getItem('pv_lang') || 'vi';
      switchPostLang(saved === 'en' ? 'en' : 'vi');
      setTimeout(renderActiveMermaid, 100);
    }})();

    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const bar = document.getElementById('reading-progress');
      if (height > 0 && bar) {{
        bar.style.width = ((winScroll / height) * 100) + '%';
      }}
    }});
  </script>
</body>
</html>
"""
    with open(os.path.join(posts_dir, f"{art['id']}.html"), "w", encoding="utf-8") as pf:
        pf.write('\n'.join(line.rstrip() for line in html_page.splitlines()) + '\n')

print(f"Successfully generated all {len(articles)} bilingual (EN + VI) standalone blog post pages!")
