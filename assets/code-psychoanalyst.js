/**
 * TreScout · Kod Bilinçaltı Analizcisi (Codebase Psychoanalyst)
 * =============================================================
 * Geliştiricilerin karmaşık kodlarını analiz ederek bilinçaltı kaygılarını
 * eğlenceli şekilde teşhis eder ve sakinleştirici açık kaynak reçetesi sunar.
 */

(function () {
  'use strict';

  var SAMPLE_SPAGHETTI = [
    'function processOrder(data) {',
    '  // TODO: burası çok çirkin oldu, sonra refactor et',
    '  if (data) {',
    '    if (data.user) {',
    '      if (data.user.cart && data.user.cart.items) {',
    '        if (data.user.cart.items.length > 0) {',
    '          try {',
    '            let token: any = data.token;',
    '            let amount: any = data.user.cart.total;',
    '            if (amount !== undefined && amount !== null && !isNaN(amount)) {',
    '              return { status: "OK", charge: amount };',
    '            }',
    '          } catch (e) {',
    '            // sessizce yut',
    '          }',
    '        }',
    '      }',
    '    }',
    '  }',
    '  return { status: "FAIL" };',
    '}'
  ].join('\n');

  function analyzeCode(code) {
    var lines = code.split('\n');
    var ifCount = (code.match(/\bif\b/g) || []).length;
    var tryCount = (code.match(/\btry\b/g) || []).length;
    var anyCount = (code.match(/\bany\b/g) || []).length;
    var todoCount = (code.match(/TODO|FIXME|HACK/gi) || []).length;

    var paranoia = Math.min(96, Math.max(25, ifCount * 14 + tryCount * 10));
    var anxiety = Math.min(94, Math.max(30, todoCount * 20 + anyCount * 25));
    var burnout = Math.min(90, Math.max(20, Math.round(lines.length * 2.5)));

    var findings = [];
    if (ifCount >= 4) {
      findings.push('İç içe geçmiş 4+ `if` bloğu: Geliştiricinin geçmişte beklenmeyen bir `null pointer` travması yaşadığını ve evrene karşı derin bir güvensizlik beslediğini gösteriyor.');
    }
    if (anyCount >= 1) {
      findings.push('`any` tipi kullanımı: Tip denetiminden kaçış, kurallara başkaldırı ve teslim tarihinin acımasız baskısı altında benliğini kaybetme belirtisi.');
    }
    if (todoCount >= 1) {
      findings.push('TODO / HACK yorumları: "Bir ara düzeltirim" diyerek sorumluluğu gelecekteki benliğine devreden klasik erteleme (procrastination) savunma mekanizması.');
    }

    if (findings.length === 0) {
      findings.push('Kod oldukça sakin görünüyor ancak yüzeyin altında gizli bir kontrol arzusu ve sessiz bir mükemmeliyetçilik seziliyor.');
    }

    return {
      paranoia: paranoia,
      anxiety: anxiety,
      burnout: burnout,
      diagnosis: findings.join(' '),
      prescription: {
        tool: 'Zod & Claude Code',
        note: 'Gelen veriyi kapıda tek satırda doğrulayın (schema parsing) ve iç içe if cehennemine son vererek zihninize huzur kazandırın.'
      }
    };
  }

  function renderPsychoanalystUI(container) {
    container.innerHTML = [
      '<div class="cpa-wrap">',
      '  <div class="cpa-head">',
      '    <span class="cpa-top-badge">🛋️ CODEBASE PSYCHOANALYST</span>',
      '    <h2 class="cpa-title">Spagetti Kodun Bilinçaltı Analizi</h2>',
      '    <p class="cpa-desc">En karmaşık kodunuzu yapıştırın; Yapay Zeka Terapisti bu kodu yazarken hissettiğiniz bilinçaltı travmaları teşhis etsin.</p>',
      '  </div>',
      '  <div class="cpa-couch-box">',
      '    <div class="cpa-input-header">',
      '      <label for="js-cpa-input"><strong>📝 Analiz Edilecek Kod Parçası:</strong></label>',
      '      <button type="button" class="btn-sample-code" id="js-btn-sample">Örnek Spagetti Kod Yükle</button>',
      '    </div>',
      '    <textarea id="js-cpa-input" class="cpa-textarea" rows="6" placeholder="Kodu buraya yapıştırın..."></textarea>',
      '    <button type="button" class="btn btn-primary cpa-btn-analyze" id="js-btn-analyze">🧠 Bilinçaltını Teşhis Et</button>',
      '  </div>',
      '  <div class="cpa-report-area" id="js-cpa-report" style="display:none;"></div>',
      '</div>'
    ].join('\n');

    var inputEl = container.querySelector('#js-cpa-input');
    var sampleBtn = container.querySelector('#js-btn-sample');
    var analyzeBtn = container.querySelector('#js-btn-analyze');
    var reportEl = container.querySelector('#js-cpa-report');

    sampleBtn.addEventListener('click', function () {
      inputEl.value = SAMPLE_SPAGHETTI;
    });

    analyzeBtn.addEventListener('click', function () {
      var code = inputEl.value.trim();
      if (!code) {
        inputEl.focus();
        return;
      }

      var res = analyzeCode(code);

      reportEl.style.display = 'flex';
      reportEl.innerHTML = [
        '<div class="cpa-report-card">',
        '  <div class="cpa-metrics-grid">',
        '    <div class="cpa-metric"><span class="cpa-val">' + res.paranoia + '%</span><span class="cpa-label">Edge-Case Paranoyası</span></div>',
        '    <div class="cpa-metric"><span class="cpa-val">' + res.anxiety + '%</span><span class="cpa-label">Cuma Deploy Anksiyetesi</span></div>',
        '    <div class="cpa-metric"><span class="cpa-val">' + res.burnout + '%</span><span class="cpa-label">Tükenmişlik Seviyesi</span></div>',
        '  </div>',
        '  <div class="cpa-diagnosis-box">',
        '    <h4>🩺 Terapist Teşhis Raporu:</h4>',
        '    <p>' + res.diagnosis + '</p>',
        '  </div>',
        '  <div class="cpa-prescription-box">',
        '    <h4>💊 TreScout İyileştirici Reçetesi:</h4>',
        '    <p><strong>Tavsiye Edilen Açık Kaynak Araç:</strong> ' + res.prescription.tool + '</p>',
        '    <p class="cpa-therapy-note">' + res.prescription.note + '</p>',
        '  </div>',
        '</div>'
      ].join('\n');
    });
  }

  window.TreScoutPsychoanalyst = {
    init: renderPsychoanalystUI
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-psychoanalyst-container');
    targets.forEach(renderPsychoanalystUI);
  });
})();
