/**
 * TreScout · Topluluk Sözlük Katkı Sihirbazı (Community Contribution Helper)
 * =========================================================================
 * Kullanıcıların doğrudan arayüzden sözlüğe yeni terim veya analoji önermesini
 * sağlar ve tek tıkla formatı hazır GitHub Issue/PR bağlantısı üretir.
 */

(function () {
  'use strict';

  var GITHUB_REPO = 'trescout/landing';

  function createContributeButton(container) {
    var existingTerm = container.getAttribute('data-term') || '';

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'btn btn-ghost tre-btn-contribute';
    button.innerHTML = existingTerm
      ? '💡 Bu kavrama analoji / açıklama ekle'
      : '✨ Sözlüğe yeni bir terim öner';

    button.addEventListener('click', function () {
      openContributionModal(existingTerm);
    });

    container.appendChild(button);
  }

  function openContributionModal(existingTerm) {
    var existingModal = document.getElementById('tre-contribute-modal');
    if (existingModal) existingModal.remove();

    var modal = document.createElement('div');
    modal.id = 'tre-contribute-modal';
    modal.className = 'tre-modal-overlay';
    modal.innerHTML = [
      '<div class="tre-modal-card" role="dialog" aria-modal="true" aria-labelledby="modal-title">',
      '  <div class="tre-modal-head">',
      '    <h3 id="modal-title">' + (existingTerm ? '💡 "' + existingTerm + '" İçin Katkı Sağla' : '✨ Yeni Sözlük Terimi Öner') + '</h3>',
      '    <button type="button" class="tre-modal-close" id="js-modal-close" aria-label="Kapat">&times;</button>',
      '  </div>',
      '  <div class="tre-modal-body">',
      '    <p class="tre-modal-desc">TreScout Sözlüğü açık kaynak ve topluluk odaklıdır. Öneriniz doğrudan GitHub üzerinden incelenir ve yayına alınır.</p>',
      '    <div class="tre-form-group">',
      '      <label for="js-c-name">Terim Adı (İngilizce / Global İsim):</label>',
      '      <input type="text" id="js-c-name" class="input" value="' + existingTerm + '" placeholder="Örn: Vector Search, Context Window, MCP" required>',
      '    </div>',
      '    <div class="tre-form-group">',
      '      <label for="js-c-def">Kısa ve Yalın Türkçe Tanım:</label>',
      '      <textarea id="js-c-def" class="input" rows="3" placeholder="Teknik jargona boğmadan, 1-2 cümleyle açıklayın..."></textarea>',
      '    </div>',
      '    <div class="tre-form-group">',
      '      <label for="js-c-analogy">Günlük Hayattan Analoji / Benzetme (İsteğe Bağlı):</label>',
      '      <textarea id="js-c-analogy" class="input" rows="2" placeholder="Kavramın kolay anlaşılması için zihinde canlanan bir benzetme..."></textarea>',
      '    </div>',
      '  </div>',
      '  <div class="tre-modal-foot">',
      '    <button type="button" class="btn btn-ghost" id="js-modal-cancel">Vazgeç</button>',
      '    <button type="button" class="btn btn-primary" id="js-modal-submit">GitHub\'da Gönder ↗</button>',
      '  </div>',
      '</div>'
    ].join('\n');

    document.body.appendChild(modal);

    var closeBtn = modal.querySelector('#js-modal-close');
    var cancelBtn = modal.querySelector('#js-modal-cancel');
    var submitBtn = modal.querySelector('#js-modal-submit');
    var nameInput = modal.querySelector('#js-c-name');
    var defInput = modal.querySelector('#js-c-def');
    var analogyInput = modal.querySelector('#js-c-analogy');

    function closeModal() {
      modal.remove();
    }

    closeBtn.addEventListener('click', closeModal);
    cancelBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function (e) {
      if (e.target === modal) closeModal();
    });

    submitBtn.addEventListener('click', function () {
      var name = nameInput.value.trim();
      var def = defInput.value.trim();
      var analogy = analogyInput.value.trim();

      if (!name) {
        nameInput.focus();
        return;
      }

      var issueTitle = encodeURIComponent('📖 Terim Önerisi: ' + name);
      var issueBodyText = [
        '### Terim Adı',
        name,
        '',
        '### Türkçe Tanım',
        def || '*(Topluluk incelemesinde tamamlanacak)*',
        '',
        '### Analoji / Benzetme',
        analogy || '*(Belirtilmedi)*',
        '',
        '---',
        '*Bu öneri TreScout web katkı sihirbazı üzerinden oluşturuldu.*'
      ].join('\n');

      var issueUrl = 'https://github.com/' + GITHUB_REPO + '/issues/new?title=' + issueTitle +
                     '&body=' + encodeURIComponent(issueBodyText) +
                     '&labels=community-term,sozluk';

      window.open(issueUrl, '_blank', 'noopener,noreferrer');
      closeModal();
    });
  }

  function init() {
    var targets = document.querySelectorAll('.tre-contribute-hook');
    targets.forEach(createContributeButton);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
