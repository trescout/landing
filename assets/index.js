/* ──────────────────
 * TreScout · index.html davranış JS'i
 * Önceden inline <script> bloklarıydı · CSP script-src 'unsafe-inline'
 * kaldırılabilsin diye harici alındı. <script src defer> ile yüklenir.
 * Tüm bloklar bağımsız IIFE · sıra önemli değil, kaynak sırası korundu.
 * ────────────────── */


/* ---------- arşiv rozeti · sitemap fetch → CANLI · N rapor ---------- */
(function(){fetch('/sitemap.xml').then(function(r){return r.text();}).then(function(t){var n=(t.match(/\/reports\/\d{4}-\d{2}-\d{2}\//g)||[]).length;var el=document.getElementById('js-arch-badge');if(n>0&&el)el.textContent='CANLI · '+n+' rapor';}).catch(function(){});})();


/* ---------- dil · tüm bölümler paylaşıyor ----------
   Form metinleri, modal durum yazısı ve aydınlatma metni yolu sayfanın
   diline göre seçilir. Dosya kapsamında duruyor: önce form IIFE'sinin
   içindeydi ve modal bölümü `T is not defined` ile kırıldı (2026-08-07). */
  var SAYFA_DILI = document.documentElement.lang || 'tr';
  var METIN = {
    en: {
    zaten: '<strong>You are already on the list.</strong> We will let you know when we go live.',
    aldik: '<strong>Got it.</strong> We will let you know when we go live. Have a good week.',
    onay: 'Please accept the privacy notice to continue.',
    gonderiliyor: 'Sending...',
    genel: 'Something went wrong. Please try again.',
    baglanti: 'Connection error. Please try again.',
    metinYolu: '/en/privacy.html',
    onayaDokun: 'Tap the button below to give consent'
    },
    fr: {
      zaten: '<strong>Vous êtes déjà sur la liste.</strong> Nous vous préviendrons au lancement.',
      aldik: '<strong>C\'est noté.</strong> Nous vous préviendrons au lancement. Bonne semaine.',
      onay: 'Veuillez accepter la notice de confidentialité pour continuer.',
      gonderiliyor: 'Envoi...',
      genel: 'Une erreur est survenue. Veuillez réessayer.',
      baglanti: 'Erreur de connexion. Veuillez réessayer.',
      metinYolu: '/fr/privacy.html',
      onayaDokun: 'Touchez le bouton ci-dessous pour donner votre consentement'
    },
    pt: {
      zaten: '<strong>Você já está na lista.</strong> Avisaremos quando entrarmos no ar.',
      aldik: '<strong>Anotado.</strong> Avisaremos quando entrarmos no ar. Boa semana.',
      onay: 'Aceite o aviso de privacidade para continuar.',
      gonderiliyor: 'Enviando...',
      genel: 'Algo deu errado. Tente novamente.',
      baglanti: 'Erro de conexão. Tente novamente.',
      metinYolu: '/pt/privacy.html',
      onayaDokun: 'Toque no botão abaixo para dar o seu consentimento'
    },
    es: {
      zaten: '<strong>Ya está en la lista.</strong> Le avisaremos cuando estemos en marcha.',
      aldik: '<strong>Anotado.</strong> Le avisaremos cuando estemos en marcha. Buena semana.',
      onay: 'Acepte el aviso de privacidad para continuar.',
      gonderiliyor: 'Enviando...',
      genel: 'Algo ha fallado. Inténtelo de nuevo.',
      baglanti: 'Error de conexión. Inténtelo de nuevo.',
      metinYolu: '/es/privacy.html',
      onayaDokun: 'Toque el botón de abajo para dar su consentimiento'
    },
    de: {
      zaten: '<strong>Sie stehen bereits auf der Liste.</strong> Wir melden uns, sobald wir starten.',
      aldik: '<strong>Notiert.</strong> Wir melden uns, sobald wir starten. Eine gute Woche.',
      onay: 'Stimmen Sie dem Datenschutzhinweis zu, um fortzufahren.',
      gonderiliyor: 'Wird gesendet...',
      genel: 'Etwas ist schiefgelaufen. Bitte versuchen Sie es erneut.',
      baglanti: 'Verbindungsfehler. Bitte versuchen Sie es erneut.',
      metinYolu: '/de/privacy.html',
      onayaDokun: 'Tippen Sie unten auf die Schaltfläche, um zuzustimmen'
    },
    tr: {
      zaten: '<strong>Zaten listemizdesiniz.</strong> Yayında olduğumuzda size haber vereceğiz.',
    aldik: '<strong>Aldık.</strong> Yayında olduğumuzda size haber vereceğiz. İyi haftalar.',
    onay: 'Devam etmek için Aydınlatma Metni onayı gerekli.',
    gonderiliyor: 'Gönderiliyor...',
    genel: 'Bir şeyler ters gitti. Lütfen tekrar deneyin.',
      baglanti: 'Bağlantı hatası. Lütfen tekrar deneyin.',
      metinYolu: '/privacy.html',
      onayaDokun: 'Aşağıdaki butona dokunarak onaylayın'
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


/* ---------- abone formu · /api/subscribe ---------- */
    (function () {
      var ENDPOINT = '/api/subscribe';

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
  


/* ---------- nav scroll state ---------- */
    (function () {
      var nav = document.querySelector('nav');
      if (!nav) return;
      var ticking = false;
      function update() {
        nav.classList.toggle('scrolled', window.scrollY > 8);
        ticking = false;
      }
      window.addEventListener('scroll', function () {
        if (!ticking) { requestAnimationFrame(update); ticking = true; }
      }, { passive: true });
      update();
    })();
  


/* ---------- aydınlatma metni modal · scroll-to-bottom gate ---------- */
    (function () {
      var modal = document.getElementById('privacy-modal');
      if (!modal) return;

      var iframe = modal.querySelector('.privacy-modal-iframe');
      var closeX = modal.querySelector('.privacy-modal-x');
      var confirmBtn = modal.querySelector('.privacy-modal-confirm');
      var statusEl = modal.querySelector('.privacy-modal-status');
      var statusText = modal.querySelector('.privacy-modal-status-text');
      var links = document.querySelectorAll('a[data-privacy-modal]');
      var hasRead = false;
      var activeCheckbox = null;
      var activeHint = null;
      var lastFocus = null;

      function setRead() {
        if (hasRead) return;
        hasRead = true;
        // "Okundu" iddiası YOK · sadece butonu enable et · kullanıcı eksplisit onay verecek
        confirmBtn.disabled = false;
        statusEl.classList.add('read');
        statusText.textContent = T.onayaDokun;
      }

      function openModal(checkbox, hint) {
        // Guard · zaten açıksa tekrar çalışma (double-fire koruması)
        if (modal.getAttribute('aria-hidden') === 'false') return;
        activeCheckbox = checkbox || null;
        activeHint = hint || null;
        hasRead = false;
        confirmBtn.disabled = true;
        statusEl.classList.remove('read');
        statusText.textContent = '';
        lastFocus = document.activeElement;
        // Iframe'i her açılışta yeniden yükle → scroll tepesinden başlasın
        // Sayfanın dilindeki metin · İngilizce ziyaretçi Türkçe KVKK metnini okumak
        // zorunda kalmasın (2026-08-07).
        iframe.src = T.metinYolu + '?embed=1&t=' + Date.now();
        modal.setAttribute('aria-hidden', 'false');
        // BODY SCROLL LOCK KASTEN YOK · modal zaten position:fixed inset:0
        // ile viewport'u tam kaplıyor; pointer-events:auto ile body
        // dokunulamaz. iOS Safari'de body position:fixed pattern viewport
        // bozuyordu (address bar dinamiği), o yüzden kaldırıldı.
        setTimeout(function () { closeX.focus(); }, 60);
      }

      function closeModal() {
        modal.setAttribute('aria-hidden', 'true');
        // Eski state'ler (önceki version'lardan kalmış olabilir) defensive cleanup
        ['position', 'top', 'left', 'right', 'width', 'overflow'].forEach(function (p) {
          document.body.style.removeProperty(p);
        });
        document.documentElement.style.removeProperty('overflow');
        document.body.classList.remove('modal-open');
        document.documentElement.classList.remove('modal-open');
        activeCheckbox = null;
        activeHint = null;
        if (lastFocus && typeof lastFocus.focus === 'function') {
          lastFocus.focus();
        }
      }

      // Iframe'den "okundu" mesajını dinle
      window.addEventListener('message', function (e) {
        if (e.data && e.data.type === 'trescout-privacy-read') {
          setRead();
        }
      });

      // Form içindeki Aydınlatma Metni link'leri modal açar
      links.forEach(function (link) {
        link.addEventListener('click', function (e) {
          e.preventDefault();
          var form = link.closest('form');
          var checkbox = form ? form.querySelector('input[name="consent"]') : null;
          var hint = form ? form.querySelector('.form-consent-hint') : null;
          openModal(checkbox, hint);
        });
      });

      closeX.addEventListener('click', closeModal);
      confirmBtn.addEventListener('click', function () {
        // "Okudum, onaylıyorum" · eksplisit onay · checkbox aktif + işaretli + hint gizle
        if (hasRead && activeCheckbox) {
          activeCheckbox.removeAttribute('data-needs-consent');
          activeCheckbox.checked = true;
          if (activeHint) activeHint.style.display = 'none';
        }
        closeModal();
      });

      // Backdrop click
      modal.addEventListener('click', function (e) {
        if (e.target === modal) closeModal();
      });

      // ESC ile kapat
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal.getAttribute('aria-hidden') === 'false') {
          closeModal();
        }
      });

      // Consent gerektiren durumda: her formun kendi label'ı → aynı formun modal'ı
      // Böylece hero ve final CTA arasında ilk checkbox'a yanlışlıkla yazılmaz.
      document.querySelectorAll('input[name="consent"]').forEach(function (checkbox) {
        var consentLabel = checkbox.closest('.form-consent');
        var hint = consentLabel ? consentLabel.querySelector('.form-consent-hint') : null;
        if (!consentLabel) return;

        consentLabel.addEventListener('click', function (e) {
          if (!checkbox.hasAttribute('data-needs-consent')) return;
          // Aydınlatma Metni link'i kendi handler'ında açıyor · skip
          if (e.target.closest('a[data-privacy-modal]')) return;
          e.preventDefault();
          if (hint) {
            hint.classList.remove('shake');
            void hint.offsetWidth;
            hint.classList.add('shake');
            setTimeout(function () { hint.classList.remove('shake'); }, 700);
          }
          openModal(checkbox, hint);
        });
      });

      // Defensive cleanup · sayfa görünür olduğunda stuck scroll lock'u temizle
      // (Modal açıkken tab değişip dönüldüğünde body fixed kalmış olabilir)
      document.addEventListener('visibilitychange', function () {
        if (document.visibilityState === 'visible' &&
            modal.getAttribute('aria-hidden') === 'true' &&
            document.body.style.position === 'fixed') {
          // Modal kapalı ama body hala fixed · stuck state · temizle
          ['position', 'top', 'left', 'right', 'width', 'overflow'].forEach(function (p) {
            document.body.style.removeProperty(p);
          });
          document.documentElement.style.removeProperty('overflow');
          document.body.classList.remove('modal-open');
          document.documentElement.classList.remove('modal-open');
        }
      });

      // Pageshow event'i de aynı cleanup (back-forward cache)
      window.addEventListener('pageshow', function (e) {
        if (e.persisted && document.body.style.position === 'fixed') {
          ['position', 'top', 'left', 'right', 'width', 'overflow'].forEach(function (p) {
            document.body.style.removeProperty(p);
          });
          document.documentElement.style.removeProperty('overflow');
          document.body.classList.remove('modal-open');
          document.documentElement.classList.remove('modal-open');
        }
      });
    })();
  


/* ---------- tabs · ARIA tablist + klavye ---------- */
    (function () {
      var tablists = document.querySelectorAll('[role="tablist"]');
      if (!tablists.length) return;

      tablists.forEach(function (tablist) {
        var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
        if (!tabs.length) return;

        function activate(tab, setFocus) {
          tabs.forEach(function (t) {
            var selected = t === tab;
            t.setAttribute('aria-selected', selected ? 'true' : 'false');
            t.setAttribute('tabindex', selected ? '0' : '-1');
            var panelId = t.getAttribute('aria-controls');
            var panel = panelId ? document.getElementById(panelId) : null;
            if (panel) {
              if (selected) panel.removeAttribute('hidden');
              else panel.setAttribute('hidden', '');
            }
          });
          if (setFocus) tab.focus();
        }

        tabs.forEach(function (tab, idx) {
          tab.addEventListener('click', function () { activate(tab, false); });
          tab.addEventListener('keydown', function (e) {
            var nextIdx = null;
            switch (e.key) {
              case 'ArrowRight': nextIdx = (idx + 1) % tabs.length; break;
              case 'ArrowLeft':  nextIdx = (idx - 1 + tabs.length) % tabs.length; break;
              case 'Home':       nextIdx = 0; break;
              case 'End':        nextIdx = tabs.length - 1; break;
              default: return;
            }
            e.preventDefault();
            activate(tabs[nextIdx], true);
          });
        });
      });
    })();
  


/* ---------- scroll reveal · IntersectionObserver ---------- */
    (function () {
      if (!('IntersectionObserver' in window)) {
        document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
        return;
      }
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
      document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
    })();
  
