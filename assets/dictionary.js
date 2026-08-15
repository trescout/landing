/* TreScout · Sözlük index · statik kartları arama + kategori ile filtreler (CSP-temiz).
 * Kartlar HTML'de statik (SEO + no-JS çalışır); JS yalnız göster/gizle + sayım. */
(function () {
  /* Sayaç metni sayfanın dilinden · önceden sabit Türkçe "terim" idi ve
     İngilizce dizinde de öyle görünüyordu (2026-08-07). */
  var METIN = { tr: ' terim', en: ' terms', fr: ' termes', 'pt-BR': ' termos', es: ' términos', de: ' Begriffe' };
  var _l = document.documentElement.lang || 'tr';
  var BIRIM = METIN[_l] || METIN[_l.split('-')[0]] || METIN.tr;

  var grid = document.getElementById('dict-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.dict-card'));
  var search = document.getElementById('dict-search');
  var chipBox = document.getElementById('dict-tags');
  var countEl = document.getElementById('dict-count');
  var emptyEl = document.getElementById('dict-empty');
  var total = cards.length;
  var state = { q: '', cat: '' };

  function apply() {
    var q = state.q.toLowerCase().trim();
    var shown = 0;
    cards.forEach(function (c) {
      var okCat = !state.cat || c.getAttribute('data-cat') === state.cat;
      var hay = (c.getAttribute('data-search') || '').toLowerCase();
      var okQ = !q || hay.indexOf(q) >= 0;
      var show = okCat && okQ;
      c.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    if (countEl) countEl.textContent = (shown === total) ? (total + BIRIM) : (shown + ' / ' + total + BIRIM);
    if (emptyEl) emptyEl.style.display = shown ? 'none' : 'block';
  }

  if (search) search.addEventListener('input', function () { state.q = search.value; apply(); });
  if (chipBox) {
    chipBox.querySelectorAll('.dict-chip').forEach(function (b) {
      b.addEventListener('click', function () {
        state.cat = b.getAttribute('data-cat') || '';
        chipBox.querySelectorAll('.dict-chip').forEach(function (x) { x.classList.remove('dict-chip-active'); });
        b.classList.add('dict-chip-active');
        apply();
      });
    });
  }
})();
