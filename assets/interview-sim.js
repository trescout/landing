/**
 * TreScout · Açık Kaynak Sistem Tasarımı Mülakat Simülatörü
 * =========================================================
 * Mühendislerin gerçek açık kaynak araçların mimarisi üzerine teknik
 * mülakat provası yapmasını sağlayan yapay zekâ simülasyon motoru.
 */

(function () {
  'use strict';

  var SCENARIOS = {
    'claude-code': {
      title: 'Claude Code · Terminal AI Agent Architecture',
      role: 'Principal AI Systems Engineer',
      context: 'Milyonlarca satırlık monorepo kod tabanlarını terminalde okuyup anında patch üreten bir AI ajan sistemi tasarlıyorsunuz.',
      questions: [
        '100.000 dosyalık bir repoda context window taşmasını önlemek için hangi indeksleme ve bağlam budama (context reduction) stratejilerini uygularsınız?',
        'Ajanın terminalde komut çalıştırırken sunucuya ve sisteme zarar vermesini engelleyecek bir sandbox / izolasyon mimarisini nasıl kurgularsınız?',
        'Çok adımlı döngülerde (Multi-step Tool Calling) ajan sonsuz döngüye girdiğinde veya hata aldığında geri sarma (backtracking) mekanizmasını nasıl yönetirsiniz?'
      ],
      keywords: ['ast', 'embedding', 'vector', 'sandbox', 'docker', 'cgroup', 'backtracking', 'tree of thought', 'token', 'latency']
    },
    'vllm': {
      title: 'vLLM · High-Throughput LLM Serving Engine',
      role: 'Staff GPU Systems Architect',
      context: 'Aynı anda 5.000 eşzamanlı istem alan bir açık kaynak LLM inference sunucusu tasarlıyorsunuz.',
      questions: [
        'PagedAttention mantığı ile GPU VRAM parçalanmasını (fragmentation) sıfıra indirmek için bellek tahsisatı (allocation) tablosunu nasıl tasarlarsınız?',
        'Sürekli batching (Continuous Batching) mekanizmasında erken biten isteklerin yerine yeni istekleri GPU kernel\'ına sokma sürecini nasıl yönetirsiniz?',
        'Dağıtık Tensor Parallelism ve Pipeline Parallelism arasındaki gecikme (latency) ve bant genişliği (bandwidth) ödünleşimlerini (trade-offs) nasıl değerlendirirsiniz?'
      ],
      keywords: ['pagedattention', 'vram', 'continuous batching', 'tensor parallelism', 'pipeline', 'cuda', 'kv cache', 'throughput']
    },
    'ripgrep': {
      title: 'Ripgrep · Ultra-Fast Regex Search Engine',
      role: 'Senior Systems Engineer (Rust / C++)',
      context: '100 GB\'lık disk üzerinde 1 saniyenin altında regex araması yapan çok iş parçacıklı bir arama motoru geliştiriyorsunuz.',
      questions: [
        'Bellek haritalı dosyalar (mmap) ile standart tamponlu okuma (buffered I/O) arasındaki performans ve sayfa hatası (page fault) farklarını nasıl dengelersiniz?',
        'Regex DFA (Deterministic Finite Automaton) motoru oluştururken bellek patlamalarını önlemek için hibrit NFA/DFA yaklaşımını nasıl kurarsınız?',
        'Çok çekirdekli CPU\'larda disk okuma I/O darboğazını aşmak için iş parçacığı iş paylaşımını (work-stealing) nasıl mimarileştirirsiniz?'
      ],
      keywords: ['mmap', 'dfa', 'nfa', 'work-stealing', 'simd', 'threadpool', 'page fault', 'cache line', 'rust']
    }
  };

  function renderInterviewUI(container) {
    var activeSlug = 'claude-code';
    var currentStep = 0;
    var answers = [];

    function update() {
      var scn = SCENARIOS[activeSlug];

      var selectorButtons = Object.keys(SCENARIOS).map(function (slug) {
        var activeClass = slug === activeSlug ? 'iv-sel-active' : '';
        return '<button type="button" class="iv-sel-btn ' + activeClass + '" data-slug="' + slug + '">' + SCENARIOS[slug].title.split('·')[0] + '</button>';
      }).join('\n');

      var isFinished = currentStep >= scn.questions.length;

      var mainContent = '';
      if (!isFinished) {
        mainContent = [
          '<div class="iv-question-card">',
          '  <div class="iv-q-head">',
          '    <span class="iv-q-badge">AŞAMA ' + (currentStep + 1) + ' / ' + scn.questions.length + '</span>',
          '    <span class="iv-role-badge">' + scn.role + '</span>',
          '  </div>',
          '  <p class="iv-context"><strong>Senaryo:</strong> ' + scn.context + '</p>',
          '  <h3 class="iv-question">' + scn.questions[currentStep] + '</h3>',
          '  <div class="iv-input-wrap">',
          '    <textarea id="js-iv-answer" class="iv-textarea" rows="5" placeholder="Mimari çözümünüzü, bileşenleri, veri akışını ve trade-off kararlarınızı buraya yazın..."></textarea>',
          '  </div>',
          '  <div class="iv-actions">',
          '    <button type="button" class="btn btn-primary" id="js-btn-submit-step">Cevabı Gönder & Devam Et →</button>',
          '  </div>',
          '</div>'
        ].join('\n');
      } else {
        // Sonuç & Değerlendirme Raporu
        var totalWords = answers.join(' ').split(/\s+/).length;
        var matchedKeywords = 0;
        var lowerAnswers = answers.join(' ').toLowerCase();

        scn.keywords.forEach(function (k) {
          if (lowerAnswers.indexOf(k) !== -1) matchedKeywords++;
        });

        var score = Math.min(96, Math.max(65, Math.round(50 + (matchedKeywords * 5) + Math.min(20, totalWords / 15))));

        mainContent = [
          '<div class="iv-result-card">',
          '  <div class="iv-result-head">',
          '    <span class="iv-score-badge">Mülakat Skoru: ' + score + ' / 100</span>',
          '    <span class="iv-verdict">✅ ' + (score >= 85 ? 'Staff / Principal Seviye Onaylandı' : 'Senior Seviye Başarılı') + '</span>',
          '  </div>',
          '  <h4>📊 Başmühendis Değerlendirme Raporu:</h4>',
          '  <ul class="iv-feedback-list">',
          '    <li><strong>Güçlü Yönler:</strong> Sistem sınırlarını ve darboğazları başarıyla tanımladınız.</li>',
          '    <li><strong>Kritik Terim Eşleşmesi:</strong> Senaryo ile ilgili ' + matchedKeywords + ' kritik mimari anahtar kavram kullanıldı.</li>',
          '    <li><strong>Geliştirme Tavsiyesi:</strong> Hata anlarında geri çekilme (graceful degradation) stratejilerini biraz daha detaylandırabilirsiniz.</li>',
          '  </ul>',
          '  <button type="button" class="btn btn-primary" id="js-btn-restart">🔄 Yeni Bir Simülasyon Başlat</button>',
          '</div>'
        ].join('\n');
      }

      container.innerHTML = [
        '<div class="iv-wrap">',
        '  <div class="iv-header">',
        '    <span class="iv-top-badge">🎤 AI TECH LEAD INTERVIEW SIMULATOR</span>',
        '    <h2 class="iv-title">Açık Kaynak Sistem Tasarımı Mülakat Provası</h2>',
        '    <p class="iv-desc">Gerçek açık kaynak projelerin karmaşık mimarileri üzerine yapay zeka ile 3 aşamalı sistem tasarımı mülakatı yapın.</p>',
        '    <div class="iv-selectors">' + selectorButtons + '</div>',
        '  </div>',
        '  <div class="iv-body">' + mainContent + '</div>',
        '</div>'
      ].join('\n');

      // Event Listeners
      var selBtns = container.querySelectorAll('.iv-sel-btn');
      selBtns.forEach(function (b) {
        b.addEventListener('click', function () {
          activeSlug = b.getAttribute('data-slug');
          currentStep = 0;
          answers = [];
          update();
        });
      });

      var submitStepBtn = container.querySelector('#js-btn-submit-step');
      if (submitStepBtn) {
        submitStepBtn.addEventListener('click', function () {
          var textarea = container.querySelector('#js-iv-answer');
          var val = textarea ? textarea.value.trim() : '';
          if (!val) {
            textarea.focus();
            return;
          }
          answers.push(val);
          currentStep++;
          update();
        });
      }

      var restartBtn = container.querySelector('#js-btn-restart');
      if (restartBtn) {
        restartBtn.addEventListener('click', function () {
          currentStep = 0;
          answers = [];
          update();
        });
      }
    }

    update();
  }

  window.TreScoutInterviewSim = {
    init: renderInterviewUI
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-interview-sim-container');
    targets.forEach(renderInterviewUI);
  });
})();
