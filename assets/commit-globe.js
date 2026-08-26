/**
 * TreScout · Küresel Açık Kaynak Commit Küresi (Global Commit Globe)
 * =================================================================
 * Dünyanın dört bir yanından açık kaynak projelere atılan commit'leri
 * ve yıldız patlamalarını 3D dönen interaktif dünya üzerinde görselleştirir.
 */

(function () {
  'use strict';

  var HUBS = [
    { name: 'San Francisco', lat: 37.7749, lon: -122.4194, color: '#38BDF8' },
    { name: 'Tokyo', lat: 35.6762, lon: 139.6503, color: '#F43F5E' },
    { name: 'Berlin', lat: 52.5200, lon: 13.4050, color: '#10B981' },
    { name: 'İstanbul', lat: 41.0082, lon: 28.9784, color: '#F4D35E' },
    { name: 'London', lat: 51.5074, lon: -0.1278, color: '#8B5CF6' },
    { name: 'Singapore', lat: 1.3521, lon: 103.8198, color: '#06B6D4' },
    { name: 'Bangalore', lat: 12.9716, lon: 77.5946, color: '#F59E0B' },
    { name: 'São Paulo', lat: -23.5505, lon: -46.6333, color: '#EC4899' }
  ];

  var LIVE_EVENTS = [
    { from: 'Tokyo', to: 'San Francisco', tool: 'Claude Code', msg: 'Merge PR #412: AST cache rewrite', stars: '+12 ★' },
    { from: 'Berlin', to: 'İstanbul', tool: 'vLLM', msg: 'Commit 8f19a: PagedAttention kernel tweak', stars: '+8 ★' },
    { from: 'London', to: 'Bangalore', tool: 'Ripgrep', msg: 'Release v14.2: SIMD AVX-512 optimization', stars: '+45 ★' },
    { from: 'San Francisco', to: 'Tokyo', tool: 'Understand Anything', msg: 'Commit b33c: Agent memory fix', stars: '+19 ★' },
    { from: 'İstanbul', to: 'Berlin', tool: 'TradingAgents', msg: 'Merge PR #88: Multi-agent state loop', stars: '+6 ★' }
  ];

  function renderGlobe(container) {
    container.innerHTML = [
      '<div class="cg-wrap">',
      '  <div class="cg-head">',
      '    <span class="cg-top-badge">🛰️ GLOBAL COMMIT GLOBE</span>',
      '    <h2 class="cg-title">Küresel Açık Kaynak Nabzı Canlı Haritası</h2>',
      '    <p class="cg-desc">Dünyanın dört bir yanından TreScout kataloğundaki projelere akan canlı commit ve yıldız trafiği.</p>',
      '  </div>',
      '  <div class="cg-viewport">',
      '    <canvas id="js-globe-canvas" class="cg-canvas" width="600" height="420"></canvas>',
      '    <div class="cg-overlay-info">',
      '      <div class="cg-live-stat"><span class="cg-pulse-dot"></span> <strong>2.840 Eşzamanlı Geliştirici</strong></div>',
      '      <div class="cg-event-ticker" id="js-cg-ticker">Canlı commit akışı başlatılıyor...</div>',
      '    </div>',
      '  </div>',
      '</div>'
    ].join('\n');

    var canvas = container.querySelector('#js-globe-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var tickerEl = container.querySelector('#js-cg-ticker');

    var rotation = 0;
    var isDragging = false;
    var lastX = 0;

    canvas.addEventListener('mousedown', function (e) {
      isDragging = true;
      lastX = e.clientX;
    });

    window.addEventListener('mouseup', function () {
      isDragging = false;
    });

    canvas.addEventListener('mousemove', function (e) {
      if (isDragging) {
        var dx = e.clientX - lastX;
        rotation += dx * 0.008;
        lastX = e.clientX;
      }
    });

    // Projeksiyon formülü: Lat/Lon -> Canvas 2D x,y
    function project(lat, lon, rot) {
      var radLat = (lat * Math.PI) / 180;
      var radLon = ((lon + rot) * Math.PI) / 180;

      var cx = canvas.width / 2;
      var cy = canvas.height / 2;
      var radius = 150;

      var x = cx + radius * Math.cos(radLat) * Math.sin(radLon);
      var y = cy - radius * Math.sin(radLat);
      var visible = Math.cos(radLat) * Math.cos(radLon) > 0;

      return { x: x, y: y, visible: visible };
    }

    var pulseTime = 0;
    var activeArcIdx = 0;

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      var cx = canvas.width / 2;
      var cy = canvas.height / 2;
      var radius = 150;

      // Küre Arka Planı
      var grad = ctx.createRadialGradient(cx - 30, cy - 30, 10, cx, cy, radius);
      grad.addColorStop(0, '#1E293B');
      grad.addColorStop(1, '#090D16');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI * 2);
      ctx.fill();

      // Dış Atmosfer Parlaması
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
      ctx.lineWidth = 3;
      ctx.stroke();

      // Enlem / Boylam Grid Çizgileri
      ctx.strokeStyle = 'rgba(95, 168, 211, 0.12)';
      ctx.lineWidth = 1;
      for (var lat = -60; lat <= 60; lat += 30) {
        var rLat = (lat * Math.PI) / 180;
        var rY = cy - radius * Math.sin(rLat);
        var rWidth = radius * Math.cos(rLat);
        ctx.beginPath();
        ctx.ellipse(cx, rY, rWidth, rWidth * 0.25, 0, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Hub Düğümlerini Çiz
      var rotDegrees = (rotation * 180) / Math.PI;
      HUBS.forEach(function (h) {
        var p = project(h.lat, h.lon, rotDegrees);
        if (p.visible) {
          // Işıma
          ctx.fillStyle = h.color;
          ctx.beginPath();
          ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
          ctx.fill();

          // Hub Etiketi
          ctx.font = '10px ui-monospace, sans-serif';
          ctx.fillStyle = '#E2E8F0';
          ctx.fillText(h.name, p.x + 8, p.y + 3);
        }
      });

      // Canlı Commit Yayı (Animated Arc)
      var curEvent = LIVE_EVENTS[activeArcIdx];
      var hub1 = HUBS.find(function (h) { return h.name === curEvent.from; });
      var hub2 = HUBS.find(function (h) { return h.name === curEvent.to; });

      if (hub1 && hub2) {
        var p1 = project(hub1.lat, hub1.lon, rotDegrees);
        var p2 = project(hub2.lat, hub2.lon, rotDegrees);

        if (p1.visible && p2.visible) {
          ctx.strokeStyle = '#38BDF8';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          var midX = (p1.x + p2.x) / 2;
          var midY = Math.min(p1.y, p2.y) - 40;
          ctx.quadraticCurveTo(midX, midY, p2.x, p2.y);
          ctx.stroke();

          // Kayan Işık Parçacığı
          var t = (pulseTime % 100) / 100;
          var sparkX = (1 - t) * (1 - t) * p1.x + 2 * (1 - t) * t * midX + t * t * p2.x;
          var sparkY = (1 - t) * (1 - t) * p1.y + 2 * (1 - t) * t * midY + t * t * p2.y;

          ctx.fillStyle = '#F4D35E';
          ctx.beginPath();
          ctx.arc(sparkX, sparkY, 4, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      pulseTime += 1.5;
      if (pulseTime % 150 === 0) {
        activeArcIdx = (activeArcIdx + 1) % LIVE_EVENTS.length;
        if (tickerEl) {
          var ev = LIVE_EVENTS[activeArcIdx];
          tickerEl.innerHTML = '⚡ <strong>[' + ev.from + ' ➔ ' + ev.to + ']</strong> ' + ev.tool + ' · ' + ev.msg + ' <span class="cg-stars">' + ev.stars + '</span>';
        }
      }

      if (!isDragging) {
        rotation += 0.003; // Otomatik dönüş
      }

      requestAnimationFrame(draw);
    }

    draw();
  }

  window.TreScoutGlobe = {
    init: renderGlobe
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-globe-container');
    targets.forEach(renderGlobe);
  });
})();
