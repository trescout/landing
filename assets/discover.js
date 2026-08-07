/* TreScout · /discover · CSP-temiz (harici, inline yok).
 *  - entry sayfaları: komut "Kopyala" butonları
 *  - /discover index: catalog.json'dan arama + kategori filtresi + sıralama ile kart ızgarası */
(function () {
  /* Dizin İngilizce de servis ediliyor · aynı catalog.json'dan besleniyor.
     Kart metni tagline_en'e, etiketler EN karşılıklarına, arayüz metinleri
     sayfanın diline göre seçiliyor (2026-08-07 · İngilizce dizinde arama,
     sıralama ve kategori filtresi hiç çalışmıyordu). */
  var EN = document.documentElement.lang === 'en';
  var TAG_EN = {
    "Yapay zekâ araçları": "AI Tools",
    "Geliştirici aracı": "Developer Tool",
    "Kod bilmeyenler için": "No-Code",
    "Öğrenme": "Learning",
    "Üretkenlik": "Productivity"
  };
  var M = EN
    ? { tumu: 'All', birim: ' tools', bos: 'No matches. Try a different filter.', kopyalandi: 'Copied ✓' }
    : { tumu: 'Tümü', birim: ' araç', bos: 'Eşleşme yok. Filtreyi değiştirin.', kopyalandi: 'Kopyalandı ✓' };
  function etiket(t) { return EN ? (TAG_EN[t] || t) : t; }
  function tanitim(it) { return (EN && it.tagline_en) ? it.tagline_en : it.tagline; }
  function yol(slug) { return (EN ? '/en/discover/' : '/discover/') + slug + '/'; }

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }

  /* 1) Kopyala butonları */
  document.querySelectorAll('.disc-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.disc-cmd, .disc-ai');
      var code = box && (box.querySelector('code') || box.querySelector('.disc-ai-text'));
      if (!code || !navigator.clipboard) return;
      navigator.clipboard.writeText(code.textContent.trim()).then(function () {
        var prev = btn.textContent;
        btn.textContent = M.kopyalandi;
        setTimeout(function () { btn.textContent = prev; }, 1500);
      }).catch(function () {});
    });
  });

  /* 2) Keşif index: arama + filtre + sıralama */
  var grid = document.getElementById('discover-grid');
  if (!grid) return;

  var TAG_ORDER = ["Yapay zekâ araçları", "Geliştirici aracı", "Üretkenlik", "Öğrenme", "Kod bilmeyenler için"];
  var state = { q: "", tag: null, sort: "stars" };
  var items = [];

  function card(it) {
    var img = it.image ? '<img class="disc-card-img" src="' + esc(it.image) + '" alt="" loading="lazy" decoding="async">' : '';
    var meta = it.meta ? '<span class="disc-card-meta">' + esc(it.meta) + '</span>' : '';
    var tags = (it.tags || []).map(function (t) { return '<span class="disc-card-tagchip">' + esc(etiket(t)) + '</span>'; }).join('');
    return '<a class="disc-card" href="' + yol(esc(it.slug)) + '">' + img +
      '<div class="disc-card-body">' +
        '<h2 class="disc-card-title">' + esc(it.title) + '</h2>' +
        '<p class="disc-card-tag">' + esc(tanitim(it)) + '</p>' +
        (tags ? '<div class="disc-card-tags">' + tags + '</div>' : '') + meta +
      '</div></a>';
  }

  function render() {
    var q = state.q.toLowerCase().trim();
    var list = items.filter(function (it) {
      if (state.tag && (it.tags || []).indexOf(state.tag) < 0) return false;
      if (q) {
        var hay = ((it.title || '') + ' ' + (tanitim(it) || '')).toLowerCase();
        if (hay.indexOf(q) < 0) return false;
      }
      return true;
    });
    if (state.sort === 'stars') list.sort(function (a, b) { return (b.stars || 0) - (a.stars || 0); });
    else if (state.sort === 'date') list.sort(function (a, b) { return (b.date || '').localeCompare(a.date || ''); });
    else list.sort(function (a, b) { return (a.title || '').localeCompare(b.title || '', EN ? 'en' : 'tr'); });

    var cnt = document.getElementById('disc-count');
    if (cnt) cnt.textContent = list.length === items.length ? (items.length + M.birim) : (list.length + ' / ' + items.length + M.birim);
    grid.innerHTML = list.length ? list.map(card).join('') : '<p class="disc-loading">' + M.bos + '</p>';
  }

  function chips() {
    var box = document.getElementById('disc-tags');
    if (!box) return;
    var present = TAG_ORDER.filter(function (t) { return items.some(function (it) { return (it.tags || []).indexOf(t) >= 0; }); });
    var all = [null].concat(present);
    box.innerHTML = all.map(function (t) {
      var active = (state.tag === t) ? ' disc-chip-active' : '';
      return '<button type="button" class="disc-chip' + active + '" data-tag="' + (t === null ? '' : esc(t)) + '">' + esc(t === null ? M.tumu : etiket(t)) + '</button>';
    }).join('');
    box.querySelectorAll('.disc-chip').forEach(function (b) {
      b.addEventListener('click', function () {
        state.tag = b.getAttribute('data-tag') || null;
        chips(); render();
      });
    });
  }

  fetch('/assets/discover/catalog.json')
    .then(function (r) { return r.json(); })
    .then(function (d) {
      items = Array.isArray(d) ? d : [];
      if (!items.length) { grid.innerHTML = '<p class="disc-loading">Yakında ilk keşifler burada.</p>'; return; }
      chips(); render();
      var s = document.getElementById('disc-search');
      if (s) s.addEventListener('input', function () { state.q = s.value; render(); });
      var so = document.getElementById('disc-sort');
      if (so) so.addEventListener('change', function () { state.sort = so.value; render(); });
    })
    .catch(function () {
      grid.innerHTML = '<p class="disc-loading">Liste şu an yüklenemedi. <a href="/reports/">Raporlara bakın →</a></p>';
    });
})();
