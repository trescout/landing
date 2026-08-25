/**
 * TreScout New Tab Script
 * =======================
 * Live Clock, Offline Curated Discoveries, Search & Shuffle.
 */

(function () {
  'use strict';

  // Sample curated tools pool for instant offline new-tab loading
  var CURATED_TOOLS = [
    {
      slug: 'claude-code',
      title: 'Claude Code',
      desc: 'Terminalde çalışan ve kod tabanınızı anlayan AI ajan kodlama aracı (Anthropic ürünü).',
      stars: '★ 142.599',
      cmd: 'npm install -g @anthropic-ai/claude-code',
      tags: ['Yapay zekâ araçları', 'Geliştirici aracı', 'Terminal']
    },
    {
      slug: 'understand-anything',
      title: 'Understand Anything',
      desc: 'Kodlarınızı veya dokümanlarınızı yapay zekâ ile etkileşimli hale getiren analiz aracı.',
      stars: '★ 77.021',
      cmd: '/plugin marketplace add Lum1104/Understand-Anything',
      tags: ['Geliştirici aracı', 'Kod anlama', 'AI']
    },
    {
      slug: 'tradingagents',
      title: 'TradingAgents',
      desc: 'Finansal piyasaları analiz eden çoklu otonom yapay zekâ ajanları çerçevesi.',
      stars: '★ 21.430',
      cmd: 'git clone https://github.com/TuringComplete-Labs/TradingAgents.git',
      tags: ['Multi-Agent', 'Finans', 'Python']
    },
    {
      slug: 'code-graph-rag',
      title: 'Code Graph RAG',
      desc: 'Büyük kod depolarındaki monorepo yapılarını anlamak için bilgi grafikleri tabanlı RAG.',
      stars: '★ 4.782',
      cmd: 'pip install code-graph-rag',
      tags: ['RAG', 'Knowledge Graph', 'Kod arama']
    },
    {
      slug: 'maka',
      title: 'Maka',
      desc: 'Mikroservisler ve dağıtık sistemler için modern Go tabanlı geliştirici platformu.',
      stars: '★ 12.890',
      cmd: 'go install github.com/maka-dev/maka@latest',
      tags: ['Go', 'Mikroservis', 'DevOps']
    }
  ];

  var clockEl = document.getElementById('js-clock');
  var dateEl = document.getElementById('js-date');
  var titleEl = document.getElementById('js-tool-title');
  var descEl = document.getElementById('js-tool-desc');
  var starsEl = document.getElementById('js-tool-stars');
  var cmdEl = document.getElementById('js-tool-cmd');
  var tagsEl = document.getElementById('js-tool-tags');
  var linkEl = document.getElementById('js-tool-link');
  var copyBtn = document.getElementById('js-btn-copy');
  var shuffleBtn = document.getElementById('js-btn-shuffle');
  var searchInput = document.getElementById('js-search-input');

  // Update Clock & Date
  function updateClock() {
    var now = new Date();
    var hours = String(now.getHours()).padStart(2, '0');
    var minutes = String(now.getMinutes()).padStart(2, '0');
    if (clockEl) clockEl.textContent = hours + ':' + minutes;

    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    if (dateEl) dateEl.textContent = now.toLocaleDateString('tr-TR', options);
  }

  // Display Tool Card
  var currentIndex = 0;

  function renderTool(tool) {
    if (!tool) return;
    if (titleEl) titleEl.textContent = tool.title;
    if (descEl) descEl.textContent = tool.desc;
    if (starsEl) starsEl.textContent = tool.stars;
    if (cmdEl) cmdEl.textContent = tool.cmd;
    if (linkEl) linkEl.href = 'https://trescout.com/discover/' + tool.slug + '/';

    if (tagsEl) {
      tagsEl.innerHTML = (tool.tags || []).map(function (t) {
        return '<span class="nt-tag">' + t + '</span>';
      }).join('');
    }
  }

  function shuffleTool() {
    currentIndex = (currentIndex + 1) % CURATED_TOOLS.length;
    renderTool(CURATED_TOOLS[currentIndex]);
  }

  // Copy command
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      if (!cmdEl) return;
      navigator.clipboard.writeText(cmdEl.textContent).then(function () {
        var originalText = copyBtn.textContent;
        copyBtn.textContent = 'Kopyalandı! ✓';
        setTimeout(function () {
          copyBtn.textContent = originalText;
        }, 1800);
      });
    });
  }

  if (shuffleBtn) {
    shuffleBtn.addEventListener('click', shuffleTool);
  }

  // Search Redirect
  if (searchInput) {
    searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        var val = searchInput.value.trim();
        if (val) {
          window.location.href = 'https://trescout.com/discover/?q=' + encodeURIComponent(val);
        }
      }
    });
  }

  // Initialize
  updateClock();
  setInterval(updateClock, 1000);
  renderTool(CURATED_TOOLS[0]);
})();
