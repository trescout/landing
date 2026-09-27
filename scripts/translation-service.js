const https = require('https');
const fs = require('fs');
const os = require('os');
const path = require('path');

// Model zinciri · scripts/gemini_zinciri.py ile AYNI kurallar (iki dilde tek
// sözleşme; birini değiştirirseniz diğerini de değiştirin, check-gemini-zinciri.py
// varsayılan zincirin aynı kaldığını denetler). Sıra, sınıflar ve gerekçeler
// için Python modülünün başlığına bakın.
const DEFAULT_CHAIN = 'gemini-3.8-flash:5,gemini-3.7-flash:5,gemini-3.6-flash:5,gemini-3.5-flash:5,'
  + 'gemini-3.5-flash-lite:15,'
  + 'gemini-3-flash-preview:5,'
  + 'gemini-3.1-flash-lite:15';
// gemini-3.1-flash-lite en sonda · landing ayrı projede (gerekçe gemini_zinciri.py).
const CHAIN = (process.env.GEMINI_MODELS || process.env.GEMINI_MODEL || process.env.TREESCOUT_TRANSLATION_MODEL || DEFAULT_CHAIN)
  .split(',').map(s => s.trim()).filter(Boolean)
  .map(s => { const [model, rpm] = s.split(':'); return [model.trim(), Number(rpm) || 15]; });
const MODELS = CHAIN.map(([m]) => m);
const RPM = new Map(CHAIN);
const FAILURE_LIMIT = 3;
const MIN_OUTPUT_TOKENS = 8192;
// Biten modeller süreçler arasında paylaşılır (Python modülüyle AYNI dosya) ·
// gerekçe gemini_zinciri.py'de. Dosya repo dışında, kota Pasifik gününe ait.
const STATE_FILE = process.env.GEMINI_ZINCIR_DURUM
  || path.join(process.env.RUNNER_TEMP || os.tmpdir(), 'trescout-gemini-zinciri.json');

function quotaDay() {
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Los_Angeles' }).format(new Date());
}

function readState() {
  try {
    const d = JSON.parse(fs.readFileSync(STATE_FILE, 'utf8'));
    return d.gun === quotaDay() ? new Set(d.bitenler || []) : new Set();
  } catch { return new Set(); }
}

function writeState(model) {
  try {
    const all = [...new Set([...readState(), model])].sort();
    fs.writeFileSync(STATE_FILE, JSON.stringify({ gun: quotaDay(), bitenler: all }));
  } catch { /* yalnız hız kazancı; yazılamazsa zincir yine çalışır */ }
}

const exhausted = new Set([...readState()].filter(m => MODELS.includes(m)));
if (exhausted.size) console.error(`  · Gemini: bugün kotası biten modeller atlanıyor (${[...exhausted].sort().join(', ')})`);
const consecutiveFailures = new Map();
let geminiDisabled = false;
let lastRequestAt = 0;

function activeModel() {
  if (geminiDisabled) return null;
  return MODELS.find(m => !exhausted.has(m)) || null;
}

function dropModel(model, reason, persist = true) {
  exhausted.add(model);
  if (persist) writeState(model);
  const next = activeModel();
  console.log(`  ! Gemini ${model}: ${reason} · ${next ? `${next} ile devam` : 'zincirde model kalmadı, Gemini bu koşuda kapalı'}`);
}

function disableGemini(reason) {
  if (geminiDisabled) return;
  geminiDisabled = true;
  console.log(`  ! Gemini kapatıldı: ${reason} · anahtar/hesap sorunu, hiçbir model denenmeyecek`);
}

function recordFailure(model) {
  const n = (consecutiveFailures.get(model) || 0) + 1;
  consecutiveFailures.set(model, n);
  // Kalıcı değil: sebep kota değil, ertesi süreç modeli yeniden denesin
  if (n >= FAILURE_LIMIT && !exhausted.has(model)) dropModel(model, `üst üste ${FAILURE_LIMIT} başarısız istek`, false);
}

function classify(status, body) {
  if (status === 429) return /PerDay|quota_exceeded|daily quota/i.test(body) ? 'daily' : 'transient';
  if (status === 401 || status === 402 || /API_KEY_INVALID|FAILED_PRECONDITION|failed_precondition|leaked/.test(body)) return 'key';
  if (status === 404 || status === 403) return 'model';
  if ([408, 500, 502, 503, 504].includes(status)) return 'transient';
  return 'request';
}

