const https = require('https');

// Model zinciri · scripts/gemini_zinciri.py ile AYNI kurallar (iki dilde tek
// sözleşme; birini değiştirirseniz diğerini de değiştirin). Kota model başına:
// günlük kotası biten (429 + "PerDay") ya da bulunamayan (404) model bu koşuda
// bırakılır, sıradakine geçilir. Dakikalık 429'da beklenip aynı modelle denenir.
const MODELS = (process.env.GEMINI_MODELS || process.env.GEMINI_MODEL || process.env.TREESCOUT_TRANSLATION_MODEL
  || 'gemini-3.5-flash-lite,gemini-3.1-flash-lite').split(',').map(m => m.trim()).filter(Boolean);
const MIN_INTERVAL_MS = Number(process.env.GEMINI_MIN_INTERVAL || 4.2) * 1000;
const CONSECUTIVE_429_LIMIT = 3;
const exhausted = new Set();
const consecutive429 = new Map();
let lastRequestAt = 0;

function activeModel() {
  return MODELS.find(m => !exhausted.has(m)) || null;
}

function dropModel(model, reason) {
  exhausted.add(model);
  const next = activeModel();
  console.log(`  ! Gemini ${model}: ${reason} · ${next ? `${next} ile devam` : 'zincirde model kalmadı, Gemini bu koşuda kapalı'}`);
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
  let attempt = 0;
  for (;;) {
    const model = activeModel();
    if (!model) return null;
    const wait = lastRequestAt + MIN_INTERVAL_MS - Date.now();
    if (wait > 0) await sleep(wait);
    lastRequestAt = Date.now();
    try {
      const data = await requestJson(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
      }, body, timeoutMs);
      consecutive429.set(model, 0);
      return data;
    } catch (error) {
      const status = error?.status;
      const raw = String(error?.body || '');
      if (status === 429 && raw.includes('PerDay')) { dropModel(model, 'günlük kota doldu'); attempt = 0; continue; }
      if (status === 404) { dropModel(model, 'model bulunamadı (404)'); attempt = 0; continue; }
      const msg = String(error?.message || error);
      const retryable = [429, 500, 502, 503].includes(status) || /timeout|ECONNRESET|UNAVAILABLE/i.test(msg);
      if (retryable && attempt < attempts - 1) {
        const hinted = raw.match(/"retryDelay"\s*:\s*"([0-9.]+)s"/);
        await sleep(hinted ? Math.min(Math.max(Number(hinted[1]), 1), 90) * 1000 : Math.min(5000 * (attempt + 1), 60000));
        attempt += 1;
        continue;
      }
      if (status === 429) {
        const n = (consecutive429.get(model) || 0) + 1;
        consecutive429.set(model, n);
        if (n >= CONSECUTIVE_429_LIMIT) dropModel(model, `üst üste ${CONSECUTIVE_429_LIMIT} kez 429`);
      }
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
  const textParts = data?.candidates?.[0]?.content?.parts || [];
  return clean(textParts.map(part => part?.text || '').join('')) || null;
}

async function gtx(text, lang) {
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
      const raw = clean((data?.candidates?.[0]?.content?.parts || []).map(part => part?.text || '').join(''));
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
