/**
 * TreScout · Açık Kaynak Katkı Rehberi Bileşeni (Good First Issue Helper)
 * ======================================================================
 * Keşif sayfalarında geliştiricilere ilk katkı bağlantılarını, Good First Issue
 * listesini ve lisans güvenliği bilgilerini sunar.
 */

(function () {
  'use strict';

  function renderContributorGuide(container, data) {
    if (!data || !data.github_repo) return;

    var lic = data.license || {};
    var badgeClass = lic.badge_color === 'green' ? 'lic-green' : (lic.badge_color === 'yellow' ? 'lic-yellow' : 'lic-blue');

    container.innerHTML = [
      '<div class="cg-wrap">',
      '  <div class="cg-head">',
      '    <span class="cg-title">🤝 Bu Projeye İlk Katkını Yap</span>',
      '    <span class="cg-lic ' + badgeClass + '">' + (lic.badge || 'Açık Kaynak') + '</span>',
      '  </div>',
      '  <p class="cg-desc">Açık kaynak projelerine katkı sağlamak portfolyonuzu güçlendirir ve küresel yazılım komünitesine destek olur.</p>',
      '  <div class="cg-links">',
      '    <a class="cg-btn cg-btn-issue" href="' + data.good_first_issues_url + '" target="_blank" rel="noopener">🎯 Kolay Görevler (Good First Issues) ↗</a>',
      '    <a class="cg-btn cg-btn-guide" href="' + data.contributing_guide_url + '" target="_blank" rel="noopener">📖 Katkı Kılavuzu (CONTRIBUTING.md) ↗</a>',
      '    <a class="cg-btn cg-btn-fork" href="' + data.fork_url + '" target="_blank" rel="noopener">🍴 Fork Yap ↗</a>',
      '  </div>',
      '  <div class="cg-cmd-wrap">',
      '    <code>' + data.quick_contribute_cmd + '</code>',
      '  </div>',
      '</div>'
    ].join('\n');
  }

  function init() {
    var targets = document.querySelectorAll('.tre-contribute-box');
    if (targets.length === 0) return;

    fetch('/assets/discover/contributor-guides.json')
      .then(function (res) { return res.json(); })
      .then(function (guides) {
        targets.forEach(function (el) {
          var slug = el.getAttribute('data-slug');
          if (slug && guides[slug]) {
            renderContributorGuide(el, guides[slug]);
          }
        });
      })
      .catch(function () {});
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
