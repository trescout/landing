/**
 * TreScout · Açık Kaynak Zaman Tüneli (Open Source Time Machine: 2016-2026)
 * =========================================================================
 * Açık kaynak yazılım dünyasının 10 yıllık evrimini interaktif bir zaman
 * kaydırıcısı ve trend karşılaştırmasıyla görselleştirir.
 */

(function () {
  'use strict';

  var TIMELINE_DATA = [
    {
      year: '2016',
      title: 'JavaScript & Konteyner Devrimi',
      lead: 'Web 2.0 mimarisinin bileşen tabanlı SPA modellerine ve mikroservislere geçtiği dönem.',
      paradigm: 'DOM Manipülasyonundan Sanal DOM ve Konteynerleşmeye Geçiş',
      topTools: [
        { name: 'React', stars: '★ 55.000 (2016)', desc: 'Facebook tarafından açık kaynağa açılan deklaratif UI kütüphanesi.' },
        { name: 'Docker', stars: '★ 38.000 (2016)', desc: 'Yazılım dağıtımını standartlaştıran konteyner motoru.' },
        { name: 'Webpack', stars: '★ 22.000 (2016)', desc: 'Modern JavaScript projeleri için modül paketleyici.' },
        { name: 'Vue.js', stars: '★ 35.000 (2016)', desc: 'Kademeli olarak benimsenebilen hafif reaktif arayüz kütüphanesi.' }
      ],
      dominantLanguages: ['JavaScript (ES6)', 'Python 2.7/3.5', 'Go 1.7', 'Java 8']
    },
    {
      year: '2020',
      title: 'Cloud-Native & Modern Sistem Dilleri',
      lead: 'Sunucusuz (serverless) mimarilerin, Jamstack ekosisteminin ve Rust yükselişinin dönemi.',
      paradigm: 'Monolitlerden Sunucusuz Fonksiyonlara ve Statik Üretim (SSG) Modeline Geçiş',
      topTools: [
        { name: 'Next.js', stars: '★ 60.000 (2020)', desc: 'React tabanlı tam kapsamlı sunucu taraflı render (SSR) çatısı.' },
        { name: 'FastAPI', stars: '★ 25.000 (2020)', desc: 'Python tip ipuçları ve asenkron yapı üzerine kurulu yüksek hızlı API çatısı.' },
        { name: 'Ripgrep', stars: '★ 28.000 (2020)', desc: 'Rust ile yazılmış, grep alternatifinden kat kat hızlı kod arama aracı.' },
        { name: 'Tailwind CSS', stars: '★ 32.000 (2020)', desc: 'Utility-first CSS tasarım metodolojisi.' }
      ],
      dominantLanguages: ['TypeScript', 'Python 3.8', 'Rust 1.45', 'Go 1.15']
    },
    {
      year: '2023',
      title: 'Üretken Yapay Zekânın Doğuşu',
      lead: 'Büyük dil modellerinin (LLM) geliştirici araçlarını baştan tanımladığı yapay zeka patlaması.',
      paradigm: 'Geleneksel Algoritmalardan Prompt Mühendisliği ve RAG Mimarilerine Geçiş',
      topTools: [
        { name: 'LangChain', stars: '★ 70.000 (2023)', desc: 'LLM tabanlı uygulamalar ve bağlam zincirleri kurma çerçevesi.' },
        { name: 'AutoGPT', stars: '★ 150.000 (2023)', desc: 'Kendi kendine hedef belirleyip çalışan ilk otonom yapay zeka deneyi.' },
        { name: 'vLLM', stars: '★ 18.000 (2023)', desc: 'PagedAttention ile yüksek performanslı açık kaynak LLM çıkarım motoru.' },
        { name: 'Ollama', stars: '★ 45.000 (2023)', desc: 'Lokal makinelerde açık modelleri tek komutla çalıştırma aracı.' }
      ],
      dominantLanguages: ['Python (PyTorch)', 'TypeScript', 'C++/CUDA', 'Rust']
    },
    {
      year: '2026',
      title: 'Otonom Ajanlar & Yerel Öncelikli Sistemler (Bugün)',
      lead: 'Terminalde ve kod tabanında doğrudan görev yürüten çoklu ajanlar ve Model Context Protocol çağı.',
      paradigm: 'İstem Yazmaktan Doğrudan Kod Tabanını Yöneten Otonom Ajan Orkestrasyonuna Geçiş',
      topTools: [
        { name: 'Claude Code', stars: '★ 142.599 (2026)', desc: 'Terminalde çalışan ve kod tabanınızı bütünüyle anlayan AI ajan kodlama aracı.' },
        { name: 'Understand Anything', stars: '★ 77.021 (2026)', desc: 'Kod ve dokümanları yapay zekâ ile etkileşimli analiz eden platform.' },
        { name: 'TradingAgents', stars: '★ 21.430 (2026)', desc: 'Finansal piyasaları analiz eden çoklu otonom yapay zekâ ajanları.' },
        { name: 'Code Graph RAG', stars: '★ 4.782 (2026)', desc: 'Monorepo yapılarını bilgi grafikleri tabanlı RAG ile anlama aracı.' }
      ],
      dominantLanguages: ['Rust (Sistem & Tooling)', 'Python (AI)', 'TypeScript', 'WASM / Local-First']
    }
  ];

  function renderTimeMachine(container) {
    var selectedIdx = 3; // Varsayılan: 2026 (Bugün)

    function update() {
      var era = TIMELINE_DATA[selectedIdx];

      var buttonsHtml = TIMELINE_DATA.map(function (item, idx) {
        var activeClass = idx === selectedIdx ? 'tm-btn-active' : '';
        return '<button type="button" class="tm-year-btn ' + activeClass + '" data-idx="' + idx + '">' + item.year + '</button>';
      }).join('\n');

      var toolsHtml = era.topTools.map(function (t) {
        return [
          '<div class="tm-tool-card">',
          '  <div class="tm-tool-head">',
          '    <strong>' + t.name + '</strong>',
          '    <span class="tm-stars">' + t.stars + '</span>',
          '  </div>',
          '  <p>' + t.desc + '</p>',
          '</div>'
        ].join('\n');
      }).join('\n');

      var langsHtml = era.dominantLanguages.map(function (l) {
        return '<span class="tm-lang-pill">' + l + '</span>';
      }).join(' ');

      container.innerHTML = [
        '<div class="tm-wrap">',
        '  <div class="tm-head">',
        '    <span class="tm-badge">⏳ AÇIK KAYNAK ZAMAN TÜNELİ</span>',
        '    <h2 class="tm-title">10 Yılda Açık Kaynak Dünyası Nasıl Değişti?</h2>',
        '    <p class="tm-subtitle">2016\'dan 2026\'ya teknoloji yığınlarının ve mühendislik paradigmalarının evrimini inceleyin.</p>',
        '    <div class="tm-timeline-nav">' + buttonsHtml + '</div>',
        '  </div>',
        '  <div class="tm-content">',
        '    <div class="tm-era-intro">',
        '      <span class="tm-era-year">' + era.year + '</span>',
        '      <h3>' + era.title + '</h3>',
        '      <p class="tm-era-lead">' + era.lead + '</p>',
        '      <div class="tm-paradigm-box"><strong>💡 Ana Paradigma Değişimi:</strong> ' + era.paradigm + '</div>',
        '    </div>',
        '    <div class="tm-tools-grid">',
        '      <h4>🚀 Dönemin En Popüler Açık Kaynak Projeleri:</h4>',
        '      <div class="tm-grid">' + toolsHtml + '</div>',
        '    </div>',
        '    <div class="tm-langs-wrap">',
        '      <strong>🔥 Dönemin Baskın Dilleri:</strong> ' + langsHtml,
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');

      var navBtns = container.querySelectorAll('.tm-year-btn');
      navBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          selectedIdx = parseInt(btn.getAttribute('data-idx'), 10);
          update();
        });
      });
    }

    update();
  }

  window.TreScoutTimeMachine = {
    init: renderTimeMachine
  };

  document.addEventListener('DOMContentLoaded', function () {
    var containers = document.querySelectorAll('.tre-time-machine-container');
    containers.forEach(renderTimeMachine);
  });
})();
