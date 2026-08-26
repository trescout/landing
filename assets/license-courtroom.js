/**
 * TreScout · Açık Kaynak Lisans Mahkemesi (License Courtroom Simulator)
 * ====================================================================
 * Geliştiricilerin ve girişimcilerin açık kaynak lisans kombinasyonlarını
 * hukuki açıdan test etmesini ve güvenli alternatifler bulmasını sağlar.
 */

(function () {
  'use strict';

  var CASES = [
    {
      id: 'agpl-saas',
      title: 'Dava 1: Kapalı Kaynak SaaS & AGPL-3.0',
      scenario: 'Kapalı kaynak bir kurumsal yapay zeka SaaS platformu geliştirdiniz. Backend\'de AGPL-3.0 lisanslı bir aracı doğrudan ana API sürecine dahil ettiniz.',
      verdict: '⚠️ CİDDİ HUKUKİ RİSK (Copyleft İhlali)',
      verdictClass: 'lc-risk-high',
      score: 'Yüksek Risk (%88)',
      ruling: 'AGPL (Affero GPL), yazılımın ağ üzerinden (SaaS) sunulmasını da "dağıtım" sayar. Kullanıcılar talep ederse tüm SaaS mimarinizin kaynak kodunu AGPL ile açmak zorunda kalabilirsiniz.',
      alternatives: [
        { name: 'ChromaDB / Qdrant (Apache 2.0)', desc: 'Patent korumalı ve ticari SaaS içine entegre etmesi %100 güvenli.' },
        { name: 'SQLite-VSS (MIT)', desc: 'Maksimum özgürlük, sıfır copyleft kod açma zorunluluğu.' }
      ]
    },
    {
      id: 'gpl-mobile',
      title: 'Dava 2: Ücretli Mobil Uygulamada GPL-2.0',
      scenario: 'Geliştirdiğiniz ücretli mobil oyunda ses işleme için GPL-2.0 lisanslı popüler bir C++ kütüphanesini statik derlediniz.',
      verdict: '🚨 KESİN TELİF İHLALİ (Statik Linkleme Yasağı)',
      verdictClass: 'lc-risk-critical',
      score: 'Kritik Risk (%96)',
      ruling: 'GPL-2.0 statik bağlanan tüm projeyi türev eser sayar. Uygulamanız App Store kurallarıyla çelişir; telif ihtarı ile mağazadan kaldırılabilir.',
      alternatives: [
        { name: 'Miniaudio (MIT / Unlicense)', desc: 'Tek başlık dosyası (header-only) ve sınırsız ticari kullanım.' },
        { name: 'SDL2 (Zlib)', desc: 'Ticari oyun ve mobil uygulamalar için sektör standardı.' }
      ]
    },
    {
      id: 'mit-apache',
      title: 'Dava 3: Kurumsal Ticari Projede MIT + Apache',
      scenario: 'Fintech şirketiniz FastAPI (MIT) ve vLLM (Apache 2.0) kullanarak kurumsal müşterilerine yapay zeka servisi satıyor.',
      verdict: '✅ BERAAT: %100 TİCARİ GÜVENLİ LİMAN',
      verdictClass: 'lc-risk-safe',
      score: 'Sıfır Risk (%0)',
      ruling: 'MIT ve Apache 2.0 lisansları permissive lisanslardır. Orijinal telif bildirimini koruduğunuz sürece kodunuzu açma zorunluluğunuz yoktur. Ticari satış ve patent hakkı tamdır.',
      alternatives: [
        { name: 'FastAPI + vLLM + Ripgrep', desc: 'Modern kurumsal açık kaynak stack\'inin en temiz ve güvenli çekirdeğidir.' }
      ]
    }
  ];

  function renderCourtroom(container) {
    var activeIdx = 0;

    function update() {
      var c = CASES[activeIdx];

      var caseButtons = CASES.map(function (item, idx) {
        var activeClass = idx === activeIdx ? 'lc-tab-active' : '';
        return '<button type="button" class="lc-tab-btn ' + activeClass + '" data-idx="' + idx + '">' + item.title.split(':')[0] + '</button>';
      }).join('\n');

      var altHtml = c.alternatives.map(function (a) {
        return [
          '<div class="lc-alt-card">',
          '  <strong>🛡️ ' + a.name + '</strong>',
          '  <p>' + a.desc + '</p>',
          '</div>'
        ].join('\n');
      }).join('\n');

      container.innerHTML = [
        '<div class="lc-wrap">',
        '  <div class="lc-head">',
        '    <span class="lc-top-badge">⚖️ OPEN SOURCE COURTROOM</span>',
        '    <h2 class="lc-title">Açık Kaynak Mahkemesi & Lisans Riski Simülatörü</h2>',
        '    <p class="lc-desc">Ticari projelerinizde kullandığınız açık kaynak kütüphanelerin telif ve lisans risklerini Yargıç AI huzurunda test edin.</p>',
        '    <div class="lc-tabs">' + caseButtons + '</div>',
        '  </div>',
        '  <div class="lc-court-card">',
        '    <div class="lc-case-header">',
        '      <span class="lc-gavel">👨‍⚖️</span>',
        '      <div>',
        '        <h3 class="lc-case-title">' + c.title + '</h3>',
        '        <p class="lc-scenario">' + c.scenario + '</p>',
        '      </div>',
        '    </div>',
        '    <div class="lc-verdict-box ' + c.verdictClass + '">',
        '      <div class="lc-verdict-head">',
        '        <strong>Gerekçeli Karar: ' + c.verdict + '</strong>',
        '        <span class="lc-score-pill">' + c.score + '</span>',
        '      </div>',
        '      <p class="lc-ruling-text">' + c.ruling + '</p>',
        '    </div>',
        '    <div class="lc-alts-section">',
        '      <h4>✅ Şirketinizi Koruyacak Güvenli Açık Kaynak Alternatifleri:</h4>',
        '      <div class="lc-alts-grid">' + altHtml + '</div>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');

      var btns = container.querySelectorAll('.lc-tab-btn');
      btns.forEach(function (b) {
        b.addEventListener('click', function () {
          activeIdx = parseInt(b.getAttribute('data-idx'), 10);
          update();
        });
      });
    }

    update();
  }

  window.TreScoutCourtroom = {
    init: renderCourtroom
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-courtroom-container');
    targets.forEach(renderCourtroom);
  });
})();
