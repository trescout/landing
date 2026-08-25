/* TreScout · paylaşılan abone formu · /api/subscribe → Resend
 * index.html dışındaki sayfalarda (.js-subscribe formları) kullanılır.
 * İkincil formlar sade consent checkbox + yeni-sekme Aydınlatma Metni linki kullanır
 * (anasayfa hero'sundaki scroll-gate modal'a ihtiyaç yok). CSP-temiz, harici. */
(function () {
  var ENDPOINT = '/api/subscribe';

  /* Sayfanın dili · /en/ altındaki sayfalarda İngilizce metin.
     NOT: aynı sözlük assets/index.js içinde de var (anasayfa formu ayrı akış
     kullanıyor · scroll-gate modal). Birini değiştirirken diğerine bakın. */
  var SAYFA_DILI = document.documentElement.lang || 'tr';
  var METIN = {
    en: {
    zaten: '<strong>You are already on the list.</strong> We will let you know when we go live.',
    aldik: '<strong>Got it.</strong> We will let you know when we go live. Have a good week.',
    onay: 'Please accept the privacy notice to continue.',
    gonderiliyor: 'Sending...',
    genel: 'Something went wrong. Please try again.',
    baglanti: 'Connection error. Please try again.'
    },
    fr: {
      zaten: '<strong>Vous êtes déjà sur la liste.</strong> Nous vous préviendrons au lancement.',
      aldik: '<strong>C\'est noté.</strong> Nous vous préviendrons au lancement. Bonne semaine.',
      onay: 'Veuillez accepter la notice de confidentialité pour continuer.',
      gonderiliyor: 'Envoi...',
      genel: 'Une erreur est survenue. Veuillez réessayer.',
      baglanti: 'Erreur de connexion. Veuillez réessayer.'
    },
    pt: {
      zaten: '<strong>Você já está na lista.</strong> Avisaremos quando entrarmos no ar.',
      aldik: '<strong>Anotado.</strong> Avisaremos quando entrarmos no ar. Boa semana.',
      onay: 'Aceite o aviso de privacidade para continuar.',
      gonderiliyor: 'Enviando...',
      genel: 'Algo deu errado. Tente novamente.',
      baglanti: 'Erro de conexão. Tente novamente.'
    },
    es: {
      zaten: '<strong>Ya está en la lista.</strong> Le avisaremos cuando estemos en marcha.',
      aldik: '<strong>Anotado.</strong> Le avisaremos cuando estemos en marcha. Buena semana.',
      onay: 'Acepte el aviso de privacidad para continuar.',
      gonderiliyor: 'Enviando...',
      genel: 'Algo ha fallado. Inténtelo de nuevo.',
      baglanti: 'Error de conexión. Inténtelo de nuevo.'
    },
    de: {
      zaten: '<strong>Sie stehen bereits auf der Liste.</strong> Wir melden uns, sobald wir starten.',
      aldik: '<strong>Notiert.</strong> Wir melden uns, sobald wir starten. Eine gute Woche.',
      onay: 'Stimmen Sie dem Datenschutzhinweis zu, um fortzufahren.',
      gonderiliyor: 'Wird gesendet...',
      genel: 'Etwas ist schiefgelaufen. Bitte versuchen Sie es erneut.',
      baglanti: 'Verbindungsfehler. Bitte versuchen Sie es erneut.'
    },
    tr: {
      zaten: '<strong>Zaten listemizdesiniz.</strong> Yayında olduğumuzda size haber vereceğiz.',
    aldik: '<strong>Aldık.</strong> Yayında olduğumuzda size haber vereceğiz. İyi haftalar.',
    onay: 'Devam etmek için Aydınlatma Metni onayı gerekli.',
    gonderiliyor: 'Gönderiliyor...',
    genel: 'Bir şeyler ters gitti. Lütfen tekrar deneyin.',
      baglanti: 'Bağlantı hatası. Lütfen tekrar deneyin.'
    }
  };
  /* Sayfanın dili · <html lang> bölge kodu taşıyabiliyor ("pt-BR"). Sözlük
     anahtarı hem tam kodu hem ana dili kabul etsin · yoksa Portekizce sayfa
     sessizce TÜRKÇE metinlere düşüyordu ve aydınlatma modal'ı Türkçe metni
     açıyordu (2026-08-14). */
  function _dilSec(tablo) {
    var l = (document.documentElement.lang || 'tr');
    return tablo[l] || tablo[l.split('-')[0]] || tablo.tr;
  }
  var T = _dilSec(METIN);


  function showSuccess(form, isDuplicate) {
    var msg = isDuplicate
      ? T.zaten
      : T.aldik;
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
        showError(form, T.onay);
        consent.focus();
        return;
      }

      var originalText = button.textContent;
      button.disabled = true;
      button.textContent = T.gonderiliyor;

      try {
        var honeypot = form.querySelector('input[name="website"]');
        var pageType = form.dataset.pageType || '';
        var contentSlug = form.dataset.contentSlug || '';
        var placement = form.dataset.ctaPlacement || form.dataset.source || 'default';

        var res = await fetch(ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: email,
            source: form.dataset.source || 'unknown',
            pageType: pageType,
            contentSlug: contentSlug,
            placement: placement,
            // Sayfa yolu · data-source tüm sözlük sayfalarında aynı ("dictionary-en"),
            // hangi girdinin kişiyi getirdiğini ancak bu satır gösteriyor.
            path: location.pathname,
            consent: true,
            website: honeypot ? honeypot.value : ''
          })
        });
        var data = await res.json().catch(function () { return {}; });

        if (res.ok && data.ok) {
          if (window.TreScoutTelemetry && typeof window.TreScoutTelemetry.track === 'function') {
            window.TreScoutTelemetry.track('early_access_submit', {
              pageType: pageType,
              contentSlug: contentSlug,
              placement: placement,
              isDuplicate: data.duplicate === true
            });
          }
          showSuccess(form, data.duplicate === true);
        } else {
          button.disabled = false;
          button.textContent = originalText;
          showError(form, data.error || T.genel);
        }
      } catch (err) {
        button.disabled = false;
        button.textContent = originalText;
        showError(form, T.baglanti);
      }
    });
  }

  document.querySelectorAll('form.js-subscribe').forEach(bind);
})();
