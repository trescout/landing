/*
 * TreScout · ana sayfa etkileşimleri
 *
 * Plan Agent · dönüşüm UX: canlı değeri kayıt formundan önce göster.
 * Manual · source/summary/glossary tab interaction; no network calls.
 * Future measurement can listen to `trescout:interaction`; this file never
 * sends email, signup, analytics, or third-party requests.
 */
(function () {
  'use strict';

  function emit(name, detail) {
    document.dispatchEvent(new CustomEvent('trescout:interaction', {
      detail: Object.assign({ name: name }, detail || {})
    }));
  }

  function initReportTasting(root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll('[data-tasting-tab]'));
    var panels = Array.prototype.slice.call(root.querySelectorAll('[data-tasting-panel]'));
    if (!tabs.length || !panels.length) return;

    function activate(name, focus) {
      tabs.forEach(function (tab) {
        var active = tab.getAttribute('data-tasting-tab') === name;
        tab.setAttribute('aria-selected', active ? 'true' : 'false');
        tab.setAttribute('tabindex', active ? '0' : '-1');
        if (active && focus) tab.focus();
      });
      panels.forEach(function (panel) {
        panel.hidden = panel.getAttribute('data-tasting-panel') !== name;
      });
      emit('report_tasting_tab', { tab: name, language: document.documentElement.lang || 'tr' });
    }

    tabs.forEach(function (tab, index) {
      tab.addEventListener('click', function () {
        activate(tab.getAttribute('data-tasting-tab'), false);
      });
      tab.addEventListener('keydown', function (event) {
        var next = index;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (next !== index || event.key === 'Home' || event.key === 'End') {
          event.preventDefault();
          activate(tabs[next].getAttribute('data-tasting-tab'), true);
        }
      });
    });

    root.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        emit('report_tasting_source_click', { language: document.documentElement.lang || 'tr' });
      });
    });

    emit('report_tasting_view', { language: document.documentElement.lang || 'tr' });
  }

  function init() {
    document.querySelectorAll('[data-report-tasting]').forEach(initReportTasting);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
