/* TreScout · provider-consent.js
 *
 * Vercel Analytics ve Speed Insights provider scriptleri yalnızca kullanıcı
 * açıkça anonim ürün ölçümüne izin verdikten sonra etkinleştirilir. HTML’deki
 * provider URL’leri inert data-consent-src attribute’unda tutulur; tarayıcı
 * consent yokken bu scriptleri çalıştırmaz.
 */
(function () {
  'use strict';

  var CONSENT_KEY = 'ts_telemetry_consent';
  var PROVIDER_SELECTOR = 'script[data-consent-src]';
  var loaded = {};

  function readConsent() {
    try {
      return window.localStorage.getItem(CONSENT_KEY) === 'granted';
    } catch (error) {
      return false;
    }
  }

  function sameOriginProvider(src) {
    try {
      var url = new URL(src, window.location.origin);
      return url.origin === window.location.origin &&
        (url.pathname === '/_vercel/insights/script.js' ||
         url.pathname === '/_vercel/speed-insights/script.js');
    } catch (error) {
      return false;
    }
  }

  function loadProviders() {
    if (!readConsent()) return;

    var inertScripts = document.querySelectorAll(PROVIDER_SELECTOR);
    Array.prototype.forEach.call(inertScripts, function (inert) {
      var src = inert.getAttribute('data-consent-src');
      if (!src || !sameOriginProvider(src) || loaded[src]) return;
      loaded[src] = true;

      var script = document.createElement('script');
      script.src = src;
      script.defer = true;
      script.async = false;
      script.setAttribute('data-consent-provider', 'true');
      inert.parentNode.insertBefore(script, inert.nextSibling);
    });
  }

  function handleConsentChange(event) {
    if (event && event.key && event.key !== CONSENT_KEY) return;
    loadProviders();
  }

  window.TreScoutProviderConsent = {
    loadIfConsented: loadProviders
  };

  if (typeof window.addEventListener === 'function') {
    window.addEventListener('storage', handleConsentChange);
    window.addEventListener('trescout:telemetry-consent', handleConsentChange);
  }

  loadProviders();
})();
