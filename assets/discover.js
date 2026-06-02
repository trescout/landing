/* TreScout · /discover · CSP-temiz (harici, inline yok).
 *  - entry sayfalarında: komut "Kopyala" butonları
 *  - /discover index'inde: catalog.json'dan kart ızgarası render */
(function () {
  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }

  // 1) Kopyala butonları
  document.querySelectorAll('.disc-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.disc-cmd');
      var code = box && box.querySelector('code');
      if (!code || !navigator.clipboard) return;
      navigator.clipboard.writeText(code.textContent.trim()).then(function () {
        var prev = btn.textContent;
        btn.textContent = 'Kopyalandı ✓';
        setTimeout(function () { btn.textContent = prev; }, 1500);
      }).catch(function () {});
    });
  });

  // 2) Keşif index ızgarası
  var grid = document.getElementById('discover-grid');
  if (grid) {
    fetch('/assets/discover/catalog.json')
      .then(function (r) { return r.json(); })
      .then(function (items) {
        if (!Array.isArray(items) || !items.length) {
          grid.innerHTML = '<p class="disc-loading">Yakında ilk keşifler burada.</p>';
          return;
        }
        grid.innerHTML = items.map(function (it) {
          var img = it.image
            ? '<img class="disc-card-img" src="' + esc(it.image) + '" alt="" loading="lazy" decoding="async">'
            : '';
          var meta = it.meta ? '<span class="disc-card-meta">' + esc(it.meta) + '</span>' : '';
          return '<a class="disc-card" href="/discover/' + esc(it.slug) + '/">' + img +
            '<div class="disc-card-body">' +
              '<h2 class="disc-card-title">' + esc(it.title) + '</h2>' +
              '<p class="disc-card-tag">' + esc(it.tagline) + '</p>' + meta +
            '</div></a>';
        }).join('');
      })
      .catch(function () {
        grid.innerHTML = '<p class="disc-loading">Liste şu an yüklenemedi. <a href="/reports/">Raporlara bakın →</a></p>';
      });
  }
})();
