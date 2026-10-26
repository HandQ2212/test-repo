// Pulse & Vitality Health Hub Frontend Controller (Bilingual EN / VI)
let allArticles = [];
let currentCategory = 'All';
let currentType = 'All';
let currentGender = 'All';
let searchQuery = '';
let isAppModalMode = false;
let currentArticle = null;
let currentLang = localStorage.getItem('pv_lang') || 'vi';

// Check URL query parameter ?lang=en or ?lang=vi
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('lang') === 'en' || urlParams.get('lang') === 'vi') {
  currentLang = urlParams.get('lang');
  localStorage.setItem('pv_lang', currentLang);
}

// Category Icons & Colors
const categoryIcons = {
  'Sleep': '🌙',
  'Recovery': '🔋',
  'Activity': '🏃',
  'Health & Wellness': '🌿',
  "Women's Health": '🌸',
  "Men's Health": '💪'
};

const categoryTranslations = {
  en: {
    'All': 'All Categories',
    'Sleep': '🌙 Sleep',
    'Recovery': '🔋 Recovery',
    'Activity': '🏃 Activity',
    'Health & Wellness': '🌿 Health & Wellness',
    "Women's Health": "🌸 Women's Health",
    "Men's Health": "💪 Men's Health"
  },
  vi: {
    'All': 'Tất cả chủ đề',
    'Sleep': '🌙 Giấc ngủ',
    'Recovery': '🔋 Phục hồi',
    'Activity': '🏃 Vận động',
    'Health & Wellness': '🌿 Sức khỏe toàn diện',
    "Women's Health": '🌸 Sức khỏe Nữ giới',
    "Men's Health": '💪 Sức khỏe Nam giới'
  }
};

const categoryNameOnly = {
  en: {
    'Sleep': 'Sleep',
    'Recovery': 'Recovery',
    'Activity': 'Activity',
    'Health & Wellness': 'Health & Wellness',
    "Women's Health": "Women's Health",
    "Men's Health": "Men's Health"
  },
  vi: {
    'Sleep': 'Giấc ngủ',
    'Recovery': 'Phục hồi',
    'Activity': 'Vận động',
    'Health & Wellness': 'Sức khỏe toàn diện',
    "Women's Health": 'Sức khỏe Nữ giới',
    "Men's Health": 'Sức khỏe Nam giới'
  }
};

