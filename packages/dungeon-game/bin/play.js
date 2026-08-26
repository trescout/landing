#!/usr/bin/env node

/**
 * TreScout · Açık Kaynak Zindanı (The Open Source Dungeon)
 * =======================================================
 * Terminal Roguelike RPG Game
 * Zero-dependency, pure Node.js ANSI gaming experience.
 */

const readline = require('readline');

// ANSI Renkleri
const C = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m',
  bgDark: '\x1b[40m'
};

// Oyun Durumu
const state = {
  hero: {
    name: 'OpenSource Hero',
    hp: 100,
    maxHp: 100,
    level: 1,
    xp: 0,
    gold: 50,
    weapon: { name: 'Ripgrep Kılıcı', atk: 18 },
    shield: { name: 'Rust Kalkanı', def: 8 },
    inventory: ['Ollama İksiri (+30 HP)', 'Claude Code Parşömeni']
  },
  floor: 1,
  log: ['Zindana girdiniz. Etrafta derleme sesleri yankılanıyor...'],
  currentEnemy: null
};

const ENEMIES = [
  { name: 'Merge Conflict Canavarı', hp: 35, maxHp: 35, atk: 12, xp: 25, gold: 15 },
  { name: 'Bellek Sızıntısı Ejderhası (Memory Leak)', hp: 60, maxHp: 60, atk: 18, xp: 50, gold: 35 },
  { name: 'Bağımlılık Cehennemi İblisi (Dependency Hell)', hp: 90, maxHp: 90, atk: 24, xp: 85, gold: 60 },
  { name: 'OOM Killer Titanı (Out of Memory)', hp: 130, maxHp: 130, atk: 32, xp: 150, gold: 120 }
];

function spawnEnemy() {
  const template = ENEMIES[Math.min(state.floor - 1, ENEMIES.length - 1)];
  state.currentEnemy = { ...template };
  state.log.push(`⚠️ ${C.red}${C.bold}${state.currentEnemy.name}${C.reset} belirdi!`);
}

function renderUI() {
  console.clear();
  console.log(`${C.cyan}${C.bold}========================================================================${C.reset}`);
  console.log(`${C.yellow}${C.bold}   🏰 TRESCOUT: THE OPEN SOURCE DUNGEON (KAT ${state.floor})   ${C.reset}`);
  console.log(`${C.cyan}${C.bold}========================================================================${C.reset}`);

  // Kahraman Bilgisi
  const hpBar = '█'.repeat(Math.max(0, Math.round((state.hero.hp / state.hero.maxHp) * 15)));
  const emptyBar = '░'.repeat(Math.max(0, 15 - hpBar.length));
  console.log(`🧙 ${C.bold}Kahraman:${C.reset} ${state.hero.name} (Seviye ${state.hero.level}) | XP: ${state.hero.xp} | Altın: 🪙 ${state.hero.gold}`);
  console.log(`❤️  HP: [${C.green}${hpBar}${C.dim}${emptyBar}${C.reset}] ${state.hero.hp}/${state.hero.maxHp}`);
  console.log(`⚔️  Silah: ${C.magenta}${state.hero.weapon.name}${C.reset} (+${state.hero.weapon.atk} Saldırı) | 🛡️  Kalkan: ${C.blue}${state.hero.shield.name}${C.reset} (+${state.hero.shield.def} Defans)`);
  console.log(`${C.dim}------------------------------------------------------------------------${C.reset}`);

  // Düşman Bilgisi
  if (state.currentEnemy && state.currentEnemy.hp > 0) {
    const e = state.currentEnemy;
    const eBar = '█'.repeat(Math.max(0, Math.round((e.hp / e.maxHp) * 15)));
    const eEmpty = '░'.repeat(Math.max(0, 15 - eBar.length));
    console.log(`👾 ${C.red}${C.bold}DÜŞMAN:${C.reset} ${e.name}`);
    console.log(`💔 HP: [${C.red}${eBar}${C.dim}${eEmpty}${C.reset}] ${e.hp}/${e.maxHp} | Saldırı Gücü: ⚔️  ${e.atk}`);
  } else {
    console.log(`✨ Bu kat temizlendi! Sonraki kata inmeye hazırsınız.`);
  }

  console.log(`${C.dim}------------------------------------------------------------------------${C.reset}`);
  console.log(`${C.bold}📜 Zindan Günlüğü:${C.reset}`);
  state.log.slice(-4).forEach(l => console.log(`  > ${l}`));
  console.log(`${C.dim}------------------------------------------------------------------------${C.reset}`);

  console.log(`${C.bold}Hamlenizi Seçin:${C.reset}`);
  console.log(` [1] ⚔️  Saldır (${state.hero.weapon.name})`);
  console.log(` [2] 🧪 İksir Kullan (${state.hero.inventory[0] || 'Tükendi'})`);
  console.log(` [3] 🚪 Sonraki Kata İlerle (Kat ${state.floor + 1})`);
  console.log(` [q] Çıkış`);
  process.stdout.write(`\nSeçiminiz (1-3): `);
}

