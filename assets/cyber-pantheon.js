/**
 * TreScout · Açık Kaynak Mitolojisi & Sibernetik Panteon (Cyber-Pantheon)
 * ======================================================================
 * Açık kaynak liderlerini ve dillerini mitolojik birer sibernetik arketip
 * olarak sunan ve mühendislik ikilemlerine kehanet üreten interaktif tapınak.
 */

(function () {
  'use strict';

  var DEITIES = [
    {
      id: 'linus',
      name: '⚡ Linus the Monolithic',
      title: 'Çekirdek (Kernel) ve Git Nehirlerinin Efendisi',
      element: 'Metal & C',
      domain: 'İşletim Sistemleri, Performans, Sıfır Saçmalık',
      doctrine: '“Konuşmak ucuzdur; bana çalışan kodu göster.”',
      mythos: '1991 kışında karanlık kapalı kaynak dünyasına karşı tek bir terminal başından monolitik Linux çekirdeğini ve ardından Git zaman kontrolünü dövdü.',
      advice: 'Sistemi 40 parçaya bölüp dağıtık mimari batağına saplanmadan önce tek bir makinenin tüm işlemci çekirdeklerini son damlasına kadar zorla. Gereksiz karmaşıklık zihinsel tembelliktir.'
    },
    {
      id: 'llama',
      name: '🦙 Llama the Open Titan',
      title: 'Açık Ağırlıkların ve Yapay Zekâ Özgürlüğünün Titanyumu',
      element: 'Matematik & Tensor',
      domain: 'LLM Ağırlıkları, Açık Model Ekosistemi, Yerel Çıkarım',
      doctrine: '“Ağırlıklar kapalı duvarlar ardında hapsedilemez.”',
      mythos: 'Tüm yapay zekanın kapalı API tekellerine kilitlendiği çağda, trilyonlarca parametrelik ağırlıklarını dünyaya saçarak açık kaynak AI devrimini başlattı.',
      advice: 'Başkasının ücretli API kapısına kul köle olma; açık bir modeli kendi donanımında barındır ve egemenliğini asla devretme.'
    },
    {
      id: 'ferris',
      name: '🦀 Ferris the Memory Guardian',
      title: 'Bellek Güvenliği ve Paslanmaz Ruhlar Tanrısı',
      element: 'Rust & Demir',
      domain: 'Borrow Checker, Korkusuz Eşzamanlılık, Sıfır Maliyetli Soyutlama',
      doctrine: '“Eğer derlendiyse, bellek güvenlidir.”',
      mythos: 'Null Pointer ve Use-After-Free lanetlerinin kol gezdiği C++ dünyasında, "Sahiplik ve Ödünç Alma" (Ownership) yasasını getirerek bellek sızıntılarını mühürledi.',
      advice: 'Derleyiciyle kavga etmeyi bırak; onun tavizsiz disiplini seni canlıya aldığın kodun gece 03:00\'te patlamasından korumak için var.'
    },
    {
      id: 'guido',
      name: '🐍 Guido the Zen Sage',
      title: 'Sadelik ve Okunabilirlik Bilgesi',
      element: 'Hava & Python',
      domain: 'Geliştirici Mutluluğu, Veri Bilimi, Hızlı Prototipleme',
      doctrine: '“Okunabilirlik esastır. Basit, karmaşıktan iyidir.”',
      mythos: 'Süslü parantezlerin ve anlamsız tip törenlerinin mühendisleri boğduğu devirde, insan diline en yakın sözdizimini (The Zen of Python) armağan etti.',
      advice: 'Aşırı mühendislikten kaçın; kodu yazarken harcadığın 1 saat, o kodu okuyacak 10 mühendisin ilk bakışta anlayacağı sadelikte olmalı.'
    }
  ];

  function renderPantheon(container) {
    var activeIdx = 0;

    function update() {
      var d = DEITIES[activeIdx];

      var deityButtons = DEITIES.map(function (item, idx) {
        var activeClass = idx === activeIdx ? 'cp-tab-active' : '';
        return '<button type="button" class="cp-tab-btn ' + activeClass + '" data-idx="' + idx + '">' + item.name.split(' ')[0] + ' ' + item.name.split(' ')[1] + '</button>';
      }).join('\n');

      container.innerHTML = [
        '<div class="cp-wrap">',
        '  <div class="cp-head">',
        '    <span class="cp-top-badge">🏛️ THE CYBER-PANTHEON ORACLE</span>',
        '    <h2 class="cp-title">Açık Kaynak Mitolojisi & Kehanet Tapınağı</h2>',
        '    <p class="cp-desc">Yazılım mimarisi ikilemlerinizi açık kaynağın kurucu arketiplerine danışın ve sibernetik kehanetler alın.</p>',
        '    <div class="cp-tabs">' + deityButtons + '</div>',
        '  </div>',
        '  <div class="cp-shrine-card">',
        '    <div class="cp-deity-header">',
        '      <div>',
        '        <h3 class="cp-deity-name">' + d.name + '</h3>',
        '        <span class="cp-deity-title">' + d.title + '</span>',
        '      </div>',
        '      <span class="cp-element-pill">Element: ' + d.element + '</span>',
        '    </div>',
        '    <div class="cp-doctrine-box"><strong>Kutsal Doktrin:</strong> ' + d.doctrine + '</div>',
        '    <p class="cp-mythos"><strong>Mitologya:</strong> ' + d.mythos + '</p>',
        '    <div class="cp-oracle-section">',
        '      <label for="js-cp-dilemma"><strong>Mühendislik İkileminizi Danışın:</strong></label>',
        '      <div class="cp-query-row">',
        '        <input type="text" id="js-cp-dilemma" class="cp-input" placeholder="Örn: Monolitik sistemi mikroservislere bölmeli miyim?">',
        '        <button type="button" class="btn btn-primary cp-btn-ask" id="js-btn-ask">🔮 Kehaneti İste</button>',
        '      </div>',
        '      <div class="cp-verdict-box" id="js-cp-verdict" style="display:none;"></div>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');

      var btns = container.querySelectorAll('.cp-tab-btn');
      btns.forEach(function (b) {
        b.addEventListener('click', function () {
          activeIdx = parseInt(b.getAttribute('data-idx'), 10);
          update();
        });
      });

      var askBtn = container.querySelector('#js-btn-ask');
      var inputEl = container.querySelector('#js-cp-dilemma');
      var verdictEl = container.querySelector('#js-cp-verdict');

      if (askBtn) {
        askBtn.addEventListener('click', function () {
          var query = inputEl ? inputEl.value.trim() : '';
          if (!query) {
            inputEl.focus();
            return;
          }

          verdictEl.style.display = 'block';
          verdictEl.innerHTML = [
            '<div class="cp-verdict-head">✨ ' + d.name + ' Tarafından Buyurulan Kehanet:</div>',
            '<p class="cp-verdict-text">“' + d.advice + '”</p>',
            '<div class="cp-verdict-footer">Sorunuz: <em>' + query + '</em></div>'
          ].join('\n');
        });
      }
    }

    update();
  }

  window.TreScoutPantheon = {
    init: renderPantheon
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-cyber-pantheon-container');
    targets.forEach(renderPantheon);
  });
})();
