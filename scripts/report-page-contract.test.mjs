import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join, relative } from 'node:path';
import test from 'node:test';

const root = new URL('..', import.meta.url);
const reportSources = [
  '/_vercel/insights/script.js',
  '/_vercel/speed-insights/script.js',
  '/assets/telemetry.js',
];

async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name === '.git' || entry.name === 'node_modules') continue;
    const path = join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await walk(path));
    else if (entry.isFile() && entry.name === 'index.html') files.push(path);
  }
  return files;
}

test('report detail pages have one canonical analytics/runtime block', async () => {
  const rootPath = decodeURIComponent(root.pathname);
  const files = await walk(rootPath);
  const reportFiles = [];

  for (const path of files) {
    const text = await readFile(path, 'utf8');
    if (!path.includes('/reports/') ||
        (!text.includes('class="signup-cta"') && !text.includes('data-page-type="report"'))) {
      continue;
    }
    reportFiles.push([path, text]);
  }

  assert.ok(reportFiles.length > 0, 'expected at least one report detail page');
  for (const [path, text] of reportFiles) {
    const relativePath = relative(rootPath, path);
    for (const source of reportSources) {
      assert.equal(text.split(source).length - 1, 1, `${relativePath}: expected exactly one ${source}`);
    }
    const positions = reportSources.map(source => text.indexOf(source));
    assert.deepEqual(
      positions,
      [...positions].sort((a, b) => a - b),
      `${relativePath}: expected Insights, Speed Insights, telemetry order`,
    );
    assert.doesNotMatch(text, /KVKK uyumlu|GDPR compliant|GDPR uyumludur|SOC 2 uyumlu/i);
  }
});