const uiStrings = {
  en: {
    brandSubtitle: 'Health & Human Performance Knowledge Hub',
    heroBadge: 'Health education • Sources and limitations',
    heroTitle: 'Evidence-Based Science for Sleep, Recovery, Activity & Longevity',
    heroSubtitle: 'Explore 83 bilingual health guides with linked sources, practical advice and clearly labelled editorial illustrations.',
    searchPlaceholder: 'Search by topic, metric (HRV, Deep Sleep, BBT, VO2 Max, Kegel), or keywords...',
    labelCategory: 'Category:',
    labelFormat: 'Format:',
    labelAudience: 'Audience:',
    typeAll: 'All Formats',
    typeLearn: 'Learn more (Metric Explainers)',
    typeDiscover: 'Discover more (Topic Guides)',
    genderAll: 'All Audiences',
    genderFemale: 'Female (Cycle & Hormonal)',
    genderMale: 'Male (Pelvic & Stamina)',
    inAppModeBtn: '📱 In-App Modal Mode',
    fullBlogModeBtn: '📖 Full Blog Mode',
    showingCount: (shown, total) => `Showing ${shown} of ${total} articles`,
    noResultsTitle: 'No matching health articles found',
    noResultsDesc: 'Try clearing your search keyword or selecting "All Categories".',
    readFullBlog: 'Read Full Blog →',
    backToHub: '← Back to All Articles',
    previewInApp: '📱 In-App Tooltip View',
    standaloneFile: '📄 Standalone File ↗',
    authorBoard: 'Pulse & Vitality • Health education',
    metaRef: 'Primary reference:',
    metaScreen: 'Mapped Screen:',
    metaMetric: 'Biometric:',
    takeawayHeader: 'Key Actionable Takeaway',
    citationHeader: 'References and evidence limits',
    citationDesc: (source) => `Primary reference: <strong>${source}</strong>. The article lists additional sources and what each supports. Content updated 26 October 2026; clinical sign-off has not been recorded.`,
    readCanonicalBtn: 'Read primary reference ↗',
    prevArticle: '← Previous Article',
    nextArticle: 'Next Article →',
    relatedHeading: (cat) => `Related Reads in ${cat}`,
    returnHubBottom: '← Back to Knowledge Hub & Search',
    scrollTopBottom: '↑ Back to Top',
    heroPhotoSourceLabel: 'Original editorial artwork ↗',
    inlineFigSourceLabel: 'Editorial summary artwork ↗',
    gotIt: 'Got It'
  },
  vi: {
    brandSubtitle: 'Cẩm Nang Khoa Học Sức Khỏe & Thiết Bị Đeo Thông Minh',
    heroBadge: 'Kiến thức sức khỏe • Nguồn và giới hạn bằng chứng',
    heroTitle: 'Khoa Học Thực Chứng Về Giấc Ngủ, Phục Hồi, Vận Động & Sức Khỏe',
    heroSubtitle: '83 bài song ngữ với nguồn trích dẫn, hướng dẫn thực tế và minh họa biên tập được ghi rõ xuất xứ.',
    searchPlaceholder: 'Tìm kiếm theo chủ đề, chỉ số (HRV, Ngủ sâu, BBT, VO2 Max, Kegel) hoặc từ khóa...',
    labelCategory: 'Chủ đề:',
    labelFormat: 'Định dạng:',
    labelAudience: 'Đối tượng:',
    typeAll: 'Tất cả định dạng',
    typeLearn: 'Learn more (Giải thích chỉ số)',
    typeDiscover: 'Discover more (Hướng dẫn theo chủ đề)',
    genderAll: 'Tất cả đối tượng',
    genderFemale: 'Nữ giới (Chu kỳ & Nội tiết)',
    genderMale: 'Nam giới (Sàn chậu & Sinh lý)',
    inAppModeBtn: '📱 Chế độ Popup Trong App',
    fullBlogModeBtn: '📖 Chế độ Trang Blog Đầy Đủ',
    showingCount: (shown, total) => `Đang hiển thị ${shown} / ${total} bài viết`,
    noResultsTitle: 'Không tìm thấy bài viết phù hợp',
    noResultsDesc: 'Hãy thử xóa từ khóa tìm kiếm hoặc chọn "Tất cả chủ đề".',
    readFullBlog: 'Đọc bài viết đầy đủ →',
    backToHub: '← Quay lại Danh sách Bài viết',
    previewInApp: '📱 Xem thử Popup App',
    standaloneFile: '📄 Mở trang HTML riêng ↗',
    authorBoard: 'Pulse & Vitality • Nội dung giáo dục sức khỏe',
    metaRef: 'Nguồn tham khảo chính:',
    metaScreen: 'Màn hình App:',
    metaMetric: 'Chỉ số đo:',
    takeawayHeader: 'Điểm Cốt Lõi & Hành Động Thực Tế',
    citationHeader: 'Nguồn tham khảo và giới hạn bằng chứng',
    citationDesc: (source) => `Nguồn chính: <strong>${source}</strong>. Danh mục trong bài ghi rõ các nguồn khác và phạm vi hỗ trợ. Cập nhật 26/10/2026; chưa có xác nhận duyệt bởi bác sĩ.`,
    readCanonicalBtn: 'Đọc nguồn tham khảo chính ↗',
    prevArticle: '← Bài viết trước',
    nextArticle: 'Bài tiếp theo →',
    relatedHeading: (cat) => `Bài viết liên quan thuộc chủ đề ${cat}`,
    returnHubBottom: '← Quay lại Trang chủ & Tìm kiếm',
    scrollTopBottom: '↑ Lên đầu trang',
    heroPhotoSourceLabel: 'Mở minh họa biên tập gốc ↗',
    inlineFigSourceLabel: 'Mở sơ đồ tóm tắt biên tập ↗',
    gotIt: 'Đã hiểu'
  }
};

