/* TreScout · privacy.js · önceden privacy.html içinde inline'dı · CSP için harici alındı */

    (function () {
      if (window.parent === window) return;
      function nearBottom() {
        var sh = document.documentElement.scrollHeight;
        var ch = document.documentElement.clientHeight;
        var st = window.scrollY || document.documentElement.scrollTop;
        return sh - st - ch < 80;
      }
      function notify() {
        try { window.parent.postMessage({ type: 'trescout-privacy-read' }, '*'); } catch (e) {}
      }
      window.addEventListener('scroll', function () {
        if (nearBottom()) notify();
      }, { passive: true });
      window.addEventListener('load', function () {
        // Eğer içerik viewport'a sığıyorsa direkt okunmuş say
        if (nearBottom()) notify();
      });
    })();
  
