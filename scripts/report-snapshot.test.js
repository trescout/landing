const assert = require('node:assert/strict');
const test = require('node:test');
const { snapshotChips, snapshotNote, snapshotTotal } = require('./report-snapshot.js');

const translations = {
  'öne çıkan': 'highlights',
  yeni: 'new',
  'GitHub Trending': 'GitHub Trending',
  'Hacker News': 'Hacker News',
};

const escapeHtml = (value) => String(value).replace(/[&<>\"]/g, (char) => ({
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
}[char]));

test('chips use the localized WebReport JSON section counts', () => {
  const localizedReport = {
    // This intentionally disagrees with any Turkish cover that might be scraped.
    sections: [
      { sourceName: 'github', items: [{}, {}] },
      { sourceName: 'hackernews', items: [{}] },
    ],
  };

  const chips = snapshotChips(localizedReport, 'normal', translations, escapeHtml);

  assert.match(chips, /GitHub Trending · 2/);
  assert.match(chips, /Hacker News · 1/);
  assert.match(chips, /3 highlights/);
  assert.equal(snapshotTotal(localizedReport), 3);
  assert.doesNotMatch(chips, /5/);
});

test('snapshot note is rendered only when a capture time exists', () => {
  assert.equal(snapshotNote('', 'Snapshot <test>', escapeHtml), '');
  assert.equal(
    snapshotNote('24 August 2026, 07:45', 'Snapshot <test>', escapeHtml),
    '<p class="rep-captured rep-snapshot-note">Snapshot &lt;test&gt;</p>',
  );
});

test('fresh chips use the fresh label and empty sections are ignored', () => {
  const chips = snapshotChips({
    sections: [
      { sourceName: 'github', items: [] },
      { sourceName: 'hackernews', items: [{}] },
    ],
  }, 'fresh', translations, escapeHtml);

  assert.match(chips, /Hacker News · 1/);
  assert.match(chips, /1 new/);
  assert.doesNotMatch(chips, /GitHub Trending/);
});
