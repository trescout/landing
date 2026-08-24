/*
 * TreScout · homepage interactions
 *
 * Manual · report source/summary/glossary tabs and catalog discovery radar.
 * All data stays in the page: no email, signup, analytics, or third-party call.
 * Future measurement can listen to `trescout:interaction`.
 */
(function () {
  'use strict';

  function emit(name, detail) {
    document.dispatchEvent(new CustomEvent('trescout:interaction', {
      detail: Object.assign({ name: name }, detail || {})
    }));
  }

  function language() {
    return (document.documentElement.lang || 'tr').toLowerCase();
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
      emit('report_tasting_tab', { tab: name, language: language() });
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
        emit('report_tasting_source_click', { language: language() });
      });
    });
    emit('report_tasting_view', { language: language() });
  }

  var FILTER_TERMS = {
    ai: ['yapay zek', 'artificial intelligence', 'ai ', 'ia ', 'intelligence artificielle', 'inteligência artificial', 'inteligencia artificial', 'künstliche intelligenz'],
    dev: ['geliştirici', 'developer', 'développeur', 'développement', 'desenvolvedor', 'desenvolvimento', 'desarrollo', 'entwickler', 'entwicklung', 'kod', 'code', 'cli', 'program'],
    learn: ['öğren', 'learning', 'apprentissage', 'aprendiz', 'aprendizaje', 'lernen', 'course', 'kurs', 'curso', 'cours'],
    selfhost: ['self-host', 'self host', 'kendi sunucu', 'auto-héberg', 'auto-héberge', 'auto-hosped', 'autoaloj', 'selbst gehost']
  };

  var EMPTY_TEXT = {
    tr: 'Bu filtrede şu an gösterilecek kayıt yok.', en: 'There are no entries to show for this filter yet.',
    fr: 'Aucune entrée à afficher pour ce filtre.', pt: 'Ainda não há entradas para este filtro.',
    es: 'Todavía no hay entradas para este filtro.', de: 'Für diesen Filter gibt es noch keine Einträge.'
  };

  function entryText(entry, lang) {
    return [entry.title, entry.tagline, entry['tagline_' + lang], entry.slug]
      .concat(entry.tags || []).join(' ').toLowerCase();
  }

  function matches(entry, filter, lang) {
    if (filter === 'all') return true;
    var text = entryText(entry, lang);
    return (FILTER_TERMS[filter] || []).some(function (term) { return text.indexOf(term) !== -1; });
  }

  function displayDate(value, lang) {
    if (!value) return '';
    var date = new Date(value + 'T00:00:00Z');
    if (Number.isNaN(date.getTime())) return value;
    try {
      return new Intl.DateTimeFormat(lang === 'pt' ? 'pt-BR' : lang, { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' }).format(date);
    } catch (error) {
      return value;
    }
  }

  function makeCard(entry, lang) {
    var card = document.createElement('article');
    card.className = 'radar-card';
    var eyebrow = document.createElement('span');
    eyebrow.className = 'radar-card-meta';
    eyebrow.textContent = (entry.source || 'GitHub') + ' · ' + displayDate(entry.last_review || entry.date, lang);
    var title = document.createElement('h3');
    title.textContent = entry.title || entry.slug;
    var text = document.createElement('p');
    text.textContent = entry['tagline_' + lang] || entry.tagline || '';
    var tags = document.createElement('div');
    tags.className = 'radar-card-tags';
    (entry.tags || []).slice(0, 2).forEach(function (tag) {
      var chip = document.createElement('span');
      chip.textContent = tag;
      tags.appendChild(chip);
    });
    var link = document.createElement('a');
    link.className = 'radar-card-link';
    link.href = (lang === 'tr' ? '' : '/' + lang) + '/discover/' + encodeURIComponent(entry.slug) + '/';
    link.textContent = lang === 'tr' ? 'Ayrıntıyı aç →' : (lang === 'fr' ? 'Voir le détail →' : lang === 'pt' ? 'Ver detalhes →' : lang === 'es' ? 'Ver detalle →' : lang === 'de' ? 'Details ansehen →' : 'Open details →');
    link.addEventListener('click', function () {
      emit('discovery_card_click', { slug: entry.slug, language: lang });
    });
    card.appendChild(eyebrow);
    card.appendChild(title);
    card.appendChild(text);
    if (tags.childNodes.length) card.appendChild(tags);
    card.appendChild(link);
    return card;
  }

  function initRadar(root) {
    var grid = root.querySelector('[data-radar-grid]');
    var filters = Array.prototype.slice.call(root.querySelectorAll('[data-radar-filter]'));
    if (!grid || !filters.length) return;
    var lang = language();
    var catalog = [];
    var activeFilter = 'all';
    var loading = grid.querySelector('.radar-loading');

    function activateFilter(filter, focus) {
      activeFilter = filter;
      filters.forEach(function (button) {
        var active = button.getAttribute('data-radar-filter') === filter;
        button.setAttribute('aria-selected', active ? 'true' : 'false');
        button.setAttribute('tabindex', active ? '0' : '-1');
        if (active && focus) button.focus();
      });
      render();
      emit('discovery_radar_filter', { filter: filter, language: lang });
    }

    function render() {
      grid.replaceChildren();
      var selected = catalog.filter(function (entry) { return matches(entry, activeFilter, lang); }).slice(0, 6);
      if (!selected.length) {
        var empty = document.createElement('p');
        empty.className = 'radar-empty';
        empty.textContent = EMPTY_TEXT[lang] || EMPTY_TEXT.en;
        grid.appendChild(empty);
        return;
      }
      selected.forEach(function (entry) { grid.appendChild(makeCard(entry, lang)); });
      grid.setAttribute('aria-busy', 'false');
    }

    filters.forEach(function (button, index) {
      button.addEventListener('click', function () {
        activateFilter(button.getAttribute('data-radar-filter'), false);
      });
      button.addEventListener('keydown', function (event) {
        var next = index;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % filters.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + filters.length) % filters.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = filters.length - 1;
        if (next !== index || event.key === 'Home' || event.key === 'End') {
          event.preventDefault();
          activateFilter(filters[next].getAttribute('data-radar-filter'), true);
        }
      });
    });
    root.querySelectorAll('[data-radar-cta]').forEach(function (link) {
      link.addEventListener('click', function () {
        emit('discovery_radar_cta', { language: lang, filter: activeFilter });
      });
    });

    fetch('/assets/discover/catalog.json', { credentials: 'same-origin' })
      .then(function (response) {
        if (!response.ok) throw new Error('catalog ' + response.status);
        return response.json();
      })
      .then(function (entries) {
        catalog = Array.isArray(entries) ? entries.slice() : [];
        catalog.sort(function (a, b) {
          return String(b.last_review || b.date || '').localeCompare(String(a.last_review || a.date || '')) || Number(b.stars || 0) - Number(a.stars || 0);
        });
        render();
        emit('discovery_radar_view', { language: lang, count: catalog.length });
      })
      .catch(function () {
        grid.replaceChildren();
        var empty = document.createElement('p');
        empty.className = 'radar-empty';
        empty.textContent = EMPTY_TEXT[lang] || EMPTY_TEXT.en;
        grid.appendChild(empty);
        grid.setAttribute('aria-busy', 'false');
        emit('discovery_radar_error', { language: lang });
      });

    if (loading) loading.setAttribute('aria-live', 'polite');
  }

  function init() {
    document.querySelectorAll('[data-report-tasting]').forEach(initReportTasting);
    document.querySelectorAll('[data-discovery-radar]').forEach(initRadar);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
