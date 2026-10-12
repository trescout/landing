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
  var state = { q: '', cat: '', limit: 24 };
  var labels = {tr: ['Daha fazla göster', 'Rastgele keşfet'], en: ['Show more', 'Explore randomly'], fr: ['Afficher plus', 'Découvrir au hasard'], 'pt-BR': ['Mostrar mais', 'Explorar ao acaso'], es: ['Mostrar más', 'Explorar al azar'], de: ['Mehr anzeigen', 'Zufällig entdecken']};
  var copy = labels[_l] || labels[_l.split('-')[0]] || labels.tr;
  var random = document.createElement('a');
  random.className = 'catalog-random';
  random.textContent = copy[1];
  grid.before(random);
  var paging = document.createElement('div');
  paging.className = 'catalog-browse';
  var more = document.createElement('button');
  more.type = 'button';
  more.className = 'btn catalog-more';
  more.textContent = copy[0];
  more.setAttribute('aria-controls', grid.id);
  var progress = document.createElement('span');
  progress.setAttribute('aria-live', 'polite');
  progress.setAttribute('aria-atomic', 'true');
  paging.append(more, progress);
  grid.after(paging);
  var matches = [];
  random.addEventListener('click', function () {
    if (matches.length) random.href = matches[Math.floor(Math.random() * matches.length)].href;
  });

  function apply() {
    var q = state.q.toLowerCase().trim();
    var shown = 0;
    matches = cards.filter(function (c) {
      var okCat = !state.cat || c.getAttribute('data-cat') === state.cat;
      var hay = (c.getAttribute('data-search') || '').toLowerCase();
      var okQ = !q || hay.indexOf(q) >= 0;
      return okCat && okQ;
    });
    var visible = matches.slice(0, state.limit);
    cards.forEach(function (c) {
      var show = visible.indexOf(c) !== -1;
      c.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    if (countEl) countEl.textContent = (matches.length === total) ? (total + BIRIM) : (matches.length + ' / ' + total + BIRIM);
    if (emptyEl) emptyEl.style.display = shown ? 'none' : 'block';
    more.hidden = shown >= matches.length;
    progress.textContent = shown + ' / ' + matches.length + BIRIM;
    random.hidden = !matches.length;
    if (matches.length) random.href = matches[Math.floor(Math.random() * matches.length)].href;
  }

  more.addEventListener('click', function () {
    var next = matches[state.limit];
    state.limit += 24;
    apply();
    if (next) next.focus();
  });
  if (search) search.addEventListener('input', function () { state.q = search.value; state.limit = 24; apply(); });
  if (chipBox) {
    chipBox.querySelectorAll('.dict-chip').forEach(function (b) {
      b.addEventListener('click', function () {
        state.cat = b.getAttribute('data-cat') || '';
        state.limit = 24;
        chipBox.querySelectorAll('.dict-chip').forEach(function (x) { x.classList.remove('dict-chip-active'); });
        b.classList.add('dict-chip-active');
        apply();
      });
    });
  }
  apply();
})();
