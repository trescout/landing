/**
 * TreScout Lo-Fi Stream & Live Discovery Controller
 * =================================================
 * Live Clock, Rotating Discovery Showcase, Live Log Stream & Ticker.
 */

(function () {
  'use strict';

  var TOOLS = [
    {
      title: 'Claude Code',
      desc: 'Terminalde çalışan ve kod tabanınızı anlayan AI ajan kodlama aracı (Anthropic ürünü).',
      stars: '★ 142.599 STARS',
      cmd: 'npm install -g @anthropic-ai/claude-code',
      meta: 'Etiketler: Yapay zekâ, Geliştirici aracı, Terminal · MIT'
    },
    {
      title: 'Understand Anything',
      desc: 'Kodlarınızı veya dokümanlarınızı yapay zekâ ile etkileşimli hale getiren analiz aracı.',
      stars: '★ 77.021 STARS',
      cmd: '/plugin marketplace add Lum1104/Understand-Anything',
      meta: 'Etiketler: Geliştirici aracı, Kod analizi · MIT'
    },
    {
      title: 'TradingAgents',
      desc: 'Finansal piyasaları analiz eden çoklu otonom yapay zekâ ajanları mimarisi.',
      stars: '★ 21.430 STARS',
      cmd: 'git clone https://github.com/TuringComplete-Labs/TradingAgents.git',
      meta: 'Etiketler: Multi-Agent, Finans, Python · Apache 2.0'
    },
    {
      title: 'Code Graph RAG',
      desc: 'Büyük monorepo kod depolarındaki yapıları anlamak için bilgi grafikleri tabanlı RAG.',
      stars: '★ 4.782 STARS',
      cmd: 'pip install code-graph-rag',
      meta: 'Etiketler: RAG, Knowledge Graph, Kod arama · MIT'
    },
    {
      title: 'Maka',
      desc: 'Mikroservisler ve dağıtık sistemler için modern Go tabanlı geliştirici platformu.',
      stars: '★ 12.890 STARS',
      cmd: 'go install github.com/maka-dev/maka@latest',
      meta: 'Etiketler: Go, Mikroservis, Cloud · MIT'
    }
  ];

  var LOG_MESSAGES = [
    '[CRAWLER] GitHub Trending taranıyor...',
    '[DISCOVER] Yeni proje yakalandı: awesome-gpt-image-2',
    '[GEMINI] Türkçe editoryal analiz tamamlandı.',
    '[DIGEST] Günün raporu PDF olarak derlendi.',
    '[VERCEL] Statik sayfalar optimize edildi.',
    '[INDEX] 472 açık kaynak araç ve 537 terim güncel.'
  ];

  var clockEl = document.getElementById('js-clock');
  var titleEl = document.getElementById('js-tool-title');
  var descEl = document.getElementById('js-tool-desc');
  var starsEl = document.getElementById('js-tool-stars');
  var cmdEl = document.getElementById('js-tool-cmd');
  var metaEl = document.getElementById('js-tool-meta');
  var logStreamEl = document.getElementById('js-log-stream');
  var tickerTrackEl = document.getElementById('js-ticker-track');
  var audioBtn = document.getElementById('js-btn-audio');

  // Clock
  function updateClock() {
    var now = new Date();
    var h = String(now.getHours()).padStart(2, '0');
    var m = String(now.getMinutes()).padStart(2, '0');
    var s = String(now.getSeconds()).padStart(2, '0');
    if (clockEl) clockEl.textContent = h + ':' + m + ':' + s + ' UTC+3';
  }

  // Rotate Tool Showcase
  var toolIdx = 0;
  function updateTool() {
    var t = TOOLS[toolIdx];
    if (titleEl) titleEl.textContent = t.title;
    if (descEl) descEl.textContent = t.desc;
    if (starsEl) starsEl.textContent = t.stars;
    if (cmdEl) cmdEl.textContent = t.cmd;
    if (metaEl) metaEl.textContent = t.meta;
    toolIdx = (toolIdx + 1) % TOOLS.length;
  }

  // Append Live Logs
  var logIdx = 0;
  function appendLog() {
    if (!logStreamEl) return;
    var now = new Date();
    var timeStr = String(now.getHours()).padStart(2, '0') + ':' + String(now.getMinutes()).padStart(2, '0') + ':' + String(now.getSeconds()).padStart(2, '0');
    var msg = LOG_MESSAGES[logIdx % LOG_MESSAGES.length];
    logIdx++;

    var row = document.createElement('div');
    row.className = 'ls-log-item';
    row.innerHTML = '<span class="ls-log-time">[' + timeStr + ']</span> <span class="ls-log-text">' + msg + '</span>';
    logStreamEl.appendChild(row);

    if (logStreamEl.children.length > 8) {
      logStreamEl.removeChild(logStreamEl.children[0]);
    }
  }

  // Build Ticker
  function initTicker() {
    if (!tickerTrackEl) return;
    var items = TOOLS.map(function (t) {
      return '<span class="ls-ticker-item">● ' + t.title + ' <strong>' + t.stars.split(' ')[0] + '</strong></span>';
    }).join('');
    tickerTrackEl.innerHTML = items + items; // duplicate for infinite scroll
  }

  // Audio Toggle
  var isAudioPlaying = false;
  var audioContext = null;

  if (audioBtn) {
    audioBtn.addEventListener('click', function () {
      isAudioPlaying = !isAudioPlaying;
      audioBtn.textContent = isAudioPlaying ? '❚❚ Müzik Durdur' : '▶ Müzik Başlat';
    });
  }

  // Start Loops
  updateClock();
  setInterval(updateClock, 1000);
  initTicker();
  updateTool();
  setInterval(updateTool, 8000); // 8 saniyede bir yeni araç göster
  setInterval(appendLog, 4000);
})();