const categoryColors = {
  'Sleep': { bg: '#EDE9FE', text: '#6D28D9' },
  'Recovery': { bg: '#ECFDF5', text: '#059669' },
  'Activity': { bg: '#FEF3C7', text: '#D97706' },
  'Health & Wellness': { bg: '#E0F2FE', text: '#0284C7' },
  "Women's Health": { bg: '#FCE7F3', text: '#DB2777' },
  "Men's Health": { bg: '#E0E7FF', text: '#4338CA' }
};

function getCategoryClass(cat) {
  return 'badge-' + cat.replace(/[^a-zA-Z]/g, '');
}

// Helper getters for localized article fields
function getTitle(art) {
  return (currentLang === 'vi' && art.title_vi) ? art.title_vi : art.title;
}
function getDesc(art) {
  return (currentLang === 'vi' && art.description_vi) ? art.description_vi : art.description;
}
function getTakeaway(art) {
  return (currentLang === 'vi' && art.takeaway_vi) ? art.takeaway_vi : art.takeaway;
}
function getReadTime(art) {
  return (currentLang === 'vi' && art.reading_time_vi) ? art.reading_time_vi : art.reading_time;
}
function getContent(art) {
  return (currentLang === 'vi' && art.content_vi) ? art.content_vi : art.content;
}
function getInlineCaption(art) {
  return (currentLang === 'vi' && art.inline_caption_vi) ? art.inline_caption_vi : art.inline_caption;
}
function getCatLabel(cat) {
  return (categoryNameOnly[currentLang] && categoryNameOnly[currentLang][cat]) || cat;
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

// Language Switcher Function
window.setLanguage = function(lang) {
  if (lang !== 'en' && lang !== 'vi') return;
  currentLang = lang;
  localStorage.setItem('pv_lang', lang);
  document.documentElement.lang = lang;

  const btnVi = document.getElementById('lang-btn-vi');
  const btnEn = document.getElementById('lang-btn-en');
  if (btnVi && btnEn) {
    btnVi.classList.toggle('active', lang === 'vi');
    btnEn.classList.toggle('active', lang === 'en');
  }

  applyUITranslations();
  render();

  if (currentArticle && !articleView.classList.contains('hidden')) {
    openFullArticleView(currentArticle, false);
  }
};

function applyUITranslations() {
  const t = uiStrings[currentLang];
  const brandSub = document.querySelector('.brand-subtitle');
  if (brandSub) brandSub.textContent = t.brandSubtitle;

  const setElText = (id, text) => {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
  };

  setElText('hero-badge', t.heroBadge);
  setElText('hero-title', t.heroTitle);
  setElText('hero-subtitle', t.heroSubtitle);
  if (searchInput) searchInput.placeholder = t.searchPlaceholder;

  setElText('filter-label-category', t.labelCategory);
  setElText('filter-label-format', t.labelFormat);
  setElText('filter-label-audience', t.labelAudience);

  // Category Pills
  if (categoryPills) {
    categoryPills.querySelectorAll('.pill').forEach(btn => {
      const cat = btn.dataset.category;
      if (categoryTranslations[currentLang][cat]) {
        btn.textContent = categoryTranslations[currentLang][cat];
      }
    });
  }

  // Dropdowns
  if (typeSelect && typeSelect.options.length >= 3) {
    typeSelect.options[0].textContent = t.typeAll;
    typeSelect.options[1].textContent = t.typeLearn;
    typeSelect.options[2].textContent = t.typeDiscover;
  }
  if (genderSelect && genderSelect.options.length >= 3) {
    genderSelect.options[0].textContent = t.genderAll;
    genderSelect.options[1].textContent = t.genderFemale;
    genderSelect.options[2].textContent = t.genderMale;
  }

  if (viewModeToggle) {
    viewModeToggle.textContent = isAppModalMode ? t.fullBlogModeBtn : t.inAppModeBtn;
  }

  setElText('btn-back-hub-top', t.backToHub);
  setElText('btn-preview-inapp', t.previewInApp);
  setElText('art-view-author-board', t.authorBoard);
  setElText('meta-label-ref', t.metaRef);
  setElText('meta-label-screen', t.metaScreen);
  setElText('meta-label-metric', t.metaMetric);
  setElText('takeaway-header-label', t.takeawayHeader);
  setElText('citation-header-label', t.citationHeader);
  setElText('art-view-canonical-link', t.readCanonicalBtn);
  setElText('btn-return-hub-bottom', t.returnHubBottom);
  setElText('btn-scroll-top-bottom', t.scrollTopBottom);
  if (inappDismissBtn) inappDismissBtn.textContent = t.gotIt;
}

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

  setLanguage(currentLang);
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
    const t = uiStrings[currentLang];
    if (isAppModalMode) {
      viewModeToggle.textContent = t.fullBlogModeBtn;
      viewModeToggle.classList.add('active');
    } else {
      viewModeToggle.textContent = t.inAppModeBtn;
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
  if (!hash.startsWith('#article/')) {
    closeArticleView(false);
  }
}

function filterArticles() {
  return allArticles.filter(art => {
    if (currentCategory !== 'All' && art.category !== currentCategory) return false;
    if (currentType !== 'All' && art.type !== currentType) return false;
    if (currentGender !== 'All' && art.gender !== 'All' && art.gender !== currentGender) return false;
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase();
      const haystacks = [
        art.title, art.title_vi,
        art.description, art.description_vi,
        art.sub_topic, art.metric, art.id
      ].filter(Boolean).map(s => s.toLowerCase());
      if (!haystacks.some(h => h.includes(q))) return false;
    }
    return true;
  });
}

