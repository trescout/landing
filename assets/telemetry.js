/**
 * TreScout · Privacy-First Telemetry & Ürün Keşif Takibi (PR B)
 * =============================================================
 * KVKK / GDPR uyumlu, çerezsiz (cookieless), sıfır-PII telemetri kütüphanesi.
 * Hiçbir kişisel veri (e-posta, isim, IP, hassas parametre) event payload'ına girmez.
 *
 * Temel Event'ler:
 *   - discovery_view: Keşif sayfası/aracı görüntülendiğinde
 *   - report_preview_open: Rapor sayfası / önizlemesi açıldığında
 *   - early_access_start: Form alanına ilk kez odaklanılıp yazılmaya başlandığında
 *   - early_access_submit: Başarılı erken erişim form gönderiminde
 *   - beta_report_open: PDF veya tam rapor açıldığında
 *   - beta_return_week_2: 7-14+ gün sonra geri dönen aktif okuyucu
 */

(function () {
  'use strict';

  var STORAGE_KEY_FIRST_SEEN = 'ts_first_seen';
  var STORAGE_KEY_RETENTION_FIRED = 'ts_retention_w2';

  /** URL'deki UTM parametrelerini güvenle ayrıştırır (PII temizlenmiş) */
  function getUtmParams() {
    var params = {};
    try {
      var searchParams = new URLSearchParams(window.location.search);
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(function (key) {
        var val = searchParams.get(key);
        if (val) {
          params[key] = val.slice(0, 64).replace(/[^\w\-_.]/g, '');
        }
      });
    } catch (e) {
      // sessiz fallback
    }
    return params;
  }

  /** Sayfanın bağlamsal metadata'sını çıkarır */
  function getPageContext() {
    var lang = (document.documentElement.lang || 'tr').split('-')[0];
    var path = window.location.pathname || '/';

    var pageType = 'home';
    var contentSlug = '';

    if (path.indexOf('/discover') !== -1) {
      pageType = 'discover';
      var matchDisc = path.match(/discover\/([^/]+)/);
      if (matchDisc && matchDisc[1]) contentSlug = matchDisc[1];
    } else if (path.indexOf('/dictionary') !== -1) {
      pageType = 'dictionary';
      var matchDict = path.match(/dictionary\/([^/]+)/);
      if (matchDict && matchDict[1]) contentSlug = matchDict[1];
    } else if (path.indexOf('/reports') !== -1) {
      pageType = 'report';
      var matchRep = path.match(/reports\/(?:tekrarsiz\/|fresh\/)?(\d{4}-\d{2}-\d{2})/);
      if (matchRep && matchRep[1]) contentSlug = matchRep[1];
    } else if (path.indexOf('/compare') !== -1) {
      pageType = 'compare';
    }

    return {
      locale: lang,
      pageType: pageType,
      contentSlug: contentSlug,
      path: path.slice(0, 120)
    };
  }

  /**
   * Ana event dispatch fonksiyonu.
   * Vercel Analytics / Custom Event Bus ile uyumludur.
   */
  function track(eventName, customPayload) {
    if (!eventName) return;

    var ctx = getPageContext();
    var utm = getUtmParams();

    var payload = {
      event: String(eventName).slice(0, 32),
      locale: ctx.locale,
      pageType: (customPayload && customPayload.pageType) || ctx.pageType,
      contentSlug: (customPayload && customPayload.contentSlug) || ctx.contentSlug,
      placement: (customPayload && customPayload.placement) || 'default',
      path: ctx.path,
      ts: Date.now()
    };

    // UTM'leri ekle
    Object.keys(utm).forEach(function (k) {
      payload[k] = utm[k];
    });

    if (customPayload) {
      Object.keys(customPayload).forEach(function (k) {
        if (['email', 'name', 'phone', 'address', 'password'].indexOf(k) === -1) {
          if (payload[k] === undefined) {
            payload[k] = String(customPayload[k]).slice(0, 64);
          }
        }
      });
    }

    // Custom DOM Event tetikle (dinleyiciler için)
    try {
      var ev = new CustomEvent('trescout:telemetry', { detail: payload });
      window.dispatchEvent(ev);
    } catch (e) {
      // IE fallback
    }

    // Vercel Web Analytics custom event varsa ilet
    if (typeof window.va === 'function') {
      try {
        window.va('event', { name: eventName, data: payload });
      } catch (e) {}
    }

    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('[TreScout Telemetry]', eventName, payload);
    }
  }

  /** 2. Hafta Geri Dönüş (Week-2 Retention) Kontrolü */
  function checkRetention() {
    try {
      var now = Date.now();
      var firstSeen = localStorage.getItem(STORAGE_KEY_FIRST_SEEN);

      if (!firstSeen) {
        localStorage.setItem(STORAGE_KEY_FIRST_SEEN, String(now));
        return;
      }

      var diffDays = (now - parseInt(firstSeen, 10)) / (1000 * 60 * 60 * 24);
      var alreadyFired = localStorage.getItem(STORAGE_KEY_RETENTION_FIRED);

      if (diffDays >= 7 && diffDays <= 30 && !alreadyFired) {
        track('beta_return_week_2', { daysSinceFirstSeen: Math.round(diffDays) });
        localStorage.setItem(STORAGE_KEY_RETENTION_FIRED, 'true');
      }
    } catch (e) {
      // LocalStorage kapalı veya kısıtlı olabilir
    }
  }

  /** Sayfa bazlı otomatik event'leri bağlar */
  function initAutoEvents() {
    var ctx = getPageContext();

    if (ctx.pageType === 'discover' && ctx.contentSlug) {
      track('discovery_view', { placement: 'detail' });
    } else if (ctx.pageType === 'report' && ctx.contentSlug) {
      track('report_preview_open', { placement: 'detail' });
    }

    // Form başlangıç dinleyicisi (early_access_start)
    var forms = document.querySelectorAll('.js-subscribe');
    forms.forEach(function (form) {
      var input = form.querySelector('input[type="email"]');
      if (input) {
        var started = false;
        input.addEventListener('focus', function () {
          if (!started) {
            started = true;
            track('early_access_start', {
              pageType: form.getAttribute('data-page-type') || ctx.pageType,
              contentSlug: form.getAttribute('data-content-slug') || ctx.contentSlug,
              placement: form.getAttribute('data-cta-placement') || form.getAttribute('data-source') || 'form'
            });
          }
        }, { once: true });
      }
    });

    // PDF / Rapor link tıklamaları (beta_report_open)
    var pdfLinks = document.querySelectorAll('a[href$=".pdf"], a.act-pdf, a.act-read');
    pdfLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        track('beta_report_open', {
          href: link.getAttribute('href') || '',
          placement: 'report_action'
        });
      });
    });
  }

  // Global API erişimi
  window.TreScoutTelemetry = {
    track: track,
    getPageContext: getPageContext,
    getUtmParams: getUtmParams
  };

  // Başlat
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      checkRetention();
      initAutoEvents();
    });
  } else {
    checkRetention();
    initAutoEvents();
  }
})();
