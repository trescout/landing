/**
 * TreScout · Kodu Biyolojik DNA Dizilimine Dönüştürücü (Code to DNA)
 * =================================================================
 * Açık kaynak yazılım kodlarını sentetik biyolojik DNA baz çiftlerine
 * (A, T, C, G) dönüştürür ve 3D çift sarmal (Double Helix) ile görselleştirir.
 */

(function () {
  'use strict';

  var MAP_2BIT_TO_DNA = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
  };

  var COLOR_MAP = {
    'A': '#EF4444', // Kırmızı (Adenin)
    'T': '#10B981', // Yeşil (Timin)
    'C': '#38BDF8', // Mavi (Sitozin)
    'G': '#F4D35E'  // Sarı (Guanin)
  };

  var COMPLEMENT_MAP = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
  };

  function encodeStringToDNA(str) {
    var encoder = new TextEncoder();
    var bytes = encoder.encode(str);
    var dna = [];

    for (var i = 0; i < bytes.length; i++) {
      var byteVal = bytes[i];
      var bits = byteVal.toString(2).padStart(8, '0');
      for (var j = 0; j < 8; j += 2) {
        var pair = bits.substr(j, 2);
        dna.push(MAP_2BIT_TO_DNA[pair]);
      }
    }
    return dna.join('');
  }

  function renderDnaSynthesizer(container) {
    container.innerHTML = [
      '<div class="dna-wrap">',
      '  <div class="dna-head">',
      '    <span class="dna-top-badge">🧬 SYNTHETIC BIO-STORAGE LAB</span>',
      '    <h2 class="dna-title">Kodu Biyolojik DNA Dizilimine Dönüştür</h2>',
      '    <p class="dna-desc">Yazılımınızı disklerden çıkarıp canlı bitki veya sentetik DNA tüplerinde 10.000 yıl yaşayacak moleküler baz çiftlerine (A-T-C-G) dönüştürün.</p>',
      '  </div>',
      '  <div class="dna-main-grid">',
      '    <div class="dna-input-col">',
      '      <label for="js-dna-input"><strong>Kaynak Kod Girdisi:</strong></label>',
      '      <textarea id="js-dna-input" class="dna-textarea" rows="5" placeholder="Dönüştürmek istediğiniz kodu buraya yazın...">fn main() {\n    println!("TreScout Bio-Storage Active!");\n}</textarea>',
      '      <button type="button" class="btn btn-primary dna-btn-synth" id="js-btn-synth">🧬 DNA Sarmalına Dönüştür</button>',
      '    </div>',
      '    <div class="dna-canvas-col">',
      '      <canvas id="js-dna-canvas" class="dna-canvas" width="340" height="240"></canvas>',
      '    </div>',
      '  </div>',
      '  <div class="dna-results" id="js-dna-results">',
      '    <div class="dna-metrics">',
      '      <div class="dna-metric"><span class="dna-m-val" id="js-bp-count">336 bp</span><span class="dna-m-lbl">Baz Çifti Uzunluğu</span></div>',
      '      <div class="dna-metric"><span class="dna-m-val" id="js-gc-ratio">%54.2</span><span class="dna-m-lbl">GC Sentez Kararlılığı</span></div>',
      '      <div class="dna-metric"><span class="dna-m-val">10.000+ Yıl</span><span class="dna-m-lbl">Fosil Veri Ömrü</span></div>',
      '    </div>',
      '    <div class="dna-seq-box">',
      '      <div class="dna-seq-label">NCBI Standardı DNA Nükleotit Dizilimi (İlk 120 bp):</div>',
      '      <div class="dna-seq-text" id="js-dna-seq"></div>',
      '    </div>',
      '    <button type="button" class="btn btn-ghost dna-btn-fasta" id="js-btn-download-fasta">📥 .FASTA Biyolojik Dosyasını İndir</button>',
      '  </div>',
      '</div>'
    ].join('\n');

    var inputEl = container.querySelector('#js-dna-input');
    var synthBtn = container.querySelector('#js-btn-synth');
    var canvas = container.querySelector('#js-dna-canvas');
    var bpCountEl = container.querySelector('#js-bp-count');
    var gcRatioEl = container.querySelector('#js-gc-ratio');
    var seqEl = container.querySelector('#js-dna-seq');
    var downloadBtn = container.querySelector('#js-btn-download-fasta');

    if (!canvas) return;
    var ctx = canvas.getContext('2d');

    var currentDNA = encodeStringToDNA(inputEl.value);

    function updateMetrics() {
      var bp = currentDNA.length;
      var gCount = (currentDNA.match(/G/g) || []).length;
      var cCount = (currentDNA.match(/C/g) || []).length;
      var gcRatio = bp > 0 ? (((gCount + cCount) / bp) * 100).toFixed(1) : '0.0';

      if (bpCountEl) bpCountEl.textContent = bp + ' bp';
      if (gcRatioEl) gcRatioEl.textContent = '%' + gcRatio;

      if (seqEl) {
        var preview = currentDNA.substring(0, 120);
        var colored = '';
        for (var i = 0; i < preview.length; i++) {
          var char = preview[i];
          colored += '<span style="color:' + (COLOR_MAP[char] || '#fff') + '; font-weight:800;">' + char + '</span>';
        }
        seqEl.innerHTML = colored + (currentDNA.length > 120 ? '...' : '');
      }
    }

    // 3D Çift Sarmal Animasyonu
    var angleOffset = 0;
    function drawHelix() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      var W = canvas.width;
      var H = canvas.height;
      var numRungs = 18;
      var spacing = H / numRungs;
      var radius = 55;
      var cx = W / 2;

      for (var i = 0; i < numRungs; i++) {
        var y = i * spacing + 10;
        var angle = angleOffset + (i * 0.35);
        var x1 = cx + Math.sin(angle) * radius;
        var x2 = cx - Math.sin(angle) * radius;
        var z = Math.cos(angle);

        // Baz Eşleşmesi (A-T veya C-G)
        var baseIdx = (i % (currentDNA.length || 1));
        var base1 = currentDNA[baseIdx] || 'A';
        var base2 = COMPLEMENT_MAP[base1] || 'T';

        // Hidrojen Bağı Çizgisi
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
        ctx.stroke();

        // 1. Nükleotit Düğümü
        var size1 = Math.max(3, 5 + z * 2);
        ctx.fillStyle = COLOR_MAP[base1] || '#38BDF8';
        ctx.beginPath();
        ctx.arc(x1, y, size1, 0, Math.PI * 2);
        ctx.fill();

        // 2. Nükleotit Düğümü (Komplementer)
        var size2 = Math.max(3, 5 - z * 2);
        ctx.fillStyle = COLOR_MAP[base2] || '#10B981';
        ctx.beginPath();
        ctx.arc(x2, y, size2, 0, Math.PI * 2);
        ctx.fill();
      }

      angleOffset += 0.03;
      requestAnimationFrame(drawHelix);
    }

    synthBtn.addEventListener('click', function () {
      currentDNA = encodeStringToDNA(inputEl.value);
      updateMetrics();
    });

    if (downloadBtn) {
      downloadBtn.addEventListener('click', function () {
        var fasta = '>TreScout_BioVault | Length=' + currentDNA.length + 'bp\n' + currentDNA;
        var blob = new Blob([fasta], { type: 'text/plain;charset=utf-8' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'trescout-code.fasta';
        a.click();
        URL.revokeObjectURL(url);
      });
    }

    updateMetrics();
    drawHelix();
  }

  window.TreScoutDna = {
    init: renderDnaSynthesizer
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-dna-container');
    targets.forEach(renderDnaSynthesizer);
  });
})();
