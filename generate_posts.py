import json
import os
import markdown

with open("Health_Blog_Demo/articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

category_icons = {
    "Sleep": "🌙",
    "Recovery": "🔋",
    "Activity": "🏃",
    "Health & Wellness": "🌿",
    "Women's Health": "🌸",
    "Men's Health": "💪"
}

category_colors = {
    "Sleep": ("#EDE9FE", "#6D28D9", "#8B5CF6"),
    "Recovery": ("#ECFDF5", "#059669", "#10B981"),
    "Activity": ("#FEF3C7", "#D97706", "#F59E0B"),
    "Health & Wellness": ("#E0F2FE", "#0284C7", "#0EA5E9"),
    "Women's Health": ("#FCE7F3", "#DB2777", "#EC4899"),
    "Men's Health": ("#E0E7FF", "#4338CA", "#6366F1")
}

def clean_cat_id(cat):
    return ''.join(c for c in cat if c.isalnum())

os.makedirs("Health_Blog_Demo/posts", exist_ok=True)

for i, art in enumerate(articles):
    cat = art["category"]
    icon = category_icons.get(cat, "📄")
    bg_pill, text_pill, accent_col = category_colors.get(cat, ("#F1F5F9", "#334155", "#64748B"))
    
    # Pre-render markdown to HTML
    body_html = markdown.markdown(
        art["content"],
        extensions=['extra', 'tables', 'nl2br', 'sane_lists']
    )
    
    # Previous and Next articles
    prev_art = articles[i - 1] if i > 0 else None
    next_art = articles[i + 1] if i < len(articles) - 1 else None
    
    # Related articles (same category, different id)
    related = [a for a in articles if a["category"] == cat and a["id"] != art["id"]][:3]
    if len(related) < 3:
        # fill with others if less than 3
        others = [a for a in articles if a["id"] != art["id"] and a not in related]
        related.extend(others[:3 - len(related)])
        
    related_html_cards = ""
    for rel in related:
        rel_icon = category_icons.get(rel["category"], "📄")
        rel_bg, rel_text, _ = category_colors.get(rel["category"], ("#F1F5F9", "#334155", "#64748B"))
        related_html_cards += f"""
        <a href="{rel['id']}.html" class="related-post-card">
          <div class="related-post-badge" style="background: {rel_bg}; color: {rel_text};">
            {rel_icon} {rel['category']}
          </div>
          <h4 class="related-post-title">{rel['title']}</h4>
          <p class="related-post-desc">{rel['description'][:95]}...</p>
          <div class="related-post-meta">
            <span>⏱ {rel['reading_time']}</span>
            <span>•</span>
            <span>{rel['type']}</span>
          </div>
        </a>
        """

    prev_button_html = f"""
    <a href="{prev_art['id']}.html" class="post-nav-btn prev">
      <span class="nav-direction">← Previous Article</span>
      <span class="nav-title">{prev_art['title']}</span>
    </a>
    """ if prev_art else '<div class="post-nav-placeholder"></div>'

    next_button_html = f"""
    <a href="{next_art['id']}.html" class="post-nav-btn next">
      <span class="nav-direction">Next Article →</span>
      <span class="nav-title">{next_art['title']}</span>
    </a>
    """ if next_art else '<div class="post-nav-placeholder"></div>'

    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{art['title']} — Pulse & Vitality Blog</title>
  <link rel="stylesheet" href="../styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
</head>
<body class="blog-post-page">
  <!-- Reading Progress Bar -->
  <div class="reading-progress-container">
    <div id="reading-progress" class="reading-progress-bar"></div>
  </div>

  <!-- Sticky Top Navigation -->
  <header class="navbar post-navbar">
    <div class="nav-container">
      <a href="../index.html" class="brand" style="text-decoration: none;">
        <div class="brand-logo">⚡</div>
        <div class="brand-text">
          <span class="brand-title">PULSE & VITALITY</span>
          <span class="brand-subtitle">Health & Human Performance Knowledge Hub</span>
        </div>
      </a>
      <div class="nav-actions">
        <a href="../index.html" class="btn-back-hub">
          ← Back to All Articles
        </a>
      </div>
    </div>
  </header>

  <!-- Main Article Layout -->
  <main class="article-page-container">
    <!-- Breadcrumb -->
    <nav class="article-breadcrumb">
      <a href="../index.html">Knowledge Hub</a>
      <span class="sep">/</span>
      <a href="../index.html?cat={cat}">{cat}</a>
      <span class="sep">/</span>
      <span class="current">{art['sub_topic']}</span>
    </nav>

    <!-- Article Hero -->
    <header class="article-page-header">
      <div class="article-badges-row">
        <span class="badge" style="background: {bg_pill}; color: {text_pill}; font-weight: 700;">
          {icon} {cat}
        </span>
        <span class="badge badge-sub">{art['sub_topic']}</span>
        <span class="badge badge-type">{art['type']}</span>
        <span class="article-read-time">⏱ {art['reading_time']} read</span>
      </div>

      <h1 class="article-main-title">{art['title']}</h1>
      
      <p class="article-sapo-lead">{art['description']}</p>

      <!-- Editorial & Clinical Metadata Card -->
      <div class="article-metadata-card">
        <div class="meta-avatar">PV</div>
        <div class="meta-content">
          <div class="meta-author">Pulse & Vitality Clinical Editorial Board</div>
          <div class="meta-details">
            <span>Clinical Wearable Reference: <strong>{art['source_name']}</strong></span>
            <span class="meta-dot">•</span>
            <span>Mapped Screen: <strong>{art['screen']}</strong></span>
            <span class="meta-dot">•</span>
            <span>Metric: <strong>{art['metric']}</strong></span>
          </div>
        </div>
      </div>
    </header>

    <!-- Key Actionable Takeaway Banner -->
    <section class="takeaway-banner-large">
      <div class="takeaway-banner-header">
        <span class="takeaway-icon-lg">💡</span>
        <span>Key Actionable Takeaway</span>
      </div>
      <p>{art['takeaway']}</p>
    </section>

    <!-- Full Article Markdown Content -->
    <article class="article-rich-body">
      {body_html}
    </article>

    <!-- Canonical Source Reference Box -->
    <section class="canonical-citation-card">
      <div class="citation-icon">📚</div>
      <div class="citation-body">
        <h4>Clinical Reference & Scientific Backing</h4>
        <p>This article is synthesized from peer-reviewed physiology, clinical guidelines, and wearable biometric methodologies developed by <strong>{art['source_name']}</strong>.</p>
        <div class="citation-actions">
          <a href="{art['source_url']}" target="_blank" rel="noopener noreferrer" class="btn-canonical-study">
            Read Canonical Study / Original Article ↗
          </a>
        </div>
      </div>
    </section>

    <!-- Next / Previous Article Navigation -->
    <nav class="post-pagination-nav">
      {prev_button_html}
      {next_button_html}
    </nav>

    <!-- Related Articles Section -->
    <section class="related-articles-section">
      <div class="related-section-header">
        <h3>Related Reads in {cat}</h3>
        <a href="../index.html?cat={cat}" class="view-all-link">View all {cat} articles →</a>
      </div>
      <div class="related-posts-grid">
        {related_html_cards}
      </div>
    </section>

    <!-- Return to Hub Footer CTA -->
    <div class="return-hub-cta">
      <a href="../index.html" class="btn-return-hub">
        ← Back to Knowledge Hub & Search
      </a>
      <button onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" class="btn-scroll-top">
        ↑ Back to Top
      </button>
    </div>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p>© 2026 Pulse & Vitality Performance Engine • Built for iOS / Android Wearable Integration</p>
      <p class="disclaimer">Clinical data curated from Flo Health, Clue, Natural Cycles, Fitbit Blog, WHOOP The Locker, Maven Clinic, and Dr. Kegel.</p>
    </div>
  </footer>

  <script>
    // Reading Progress Indicator
    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('reading-progress').style.width = scrolled + '%';
    }});
  </script>
</body>
</html>
"""
    file_path = f"Health_Blog_Demo/posts/{art['id']}.html"
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(html_page)

print(f"Successfully generated {len(articles)} individual blog post pages in Health_Blog_Demo/posts/")
