/**
 * TreScout · Privacy-First Telemetry & Ürün Keşif Takibi
 * =======================================================
 * Çerezsiz, sıfır-PII telemetri. Kullanıcı açıkça izin vermeden hiçbir
 * event gönderilmez ve localStorage'a retention durumu yazılmaz.
 *
 * Consent değerleri:
 *   - unknown: varsayılan · event yok, localStorage yok
 *   - granted: anonim ürün ölçümü açık
 *   - denied: anonim ürün ölçümü kapalı
 *
 * Event'ler provider hazır değilse kısa ömürlü memory queue'da tutulur.
 * Provider hiç hazır olmazsa queue gönderilmez ve sayfa kapanınca yok olur.
 */
(function () {
  'use strict';

  var STORAGE_KEY_CONSENT = 'ts_telemetry_consent';
  var STORAGE_KEY_FIRST_SEEN = 'ts_first_seen';
  var STORAGE_KEY_RETENTION_FIRED = 'ts_retention_w2';
  var MAX_QUEUE = 40;
  var PROVIDER_POLL_MS = 250;
  var PROVIDER_MAX_WAIT_MS = 10000;
  var SAFE_CUSTOM_KEYS = {
    pageType: true,
    contentSlug: true,
    placement: true,
    isDuplicate: true,
    daysSinceFirstSeen: true
  };

  var pendingEvents = [];
  var providerPollStartedAt = 0;
  var providerPollTimer = null;

  function storageGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }

  function storageSet(key, value) {
    try { window.localStorage.setItem(key, value); } catch (e) {}
  }

  function storageRemove(key) {
    try { window.localStorage.removeItem(key); } catch (e) {}
  }

  function getConsent() {
    var value = storageGet(STORAGE_KEY_CONSENT);
    return value === 'granted' || value === 'denied' ? value : 'unknown';
  }

  function isGranted() {
    return getConsent() === 'granted';
  }

  function clearTrackingState() {
    storageRemove(STORAGE_KEY_FIRST_SEEN);
    storageRemove(STORAGE_KEY_RETENTION_FIRED);
    pendingEvents = [];
    if (providerPollTimer) {
      clearTimeout(providerPollTimer);
      providerPollTimer = null;
    }
    providerPollStartedAt = 0;
  }

  function providerReady() {
    return typeof window.va === 'function';
  }

  function sendToProvider(item) {
    if (!providerReady()) return false;
    try {
      window.va('event', { name: item.name, data: item.payload });
      return true;
    } catch (e) {
      return false;
    }
  }

  function finalizeDelivery(item) {
    if (item && item.commitKey) storageSet(item.commitKey, 'true');
  }

  function flush() {
    if (!isGranted()) {
      clearTrackingState();
      return;
    }
    if (!pendingEvents.length) {
      providerPollStartedAt = 0;
      return;
    }
    if (!providerReady()) {
      scheduleProviderPoll();
      return;
    }
    while (pendingEvents.length) {
      var item = pendingEvents[0];
      if (!sendToProvider(item)) return;
      pendingEvents.shift();
      finalizeDelivery(item);
    }
    providerPollStartedAt = 0;
  }

  function scheduleProviderPoll() {
    if (providerPollTimer || !pendingEvents.length || !isGranted()) return;
    if (!providerPollStartedAt) providerPollStartedAt = Date.now();
    if (Date.now() - providerPollStartedAt >= PROVIDER_MAX_WAIT_MS) {
      pendingEvents = [];
      providerPollStartedAt = 0;
      return;
    }
    providerPollTimer = setTimeout(function () {
      providerPollTimer = null;
      flush();
    }, PROVIDER_POLL_MS);
  }

  function setConsent(value) {
    var next = value === 'granted' || value === 'denied' ? value : 'unknown';
    if (next === 'granted') {
      storageSet(STORAGE_KEY_CONSENT, next);
      providerPollStartedAt = 0;
      ensureFirstSeen();
      flush();
    } else {
      if (next === 'denied') storageSet(STORAGE_KEY_CONSENT, next);
      else storageRemove(STORAGE_KEY_CONSENT);
      clearTrackingState();
    }
    return next;
  }

  function safeToken(value, maxLength) {
    if (value === undefined || value === null) return '';
    return String(value).slice(0, maxLength).replace(/[^\w-]/g, '');
  }

  function safeCampaignValue(value) {
    if (value === undefined || value === null) return '';
    var normalized = String(value).trim().toLowerCase();
    // Campaign values are intentionally restricted to short identifier tokens.
    // This drops emails, URLs, UUIDs, long opaque identifiers and free text.
    if (!/^[a-z0-9][a-z0-9_.-]{0,63}$/.test(normalized)) return '';
    if (/^[0-9a-f]{16,}$/.test(normalized)) return '';
    if (/^[0-9a-f]{8}-[0-9a-f-]{13,}$/.test(normalized)) return '';
    return normalized;
  }

  function safePath(value) {
    try {
      var url = new URL(String(value || '/'), window.location.origin);
      if (url.origin !== window.location.origin) return '';
      return (url.pathname || '/').slice(0, 120);
    } catch (e) {
      return '/';
    }
  }

  /** URL'deki kampanya parametrelerini kısıtlı token sözleşmesiyle ayrıştırır. */
  function getUtmParams() {
    var params = {};
    try {
      var searchParams = new URLSearchParams(window.location.search || '');
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(function (key) {
        var val = safeCampaignValue(searchParams.get(key));
        if (val) params[key] = val;
      });
    } catch (e) {}
    return params;
  }

  /** Sayfanın bağlamsal metadata'sını çıkarır */
  function getPageContext() {
    var lang = (document.documentElement.lang || 'tr').split('-')[0];
    var path = safePath(window.location.pathname || '/');
    var routePath = path.replace(/^\/(?:en|fr|pt|es|de)(?=\/|$)/, '');
    var pageType = 'home';
    var contentSlug = '';

    if (/^\/discover(?:\/|$)/.test(routePath)) {
      pageType = 'discover';
      var matchDisc = routePath.match(/^\/discover\/([^/]+)/);
      if (matchDisc && matchDisc[1]) contentSlug = safeToken(matchDisc[1], 64);
    } else if (/^\/dictionary(?:\/|$)/.test(routePath)) {
      pageType = 'dictionary';
      var matchDict = routePath.match(/^\/dictionary\/([^/]+)/);
      if (matchDict && matchDict[1]) contentSlug = safeToken(matchDict[1], 64);
    } else if (/^\/reports(?:\/|$)/.test(routePath)) {
      pageType = 'report';
      var matchRep = routePath.match(/^\/reports\/(?:tekrarsiz\/|fresh\/)?(\d{4}-\d{2}-\d{2})/);
      if (matchRep && matchRep[1]) contentSlug = matchRep[1];
    } else if (/^\/compare(?:\/|$)/.test(routePath)) {
      pageType = 'compare';
    }

    return {
      locale: safeToken(lang, 12) || 'tr',
      pageType: pageType,
      contentSlug: contentSlug,
      path: path
    };
  }

  function queueForProvider(item) {
    if (pendingEvents.length >= MAX_QUEUE) pendingEvents.shift();
    pendingEvents.push(item);
    scheduleProviderPoll();
  }

  /** Ana event dispatch fonksiyonu · consent olmadan no-op */
  function track(eventName, customPayload) {
    if (!eventName || !isGranted()) return false;

    var eventKey = safeToken(eventName, 32);
    if (!eventKey) return false;
    var ctx = getPageContext();
    var custom = customPayload || {};
    var pageType = safeToken(custom.pageType, 32) || ctx.pageType;
    var contentSlug = safeToken(custom.contentSlug, 64) || ctx.contentSlug;
    var placement = safeToken(custom.placement, 32) || 'default';
    var payload = {
      event: eventKey,
      locale: ctx.locale,
      pageType: pageType,
      contentSlug: contentSlug,
      placement: placement,
      path: safePath(ctx.path) || '/',
      ts: Date.now()
    };

    var utm = getUtmParams();
    Object.keys(utm).forEach(function (key) { payload[key] = utm[key]; });

    if (SAFE_CUSTOM_KEYS.isDuplicate && typeof custom.isDuplicate === 'boolean') {
      payload.isDuplicate = custom.isDuplicate;
    }
    if (SAFE_CUSTOM_KEYS.daysSinceFirstSeen && typeof custom.daysSinceFirstSeen === 'number' && isFinite(custom.daysSinceFirstSeen)) {
      payload.daysSinceFirstSeen = Math.max(0, Math.min(30, Math.round(custom.daysSinceFirstSeen)));
    }

    try {
      window.dispatchEvent(new CustomEvent('trescout:telemetry', { detail: payload }));
    } catch (e) {}

    var item = {
      name: eventKey,
      payload: payload,
      commitKey: eventKey === 'beta_return_week_2' ? STORAGE_KEY_RETENTION_FIRED : ''
    };
    if (sendToProvider(item)) {
      finalizeDelivery(item);
    } else {
      queueForProvider(item);
    }

    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('[TreScout Telemetry]', eventKey, payload);
    }
    return true;
  }

  function ensureFirstSeen() {
    if (!isGranted()) return;
    if (!storageGet(STORAGE_KEY_FIRST_SEEN)) storageSet(STORAGE_KEY_FIRST_SEEN, String(Date.now()));
  }

  /** 2. Hafta Geri Dönüş (Week-2 Retention) Kontrolü */
  function checkRetention() {
    if (!isGranted()) {
      clearTrackingState();
      return;
    }

    try {
      ensureFirstSeen();
      var now = Date.now();
      var firstSeen = storageGet(STORAGE_KEY_FIRST_SEEN);
      if (!firstSeen) return;

      var diffDays = (now - parseInt(firstSeen, 10)) / (1000 * 60 * 60 * 24);
      var alreadyFired = storageGet(STORAGE_KEY_RETENTION_FIRED);
      if (diffDays >= 7 && diffDays <= 30 && !alreadyFired) {
        // The fired flag is committed by finalizeDelivery, not merely when the
        // event enters the memory queue.
        track('beta_return_week_2', { daysSinceFirstSeen: diffDays });
      }
    } catch (e) {}
  }

  /** Sayfa bazlı otomatik event'leri bağlar */
  function initAutoEvents() {
    var ctx = getPageContext();

    if (ctx.pageType === 'discover' && ctx.contentSlug) {
      track('discovery_view', { placement: 'detail' });
    } else if (ctx.pageType === 'report' && ctx.contentSlug) {
      track('report_preview_open', { placement: 'detail' });
    }

    var forms = document.querySelectorAll('.js-subscribe');
    Array.prototype.forEach.call(forms, function (form) {
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

    var pdfLinks = document.querySelectorAll('a[href$=".pdf"], a.act-pdf, a.act-read');
    Array.prototype.forEach.call(pdfLinks, function (link) {
      link.addEventListener('click', function () {
        track('beta_report_open', {
          placement: 'report_action'
        });
      });
    });
  }

  function handleConsentStorageChange(event) {
    if (!event || event.key !== STORAGE_KEY_CONSENT) return;
    if (event.newValue === 'granted') {
      ensureFirstSeen();
      flush();
    } else {
      clearTrackingState();
    }
  }

  window.TreScoutTelemetry = {
    track: track,
    getConsent: getConsent,
    setConsent: setConsent,
    flush: flush,
    getPendingCount: function () { return pendingEvents.length; },
    getPageContext: getPageContext,
    getUtmParams: getUtmParams
  };

  if (typeof window.addEventListener === 'function') {
    window.addEventListener('storage', handleConsentStorageChange);
  }

  function init() {
    checkRetention();
    initAutoEvents();
    flush();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
