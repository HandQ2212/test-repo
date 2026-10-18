// Pulse & Vitality Health Hub Frontend Controller
let allArticles = [];
let currentCategory = 'All';
let currentType = 'All';
let currentGender = 'All';
let searchQuery = '';
let isAppModalMode = false;
let currentArticle = null;

// Category Icons & Colors
const categoryIcons = {
  'Sleep': '🌙',
  'Recovery': '🔋',
  'Activity': '🏃',
  'Health & Wellness': '🌿',
  "Women's Health": '🌸',
  "Men's Health": '💪'
};

const categoryColors = {
  'Sleep': { bg: '#EDE9FE', text: '#6D28D9' },
  'Recovery': { bg: '#ECFDF5', text: '#059669' },
  'Activity': { bg: '#FEF3C7', text: '#D97706' },
  'Health & Wellness': { bg: '#E0F2FE', text: '#0284C7' },
  "Women's Health": { bg: '#FCE7F3', text: '#DB2777' },
  "Men's Health": { bg: '#E0E7FF', text: '#4338CA' }
};

function getBannerBg(cat) {
  const gradients = {
    'Sleep': 'linear-gradient(135deg, #1E1B4B 0%, #312E81 100%)',
    'Recovery': 'linear-gradient(135deg, #064E3B 0%, #065F46 100%)',
    'Activity': 'linear-gradient(135deg, #78350F 0%, #92400E 100%)',
    'Health & Wellness': 'linear-gradient(135deg, #0C4A6E 0%, #0369A1 100%)',
    "Women's Health": 'linear-gradient(135deg, #831843 0%, #9D174D 100%)',
    "Men's Health": 'linear-gradient(135deg, #1E3A8A 0%, #1D4ED8 100%)'
  };
  return gradients[cat] || 'linear-gradient(135deg, #0F172A 0%, #1E293B 100%)';
}

function getCategoryClass(cat) {
  return 'badge-' + cat.replace(/[^a-zA-Z]/g, '');
}

// Elements
const hubView = document.getElementById('hub-view');
const articleView = document.getElementById('article-view');
const grid = document.getElementById('articles-grid');
const resultsCount = document.getElementById('results-count');
const searchInput = document.getElementById('search-input');
const categoryPills = document.getElementById('category-pills');
const typeSelect = document.getElementById('type-select');
const genderSelect = document.getElementById('gender-select');
const viewModeToggle = document.getElementById('view-mode-toggle');
const readingProgressBar = document.getElementById('reading-progress');

// In-App Mobile Simulator Elements
const inappModal = document.getElementById('inapp-modal');
const inappCloseBtn = document.getElementById('inapp-close-btn');
const inappDismissBtn = document.getElementById('inapp-dismiss-btn');
const inappMetric = document.getElementById('inapp-metric');
const inappTitle = document.getElementById('inapp-title');
const inappTakeaway = document.getElementById('inapp-takeaway-text');
const inappContentBody = document.getElementById('inapp-content-body');
const inappSource = document.getElementById('inapp-source');

// Load Data
async function init() {
  if (window.ARTICLES_DATA && Array.isArray(window.ARTICLES_DATA)) {
    allArticles = window.ARTICLES_DATA;
  } else {
    try {
      const res = await fetch('articles.json');
      allArticles = await res.json();
    } catch (err) {
      console.error('Failed to load articles.json:', err);
      return;
    }
  }

  render();
  setupEventListeners();
  checkHashRoute();
}

