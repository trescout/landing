/*
 * TreScout · homepage interactions
 *
 * Manual · report source/summary/glossary tabs, catalog discovery radar, and daily flow preview.
 * All data stays in the page: no email, signup, analytics, or third-party call.
 * Future measurement can listen to `trescout:interaction`.
 */
(function () {
  'use strict';

  // Çeviri eksikse Türkçeye düşme (Türkçe sayfa hariç): önce İngilizce, sonra boş.
  function yerelTanitim(entry, locale) {
    if (locale === 'tr') return entry.tagline || '';
    return entry['tagline_' + locale] || entry.tagline_en || '';
  }

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

  var FILTER_TAGS = {
    ai: ['yapay zekâ araçları'],
    dev: ['geliştirici aracı'],
    learn: ['öğrenme'],
    selfhost: ['self-host']
  };

  // Eski veya eksik katalog kaydı için geriye dönük fallback. Yeni kayıtlarda
  // filtreleme yalnızca kanonik `tags` alanına dayanır; serbest metin araması
  // yanlış pozitif üretebildiği için ikinci seçenek olarak tutulur.
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
    'Üretkenlik': { en: 'Productivity', fr: 'Productivité', pt: 'Produtividade', es: 'Productividad', de: 'Produktivität' },
    'Self-host': { en: 'Self-hosted', fr: 'Auto-hébergé', pt: 'Auto-hospedado', es: 'Autoalojado', de: 'Selbst gehostet' }
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

  function normalizeTag(value) {
    return String(value || '').trim().toLocaleLowerCase('tr-TR');
  }

  function matches(entry, filter, lang) {
    if (filter === 'all') return true;
    var tags = Array.isArray(entry.tags) ? entry.tags.map(normalizeTag) : [];
    var wantedTags = (FILTER_TAGS[filter] || []).map(normalizeTag);
    if (tags.length) {
      return tags.some(function (tag) { return wantedTags.indexOf(tag) !== -1; });
    }
    var text = entryText(entry, lang);
    return (FILTER_TERMS[filter] || []).some(function (term) { return text.indexOf(term) !== -1; });
  }

  function catalogDate(entry) {
    return String(entry && (entry.date || entry.last_review) || '').slice(0, 10);
  }

  function latestCatalogDate(entries) {
    return entries.reduce(function (latest, entry) {
      var date = catalogDate(entry);
      return date > latest ? date : latest;
    }, '');
  }

  var catalogPromise = null;

  function loadCatalog() {
    if (!catalogPromise) {
      // Sayfanın diline göre hafif türev · tam katalog 241 KB, bu 31 KB (gzip).
      // Üreteni: scripts/catalog-home.py · guard: aynı betik --check ile.
      catalogPromise = fetch('/assets/discover/catalog-home-' + contentLanguage(language()) + '.json', { credentials: 'same-origin' })
        .then(function (response) {
          if (!response.ok) throw new Error('catalog ' + response.status);
          return response.json();
        })
        .then(function (entries) {
          return Array.isArray(entries) ? entries.slice() : [];
        });
    }
    return catalogPromise;
  }

  function whenVisible(root, callback) {
    if (!('IntersectionObserver' in window)) {
      callback();
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      if (entries.some(function (entry) { return entry.isIntersecting; })) {
        observer.disconnect();
        callback();
      }
    }, { rootMargin: '300px 0px' });
    observer.observe(root);
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
    eyebrow.textContent = (entry.source || 'GitHub') + ' · ' + displayDate(entry.date || entry.last_review, lang);
    var title = document.createElement('h3');
    title.textContent = entry.title || entry.slug;
    var text = document.createElement('p');
    text.textContent = yerelTanitim(entry, locale);
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

  function initRadar(root) {
    var grid = root.querySelector('[data-radar-grid]');
    var filters = Array.prototype.slice.call(root.querySelectorAll('[data-radar-filter]'));
    if (!grid || !filters.length) return;
    var lang = language();
    var catalog = [];
    var latestDate = '';
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
      var current = latestDate ? catalog.filter(function (entry) { return catalogDate(entry) === latestDate; }) : catalog;
      var selected = current.filter(function (entry) { return matches(entry, activeFilter, lang); }).slice(0, 6);
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

    whenVisible(root, function () {
      loadCatalog()
        .then(function (entries) {
          catalog = entries;
          latestDate = latestCatalogDate(catalog);
          catalog.sort(function (a, b) {
            return catalogDate(b).localeCompare(catalogDate(a)) || Number(b.stars || 0) - Number(a.stars || 0);
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