// Yalnız TAM yanıtın metni · engellendi (blockReason) ya da yarıda kesildiyse
// (finishReason != STOP, ör. MAX_TOKENS) boş döner; yarım çeviri asla yazılmaz.
function responseText(data) {
  if (!data || data?.promptFeedback?.blockReason) return '';
  const candidate = data?.candidates?.[0];
  if (!candidate) return '';
  if (candidate.finishReason && candidate.finishReason !== 'STOP') return '';
  return (candidate?.content?.parts || []).filter(p => !p?.thought).map(p => p?.text || '').join('').trim();
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function requestJson(url, options, body, timeoutMs) {
  return new Promise((resolve, reject) => {
    const req = https.request(url, { ...options, timeout: timeoutMs }, res => {
      let raw = '';
      res.setEncoding('utf8');
      res.on('data', chunk => { raw += chunk; });
      res.on('end', () => {
        let data;
        try { data = JSON.parse(raw); } catch { reject(new Error(`invalid JSON HTTP ${res.statusCode}`)); return; }
        if ((res.statusCode || 500) < 200 || (res.statusCode || 500) >= 300) {
          const err = new Error(`HTTP ${res.statusCode}: ${JSON.stringify(data).slice(0, 180)}`);
          err.status = res.statusCode;
          err.body = raw;
          reject(err);
          return;
        }
        resolve(data);
      });
    });
    req.on('timeout', () => req.destroy(new Error('translation request timeout')));
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function geminiRequest(body, timeoutMs, attempts = 4) {
  const key = (process.env.GEMINI_API_KEY || '').trim();
  if (!key) return null;
  // Yumuşak süre sınırı · bkz. gemini_zinciri.py sure_doldu()
  const son = Number(process.env.GEMINI_SON_TARIH || 0);
  if (son && Date.now() / 1000 > son) return null;
  // Düşünme token'ları maxOutputTokens'a sayılıyor · bkz. gemini_zinciri.py
  const parsed = JSON.parse(body);
  parsed.generationConfig = { ...(parsed.generationConfig || {}) };
  parsed.generationConfig.maxOutputTokens = Math.max(Number(parsed.generationConfig.maxOutputTokens) || 0, MIN_OUTPUT_TOKENS);
  const payload = JSON.stringify(parsed);
  let attempt = 0;
  for (;;) {
    const model = activeModel();
    if (!model) return null;
    const interval = process.env.GEMINI_MIN_INTERVAL != null
      ? Number(process.env.GEMINI_MIN_INTERVAL) * 1000
      : (60000 / (RPM.get(model) || 15)) * 1.05;
    const wait = lastRequestAt + interval - Date.now();
    if (wait > 0) await sleep(wait);
    lastRequestAt = Date.now();
    try {
      const data = await requestJson(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
      }, payload, timeoutMs);
      if (!responseText(data)) {
        const reason = data?.promptFeedback?.blockReason || data?.candidates?.[0]?.finishReason || 'boş yanıt';
        console.log(`  ! Gemini ${model}: yanıt kullanılamadı (${reason})`);
        recordFailure(model);
        return null;
      }
      consecutiveFailures.set(model, 0);
      return data;
    } catch (error) {
      const status = error?.status;
      const raw = String(error?.body || '');
      if (status) {
        const kind = classify(status, raw);
        if (kind === 'daily') {
          // Hangi kotanın bittiğini logla · gerekçe gemini_zinciri.py'de
          const quota = raw.match(/"quotaId"\s*:\s*"([^"]+)"/);
          dropModel(model, `günlük kota doldu (${quota ? quota[1] : 'quotaId yok'})`);
          attempt = 0;
          continue;
        }
        if (kind === 'model') { dropModel(model, `model kullanılamıyor (${status})`); attempt = 0; continue; }
        if (kind === 'key') { disableGemini(`HTTP ${status}`); return null; }
        if (kind === 'transient' && attempt < attempts - 1) {
          const hinted = raw.match(/"retryDelay"\s*:\s*"([0-9.]+)s"/);
          await sleep(hinted ? Math.min(Math.max(Number(hinted[1]), 1), 90) * 1000 : Math.min(5000 * (attempt + 1), 60000));
          attempt += 1;
          continue;
        }
        const st = raw.match(/"status"\s*:\s*"([A-Z_]+)"/);
        console.log(`  ! Gemini ${model}: istek başarısız (HTTP ${status}${st ? ' ' + st[1] : ''})`);
        recordFailure(model);
        return null;
      }
      // ağ hatası / zaman aşımı / geçersiz JSON
      if (attempt < attempts - 1) { await sleep(Math.min(5000 * (attempt + 1), 30000)); attempt += 1; continue; }
      recordFailure(model);
      return null;
    }
  }
}

function clean(value) {
  return String(value || '')
    .trim()
    .replace(/^```(?:text|plaintext)?\s*/i, '')
    .replace(/\s*```$/, '')
    .trim();
}

async function gemini(text, lang) {
  const key = (process.env.GEMINI_API_KEY || '').trim();
  if (!key) return null;
  const body = JSON.stringify({
    systemInstruction: { parts: [{ text:
      'You are a precise professional translator. Translate Turkish into the requested language. ' +
      'Return only the translation, without quotation marks, commentary, markdown, or language labels. ' +
      'Do not summarize, omit, or add claims. Preserve product names, repository names, URLs, and numbers.' }] },
    contents: [{ parts: [{ text:
      `Translate this Turkish technology-site text into ${lang}. Keep the meaning natural for the target locale.\n\n${text}` }] }],
    generationConfig: { temperature: 0.1, maxOutputTokens: 2048 },
  });
  const data = await geminiRequest(body, 60000);
  return clean(responseText(data)) || null;
}

async function gtx(text, lang) {
  // Yumuşak süre sınırı GTX yedeğini de kapsar · bkz. translation_service.py
  const son = Number(process.env.GEMINI_SON_TARIH || 0);
  if (son && Date.now() / 1000 > son) return null;
  const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl=${encodeURIComponent(lang)}&dt=t&q=${encodeURIComponent(text)}`;
  for (let attempt = 0; attempt < 3; attempt += 1) {
    try {
      const data = await requestJson(url, { method: 'GET', headers: { Accept: 'application/json', 'User-Agent': 'TreScout/1.0' } }, '', 20000);
      const result = clean((data?.[0] || []).map(part => part?.[0] || '').join(''));
      if (result) return result;
      throw new Error('GTX empty translation response');
    } catch (error) {
      const msg = String(error?.message || error);
      const retryable = /HTTP (429|500|502|503)|timeout|ECONNRESET/i.test(msg);
      if (!retryable || attempt === 2) return null;
      await sleep(Math.min(1500 * (2 ** attempt), 8000));
    }
  }
  return null;
}

async function translateText(text, lang) {
  const cleanText = String(text || '').trim();
  if (!cleanText) return '';
  return (await gemini(cleanText, lang)) || (await gtx(cleanText, lang));
}

module.exports = { translateText };


function parseJsonPayload(raw) {
  const trimmed = String(raw || '').trim();
  try {
    return JSON.parse(trimmed);
  } catch {
    const fenceMatch = trimmed.match(/```(?:json)?\s*([\s\S]*?)\s*```/i);
    if (fenceMatch) {
      try {
        return JSON.parse(fenceMatch[1].trim());
      } catch {}
    }
    const arrayMatch = trimmed.match(/\[\s*\{[\s\S]*\}\s*\]/);
    if (arrayMatch) {
      try {
        return JSON.parse(arrayMatch[0].trim());
      } catch {}
    }
    throw new Error('Could not parse JSON from Gemini response');
  }
}

async function geminiBatch(texts, lang) {
  const key = (process.env.GEMINI_API_KEY || '').trim();
  if (!key || !texts.length) return null;
  const body = JSON.stringify({
    systemInstruction: { parts: [{ text:
      'You are a precise professional translator. Output valid JSON only. Translate each Turkish item into the requested language. ' +
      'Preserve every id exactly, do not summarize, omit, merge, or add items. Preserve proper nouns, URLs, numbers, and technical meaning.' }] },
    contents: [{ parts: [{ text:
      `Translate every item into ${lang}. Return a JSON array with exactly one object per input, using the same id and the translated text in the text field.\n\n` +
      JSON.stringify(texts.map((text, index) => ({ id: String(index), text }))) }] }],
    generationConfig: { temperature: 0.1, maxOutputTokens: 8192, responseMimeType: 'application/json' },
  });
  // Kota/erişim hatasında (null) tekrar denemek sonucu değiştirmez; yalnız biçim
  // hatasında bir kez daha istenir.
  for (let attempt = 0; attempt < 2; attempt += 1) {
    const data = await geminiRequest(body, 90000);
    if (!data) return null;
    try {
      const raw = clean(responseText(data));
      const parsed = parseJsonPayload(raw);
      const rows = Array.isArray(parsed) ? parsed : parsed?.translations;
      if (!Array.isArray(rows) || rows.length !== texts.length) throw new Error('Gemini batch shape mismatch');
      const result = new Map();
      for (const row of rows) {
        const index = Number(row?.id);
        const value = clean(row?.text);
        if (!Number.isInteger(index) || index < 0 || index >= texts.length || !value) throw new Error('Gemini batch row invalid');
        result.set(texts[index], value);
      }
      if (result.size !== texts.length) throw new Error('Gemini batch ids are not unique');
      return result;
    } catch {
      // biçim hatası · bir kez daha dene
    }
  }
  return null;
}

async function translateTexts(texts, lang) {
  const unique = [...new Set(texts.map(text => String(text || '').trim()).filter(Boolean))];
  const result = new Map();
  const batchSize = 12;
  for (let start = 0; start < unique.length; start += batchSize) {
    const batch = unique.slice(start, start + batchSize);
    const translated = await geminiBatch(batch, lang);
    if (translated) {
      for (const [source, value] of translated) {
        if (value) result.set(source, value);
      }
    }
    for (const source of batch) {
      if (!result.has(source) || !result.get(source)) {
        const singleGemini = activeModel() ? await gemini(source, lang) : null;
        if (singleGemini) {
          result.set(source, singleGemini);
        } else {
          const gtxVal = await gtx(source, lang);
          if (gtxVal) result.set(source, gtxVal);
        }
      }
    }
  }
  return result;
}

module.exports = { translateText, translateTexts };