function setupEventListeners() {
  // Category filter pills
  categoryPills.querySelectorAll('.pill').forEach(btn => {
    btn.addEventListener('click', () => {
      categoryPills.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.dataset.category;
      render();
    });
  });

  // Type filter
  typeSelect.addEventListener('change', (e) => {
    currentType = e.target.value;
    render();
  });

  // Gender filter
  genderSelect.addEventListener('change', (e) => {
    currentGender = e.target.value;
    render();
  });

  // Search input
  let debounceTimer;
  searchInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      searchQuery = e.target.value;
      render();
    }, 200);
  });

  // Mode Toggle (In-App Simulator vs Full Blog)
  viewModeToggle.addEventListener('click', () => {
    isAppModalMode = !isAppModalMode;
    if (isAppModalMode) {
      viewModeToggle.textContent = '📖 Full Blog Mode';
      viewModeToggle.classList.add('active');
    } else {
      viewModeToggle.textContent = '📱 In-App Modal Mode';
      viewModeToggle.classList.remove('active');
    }
  });

  // In-app modal close
  inappCloseBtn.addEventListener('click', () => inappModal.classList.add('hidden'));
  inappDismissBtn.addEventListener('click', () => inappModal.classList.add('hidden'));
  inappModal.addEventListener('click', (e) => {
    if (e.target === inappModal) inappModal.classList.add('hidden');
  });

  // Preview in-app button inside full article view
  document.getElementById('btn-preview-inapp').addEventListener('click', () => {
    if (currentArticle) openInAppModal(currentArticle);
  });

  // Scroll reading progress
  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (height > 0) {
      const scrolled = (winScroll / height) * 100;
      readingProgressBar.style.width = scrolled + '%';
    } else {
      readingProgressBar.style.width = '0%';
    }
  });

  // Hash route changes
  window.addEventListener('hashchange', checkHashRoute);
}

function checkHashRoute() {
  const hash = window.location.hash;
  if (hash.startsWith('#article/')) {
    const id = hash.replace('#article/', '');
    const art = allArticles.find(a => a.id === id);
    if (art) {
      openFullArticleView(art, false);
      return;
    }
  }
  // Otherwise show catalog
  if (!hash.startsWith('#article/')) {
    closeArticleView(false);
  }
}

function filterArticles() {
  return allArticles.filter(art => {
    // Category filter
    if (currentCategory !== 'All' && art.category !== currentCategory) return false;
    // Type filter
    if (currentType !== 'All' && art.type !== currentType) return false;
    // Gender filter
    if (currentGender !== 'All' && art.gender !== 'All' && art.gender !== currentGender) return false;
    // Search query
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase();
      const matchTitle = art.title.toLowerCase().includes(q);
      const matchDesc = art.description.toLowerCase().includes(q);
      const matchSub = art.sub_topic.toLowerCase().includes(q);
      const matchMetric = art.metric.toLowerCase().includes(q);
      if (!matchTitle && !matchDesc && !matchSub && !matchMetric) return false;
    }
    return true;
  });
}

