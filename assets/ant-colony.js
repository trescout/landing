/**
 * TreScout · Açık Kaynak Karınca Kolonisi Simülatörü (Swarm Intelligence)
 * =======================================================================
 * Açık kaynak yazılımın kolektif bir sürü zekası olduğunu 2D fizik motoru,
 * feromon izleri ve kod kırıntılarıyla görselleştiren interaktif simülatör.
 */

(function () {
  'use strict';

  function renderAntColony(container) {
    container.innerHTML = [
      '<div class="ac-wrap">',
      '  <div class="ac-head">',
      '    <span class="ac-top-badge">🐜 SWARM INTELLIGENCE SIMULATOR</span>',
      '    <h2 class="ac-title">Açık Kaynak Karınca Kolonisi</h2>',
      '    <p class="ac-desc">Açık kaynak yazılım kolektif bir sürü zekasıdır. Ekrana tıklayarak kod kırıntısı (PR/Yıldız) bırakın, işçi karıncaların yuvaya taşımasını izleyin.</p>',
      '  </div>',
      '  <div class="ac-viewport">',
      '    <canvas id="js-ant-canvas" class="ac-canvas" width="640" height="380"></canvas>',
      '    <div class="ac-controls-bar">',
      '      <button type="button" class="ac-btn" id="js-btn-drop-star">⭐ Yıldız Kırıntısı Bırak</button>',
      '      <button type="button" class="ac-btn" id="js-btn-drop-pr">📦 PR Kırıntısı Bırak</button>',
      '      <button type="button" class="ac-btn" id="js-btn-add-ants">🐜 +20 İşçi Ekle</button>',
      '      <div class="ac-stat-pill">Toplam Taşınan: <strong id="js-ac-score">0</strong> Kırıntı</div>',
      '    </div>',
      '  </div>',
      '</div>'
    ].join('\n');

    var canvas = container.querySelector('#js-ant-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var scoreEl = container.querySelector('#js-ac-score');

    var W = canvas.width;
    var H = canvas.height;
    var nest = { x: W / 2, y: H / 2, r: 24, energy: 0 };
    var ants = [];
    var foods = [];
    var pheromones = [];
    var totalDelivered = 0;

    // Karınca Sınıfı
    function Ant(x, y) {
      this.x = x || nest.x;
      this.y = y || nest.y;
      this.angle = Math.random() * Math.PI * 2;
      this.speed = 1.8 + Math.random() * 0.8;
      this.hasFood = false;
      this.foodType = null;
    }

    Ant.prototype.update = function () {
      if (!this.hasFood) {
        // Yiyecek arama
        var nearestFood = null;
        var minDist = 120;
        for (var i = 0; i < foods.length; i++) {
          var f = foods[i];
          var d = Math.hypot(f.x - this.x, f.y - this.y);
          if (d < minDist) {
            minDist = d;
            nearestFood = f;
          }
        }

        if (nearestFood) {
          this.angle = Math.atan2(nearestFood.y - this.y, nearestFood.x - this.x);
          if (minDist < 8) {
            this.hasFood = true;
            this.foodType = nearestFood.type;
            nearestFood.amount--;
            if (nearestFood.amount <= 0) {
              foods.splice(foods.indexOf(nearestFood), 1);
            }
          }
        } else {
          this.angle += (Math.random() - 0.5) * 0.4;
        }
      } else {
        // Yuvaya dönme
        this.angle = Math.atan2(nest.y - this.y, nest.x - this.x);
        var distToNest = Math.hypot(nest.x - this.x, nest.y - this.y);

        // Feromon bırakma
        if (Math.random() < 0.3) {
          pheromones.push({ x: this.x, y: this.y, alpha: 0.6 });
        }

        if (distToNest < nest.r) {
          this.hasFood = false;
          totalDelivered++;
          nest.energy++;
          if (scoreEl) scoreEl.textContent = totalDelivered;
          this.angle += Math.PI; // Yuvadan ters yöne çık
        }
      }

      this.x += Math.cos(this.angle) * this.speed;
      this.y += Math.sin(this.angle) * this.speed;

      // Sınırlar
      if (this.x < 10) this.x = 10;
      if (this.x > W - 10) this.x = W - 10;
      if (this.y < 10) this.y = 10;
      if (this.y > H - 10) this.y = H - 10;
    };

    Ant.prototype.draw = function () {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.angle);

      // Karınca Gövdesi
      ctx.fillStyle = this.hasFood ? '#F4D35E' : '#E2E8F0';
      ctx.beginPath();
      ctx.ellipse(0, 0, 4, 2, 0, 0, Math.PI * 2);
      ctx.fill();

      // Taşınan Kırıntı
      if (this.hasFood) {
        ctx.fillStyle = this.foodType === 'star' ? '#F4D35E' : '#38BDF8';
        ctx.beginPath();
        ctx.arc(6, 0, 3, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.restore();
    };

    // Başlangıç Karıncaları
    for (var i = 0; i < 45; i++) {
      ants.push(new Ant());
    }

    // Başlangıç Yiyecekleri
    foods.push({ x: 90, y: 80, amount: 20, type: 'star' });
    foods.push({ x: 550, y: 300, amount: 25, type: 'pr' });
    foods.push({ x: 520, y: 90, amount: 15, type: 'star' });

    // Kullanıcı Tıklaması ile Kırıntı Bırakma
    canvas.addEventListener('click', function (e) {
      var rect = canvas.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      foods.push({ x: x, y: y, amount: 25, type: Math.random() > 0.5 ? 'star' : 'pr' });
    });

    // Kontrol Butonları
    var dropStarBtn = container.querySelector('#js-btn-drop-star');
    var dropPrBtn = container.querySelector('#js-btn-drop-pr');
    var addAntsBtn = container.querySelector('#js-btn-add-ants');

    if (dropStarBtn) {
      dropStarBtn.addEventListener('click', function () {
        foods.push({ x: 50 + Math.random() * (W - 100), y: 50 + Math.random() * (H - 100), amount: 30, type: 'star' });
      });
    }

    if (dropPrBtn) {
      dropPrBtn.addEventListener('click', function () {
        foods.push({ x: 50 + Math.random() * (W - 100), y: 50 + Math.random() * (H - 100), amount: 30, type: 'pr' });
      });
    }

    if (addAntsBtn) {
      addAntsBtn.addEventListener('click', function () {
        for (var k = 0; k < 20; k++) {
          ants.push(new Ant());
        }
      });
    }

    // Ana Animasyon Döngüsü
    function loop() {
      ctx.fillStyle = '#090D16';
      ctx.fillRect(0, 0, W, H);

      // Feromon İzlerini Çiz
      for (var p = pheromones.length - 1; p >= 0; p--) {
        var ph = pheromones[p];
        ctx.fillStyle = 'rgba(56, 189, 248, ' + ph.alpha + ')';
        ctx.fillRect(ph.x, ph.y, 2, 2);
        ph.alpha -= 0.005;
        if (ph.alpha <= 0) pheromones.splice(p, 1);
      }

      // Merkezi Yuva (TreScout Repo)
      var nestPulse = Math.sin(Date.now() * 0.004) * 3;
      var grad = ctx.createRadialGradient(nest.x, nest.y, 5, nest.x, nest.y, nest.r + nestPulse);
      grad.addColorStop(0, '#1B4965');
      grad.addColorStop(1, '#0F172A');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(nest.x, nest.y, nest.r + nestPulse, 0, Math.PI * 2);
      ctx.fill();

      ctx.strokeStyle = '#5FA8D3';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.font = '10px ui-monospace, sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.textAlign = 'center';
      ctx.fillText('👑 REPO', nest.x, nest.y + 4);

      // Yiyecek Kaynaklarını Çiz
      foods.forEach(function (f) {
        ctx.fillStyle = f.type === 'star' ? '#F4D35E' : '#38BDF8';
        ctx.beginPath();
        ctx.arc(f.x, f.y, Math.min(16, 4 + f.amount * 0.4), 0, Math.PI * 2);
        ctx.fill();

        ctx.font = '9px sans-serif';
        ctx.fillStyle = '#E2E8F0';
        ctx.fillText(f.type === 'star' ? '★ Star' : '📦 PR', f.x, f.y - 10);
      });

      // Karıncaları Güncelle ve Çiz
      ants.forEach(function (ant) {
        ant.update();
        ant.draw();
      });

      requestAnimationFrame(loop);
    }

    loop();
  }

  window.TreScoutAntColony = {
    init: renderAntColony
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-ant-colony-container');
    targets.forEach(renderAntColony);
  });
})();