function processTurn(action) {
  if (action === '1') {
    if (!state.currentEnemy || state.currentEnemy.hp <= 0) {
      state.log.push('Bu katta saldıracak düşman kalmadı. 3\'e basarak ilerleyin!');
      return;
    }

    // Oyuncu Saldırısı
    const dmg = Math.round(state.hero.weapon.atk * (0.9 + Math.random() * 0.4));
    state.currentEnemy.hp -= dmg;
    state.log.push(`⚔️ ${state.hero.weapon.name} ile ${dmg} hasar vurdunuz!`);

    if (state.currentEnemy.hp <= 0) {
      state.log.push(`🎉 ${C.green}${state.currentEnemy.name} yok edildi! +${state.currentEnemy.xp} XP, +🪙 ${state.currentEnemy.gold} Altın kazanıldı.${C.reset}`);
      state.hero.xp += state.currentEnemy.xp;
      state.hero.gold += state.currentEnemy.gold;

      if (state.hero.xp >= state.hero.level * 60) {
        state.hero.level++;
        state.hero.maxHp += 20;
        state.hero.hp = state.hero.maxHp;
        state.log.push(`🌟 ${C.yellow}${C.bold}SEVİYE ATLADINIZ! Seviye ${state.hero.level} oldunuz.${C.reset}`);
      }
      return;
    }

    // Düşman Karşı Saldırısı
    const enemyDmg = Math.max(2, Math.round((state.currentEnemy.atk - state.hero.shield.def) * (0.8 + Math.random() * 0.4)));
    state.hero.hp -= enemyDmg;
    state.log.push(`💥 ${state.currentEnemy.name} size ${enemyDmg} hasar verdi!`);

    if (state.hero.hp <= 0) {
      state.log.push(`☠️ ${C.red}${C.bold}Yenildiniz! Bellek taştı (Segmentation fault).${C.reset}`);
    }
  } else if (action === '2') {
    if (state.hero.inventory.length > 0) {
      state.hero.hp = Math.min(state.hero.maxHp, state.hero.hp + 35);
      state.log.push(`🧪 Ollama İksiri içtiniz! +35 HP yenilendi.`);
    } else {
      state.log.push(`İksiriniz kalmadı!`);
    }
  } else if (action === '3') {
    if (state.currentEnemy && state.currentEnemy.hp > 0) {
      state.log.push(`Düşmanı yenmeden kata geçemezsiniz!`);
    } else {
      state.floor++;
      state.log.push(`🪜 Kat ${state.floor}'e indiniz. Havadaki gecikme (latency) artıyor...`);
      spawnEnemy();
    }
  }
}

function runInteractive() {
  spawnEnemy();
  renderUI();

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.on('line', (line) => {
    const input = line.trim();
    if (input.toLowerCase() === 'q') {
      console.log(`\n${C.yellow}Açık Kaynak Zindanından ayrıldınız. Görüşmek üzere!${C.reset}\n`);
      rl.close();
      process.exit(0);
    }

    processTurn(input);
    renderUI();

    if (state.hero.hp <= 0) {
      console.log(`\n${C.red}${C.bold}OYUN BİTTİ. Tekrar denemek için oyunu baştan başlatın.${C.reset}\n`);
      rl.close();
      process.exit(0);
    }
  });
}

function runDemo() {
  spawnEnemy();
  renderUI();
  console.log(`\n${C.green}Otomatik demo turu başlatılıyor...${C.reset}`);
  processTurn('1');
  renderUI();
  console.log(`\n✅ Açık Kaynak Zindanı motoru başarıyla test edildi!\n`);
}

if (process.argv.includes('--demo') || !process.stdin.isTTY) {
  runDemo();
} else {
  runInteractive();
}
