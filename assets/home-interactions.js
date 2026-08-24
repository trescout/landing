/*
 * TreScout · homepage interactions
 *
 * Manual · report source/summary/glossary tabs, catalog discovery radar, and daily flow preview.
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

  function contentLanguage(lang) {
    return lang === 'pt-br' ? 'pt' : lang;
  }

  function routeLanguage(lang) {
    return contentLanguage(lang);
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

  var TAG_LABELS = {
    'Geliştirici aracı': { en: 'Developer tool', fr: 'Outil pour développeurs', pt: 'Ferramenta para desenvolvedores', es: 'Herramienta para desarrolladores', de: 'Entwickler-Tool' },
    'Kod bilmeyenler için': { en: 'For non-coders', fr: 'Pour les non-développeurs', pt: 'Para quem não programa', es: 'Para no programadores', de: 'Für Nicht-Programmierer' },
    'Yapay zekâ araçları': { en: 'AI tools', fr: 'Outils d’IA', pt: 'Ferramentas de IA', es: 'Herramientas de IA', de: 'KI-Tools' },
    'Öğrenme': { en: 'Learning', fr: 'Apprentissage', pt: 'Aprendizado', es: 'Aprendizaje', de: 'Lernen' },
    'Üretkenlik': { en: 'Productivity', fr: 'Productivité', pt: 'Produtividade', es: 'Productividad', de: 'Produktivität' }
  };

  function tagLabel(tag, lang) {
    var labels = TAG_LABELS[tag];
    var locale = contentLanguage(lang);
    return labels && labels[locale] ? labels[locale] : tag;
  }

  function entryText(entry, lang) {
    var locale = contentLanguage(lang);
    return [entry.title, entry.tagline, entry['tagline_' + locale], entry.slug]
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
    var locale = contentLanguage(lang);
    var route = routeLanguage(lang);
    var card = document.createElement('article');
    card.className = 'radar-card';
    var eyebrow = document.createElement('span');
    eyebrow.className = 'radar-card-meta';
    eyebrow.textContent = (entry.source || 'GitHub') + ' · ' + displayDate(entry.last_review || entry.date, lang);
    var title = document.createElement('h3');
    title.textContent = entry.title || entry.slug;
    var text = document.createElement('p');
    text.textContent = entry['tagline_' + locale] || entry.tagline || '';
    var tags = document.createElement('div');
    tags.className = 'radar-card-tags';
    (entry.tags || []).slice(0, 2).forEach(function (tag) {
      var chip = document.createElement('span');
      chip.textContent = tagLabel(tag, lang);
      tags.appendChild(chip);
    });
    var link = document.createElement('a');
    link.className = 'radar-card-link';
    link.href = (route === 'tr' ? '' : '/' + route) + '/discover/' + encodeURIComponent(entry.slug) + '/';
    link.textContent = locale === 'tr' ? 'Ayrıntıyı aç →' : (locale === 'fr' ? 'Voir le détail →' : locale === 'pt' ? 'Ver detalhes →' : locale === 'es' ? 'Ver detalle →' : locale === 'de' ? 'Details ansehen →' : 'Open details →');
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

  var FLOW_TEXT = {
    tr: { step: ['Kaynağı seç', 'Kısa özete indir', 'Ayrıntıya geç'], loading: 'Gerçek katalog kayıtları yükleniyor…', empty: 'Bu örnek konu için henüz kayıt bulunamadı.' },
    en: { step: ['Choose a source', 'Turn it into a short summary', 'Open the detail'], loading: 'Loading real catalog entries…', empty: 'There are no entries for this example topic yet.' },
    fr: { step: ['Choisir une source', 'La réduire à un résumé', 'Ouvrir le détail'], loading: 'Chargement des entrées réelles du catalogue…', empty: 'Aucune entrée pour ce sujet d’exemple pour le moment.' },
    pt: { step: ['Escolher uma fonte', 'Transformar em um resumo curto', 'Abrir os detalhes'], loading: 'Carregando registros reais do catálogo…', empty: 'Ainda não há registros para este tema de exemplo.' },
    es: { step: ['Elegir una fuente', 'Convertirla en un resumen breve', 'Abrir el detalle'], loading: 'Cargando entradas reales del catálogo…', empty: 'Todavía no hay entradas para este tema de ejemplo.' },
    de: { step: ['Quelle auswählen', 'Kurz zusammenfassen', 'Details öffnen'], loading: 'Echte Katalogeinträge werden geladen…', empty: 'Für dieses Beispielthema gibt es noch keine Einträge.' }
  };

  function initDailyFlow(root) {
    var list = root.querySelector('[data-flow-list]');
    var topicButtons = Array.prototype.slice.call(root.querySelectorAll('[data-flow-topic]'));
    var timeButtons = Array.prototype.slice.call(root.querySelectorAll('[data-flow-time]'));
    var selection = root.querySelector('[data-flow-selection]');
    if (!list || !topicButtons.length || !timeButtons.length || !selection) return;

    var lang = language();
    var locale = contentLanguage(lang);
    var copy = FLOW_TEXT[locale] || FLOW_TEXT.en;
    var catalog = [];
    var activeTopic = topicButtons[0].getAttribute('data-flow-topic');
    var activeTime = timeButtons[0].getAttribute('data-flow-time');

    function setPressed(buttons, value) {
      buttons.forEach(function (button) {
        button.setAttribute('aria-pressed', button.getAttribute('data-flow-topic') === value || button.getAttribute('data-flow-time') === value ? 'true' : 'false');
      });
    }

    function topicLabel() {
      var button = topicButtons.find(function (item) { return item.getAttribute('data-flow-topic') === activeTopic; });
      return button ? button.textContent.trim() : activeTopic;
    }

    function render() {
      setPressed(topicButtons, activeTopic);
      setPressed(timeButtons, activeTime);
      selection.textContent = activeTime + ' · ' + topicLabel();
      list.replaceChildren();
      var selected = catalog.filter(function (entry) { return matches(entry, activeTopic, lang); }).slice(0, 3);
      if (!selected.length) {
        var empty = document.createElement('p');
        empty.className = 'daily-flow-empty';
        empty.textContent = copy.empty;
        list.appendChild(empty);
        list.setAttribute('aria-busy', 'false');
        return;
      }
      selected.forEach(function (entry, index) {
        var step = document.createElement('article');
        step.className = 'daily-flow-step';
        var number = document.createElement('span');
        number.className = 'daily-flow-step-number';
        number.textContent = String(index + 1).padStart(2, '0');
        var body = document.createElement('div');
        body.className = 'daily-flow-step-body';
        var label = document.createElement('span');
        label.className = 'daily-flow-step-label';
        label.textContent = copy.step[index];
        var title = document.createElement('h4');
        title.textContent = entry.title || entry.slug;
        var description = document.createElement('p');
        description.textContent = entry['tagline_' + locale] || entry.tagline || '';
        var meta = document.createElement('span');
        meta.className = 'daily-flow-step-meta';
        meta.textContent = (entry.source || 'GitHub') + ' · ' + displayDate(entry.last_review || entry.date, lang);
        body.appendChild(label);
        body.appendChild(title);
        body.appendChild(description);
        body.appendChild(meta);
        step.appendChild(number);
        step.appendChild(body);
        list.appendChild(step);
      });
      list.setAttribute('aria-busy', 'false');
      emit('daily_flow_preview_rendered', { language: lang, topic: activeTopic, time: activeTime, count: selected.length });
    }

    topicButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        activeTopic = button.getAttribute('data-flow-topic');
        render();
        emit('daily_flow_topic_select', { language: lang, topic: activeTopic });
      });
    });
    timeButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        activeTime = button.getAttribute('data-flow-time');
        render();
        emit('daily_flow_time_select', { language: lang, time: activeTime });
      });
    });
    root.querySelectorAll('[data-flow-cta]').forEach(function (link) {
      link.addEventListener('click', function () {
        emit('daily_flow_cta', { language: lang, topic: activeTopic, time: activeTime });
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
        emit('daily_flow_catalog_loaded', { language: lang, count: catalog.length });
      })
      .catch(function () {
        list.replaceChildren();
        var empty = document.createElement('p');
        empty.className = 'daily-flow-empty';
        empty.textContent = copy.loading;
        list.appendChild(empty);
        list.setAttribute('aria-busy', 'false');
        emit('daily_flow_error', { language: lang });
      });

    emit('daily_flow_view', { language: lang });
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
        empty.textContent = EMPTY_TEXT[contentLanguage(lang)] || EMPTY_TEXT.en;
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
        empty.textContent = EMPTY_TEXT[contentLanguage(lang)] || EMPTY_TEXT.en;
        grid.appendChild(empty);
        grid.setAttribute('aria-busy', 'false');
        emit('discovery_radar_error', { language: lang });
      });

    if (loading) loading.setAttribute('aria-live', 'polite');
  }

  function init() {
    document.querySelectorAll('[data-report-tasting]').forEach(initReportTasting);
    document.querySelectorAll('[data-discovery-radar]').forEach(initRadar);
    document.querySelectorAll('[data-daily-flow]').forEach(initDailyFlow);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
