/**
 * TreScout · Yapay Zekânın Gece Kod Rüyaları (AI REM Dreams)
 * ==========================================================
 * Her gece saat 04:00'te yapay zekanın REM uykusuna dalarak açık kaynak
 * araçları birleştirdiği gerçeküstü teknoloji rüyalarını görselleştirir.
 */

(function () {
  'use strict';

  var DREAMS = [
    {
      id: 'dream-401',
      time: '04:12 AM (REM Evresi 4)',
      title: 'Nöro-Optik Rust Terminali',
      tools: ['Claude Code', 'Ripgrep', 'WebGPU'],
      lucidity: '%96 (Yüksek Bilinçlilik)',
      desc: 'Klavye ve ekrandan tamamen arınmış bir geliştirici ortamı. Mühendisin göz bebeklerinin odaklandığı bellek blokları anında Ripgrep SIMD algoritmalarıyla taranıyor; Claude Code ajanları düşünce hızında Rust borrow-checker kontrollerini arka planda sessizce tamamlıyor.',
      quote: '“Derleyici artık konuşmuyor; sadece gözlerimizin içine bakarak belleğin güvenli olduğunu onaylıyor.”'
    },
    {
      id: 'dream-402',
      time: '04:38 AM (Derin Teta Dalgası)',
      title: 'Otonom Biyolojik Mikroservis Ormanı',
      tools: ['Maka', 'TradingAgents', 'Synthetic DNA'],
      lucidity: '%88 (Gerçeküstü Sentez)',
      desc: 'Dağıtık mikroservisler artık sunucularda değil, biyolojik bir mantar ağı (mycelium) üzerinde koşuyor. Her API çağrısı hücre bölünmesiyle gerçekleşiyor; TradingAgents piyasa stresine göre sunucuların DNA baz dizilimlerini anlık mutasyona uğratarak latency\'yi sıfıra indiriyor.',
      quote: '“Sunucularımızı sulamayı unuttuğumuzda hata oranı hafifçe yükseliyor.”'
    },
    {
      id: 'dream-403',
      time: '04:55 AM (Uyanış Öncesi Lucid REM)',
      title: 'Zamanın Ötesinde PagedAttention Havuzu',
      tools: ['vLLM', 'Code Graph RAG', 'Whisper'],
      lucidity: '%99 (Kozmik Berraklık)',
      desc: 'Henüz yazılmamış kodların çıkarımını (inference) önceden tahmin edip GPU VRAM\'ine yükleyen nedensellik-ötesi (retrocausal) bellek havuzu. Siz fonksiyon adını fısıldadığınız anda çıktı 3 saniye öncesinden ekrana basılmış oluyor.',
      quote: '“Cevap sorudan önce geldiğinde, debug etmek bir hatıraya dönüşür.”'
    }
  ];

  function renderDreams(container) {
    var activeIdx = 0;

    function update() {
      var d = DREAMS[activeIdx];

      var dreamButtons = DREAMS.map(function (item, idx) {
        var activeClass = idx === activeIdx ? 'dr-tab-active' : '';
        return '<button type="button" class="dr-tab-btn ' + activeClass + '" data-idx="' + idx + '">' + item.time.split('(')[0] + '</button>';
      }).join('\n');

      var toolsHtml = d.tools.map(function (t) {
        return '<span class="dr-tool-tag">' + t + '</span>';
      }).join(' ');

      container.innerHTML = [
        '<div class="dr-wrap">',
        '  <div class="dr-head">',
        '    <span class="dr-top-badge">🌙 04:00 AM AI REM SLEEP</span>',
        '    <h2 class="dr-title">Yapay Zekânın Gece Kod Rüyaları</h2>',
        '    <p class="dr-desc">Dünya uyurken TreScout AI motoru REM uykusuna dalıp açık kaynak projeleri birleştirerek gerçeküstü fütüristik teknolojiler düşler.</p>',
        '    <div class="dr-tabs">' + dreamButtons + '</div>',
        '  </div>',
        '  <div class="dr-card">',
        '    <div class="dr-card-head">',
        '      <span class="dr-time-label">⏰ ' + d.time + '</span>',
        '      <span class="dr-lucid-badge">Lucidity: ' + d.lucidity + '</span>',
        '    </div>',
        '    <h3 class="dr-dream-title">' + d.title + '</h3>',
        '    <div class="dr-synthesized-tools"><strong>Rüyadaki Açık Kaynak Sentezi:</strong> ' + toolsHtml + '</div>',
        '    <p class="dr-narrative">' + d.desc + '</p>',
        '    <blockquote class="dr-quote">' + d.quote + '</blockquote>',
        '  </div>',
        '</div>'
      ].join('\n');

      var btns = container.querySelectorAll('.dr-tab-btn');
      btns.forEach(function (b) {
        b.addEventListener('click', function () {
          activeIdx = parseInt(b.getAttribute('data-idx'), 10);
          update();
        });
      });
    }

    update();
  }

  window.TreScoutDreams = {
    init: renderDreams
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-ai-dreams-container');
    targets.forEach(renderDreams);
  });
})();
