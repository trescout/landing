/* TreScout · privacy.js · iframe okuma sinyali + telemetry tercihi */
(function () {
  'use strict';

  var lang = (document.documentElement.lang || 'tr').split('-')[0];
  var COPY = {
    tr: {
      title: 'Anonim ürün ölçümü',
      text: 'İsteğe bağlı telemetry, e-posta veya isim toplamadan hangi sayfa türlerinin ve içerik bağlantılarının kullanıldığını anlamamıza yardımcı olur. Çerez kullanılmaz; tercihinizi istediğiniz zaman değiştirebilirsiniz.',
      label: 'Anonim ürün kullanımını ölçmeme izin ver',
      save: 'Tercihi kaydet',
      on: 'Anonim ürün ölçümü açık.',
      off: 'Anonim ürün ölçümü kapalı.'
    },
    en: {
      title: 'Anonymous product measurement',
      text: 'Optional telemetry helps us understand which page types and content links are useful without collecting email addresses or names. No tracking cookies are used; you can change this choice at any time.',
      label: 'Allow anonymous product usage measurement',
      save: 'Save preference',
      on: 'Anonymous product measurement is on.',
      off: 'Anonymous product measurement is off.'
    },
    fr: {
      title: 'Mesure anonyme du produit',
      text: 'La télémétrie facultative nous aide à comprendre quelles pages et quels liens de contenu sont utiles, sans collecter d’adresse e-mail ni de nom. Aucun cookie de suivi n’est utilisé ; vous pouvez modifier ce choix à tout moment.',
      label: 'Autoriser la mesure anonyme de l’utilisation du produit',
      save: 'Enregistrer le choix',
      on: 'La mesure anonyme est activée.',
      off: 'La mesure anonyme est désactivée.'
    },
    pt: {
      title: 'Medição anônima do produto',
      text: 'A telemetria opcional ajuda a entender quais tipos de página e links de conteúdo são úteis sem coletar e-mails ou nomes. Nenhum cookie de rastreamento é usado; você pode alterar essa escolha a qualquer momento.',
      label: 'Permitir medição anônima do uso do produto',
      save: 'Salvar preferência',
      on: 'A medição anônima está ativada.',
      off: 'A medição anônima está desativada.'
    },
    es: {
      title: 'Medición anónima del producto',
      text: 'La telemetría opcional nos ayuda a entender qué tipos de página y enlaces de contenido son útiles sin recopilar correos electrónicos ni nombres. No se usan cookies de seguimiento; puede cambiar esta elección en cualquier momento.',
      label: 'Permitir la medición anónima del uso del producto',
      save: 'Guardar preferencia',
      on: 'La medición anónima está activada.',
      off: 'La medición anónima está desactivada.'
    },
    de: {
      title: 'Anonyme Produktmessung',
      text: 'Optionale Telemetrie hilft uns zu verstehen, welche Seitentypen und Inhaltslinks nützlich sind, ohne E-Mail-Adressen oder Namen zu erfassen. Es werden keine Tracking-Cookies verwendet; Sie können diese Auswahl jederzeit ändern.',
      label: 'Anonyme Messung der Produktnutzung erlauben',
      save: 'Einstellung speichern',
      on: 'Die anonyme Messung ist aktiviert.',
      off: 'Die anonyme Messung ist deaktiviert.'
    }
  };
  var T = COPY[lang] || COPY.tr;

  function nearBottom() {
    var sh = document.documentElement.scrollHeight;
    var ch = document.documentElement.clientHeight;
    var st = window.scrollY || document.documentElement.scrollTop;
    return sh - st - ch < 80;
  }

  function notify() {
    try { window.parent.postMessage({ type: 'trescout-privacy-read' }, window.location.origin); } catch (e) {}
  }

  function initIframeGate() {
    window.addEventListener('scroll', function () {
      if (nearBottom()) notify();
    }, { passive: true });
    window.addEventListener('load', function () {
      if (nearBottom()) notify();
    });
  }

  function readConsent() {
    try { return window.localStorage.getItem('ts_telemetry_consent') === 'granted'; } catch (e) { return false; }
  }

  function writeConsent(value) {
    try {
      if (value) window.localStorage.setItem('ts_telemetry_consent', 'granted');
      else {
        window.localStorage.setItem('ts_telemetry_consent', 'denied');
        window.localStorage.removeItem('ts_first_seen');
        window.localStorage.removeItem('ts_retention_w2');
      }
      return true;
    } catch (e) { return false; }
  }

  function mountPreference() {
    var container = document.querySelector('.container');
    if (!container || document.querySelector('.privacy-telemetry-preference')) return;

    var section = document.createElement('section');
    section.className = 'privacy-telemetry-preference';
    section.setAttribute('aria-labelledby', 'telemetry-preference-title');
    section.innerHTML = '<h2 id="telemetry-preference-title"></h2>' +
      '<p class="privacy-telemetry-preference-text"></p>' +
      '<label class="privacy-telemetry-preference-label"><input type="checkbox"> <span></span></label>' +
      '<div class="privacy-telemetry-preference-actions"><button type="button"></button><span role="status" aria-live="polite"></span></div>';
    container.appendChild(section);

    var title = section.querySelector('h2');
    var text = section.querySelector('.privacy-telemetry-preference-text');
    var checkbox = section.querySelector('input[type="checkbox"]');
    var label = section.querySelector('.privacy-telemetry-preference-label span');
    var button = section.querySelector('button');
    var status = section.querySelector('[role="status"]');
    title.textContent = T.title;
    text.textContent = T.text;
    label.textContent = T.label;
    button.textContent = T.save;
    checkbox.checked = readConsent();

    button.addEventListener('click', function () {
      if (!writeConsent(checkbox.checked)) return;
      status.textContent = checkbox.checked ? T.on : T.off;
      window.setTimeout(function () { status.textContent = ''; }, 4000);
    });
  }

  if (window.parent === window) mountPreference();
  else initIframeGate();
})();
