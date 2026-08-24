/**
 * Immutable report snapshot helpers for localized landing pages.
 *
 * Localized pages must derive counts from their own WebReport JSON. They must
 * never scrape a Turkish cover, because that cover can reflect a different
 * render or a later live catalog state.
 */

const SOURCE_LABEL_TR = Object.freeze({
  github: 'GitHub Trending',
  hackernews: 'Hacker News',
  huggingface: 'HuggingFace · Günün Modelleri',
  hfpapers: 'HuggingFace · Günün Makaleleri',
  releases: 'Sürüm Notları',
  lobsters: 'Lobsters',
});

function snapshotSections(report) {
  return Array.isArray(report?.sections)
    ? report.sections.filter((section) => Array.isArray(section.items) && section.items.length > 0)
    : [];
}

function snapshotTotal(report) {
  return snapshotSections(report).reduce((sum, section) => sum + section.items.length, 0);
}

function sourceLabel(sectionName, translations) {
  const turkishLabel = SOURCE_LABEL_TR[sectionName] || sectionName;
  return translations[turkishLabel] || turkishLabel;
}

function snapshotNote(capturedAtText, label, escapeHtml) {
  return capturedAtText
    ? `<p class="rep-captured rep-snapshot-note">${escapeHtml(label)}</p>`
    : '';
}

function snapshotChips(report, kind, translations, escapeHtml) {
  const chips = snapshotSections(report)
    .map((section) =>
      `<span class="chip">${escapeHtml(sourceLabel(section.sourceName, translations))} · ${section.items.length}</span>`,
    )
    .join('');
  const totalLabel = kind === 'fresh' ? translations.yeni : translations['öne çıkan'];
  return `${chips}<span class="chip chip-total">${snapshotTotal(report)} ${escapeHtml(totalLabel)}</span>`;
}

module.exports = {
  SOURCE_LABEL_TR,
  snapshotSections,
  snapshotTotal,
  snapshotNote,
  snapshotChips,
};
