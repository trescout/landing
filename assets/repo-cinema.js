/**
 * TreScout · Kodun Doğuşu: Mimari Time-Lapse Sineması (Repo Growth Cinema)
 * =======================================================================
 * Açık kaynak projelerin ilk commit'ten bugüne mimari büyümesini, dosya
 * ağacının kök salmasını ve modüllerin bağlanmasını animasyonla görselleştirir.
 */

(function () {
  'use strict';

  var REPO_STORIES = {
    'claude-code': {
      title: 'Claude Code',
      category: 'Autonomous AI Coding Agent',
      starsToday: '★ 142.599',
      stages: [
        {
          label: '1. Gün: İlk Tohum (Genesis)',
          loc: '850 Satır',
          stars: '★ 120',
          desc: 'Minimalist bir CLI döngüsü, temel prompt şablonu ve terminal I/O motoru yazıldı.',
          nodes: [
            { id: 'root', label: 'claude-code', x: 250, y: 180, r: 18, color: '#1B4965' },
            { id: 'cli', label: 'bin/cli.ts', x: 170, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'prompt', label: 'prompts.ts', x: 330, y: 130, r: 12, color: '#5FA8D3' }
          ],
          links: [
            { from: 'root', to: 'cli' },
            { from: 'root', to: 'prompt' }
          ]
        },
        {
          label: '60. Gün: Ajan Döngüsü & Araç Çağrısı',
          loc: '6.400 Satır',
          stars: '★ 15.400',
          desc: 'Çok adımlı Tool Calling motoru, AST ayrıştırıcı ve dosya düzenleme yetenekleri eklendi.',
          nodes: [
            { id: 'root', label: 'claude-code', x: 250, y: 180, r: 20, color: '#1B4965' },
            { id: 'cli', label: 'bin/cli.ts', x: 170, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'prompt', label: 'prompts.ts', x: 330, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'agent', label: 'agent_loop.ts', x: 250, y: 90, r: 15, color: '#F4D35E' },
            { id: 'tools', label: 'tools/fs.ts', x: 130, y: 220, r: 12, color: '#10B981' },
            { id: 'ast', label: 'ast_parser.ts', x: 370, y: 220, r: 12, color: '#10B981' }
          ],
          links: [
            { from: 'root', to: 'cli' },
            { from: 'root', to: 'prompt' },
            { from: 'root', to: 'agent' },
            { from: 'root', to: 'tools' },
            { from: 'root', to: 'ast' }
          ]
        },
        {
          label: '180. Gün: Context Reduction & Sandbox',
          loc: '24.800 Satır',
          stars: '★ 68.000',
          desc: 'Büyük monorepolar için akıllı bağlam budama, güvenlik sandbox\'ı ve MCP entegrasyonu tamamlandı.',
          nodes: [
            { id: 'root', label: 'claude-code', x: 250, y: 180, r: 22, color: '#1B4965' },
            { id: 'cli', label: 'bin/cli.ts', x: 170, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'prompt', label: 'prompts.ts', x: 330, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'agent', label: 'agent_loop.ts', x: 250, y: 90, r: 15, color: '#F4D35E' },
            { id: 'tools', label: 'tools/fs.ts', x: 130, y: 220, r: 12, color: '#10B981' },
            { id: 'ast', label: 'ast_parser.ts', x: 370, y: 220, r: 12, color: '#10B981' },
            { id: 'mcp', label: 'mcp_client.ts', x: 90, y: 150, r: 13, color: '#8B5CF6' },
            { id: 'sandbox', label: 'sandbox.ts', x: 410, y: 150, r: 13, color: '#EF4444' },
            { id: 'context', label: 'context_pruner.ts', x: 250, y: 280, r: 13, color: '#3B82F6' }
          ],
          links: [
            { from: 'root', to: 'cli' },
            { from: 'root', to: 'prompt' },
            { from: 'root', to: 'agent' },
            { from: 'root', to: 'tools' },
            { from: 'root', to: 'ast' },
            { from: 'agent', to: 'mcp' },
            { from: 'agent', to: 'sandbox' },
            { from: 'root', to: 'context' }
          ]
        },
        {
          label: 'Bugün: Küresel AI Ajan Standardı',
          loc: '62.000 Satır',
          stars: '★ 142.599',
          desc: '100+ topluluk plugin\'i, yerel telemetry ve endüstri standardı AI ajan mimarisi.',
          nodes: [
            { id: 'root', label: 'claude-code', x: 250, y: 180, r: 24, color: '#1B4965' },
            { id: 'cli', label: 'bin/cli.ts', x: 170, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'prompt', label: 'prompts.ts', x: 330, y: 130, r: 12, color: '#5FA8D3' },
            { id: 'agent', label: 'agent_loop.ts', x: 250, y: 90, r: 16, color: '#F4D35E' },
            { id: 'tools', label: 'tools/fs.ts', x: 130, y: 220, r: 12, color: '#10B981' },
            { id: 'ast', label: 'ast_parser.ts', x: 370, y: 220, r: 12, color: '#10B981' },
            { id: 'mcp', label: 'mcp_client.ts', x: 90, y: 150, r: 14, color: '#8B5CF6' },
            { id: 'sandbox', label: 'sandbox.ts', x: 410, y: 150, r: 14, color: '#EF4444' },
            { id: 'context', label: 'context_pruner.ts', x: 250, y: 280, r: 14, color: '#3B82F6' },
            { id: 'plugin', label: 'plugins/', x: 170, y: 270, r: 11, color: '#F59E0B' },
            { id: 'telemetry', label: 'telemetry.ts', x: 330, y: 270, r: 11, color: '#64748B' }
          ],
          links: [
            { from: 'root', to: 'cli' },
            { from: 'root', to: 'prompt' },
            { from: 'root', to: 'agent' },
            { from: 'root', to: 'tools' },
            { from: 'root', to: 'ast' },
            { from: 'agent', to: 'mcp' },
            { from: 'agent', to: 'sandbox' },
            { from: 'root', to: 'context' },
            { from: 'tools', to: 'plugin' },
            { from: 'root', to: 'telemetry' }
          ]
        }
      ]
    },
    'vllm': {
      title: 'vLLM',
      category: 'High-Throughput LLM Serving',
      starsToday: '★ 48.200',
      stages: [
        {
          label: '1. Gün: İlk PagedAttention Deneyi',
          loc: '1.200 Satır',
          stars: '★ 300',
          desc: 'İşletim sistemi sanal bellek sayfalamasından esinlenen ilk CUDA kerneli yazıldı.',
          nodes: [
            { id: 'root', label: 'vllm', x: 250, y: 180, r: 18, color: '#1B4965' },
            { id: 'kernel', label: 'paged_attn.cu', x: 180, y: 120, r: 13, color: '#EF4444' },
            { id: 'model', label: 'model_runner.py', x: 320, y: 120, r: 13, color: '#5FA8D3' }
          ],
          links: [
            { from: 'root', to: 'kernel' },
            { from: 'root', to: 'model' }
          ]
        },
        {
          label: 'Bugün: Dağıtık Çıkarım Standartı',
          loc: '95.000 Satır',
          stars: '★ 48.200',
          desc: 'Tensor Parallelism, LoRA desteği ve OpenAI uyumlu yüksek hızlı API sunucusu.',
          nodes: [
            { id: 'root', label: 'vllm', x: 250, y: 180, r: 22, color: '#1B4965' },
            { id: 'kernel', label: 'paged_attn.cu', x: 180, y: 120, r: 13, color: '#EF4444' },
            { id: 'model', label: 'model_runner.py', x: 320, y: 120, r: 13, color: '#5FA8D3' },
            { id: 'batch', label: 'continuous_batch.py', x: 250, y: 80, r: 15, color: '#F4D35E' },
            { id: 'server', label: 'api_server.py', x: 110, y: 220, r: 13, color: '#10B981' },
            { id: 'parallel', label: 'distributed/', x: 390, y: 220, r: 13, color: '#8B5CF6' }
          ],
          links: [
            { from: 'root', to: 'kernel' },
            { from: 'root', to: 'model' },
            { from: 'root', to: 'batch' },
            { from: 'root', to: 'server' },
            { from: 'root', to: 'parallel' }
          ]
        }
      ]
    }
  };

  function renderCinemaUI(container) {
    var activeSlug = 'claude-code';
    var stageIdx = 0;
    var isPlaying = false;
    var playTimer = null;

    function drawSVG(stage) {
      var nodeMap = {};
      stage.nodes.forEach(function (n) { nodeMap[n.id] = n; });

      var linksSvg = stage.links.map(function (l) {
        var n1 = nodeMap[l.from];
        var n2 = nodeMap[l.to];
        if (!n1 || !n2) return '';
        return '<line class="rc-link" x1="' + n1.x + '" y1="' + n1.y + '" x2="' + n2.x + '" y2="' + n2.y + '" />';
      }).join('\n');

      var nodesSvg = stage.nodes.map(function (n) {
        return [
          '<g class="rc-node-group" transform="translate(' + n.x + ',' + n.y + ')">',
          '  <circle class="rc-node" r="' + n.r + '" fill="' + n.color + '" />',
          '  <text class="rc-node-text" y="' + (n.r + 14) + '" text-anchor="middle">' + n.label + '</text>',
          '</g>'
        ].join('\n');
      }).join('\n');

      return [
        '<svg class="rc-svg" viewBox="0 0 500 360" width="100%" height="320">',
        '  <defs>',
        '    <filter id="glow">',
        '      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>',
        '      <feMerge>',
        '        <feMergeNode in="coloredBlur"/>',
        '        <feMergeNode in="SourceGraphic"/>',
        '      </feMerge>',
        '    </filter>',
        '  </defs>',
        '  <g class="rc-links-layer">' + linksSvg + '</g>',
        '  <g class="rc-nodes-layer">' + nodesSvg + '</g>',
        '</svg>'
      ].join('\n');
    }

    function update() {
      var repo = REPO_STORIES[activeSlug];
      var stage = repo.stages[stageIdx];

      var repoTabs = Object.keys(REPO_STORIES).map(function (slug) {
        var activeClass = slug === activeSlug ? 'rc-tab-active' : '';
        return '<button type="button" class="rc-tab-btn ' + activeClass + '" data-slug="' + slug + '">' + REPO_STORIES[slug].title + '</button>';
      }).join('\n');

      var scrubberPills = repo.stages.map(function (s, idx) {
        var activeClass = idx === stageIdx ? 'rc-pill-active' : '';
        return '<button type="button" class="rc-scrub-pill ' + activeClass + '" data-idx="' + idx + '">' + s.label.split(':')[0] + '</button>';
      }).join('\n');

      container.innerHTML = [
        '<div class="rc-wrap">',
        '  <div class="rc-head">',
        '    <span class="rc-top-badge">🎬 REPO GROWTH CINEMA</span>',
        '    <h2 class="rc-title">Kodun Doğuşu: 30 Saniyelik Mimari Time-Lapse</h2>',
        '    <p class="rc-desc">Açık kaynak bir projenin ilk commit\'ten bugüne yaşayan bir organizma gibi nasıl büyüdüğünü izleyin.</p>',
        '    <div class="rc-tabs">' + repoTabs + '</div>',
        '  </div>',
        '  <div class="rc-cinema-box">',
        '    <div class="rc-stage-info">',
        '      <div class="rc-stage-metrics">',
        '        <span class="rc-stage-pill">' + stage.label + '</span>',
        '        <span class="rc-metric">📏 Kod Boyutu: <strong>' + stage.loc + '</strong></span>',
        '        <span class="rc-metric">⭐ Yıldız: <strong>' + stage.stars + '</strong></span>',
        '      </div>',
        '      <p class="rc-stage-desc">' + stage.desc + '</p>',
        '    </div>',
        '    <div class="rc-canvas-area">' + drawSVG(stage) + '</div>',
        '    <div class="rc-controls">',
        '      <button type="button" class="btn btn-primary rc-btn-play" id="js-rc-play">' + (isPlaying ? '❚❚ Duraklat' : '▶ Time-Lapse Oynat') + '</button>',
        '      <div class="rc-scrubber">' + scrubberPills + '</div>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');

      // Listeners
      var tabBtns = container.querySelectorAll('.rc-tab-btn');
      tabBtns.forEach(function (b) {
        b.addEventListener('click', function () {
          activeSlug = b.getAttribute('data-slug');
          stageIdx = 0;
          stopPlay();
          update();
        });
      });

      var scrubBtns = container.querySelectorAll('.rc-scrub-pill');
      scrubBtns.forEach(function (b) {
        b.addEventListener('click', function () {
          stageIdx = parseInt(b.getAttribute('data-idx'), 10);
          stopPlay();
          update();
        });
      });

      var playBtn = container.querySelector('#js-rc-play');
      if (playBtn) {
        playBtn.addEventListener('click', function () {
          if (isPlaying) {
            stopPlay();
          } else {
            startPlay();
          }
          update();
        });
      }
    }

    function startPlay() {
      isPlaying = true;
      playTimer = setInterval(function () {
        var repo = REPO_STORIES[activeSlug];
        stageIdx = (stageIdx + 1) % repo.stages.length;
        update();
      }, 2500);
    }

    function stopPlay() {
      isPlaying = false;
      if (playTimer) clearInterval(playTimer);
    }

    update();
  }

  window.TreScoutRepoCinema = {
    init: renderCinemaUI
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-repo-cinema-container');
    targets.forEach(renderCinemaUI);
  });
})();