function render() {
  const filtered = filterArticles();
  resultsCount.textContent = `Showing ${filtered.length} of ${allArticles.length} articles`;

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: #64748B;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
        <h3>No matching health articles found</h3>
        <p>Try clearing your search keyword or selecting "All Categories".</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(art => {
    const icon = categoryIcons[art.category] || '📄';
    const catClass = getCategoryClass(art.category);
    return `
      <div class="article-card" onclick="openArticle('${art.id}')">
        <div class="card-cover-img" style="background-image: linear-gradient(180deg, rgba(15, 23, 42, 0.25) 0%, rgba(15, 23, 42, 0.85) 100%), url('${art.hero_image}');">
          <div class="card-badges">
            <span class="badge ${catClass}">${icon} ${art.category}</span>
            <span class="badge badge-type">${art.type}</span>
          </div>
          <span class="card-metric">${art.metric}</span>
        </div>

        <div class="card-content">
          <div class="card-meta">
            <span class="card-subtopic">${art.sub_topic}</span>
            <span class="card-time">⏱ ${art.reading_time}</span>
          </div>

          <h3 class="card-title">${art.title}</h3>
          <p class="card-description">${art.description}</p>

          <div class="card-takeaway-preview">
            <span class="takeaway-icon">💡</span>
            <p>${art.takeaway.slice(0, 85)}...</p>
          </div>

          <div class="card-footer">
            <span class="card-source">${art.source_name}</span>
            <span class="card-read-action">Read Full Blog →</span>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function openArticle(id) {
  const art = allArticles.find(a => a.id === id);
  if (!art) return;

  if (isAppModalMode) {
    openInAppModal(art);
  } else {
    openFullArticleView(art, true);
  }
}

// -------------------------------------------------------------
// 1. FULL STANDALONE BLOG ARTICLE VIEW (SPA)
// -------------------------------------------------------------
function openFullArticleView(art, updateHash = true) {
  currentArticle = art;
  const icon = categoryIcons[art.category] || '📄';
  const colors = categoryColors[art.category] || { bg: '#F1F5F9', text: '#334155' };

  // Set breadcrumbs
  document.getElementById('article-view-cat-breadcrumb').textContent = art.category;
  document.getElementById('article-view-subtopic-breadcrumb').textContent = art.sub_topic;

  // Set Header Badges
  const catBadge = document.getElementById('art-view-category');
  catBadge.textContent = `${icon} ${art.category}`;
  catBadge.style.background = colors.bg;
  catBadge.style.color = colors.text;

  document.getElementById('art-view-subtopic').textContent = art.sub_topic;
  document.getElementById('art-view-type').textContent = art.type;
  document.getElementById('art-view-readtime').textContent = `⏱ ${art.reading_time} read`;

  // Set Title & Sapo
  document.getElementById('art-view-title').textContent = art.title;
  document.getElementById('art-view-sapo').textContent = art.description;

  // Set Featured Hero Image
  const heroImg = document.getElementById('art-view-hero-img');
  const heroCaption = document.getElementById('art-view-hero-caption');
  if (heroImg && art.hero_image) {
    heroImg.src = art.hero_image;
    heroImg.alt = art.title;
    heroCaption.textContent = `${art.title} — Clinical Editorial Feature`;
  }

  // Set Meta details
  document.getElementById('art-view-source').textContent = art.source_name;
  document.getElementById('art-view-screen').textContent = art.screen;
  document.getElementById('art-view-metric').textContent = art.metric;

  // Set Takeaway
  document.getElementById('art-view-takeaway').textContent = art.takeaway;

  // Render Markdown Body with Injected Inline Diagram Image (if not already embedded in markdown)
  let parsedHtml = marked.parse(art.content);
  if (art.inline_image && !parsedHtml.includes('article-inline-diagram')) {
    const inlineDiagramHtml = `
      <figure class="article-inline-diagram">
        <img src="${art.inline_image}" alt="${art.inline_caption}" loading="lazy">
        <figcaption>📊 <strong>Clinical Biometric Visual:</strong> ${art.inline_caption}</figcaption>
      </figure>
    `;

    const h2Idx = parsedHtml.indexOf('</h2>');
    if (h2Idx !== -1) {
      const afterH2 = h2Idx + 5;
      const pIdx = parsedHtml.indexOf('</p>', afterH2);
      if (pIdx !== -1) {
        const insertPos = pIdx + 4;
        parsedHtml = parsedHtml.slice(0, insertPos) + inlineDiagramHtml + parsedHtml.slice(insertPos);
      } else {
        parsedHtml = parsedHtml.slice(0, afterH2) + inlineDiagramHtml + parsedHtml.slice(afterH2);
      }
    } else {
      parsedHtml = inlineDiagramHtml + parsedHtml;
    }
  }
  document.getElementById('art-view-body').innerHTML = parsedHtml;

  // Set Canonical Citation
  document.getElementById('art-view-citation-desc').innerHTML = `
    This article is synthesized from peer-reviewed physiology, clinical guidelines, and wearable biometric methodologies developed by <strong>${art.source_name}</strong>.
  `;
  const canonicalLink = document.getElementById('art-view-canonical-link');
  canonicalLink.href = art.source_url;

  // Toolbar Standalone File link
  const standaloneLink = document.getElementById('btn-open-standalone');
  standaloneLink.href = `posts/${art.id}.html`;

  // Pagination (Previous & Next articles)
  const currentIndex = allArticles.findIndex(a => a.id === art.id);
  const prevArt = currentIndex > 0 ? allArticles[currentIndex - 1] : null;
  const nextArt = currentIndex < allArticles.length - 1 ? allArticles[currentIndex + 1] : null;

  let paginationHtml = '';
  if (prevArt) {
    paginationHtml += `
      <div class="post-nav-btn prev" onclick="openArticle('${prevArt.id}')" style="cursor: pointer;">
        <span class="nav-direction">← Previous Article</span>
        <span class="nav-title">${prevArt.title}</span>
      </div>
    `;
  } else {
    paginationHtml += '<div class="post-nav-placeholder"></div>';
  }

  if (nextArt) {
    paginationHtml += `
      <div class="post-nav-btn next" onclick="openArticle('${nextArt.id}')" style="cursor: pointer;">
        <span class="nav-direction">Next Article →</span>
        <span class="nav-title">${nextArt.title}</span>
      </div>
    `;
  } else {
    paginationHtml += '<div class="post-nav-placeholder"></div>';
  }
  document.getElementById('art-view-pagination').innerHTML = paginationHtml;

  // Related Articles (same category, different id)
  const related = allArticles.filter(a => a.category === art.category && a.id !== art.id).slice(0, 3);
  if (related.length < 3) {
    const others = allArticles.filter(a => a.id !== art.id && !related.includes(a)).slice(0, 3 - related.length);
    related.push(...others);
  }

  document.getElementById('art-view-related-heading').textContent = `Related Reads in ${art.category}`;
  document.getElementById('art-view-related-grid').innerHTML = related.map(rel => {
    const relIcon = categoryIcons[rel.category] || '📄';
    const relColors = categoryColors[rel.category] || { bg: '#F1F5F9', text: '#334155' };
    return `
      <div class="related-post-card" onclick="openArticle('${rel.id}')" style="cursor: pointer;">
        <div class="related-post-img" style="background-image: url('${rel.hero_image}');">
          <span class="related-post-badge" style="background: ${relColors.bg}; color: ${relColors.text};">
            ${relIcon} ${rel.category}
          </span>
        </div>
        <div class="related-post-info">
          <h4 class="related-post-title">${rel.title}</h4>
          <p class="related-post-desc">${rel.description.slice(0, 85)}...</p>
          <div class="related-post-meta">
            <span>⏱ ${rel.reading_time}</span>
            <span>•</span>
            <span>${rel.type}</span>
          </div>
        </div>
      </div>
    `;
  }).join('');

  // Switch Views
  hubView.style.display = 'none';
  articleView.classList.remove('hidden');
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Update URL hash & document title
  if (updateHash) {
    window.location.hash = 'article/' + art.id;
  }
  document.title = `${art.title} — Pulse & Vitality Blog`;
}

function closeArticleView(clearHash = true) {
  articleView.classList.add('hidden');
  hubView.style.display = 'block';
  document.title = 'Health & Human Performance Knowledge Hub (Demo)';
  if (clearHash && window.location.hash.startsWith('#article/')) {
    history.pushState(null, '', window.location.pathname);
  }
}

// -------------------------------------------------------------
// 2. IN-APP MOBILE SIMULATOR MODAL
// -------------------------------------------------------------
function openInAppModal(art) {
  inappMetric.textContent = art.metric;
  inappTitle.textContent = art.title;
  inappTakeaway.textContent = art.takeaway;
  inappContentBody.innerHTML = marked.parse(art.content);
  inappSource.textContent = `Source: ${art.source_name}`;
  inappModal.classList.remove('hidden');
}

// Start app
init();
