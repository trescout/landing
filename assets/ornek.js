/* TreScout · /ornek/ · en son günlük raporu çekip render eder.
 * Veri: /sitemap.xml → en güncel /reports/YYYY-MM-DD/ → /reports/trescout-rapor-<date>.json
 * Hep güncel · generator'a bağımlı değil · CSP-temiz (same-origin fetch, harici script). */
(function () {
  var root = document.getElementById('report-root');
  if (!root) return;

  // Kaynak başına gösterilecek item limiti (geri kalanı "ve N daha" → FOMO)
  var CAPS = [5, 4, 4];
  var MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
                'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s == null ? '' : String(s);
    return d.innerHTML;
  }
  function safeUrl(u) {
    u = String(u || '');
    return /^https?:\/\//i.test(u) ? u : '';
  }
  function fmtDate(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || ''));
    if (!m) return esc(iso);
    return parseInt(m[3], 10) + ' ' + MONTHS[parseInt(m[2], 10) - 1] + ' ' + m[1];
  }
  function fail() {
    root.innerHTML = '<p class="ornek-fallback">Rapor şu an yüklenemedi. ' +
      '<a href="/reports/">Tüm raporları görün →</a></p>';
  }

  function render(d) {
    if (!d || !d.sections || !d.sections.length) return fail();
    var html = '';
    html += '<p class="ornek-date">' + fmtDate(d.date) + ' · Günlük Rapor</p>';
    if (d.editorial) html += '<p class="ornek-editorial">' + esc(d.editorial) + '</p>';

    var shown = 0, total = 0;
    d.sections.forEach(function (s, idx) {
      var items = (s && s.items) || [];
      total += items.length;
      if (!items.length) return;
      var cap = CAPS[idx] != null ? CAPS[idx] : 3;
      html += '<section class="ornek-sec"><h2 class="ornek-sec-title">' + esc(s.sourceName) + '</h2>';
      items.slice(0, cap).forEach(function (it) {
        shown++;
        var url = safeUrl(it.url);
        var title = url
          ? '<a class="ornek-item-title" href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(it.title) + '</a>'
          : '<span class="ornek-item-title">' + esc(it.title) + '</span>';
        html += '<article class="ornek-item">' + title +
          (it.meta ? '<span class="ornek-item-meta">' + esc(it.meta) + '</span>' : '') +
          (it.summary ? '<p class="ornek-item-sum">' + esc(it.summary) + '</p>' : '') +
          '</article>';
      });
      html += '</section>';
    });

    var more = total - shown;
    if (more > 0) {
      html += '<p class="ornek-more">+ ' + more + ' gelişme daha bu raporda.</p>';
    }
    root.innerHTML = html;
  }

  fetch('/sitemap.xml')
    .then(function (r) { return r.text(); })
    .then(function (xml) {
      var dates = (xml.match(/\/reports\/(\d{4}-\d{2}-\d{2})\//g) || [])
        .map(function (m) { return m.replace(/\D/g, '').replace(/(\d{4})(\d{2})(\d{2})/, '$1-$2-$3'); });
      if (!dates.length) return fail();
      var latest = dates.sort().pop();
      return fetch('/reports/trescout-rapor-' + latest + '.json')
        .then(function (r) {
          if (!r.ok) throw new Error('json ' + r.status);
          return r.json();
        })
        .then(render);
    })
    .catch(fail);
})();
