// Keep a caption only with a successfully loaded article image.
(() => {
  const selector = 'figure.article-inline-diagram, figure.article-featured-hero';

  function discard(figure) {
    if (figure.classList.contains('article-featured-hero')) {
      // SPA article navigation reuses the hero element.
      figure.classList.add('hidden');
    } else {
      figure.remove();
    }
  }

  function inspect(figure) {
    const img = figure.querySelector('img');
    if (!img || /(^|\/)images\/editorial\//i.test(img.getAttribute('src') || '')) {
      discard(figure);
      return;
    }
    figure.classList.remove('image-ready', 'hidden');
    if (img.complete) {
      if (img.naturalWidth > 0) figure.classList.add('image-ready');
      else discard(figure);
    }
  }

  window.refreshArticleFigures = (root = document) => {
    root.querySelectorAll(selector).forEach(inspect);
  };

  document.addEventListener('error', event => {
    if (event.target instanceof HTMLImageElement) {
      const figure = event.target.closest(selector);
      if (figure) discard(figure);
    }
  }, true);
  document.addEventListener('load', event => {
    if (event.target instanceof HTMLImageElement) {
      const figure = event.target.closest(selector);
      if (figure) inspect(figure);
    }
  }, true);
  document.addEventListener('DOMContentLoaded', () => window.refreshArticleFigures());
})();
