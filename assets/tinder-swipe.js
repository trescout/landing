/**
 * TreScout · Açık Kaynak Tinder (Speed Dating for Open Source Tools)
 * =================================================================
 * 472 açık kaynak aracı kaydırarak (Swipe Right / Left / Up) keşfetmenizi
 * ve kişisel 2026 teknoloji yığınınızı oluşturmanızı sağlayan arayüz.
 */

(function () {
  'use strict';

  var TOOLS_DECK = [
    {
      slug: 'claude-code',
      title: 'Claude Code',
      stars: '★ 142.599',
      tagline: 'Terminalde çalışan ve kod tabanınızı bütünüyle anlayan AI ajan kodlama aracı.',
      tag: 'AI Ajan · Anthropic',
      cmd: 'npm install -g @anthropic-ai/claude-code',
      color: '#1B4965'
    },
    {
      slug: 'understand-anything',
      title: 'Understand Anything',
      stars: '★ 77.021',
      tagline: 'Kodlarınızı veya dokümanlarınızı yapay zekâ ile etkileşimli hale getiren analiz aracı.',
      tag: 'Geliştirici Aracı · MIT',
      cmd: '/plugin marketplace add Lum1104/Understand-Anything',
      color: '#5FA8D3'
    },
    {
      slug: 'tradingagents',
      title: 'TradingAgents',
      stars: '★ 21.430',
      tagline: 'Finansal piyasaları analiz eden çoklu otonom yapay zekâ ajanları çerçevesi.',
      tag: 'Multi-Agent · Python',
      cmd: 'git clone https://github.com/TuringComplete-Labs/TradingAgents.git',
      color: '#F4D35E'
    },
    {
      slug: 'code-graph-rag',
      title: 'Code Graph RAG',
      stars: '★ 4.782',
      tagline: 'Büyük monorepo kod depolarındaki yapıları anlamak için bilgi grafikleri tabanlı RAG.',
      tag: 'RAG · Knowledge Graph',
      cmd: 'pip install code-graph-rag',
      color: '#10B981'
    },
    {
      slug: 'vllm',
      title: 'vLLM',
      stars: '★ 48.200',
      tagline: 'PagedAttention ile yüksek performanslı açık kaynak LLM çıkarım motoru.',
      tag: 'GPU Çıkarım · Apache 2.0',
      cmd: 'pip install vllm',
      color: '#EF4444'
    },
    {
      slug: 'ripgrep',
      title: 'Ripgrep',
      stars: '★ 46.500',
      tagline: 'Rust ile yazılmış, grep alternatifinden kat kat hızlı kod arama aracı.',
      tag: 'Sistem CLI · Rust',
      cmd: 'cargo install ripgrep',
      color: '#8B5CF6'
    }
  ];

  function renderTinderUI(container) {
    var currentIndex = 0;
    var matches = [];
    var superlikes = [];

    function update() {
      if (currentIndex >= TOOLS_DECK.length) {
        renderSummary();
        return;
      }

      var tool = TOOLS_DECK[currentIndex];
      var remaining = TOOLS_DECK.length - currentIndex;

      container.innerHTML = [
        '<div class="ts-wrap">',
        '  <div class="ts-head">',
        '    <span class="ts-top-badge">🔥 OPEN SOURCE SPEED DATING</span>',
        '    <h2 class="ts-title">Açık Kaynak Tinder: Stack\'ini Oluştur</h2>',
        '    <p class="ts-desc">Sağa kaydır ➔ Stack\'ine Ekle | Sola kaydır ➔ Pas Geç | Yukarı kaydır ➔ Hafta Sonu Dene</p>',
        '    <div class="ts-counter">Kalan Aday Araçlar: ' + remaining + '</div>',
        '  </div>',
        '  <div class="ts-card-container">',
        '    <div class="ts-card" id="js-ts-card" style="border-top: 4px solid ' + tool.color + '">',
        '      <div class="ts-card-header">',
        '        <span class="ts-card-tag">' + tool.tag + '</span>',
        '        <span class="ts-card-stars">' + tool.stars + '</span>',
        '      </div>',
        '      <h3 class="ts-card-title">' + tool.title + '</h3>',
        '      <p class="ts-card-tagline">' + tool.tagline + '</p>',
        '      <div class="ts-card-cmd"><code>' + tool.cmd + '</code></div>',
        '    </div>',
        '  </div>',
        '  <div class="ts-actions">',
        '    <button type="button" class="ts-btn ts-btn-pass" id="js-btn-pass" title="Pas Geç (Sol Ok)">💔 Pas</button>',
        '    <button type="button" class="ts-btn ts-btn-super" id="js-btn-super" title="Hafta Sonu Dene (Yukarı Ok)">⭐ Hafta Sonu</button>',
        '    <button type="button" class="ts-btn ts-btn-like" id="js-btn-like" title="Stack\'e Ekle (Sağ Ok)">💚 Eşleş / Ekle</button>',
        '  </div>',
        '</div>'
      ].join('\n');

      var passBtn = container.querySelector('#js-btn-pass');
      var superBtn = container.querySelector('#js-btn-super');
      var likeBtn = container.querySelector('#js-btn-like');
      var cardEl = container.querySelector('#js-ts-card');

      function triggerAction(type) {
        if (!cardEl) return;
        if (type === 'like') {
          cardEl.classList.add('ts-swipe-right');
          matches.push(tool);
        } else if (type === 'pass') {
          cardEl.classList.add('ts-swipe-left');
        } else if (type === 'super') {
          cardEl.classList.add('ts-swipe-up');
          superlikes.push(tool);
        }

        setTimeout(function () {
          currentIndex++;
          update();
        }, 220);
      }

      passBtn.addEventListener('click', function () { triggerAction('pass'); });
      superBtn.addEventListener('click', function () { triggerAction('super'); });
      likeBtn.addEventListener('click', function () { triggerAction('like'); });
    }

    function renderSummary() {
      var matchItems = matches.map(function (m) {
        return '<li><strong>' + m.title + '</strong> · ' + m.tag + ' <code>' + m.stars + '</code></li>';
      }).join('\n') || '<li>Henüz araç eşleşmedi.</li>';

      var superItems = superlikes.map(function (s) {
        return '<li><strong>' + s.title + '</strong> (Hafta Sonu Denenecek)</li>';
      }).join('\n') || '<li>Hafta sonu listesi boş.</li>';

      container.innerHTML = [
        '<div class="ts-wrap">',
        '  <div class="ts-summary-card">',
        '    <span class="ts-top-badge">🎉 TEBRİKLER! STACK TAMAMLANDI</span>',
        '    <h2 class="ts-title">İşte 2026 Rüya Teknoloji Yığınınız</h2>',
        '    <div class="ts-summary-group">',
        '      <h4>💚 Stack\'inize Eklenen Araçlar (' + matches.length + '):</h4>',
        '      <ul>' + matchItems + '</ul>',
        '    </div>',
        '    <div class="ts-summary-group">',
        '      <h4>⭐ Hafta Sonu Deneme Listeniz (' + superlikes.length + '):</h4>',
        '      <ul>' + superItems + '</ul>',
        '    </div>',
        '    <button type="button" class="btn btn-primary" id="js-btn-restart">🔄 Yeniden Başla & Karıştır</button>',
        '  </div>',
        '</div>'
      ].join('\n');

      var restartBtn = container.querySelector('#js-btn-restart');
      if (restartBtn) {
        restartBtn.addEventListener('click', function () {
          currentIndex = 0;
          matches = [];
          superlikes = [];
          update();
        });
      }
    }

    // Klavye Kısayolları (Ok tuşları)
    window.addEventListener('keydown', function (e) {
      if (currentIndex >= TOOLS_DECK.length) return;
      if (e.key === 'ArrowRight') {
        var likeBtn = container.querySelector('#js-btn-like');
        if (likeBtn) likeBtn.click();
      } else if (e.key === 'ArrowLeft') {
        var passBtn = container.querySelector('#js-btn-pass');
        if (passBtn) passBtn.click();
      } else if (e.key === 'ArrowUp') {
        var superBtn = container.querySelector('#js-btn-super');
        if (superBtn) superBtn.click();
      }
    });

    update();
  }

  window.TreScoutTinder = {
    init: renderTinderUI
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-tinder-container');
    targets.forEach(renderTinderUI);
  });
})();
