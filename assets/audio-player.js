/**
 * TreScout · 1 Dakikalık Sesli Günlük Özet Çalar (Audio Player)
 * ============================================================
 * Sıfır bağımlılık, erişilebilir HTML5 mikro ses oynatıcısı.
 * Telemetri ve KVKK uyumlu.
 */

(function () {
  'use strict';

  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '0:00';
    var mins = Math.floor(seconds / 60);
    var secs = Math.floor(seconds % 60);
    return mins + ':' + (secs < 10 ? '0' : '') + secs;
  }

  function initPlayer(container) {
    var src = container.getAttribute('data-src');
    if (!src) return;

    var audio = new Audio(src);
    var isPlaying = false;
    var speeds = [1, 1.25, 1.5, 2];
    var currentSpeedIdx = 0;

    container.innerHTML = [
      '<div class="ap-inner" role="region" aria-label="1 Dakikalık Sesli Özet">',
      '  <button type="button" class="ap-btn-play" aria-label="Oynat">',
      '    <svg class="ap-icon-play" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>',
      '    <svg class="ap-icon-pause" viewBox="0 0 24 24" width="20" height="20" style="display:none"><path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>',
      '  </button>',
      '  <div class="ap-info">',
      '    <span class="ap-title">1 Dakikalık Sesli Özet</span>',
      '    <div class="ap-progress-wrap">',
      '      <input type="range" class="ap-seek" min="0" max="100" value="0" step="0.1" aria-label="Ses konumu">',
      '    </div>',
      '  </div>',
      '  <div class="ap-meta">',
      '    <span class="ap-time">0:00</span>',
      '    <button type="button" class="ap-speed" title="Oynatma hızı">1x</button>',
      '  </div>',
      '</div>'
    ].join('\n');

    var playBtn = container.querySelector('.ap-btn-play');
    var playIcon = container.querySelector('.ap-icon-play');
    var pauseIcon = container.querySelector('.ap-icon-pause');
    var seekInput = container.querySelector('.ap-seek');
    var timeDisplay = container.querySelector('.ap-time');
    var speedBtn = container.querySelector('.ap-speed');

    // Play / Pause Toggle
    playBtn.addEventListener('click', function () {
      if (isPlaying) {
        audio.pause();
      } else {
        audio.play().catch(function () {});
        if (window.TreScoutTelemetry && typeof window.TreScoutTelemetry.track === 'function') {
          window.TreScoutTelemetry.track('audio_digest_play', {
            src: src,
            placement: 'report_player'
          });
        }
      }
    });

    audio.addEventListener('play', function () {
      isPlaying = true;
      playIcon.style.display = 'none';
      pauseIcon.style.display = 'block';
      playBtn.setAttribute('aria-label', 'Durdur');
    });

    audio.addEventListener('pause', function () {
      isPlaying = false;
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
      playBtn.setAttribute('aria-label', 'Oynat');
    });

    audio.addEventListener('timeupdate', function () {
      if (!isNaN(audio.duration) && audio.duration > 0) {
        var pct = (audio.currentTime / audio.duration) * 100;
        seekInput.value = pct;
        timeDisplay.textContent = formatTime(audio.currentTime) + ' / ' + formatTime(audio.duration);
      }
    });

    audio.addEventListener('loadedmetadata', function () {
      timeDisplay.textContent = '0:00 / ' + formatTime(audio.duration);
    });

    audio.addEventListener('ended', function () {
      isPlaying = false;
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
      seekInput.value = 0;
    });

    seekInput.addEventListener('input', function () {
      if (!isNaN(audio.duration) && audio.duration > 0) {
        audio.currentTime = (seekInput.value / 100) * audio.duration;
      }
    });

    speedBtn.addEventListener('click', function () {
      currentSpeedIdx = (currentSpeedIdx + 1) % speeds.length;
      var speed = speeds[currentSpeedIdx];
      audio.playbackRate = speed;
      speedBtn.textContent = speed + 'x';
    });
  }

  function init() {
    var players = document.querySelectorAll('.tre-audio-player');
    players.forEach(initPlayer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
