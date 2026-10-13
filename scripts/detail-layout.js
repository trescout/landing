/** Include the detail enhancement without rewriting protected editorial HTML. */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const SCRIPT = '<script src="/assets/detail-layout.js" defer></script>';
function normalize(html) {
  if (!html.includes('<article class="disc">') || !html.includes('class="disc-cta"')) return html;
  if (html.includes('src="/assets/detail-layout.js"')) return html;
  return html.replace('<script src="/assets/subscribe.js" defer></script>', SCRIPT + '\n<script src="/assets/subscribe.js" defer></script>');
}
function updateAll() {
  let count = 0;
  for (const locale of ['', 'en', 'fr', 'pt', 'es', 'de']) {
    for (const kind of ['dictionary', 'discover']) {
      const dir = path.join(ROOT, locale, kind);
      for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
        if (!entry.isDirectory()) continue;
        const file = path.join(dir, entry.name, 'index.html');
        if (!fs.existsSync(file)) continue;
        const before = fs.readFileSync(file, 'utf8'), after = normalize(before);
        if (after !== before) { fs.writeFileSync(file, after); count++; }
      }
    }
  }
  console.log(`Detail layout: ${count} pages updated`);
}
module.exports = {normalize};
if (require.main === module) updateAll();
