#!/usr/bin/env node
/**
 * TreScout CLI
 * ============
 * Daily Tech Intelligence & Open Source Discovery right in your Terminal.
 *
 * Usage:
 *   trescout today           # Print today's tech intelligence report
 *   trescout search <query>  # Search 470+ open-source tools
 *   trescout whatis <term>   # Look up software/AI term definition
 *   trescout tools           # List top trending open-source tools
 *   trescout reports         # List recent tech reports
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '../../..');
const CATALOG_PATH = path.join(ROOT_DIR, 'assets', 'discover', 'catalog.json');
const DICTIONARY_PATH = path.join(ROOT_DIR, 'assets', 'dictionary', 'dictionary.json');
const REPORTS_DIR = path.join(ROOT_DIR, 'reports');

// Terminal Colors & Formatting
const C = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  italic: '\x1b[3m',
  underline: '\x1b[4m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  yellow: '\x1b[33m',
  green: '\x1b[32m',
  magenta: '\x1b[35m',
  gray: '\x1b[90m',
  white: '\x1b[97m',
  bgBlue: '\x1b[44m',
  bgDark: '\x1b[48;5;236m'
};

function banner() {
  console.log(`
${C.bold}${C.blue}╭─────────────────────────────────────────────────────────────╮${C.reset}
${C.bold}${C.blue}│${C.reset}  ${C.bold}${C.yellow}📡 TreScout${C.reset} · ${C.cyan}Daily Tech Intelligence in your Terminal${C.reset}     ${C.bold}${C.blue}│${C.reset}
${C.bold}${C.blue}╰─────────────────────────────────────────────────────────────╯${C.reset}
`);
}

function loadCatalog() {
  try {
    if (fs.existsSync(CATALOG_PATH)) {
      return JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf8'));
    }
  } catch (e) {}
  return [];
}

function loadDictionary() {
  try {
    if (fs.existsSync(DICTIONARY_PATH)) {
      return JSON.parse(fs.readFileSync(DICTIONARY_PATH, 'utf8'));
    }
  } catch (e) {}
  return [];
}

function getLatestReportDate() {
  if (!fs.existsSync(REPORTS_DIR)) return null;
  const dates = fs.readdirSync(REPORTS_DIR)
    .filter(d => /^\d{4}-\d{2}-\d{2}$/.test(d))
    .sort()
    .reverse();
  return dates[0] || null;
}

// Commands
function cmdToday(args) {
  banner();
  const date = args[0] || getLatestReportDate();
  if (!date) {
    console.log(`${C.yellow}Henüz yayımlanmış rapor bulunamadı.${C.reset}\n`);
    return;
  }

  const reportPath = path.join(REPORTS_DIR, date, 'index.html');
  if (!fs.existsSync(reportPath)) {
    console.log(`${C.yellow}${date} tarihli rapor bulunamadı.${C.reset}\n`);
    return;
  }

  const html = fs.readFileSync(reportPath, 'utf8');
  const titleMatch = html.match(/<h1 class="rep-title">(.*?)<\/h1>/);
  const editorialMatch = html.match(/<p class="rep-editorial">(.*?)<\/p>/);
  const chipsMatch = html.match(/<div class="rep-chips">(.*?)<\/div>/);

  const title = titleMatch ? titleMatch[1].replace(/<[^>]+>/g, '').trim() : date;
  const editorial = editorialMatch ? editorialMatch[1].replace(/<[^>]+>/g, '').trim() : '';
  const chips = chipsMatch ? chipsMatch[1].replace(/<[^>]+>/g, ' · ').replace(/\s+/g, ' ').trim() : '';

  console.log(`${C.bold}${C.white}📅 ${title}${C.reset}`);
  if (chips) {
    console.log(`${C.gray}${chips}${C.reset}\n`);
  }

  console.log(`${C.bold}${C.cyan}📝 Günün Özeti:${C.reset}`);
  console.log(`${editorial}\n`);

  // Extract featured tools
  const toolRegex = /<a class="rep-link-item" href="\/discover\/([^/]+)\/">([^<]+)<\/a>/g;
  const tools = [];
  let match;
  while ((match = toolRegex.exec(html)) !== null) {
    tools.push({ slug: match[1], name: match[2].replace(' →', '').trim() });
  }

  if (tools.length > 0) {
    console.log(`${C.bold}${C.yellow}🚀 Öne Çıkan Açık Kaynak Projeleri:${C.reset}`);
    tools.forEach(t => {
      console.log(`  ${C.green}●${C.reset} ${C.bold}${t.name}${C.reset} ${C.dim}→ https://trescout.com/discover/${t.slug}/${C.reset}`);
    });
    console.log();
  }

  console.log(`${C.dim}Tam rapor ve PDF: https://trescout.com/reports/${date}/${C.reset}\n`);
}

function cmdSearch(queryTerms) {
  banner();
  const query = queryTerms.join(' ').trim().toLowerCase();
  if (!query) {
    console.log(`${C.yellow}Kullanım: trescout search <anahtar kelime>${C.reset}\n`);
    return;
  }

  const catalog = loadCatalog();
  const results = catalog.filter(item => {
    const matchTitle = (item.title || '').toLowerCase().includes(query);
    const matchTagline = (item.tagline || '').toLowerCase().includes(query);
    const matchTags = (item.tags || []).some(t => t.toLowerCase().includes(query));
    const matchSlug = (item.slug || '').toLowerCase().includes(query);
    return matchTitle || matchTagline || matchTags || matchSlug;
  }).slice(0, 8);

  console.log(`${C.bold}🔍 "${query}" için ${results.length} sonuç bulundu:${C.reset}\n`);

  if (results.length === 0) {
    console.log(`${C.gray}Eşleşen açık kaynak aracı bulunamadı.${C.reset}\n`);
    return;
  }

  results.forEach(item => {
    const stars = item.stars ? `★ ${Number(item.stars).toLocaleString()}` : '';
    console.log(`${C.bold}${C.green}${item.title}${C.reset} ${C.yellow}${stars}${C.reset}`);
    console.log(`  ${item.tagline || item.tagline_en || ''}`);
    if (item.tags && item.tags.length > 0) {
      console.log(`  ${C.gray}Etiketler: ${item.tags.join(', ')}${C.reset}`);
    }
    console.log(`  ${C.dim}https://trescout.com/discover/${item.slug}/${C.reset}\n`);
  });
}

function cmdWhatis(terms) {
  banner();
  const query = terms.join(' ').trim().toLowerCase();
  if (!query) {
    console.log(`${C.yellow}Kullanım: trescout whatis <kavram/terim>${C.reset}\n`);
    return;
  }

  const dictionary = loadDictionary();
  const match = dictionary.find(item =>
    item.slug.toLowerCase() === query ||
    (item.en && item.en.toLowerCase() === query) ||
    (item.full && item.full.toLowerCase() === query)
  );

  if (match) {
    console.log(`${C.bold}${C.cyan}📖 ${match.en || match.slug}${C.reset} ${match.full ? C.gray + '(' + match.full + ')' + C.reset : ''}`);
    console.log(`\n${match.kisa || match.kisa_en || ''}\n`);
    console.log(`${C.dim}Detaylı Sözlük Maddesi: https://trescout.com/dictionary/${match.slug}/${C.reset}\n`);
    return;
  }

  // Partial match
  const partials = dictionary.filter(item =>
    (item.slug && item.slug.toLowerCase().includes(query)) ||
    (item.en && item.en.toLowerCase().includes(query)) ||
    (item.kisa && item.kisa.toLowerCase().includes(query))
  ).slice(0, 5);

  if (partials.length > 0) {
    console.log(`${C.bold}İlgili kavramlar:${C.reset}\n`);
    partials.forEach(p => {
      console.log(`${C.bold}${C.green}● ${p.en || p.slug}${C.reset}: ${p.kisa || p.kisa_en || ''}`);
      console.log(`  ${C.dim}https://trescout.com/dictionary/${p.slug}/${C.reset}\n`);
    });
    return;
  }

  console.log(`${C.yellow}"${query}" kavramı sözlükte bulunamadı.${C.reset}\n`);
}

function cmdTools(args) {
  banner();
  const catalog = loadCatalog();
  const limit = Number(args[0]) || 10;
  const top = catalog.slice(0, limit);

  console.log(`${C.bold}🚀 En Popüler Açık Kaynak Araçları (Top ${top.length}):${C.reset}\n`);
  top.forEach((item, idx) => {
    const stars = item.stars ? `★ ${Number(item.stars).toLocaleString()}` : '';
    console.log(`${C.bold}${C.blue}${idx + 1}.${C.reset} ${C.bold}${item.title}${C.reset} ${C.yellow}${stars}${C.reset}`);
    console.log(`   ${item.tagline || ''}`);
    console.log(`   ${C.dim}https://trescout.com/discover/${item.slug}/${C.reset}\n`);
  });
}

function cmdHelp() {
  banner();
  console.log(`${C.bold}Kullanım:${C.reset}`);
  console.log(`  ${C.green}trescout today${C.reset}          Günün teknoloji raporunu terminalde özetler`);
  console.log(`  ${C.green}trescout search <kelime>${C.reset} 470+ açık kaynak araç içinde arama yapar`);
  console.log(`  ${C.green}trescout whatis <terim>${C.reset}  Sözlükten teknik kavram ve tanım sorgular`);
  console.log(`  ${C.green}trescout tools [limit]${C.reset}  Öne çıkan popüler açık kaynak araçları listeler`);
  console.log(`  ${C.green}trescout help${C.reset}           Bu yardım menüsünü gösterir`);
  console.log();
}

// Router
const [,, command, ...args] = process.argv;

switch (command) {
  case 'today':
  case 't':
    cmdToday(args);
    break;
  case 'search':
  case 's':
  case 'find':
    cmdSearch(args);
    break;
  case 'whatis':
  case 'define':
  case 'term':
    cmdWhatis(args);
    break;
  case 'tools':
  case 'list':
    cmdTools(args);
    break;
  case '--help':
  case '-h':
  case 'help':
    cmdHelp();
    break;
  default:
    if (!command) {
      cmdToday([]);
    } else {
      cmdSearch([command, ...args]);
    }
    break;
}
