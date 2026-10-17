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
  var state = { q: '', cat: '', limit: 16 };
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

  // Arama aksan ve şapkaya duyarsız (2026-10-15): "yapay zeka" yazan "yapay zekâ"yı,
  // "gelistirme" yazan "geliştirme"yi bulsun. Önce yalnız toLowerCase vardı · şapkalı
  // yazılan binlerce kayıt klavyeden aranamıyordu.
  function katla(s) {
    return String(s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');
  }

  // Arama puanı (2026-10-16): kelime başı eşleşmesi + ad alanı ağırlığı. Önce düz alt dize vardı
  // ve sonuç sıralanmıyordu: "RAG" ilk sırada "Object Storage" (sto-rag-e) getiriyordu, "API"
  // teriminin kendisi 65 eşleşmenin 50.'siydi (ilk 16 görünür). Kelime içi eşleşme düşük puanla
  // sona kalır, kaybolmaz. DeepLearning.AI "Retrieval Augmented Generation" · R4. Sözlük ve keşif
  // aynı fonksiyonu taşır; scripts/catalog-browsing.test.mjs ikisinin aynı kaldığını sınar.
  function aramaPuani(ad, metin, q) {
    var bol = function (s) { return ' ' + s.replace(/[^0-9a-z\u00c0-\uffff]+/g, ' ').trim() + ' '; };
    var a = bol(ad), m = bol(metin), qq = bol(q).trim(), p = 0;
    var sozcukler = qq.split(' ');
    for (var i = 0; i < sozcukler.length; i++) {
      var w = ' ' + sozcukler[i];
      if (a.indexOf(w) >= 0) p += 3;
      else if (m.indexOf(w) >= 0) p += 1;
      else return metin.indexOf(q) >= 0 ? 0.5 : 0;
    }
    if (a.trim() === qq) p += 10;
    else if (a.trim().indexOf(qq) === 0) p += 5;
    return p;
  }

  // Aranan alanlar bir kez katlanır; ad (kart başlığı) ayrıca tutulur, puanda ağır basar.
  cards.forEach(function (c, i) {
    var t = c.querySelector ? c.querySelector('.dict-card-term') : null;
    c._sira = i;
    c._metin = katla(c.getAttribute('data-search'));
    c._ad = t ? katla(t.textContent) : c._metin;
  });
  var sirali = false;

  function apply() {
    var q = katla(state.q).trim();
    var shown = 0;
    matches = cards.filter(function (c) {
      if (state.cat && c.getAttribute('data-cat') !== state.cat) return false;
      c._puan = q ? aramaPuani(c._ad, c._metin, q) : 1;
      return c._puan > 0;
    });
    // Aramada en alakalı önce; görünen sıra DOM sırası olsun (klavye odağı da aynı sırayı izler).
    if (q) matches.sort(function (x, y) { return y._puan - x._puan || x._sira - y._sira; });
    if (q || sirali) { grid.append.apply(grid, q ? matches : cards); sirali = !!q; }
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
    state.limit += 16;
    apply();
    if (next) next.focus();
  });
  if (search) search.addEventListener('input', function () { state.q = search.value; state.limit = 16; apply(); });
  if (chipBox) {
    chipBox.querySelectorAll('.dict-chip').forEach(function (b) {
      b.addEventListener('click', function () {
        state.cat = b.getAttribute('data-cat') || '';
        state.limit = 16;
        chipBox.querySelectorAll('.dict-chip').forEach(function (x) { x.classList.remove('dict-chip-active'); });
        b.classList.add('dict-chip-active');
        apply();
      });
    });
  }
  apply();
})();
