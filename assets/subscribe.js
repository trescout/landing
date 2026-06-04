/* TreScout · paylaşılan abone formu · /api/subscribe → Resend
 * index.html dışındaki sayfalarda (.js-subscribe formları) kullanılır.
 * İkincil formlar sade consent checkbox + yeni-sekme Aydınlatma Metni linki kullanır
 * (anasayfa hero'sundaki scroll-gate modal'a ihtiyaç yok). CSP-temiz, harici. */
(function () {
  var ENDPOINT = '/api/subscribe';

  function showSuccess(form, isDuplicate) {
    var msg = isDuplicate
      ? '<strong>Zaten listemizdesiniz.</strong> Yayında olduğumuzda size haber vereceğiz.'
      : '<strong>Aldık.</strong> Yayında olduğumuzda size haber vereceğiz. İyi haftalar.';
    var div = document.createElement('div');
    div.className = 'form-success';
    div.setAttribute('role', 'status');
    div.setAttribute('aria-live', 'polite');
    div.innerHTML = msg;
    form.replaceWith(div);
  }

  function showError(form, message) {
    var existing = form.parentElement.querySelector('.form-error');
    if (existing) existing.remove();
    var div = document.createElement('div');
    div.className = 'form-error';
    div.setAttribute('role', 'alert');
    div.textContent = message;
    form.insertAdjacentElement('afterend', div);
    setTimeout(function () { div.remove(); }, 6000);
  }

  function bind(form) {
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      var input = form.querySelector('input[type="email"]');
      var button = form.querySelector('button[type="submit"]');
      if (!input || !button) return;

      var email = input.value.trim();
      if (!email || !input.checkValidity()) {
        input.reportValidity();
        return;
      }
      var consent = form.querySelector('input[name="consent"]');
      if (consent && !consent.checked) {
        showError(form, 'Devam etmek için Aydınlatma Metni onayı gerekli.');
        consent.focus();
        return;
      }

      var originalText = button.textContent;
      button.disabled = true;
      button.textContent = 'Gönderiliyor...';

      try {
        var honeypot = form.querySelector('input[name="website"]');
        var res = await fetch(ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: email,
            source: form.dataset.source || 'unknown',
            consent: true,
            website: honeypot ? honeypot.value : ''
          })
        });
        var data = await res.json().catch(function () { return {}; });

        if (res.ok && data.ok) {
          showSuccess(form, data.duplicate === true);
        } else {
          button.disabled = false;
          button.textContent = originalText;
          showError(form, data.error || 'Bir şeyler ters gitti. Lütfen tekrar deneyin.');
        }
      } catch (err) {
        button.disabled = false;
        button.textContent = originalText;
        showError(form, 'Bağlantı hatası. Lütfen tekrar deneyin.');
      }
    });
  }

  document.querySelectorAll('form.js-subscribe').forEach(bind);
})();