function render() {
  const t = uiStrings[currentLang];
  const filtered = filterArticles();
  resultsCount.textContent = t.showingCount(filtered.length, allArticles.length);

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: #64748B;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
        <h3>${t.noResultsTitle}</h3>
        <p>${t.noResultsDesc}</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(art => {
    const icon = categoryIcons[art.category] || '📄';
    const catClass = getCategoryClass(art.category);
    const title = getTitle(art);
    const desc = getDesc(art);
    const takeaway = getTakeaway(art);
    const readTime = getReadTime(art);
    const catLabel = getCatLabel(art.category);

    return `
      <div class="article-card" onclick="openArticle('${art.id}')">
        <div class="card-cover-img" style="background-image: linear-gradient(180deg, rgba(15, 23, 42, 0.25) 0%, rgba(15, 23, 42, 0.85) 100%), url('${art.hero_image}');">
          <div class="card-badges">
            <span class="badge ${catClass}">${icon} ${catLabel}</span>
            <span class="badge badge-type">${art.type}</span>
          </div>
          <span class="card-metric">${art.metric}</span>
        </div>

        <div class="card-content">
          <div class="card-meta">
            <span class="card-subtopic">${art.sub_topic}</span>
            <span class="card-time">⏱ ${readTime}</span>
          </div>

          <h3 class="card-title">${title}</h3>
          <p class="card-description">${desc}</p>

          <div class="card-takeaway-preview">
            <span class="takeaway-icon">💡</span>
            <p>${takeaway.slice(0, 95)}...</p>
          </div>

          <div class="card-footer">
            <span class="card-source">${art.source_name}</span>
            <span class="card-read-action">${t.readFullBlog}</span>
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
  const t = uiStrings[currentLang];
  const icon = categoryIcons[art.category] || '📄';
  const colors = categoryColors[art.category] || { bg: '#F1F5F9', text: '#334155' };
  const title = getTitle(art);
  const desc = getDesc(art);
  const takeaway = getTakeaway(art);
  const readTime = getReadTime(art);
  const contentMd = getContent(art);
  const inlineCaption = getInlineCaption(art);
  const catLabel = getCatLabel(art.category);

  // Set breadcrumbs
  document.getElementById('article-view-cat-breadcrumb').textContent = catLabel;
  document.getElementById('article-view-subtopic-breadcrumb').textContent = art.sub_topic;

  // Set Header Badges
  const catBadge = document.getElementById('art-view-category');
  catBadge.textContent = `${icon} ${catLabel}`;
  catBadge.style.background = colors.bg;
  catBadge.style.color = colors.text;

  document.getElementById('art-view-subtopic').textContent = art.sub_topic;
  document.getElementById('art-view-type').textContent = art.type;
  document.getElementById('art-view-readtime').textContent = `⏱ ${readTime}`;

  // Set Title & Sapo
  document.getElementById('art-view-title').textContent = title;
  document.getElementById('art-view-sapo').textContent = desc;

  // Set Featured Hero Image + Verified Original Source Link
  const heroImg = document.getElementById('art-view-hero-img');
  const heroCaption = document.getElementById('art-view-hero-caption');
  if (heroImg && art.hero_image) {
    heroImg.src = art.hero_image;
    heroImg.alt = title;
    const heroSourceUrl = art.hero_image_source_url || art.hero_image;
    heroCaption.innerHTML = `${title} • <a href="${heroSourceUrl}" target="_blank" rel="noopener noreferrer" class="img-source-badge">${t.heroPhotoSourceLabel}</a>`;
  }

  // Set Meta details
  const srcEl = document.getElementById('art-view-source');
  if (srcEl) {
    srcEl.innerHTML = `<a href="${art.source_url}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; font-weight: 700;">${art.source_name} ↗</a>`;
  }
  document.getElementById('art-view-screen').textContent = art.screen;
  document.getElementById('art-view-metric').textContent = art.metric;

  // Set Takeaway
  document.getElementById('art-view-takeaway').textContent = takeaway;

  // Render Markdown Body with Injected Inline Diagram Image (if not already embedded in markdown)
  let parsedHtml = marked.parse(contentMd);
  if (art.inline_image && !parsedHtml.includes('article-inline-diagram')) {
    const figSourceUrl = art.inline_image_source_url || art.inline_image;
    const inlineDiagramHtml = `
      <figure class="article-inline-diagram">
        <img src="${art.inline_image}" alt="${inlineCaption}" loading="lazy">
        <figcaption>📊 <strong>${inlineCaption}</strong> <a href="${figSourceUrl}" target="_blank" rel="noopener noreferrer" class="img-source-badge">(${t.inlineFigSourceLabel})</a></figcaption>
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

  // Convert mermaid code blocks to <div class="mermaid"> with decoded entities
  parsedHtml = processMermaidDiagrams(parsedHtml);
  document.getElementById('art-view-body').innerHTML = parsedHtml;
  renderMermaidNodes('#art-view-body');

  // Set Canonical Citation
  document.getElementById('art-view-citation-desc').innerHTML = t.citationDesc(art.source_name);
  const canonicalLink = document.getElementById('art-view-canonical-link');
  canonicalLink.href = art.source_url;
  const shortSource = art.source_name.length > 40 ? art.source_name.slice(0, 38) + '...' : art.source_name;
  canonicalLink.textContent = currentLang === 'vi' 
    ? `Truy Cập Nguồn Gốc (${shortSource}) ↗` 
    : `Access Original Source (${shortSource}) ↗`;

  // Toolbar Standalone File link
  const standaloneLink = document.getElementById('btn-open-standalone');
  standaloneLink.href = `posts/${art.id}.html?lang=${currentLang}`;
  standaloneLink.textContent = t.standaloneFile;

  // Pagination (Previous & Next articles)
  const currentIndex = allArticles.findIndex(a => a.id === art.id);
  const prevArt = currentIndex > 0 ? allArticles[currentIndex - 1] : null;
  const nextArt = currentIndex < allArticles.length - 1 ? allArticles[currentIndex + 1] : null;

  let paginationHtml = '';
  if (prevArt) {
    paginationHtml += `
      <div class="post-nav-btn prev" onclick="openArticle('${prevArt.id}')" style="cursor: pointer;">
        <span class="nav-direction">${t.prevArticle}</span>
        <span class="nav-title">${getTitle(prevArt)}</span>
      </div>
    `;
  } else {
    paginationHtml += '<div class="post-nav-placeholder"></div>';
  }

  if (nextArt) {
    paginationHtml += `
      <div class="post-nav-btn next" onclick="openArticle('${nextArt.id}')" style="cursor: pointer;">
        <span class="nav-direction">${t.nextArticle}</span>
        <span class="nav-title">${getTitle(nextArt)}</span>
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

  document.getElementById('art-view-related-heading').textContent = t.relatedHeading(catLabel);
  document.getElementById('art-view-related-grid').innerHTML = related.map(rel => {
    const relIcon = categoryIcons[rel.category] || '📄';
    const relColors = categoryColors[rel.category] || { bg: '#F1F5F9', text: '#334155' };
    return `
      <div class="related-post-card" onclick="openArticle('${rel.id}')" style="cursor: pointer;">
        <div class="related-post-img" style="background-image: url('${rel.hero_image}');">
          <span class="related-post-badge" style="background: ${relColors.bg}; color: ${relColors.text};">
            ${relIcon} ${getCatLabel(rel.category)}
          </span>
        </div>
        <div class="related-post-info">
          <h4 class="related-post-title">${getTitle(rel)}</h4>
          <p class="related-post-desc">${getDesc(rel).slice(0, 85)}...</p>
          <div class="related-post-meta">
            <span>⏱ ${getReadTime(rel)}</span>
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

  if (updateHash) {
    window.location.hash = 'article/' + art.id;
  }
  document.title = `${title} — Pulse & Vitality Blog`;
}

function closeArticleView(clearHash = true) {
  articleView.classList.add('hidden');
  hubView.style.display = 'block';
  document.title = currentLang === 'vi'
    ? 'Cẩm Nang Khoa Học Sức Khỏe & Thiết Bị Đeo Thông Minh'
    : 'Health & Human Performance Knowledge Hub';
  if (clearHash && window.location.hash.startsWith('#article/')) {
    history.pushState(null, '', window.location.pathname);
  }
}

// -------------------------------------------------------------
// MERMAID DIAGRAM HELPERS
// -------------------------------------------------------------
function processMermaidDiagrams(htmlString) {
  if (!htmlString) return htmlString;
  return htmlString.replace(/<pre><code class="(?:language-)?mermaid">([\s\S]*?)<\/code><\/pre>/gi, function(match, code) {
    const txt = document.createElement('textarea');
    txt.innerHTML = code;
    return '<div class="mermaid">' + txt.value.trim() + '</div>';
  });
}

function renderMermaidNodes(selector) {
  if (window.mermaid) {
    setTimeout(async () => {
      try {
        const nodes = document.querySelectorAll(selector + ' .mermaid:not([data-processed="true"])');
        if (nodes.length > 0) {
          await mermaid.run({ nodes: nodes });
        }
      } catch (e) {
        console.warn('Mermaid render warning:', e);
      }
    }, 60);
  }
}

// -------------------------------------------------------------
// 2. IN-APP MOBILE SIMULATOR MODAL
// -------------------------------------------------------------
function openInAppModal(art) {
  inappMetric.textContent = art.metric;
  inappTitle.textContent = getTitle(art);
  inappTakeaway.textContent = getTakeaway(art);
  let parsed = marked.parse(getContent(art));
  if (art.inline_image) {
    parsed += `<figure class="article-inline-diagram"><img src="${art.inline_image}" alt="${getInlineCaption(art)}" loading="lazy"><figcaption>${getInlineCaption(art)}</figcaption></figure>`;
  }
  parsed = processMermaidDiagrams(parsed);
  inappContentBody.innerHTML = parsed;
  renderMermaidNodes('#inapp-content-body');
  inappSource.textContent = `Source: ${art.source_name}`;
  inappModal.classList.remove('hidden');
}

// Start app
init();
