/**
 * TreScout · Açık Kaynak Canlı EKG / Kalp Monitörü (Git Heartbeat Monitor)
 * =======================================================================
 * Dünya genelindeki açık kaynak commit ve PR akışını medikal bir EKG
 * osiloskop monitörü ve kalp atış sesiyle canlı görselleştirir.
 */

(function () {
  'use strict';

  function renderHeartbeat(container) {
    container.innerHTML = [
      '<div class="gh-wrap">',
      '  <div class="gh-monitor-frame">',
      '    <div class="gh-top-bar">',
      '      <div class="gh-brand"><span class="gh-red-dot"></span> PATIENT: OPEN_SOURCE_ECOSYSTEM_V1</div>',
      '      <div class="gh-status">RHYTHM: NORMAL SINUS RHYTHM</div>',
      '    </div>',
      '    <div class="gh-screen">',
      '      <div class="gh-grid-bg"></div>',
      '      <canvas id="js-ekg-canvas" class="gh-canvas" width="600" height="240"></canvas>',
      '    </div>',
      '    <div class="gh-vitals-bar">',
      '      <div class="gh-vital-box">',
      '        <span class="gh-vital-label">HEART RATE (BPM)</span>',
      '        <div class="gh-vital-value gh-val-green"><strong id="js-bpm-val">138</strong> <small>CPM</small></div>',
      '      </div>',
      '      <div class="gh-vital-box">',
      '        <span class="gh-vital-label">SPO2 (PR HEALTH)</span>',
      '        <div class="gh-vital-value gh-val-cyan">99%</div>',
      '      </div>',
      '      <div class="gh-vital-box">',
      '        <span class="gh-vital-label">BP (CI STABILITY)</span>',
      '        <div class="gh-vital-value gh-val-yellow">120 / 80</div>',
      '      </div>',
      '      <div class="gh-vital-box gh-audio-box">',
      '        <button type="button" class="gh-btn-sound" id="js-btn-sound">🔊 Kalp Sesini Aç</button>',
      '      </div>',
      '    </div>',
      '  </div>',
      '</div>'
    ].join('\n');

    var canvas = container.querySelector('#js-ekg-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var bpmValEl = container.querySelector('#js-bpm-val');
    var soundBtn = container.querySelector('#js-btn-sound');

    var W = canvas.width;
    var H = canvas.height;
    var points = new Array(W).fill(H / 2);
    var scanX = 0;
    var bpm = 138;
    var audioCtx = null;
    var isSoundEnabled = false;

    // Web Audio Bip Sesi
    function playBeep() {
      if (!isSoundEnabled) return;
      try {
        if (!audioCtx) {
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(880, audioCtx.currentTime); // 880Hz yüksek tıbbi bip
        gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.08);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.08);
      } catch (e) {}
    }

    if (soundBtn) {
      soundBtn.addEventListener('click', function () {
        isSoundEnabled = !isSoundEnabled;
        soundBtn.textContent = isSoundEnabled ? '🔇 Sesi Kapat' : '🔊 Kalp Sesini Aç';
        soundBtn.classList.toggle('gh-btn-active', isSoundEnabled);
      });
    }

    // EKG Dalga Üretimi (P-Q-R-S-T dalgası)
    var stepInBeat = 0;
    var beatLength = 70; // BPM'e göre dalga genişliği

    function getEkgHeight(step) {
      var mid = H / 2;
      if (step === 10) return mid - 12; // P Dalgası (Atrium)
      if (step === 20) return mid + 8;  // Q Dalgası
      if (step === 25) {
        playBeep(); // R-Peak noktasında bip sesi
        return mid - 85; // R Dalgası (Büyük Zirve - Ventrikül)
      }
      if (step === 30) return mid + 35; // S Dalgası
      if (step === 45) return mid - 22; // T Dalgası (Ventriküler repolarizasyon)
      return mid; // İzolektrik hat
    }

    function loop() {
      // Bir sonraki EKG noktasını hesapla
      stepInBeat = (stepInBeat + 1) % beatLength;
      var targetY = getEkgHeight(stepInBeat);

      points[scanX] = targetY;

      // Temizleme ve Çizim
      ctx.fillStyle = 'rgba(5, 10, 18, 0.25)';
      ctx.fillRect(0, 0, W, H);

      ctx.strokeStyle = '#22C55E';
      ctx.lineWidth = 2.5;
      ctx.shadowColor = '#22C55E';
      ctx.shadowBlur = 10;

      ctx.beginPath();
      for (var x = 0; x < W; x++) {
        if (x === 0) {
          ctx.moveTo(x, points[x]);
        } else {
          ctx.lineTo(x, points[x]);
        }
      }
      ctx.stroke();
      ctx.shadowBlur = 0; // reset

      // Tarama Çizgisi (Phosphor Glow Head)
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(scanX, points[scanX], 3.5, 0, Math.PI * 2);
      ctx.fill();

      scanX = (scanX + 3) % W;

      // Nabız ufak dalgalanma simülasyonu
      if (Math.random() < 0.02) {
        bpm = Math.round(135 + Math.random() * 8);
        if (bpmValEl) bpmValEl.textContent = bpm;
      }

      requestAnimationFrame(loop);
    }

    loop();
  }

  window.TreScoutHeartbeat = {
    init: renderHeartbeat
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-git-heartbeat-container');
    targets.forEach(renderHeartbeat);
  });
})();
