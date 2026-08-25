#!/usr/bin/env node
/**
 * TreScout Model Context Protocol (MCP) Server
 * ============================================
 * Enables Claude Desktop, Cursor, Antigravity, and AI Agents to query
 * TreScout's catalog of 470+ open source tools, 530+ dictionary terms,
 * and daily tech intelligence reports.
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const ROOT_DIR = path.resolve(__dirname, '../..');
const CATALOG_PATH = path.join(ROOT_DIR, 'assets', 'discover', 'catalog.json');
const DICTIONARY_PATH = path.join(ROOT_DIR, 'assets', 'dictionary', 'dictionary.json');
const REPORTS_DIR = path.join(ROOT_DIR, 'reports');

// Load Data In-Memory
let catalogData = [];
let dictionaryData = [];

function loadData() {
  try {
    if (fs.existsSync(CATALOG_PATH)) {
      catalogData = JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf8'));
    }
  } catch (e) {
    catalogData = [];
  }

  try {
    if (fs.existsSync(DICTIONARY_PATH)) {
      dictionaryData = JSON.parse(fs.readFileSync(DICTIONARY_PATH, 'utf8'));
    }
  } catch (e) {
    dictionaryData = [];
  }
}

loadData();

// MCP Tool Definitions
const TOOLS = [
  {
    name: 'search_tools',
    description: 'Search TreScout catalog of 470+ curated open-source projects, CLI tools, and AI repositories.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Keyword to search across project titles, descriptions, and tags (e.g. "rust", "agent", "scraper").'
        },
        tag: {
          type: 'string',
          description: 'Filter by specific tag (e.g. "Yapay zekâ araçları", "Geliştirici aracı").'
        },
        limit: {
          type: 'number',
          description: 'Maximum number of results to return (default: 10, max: 50).'
        }
      }
    }
  },
  {
    name: 'get_tool_detail',
    description: 'Get detailed overview, installation commands, multilingual taglines, and update history for a specific open-source tool.',
    inputSchema: {
      type: 'object',
      properties: {
        slug: {
          type: 'string',
          description: 'Unique project slug (e.g. "understand-anything", "claude-code", "tradingagents").'
        }
      },
      required: ['slug']
    }
  },
  {
    name: 'lookup_term',
    description: 'Look up technical software and AI terms in TreScout dictionary with definitions in Turkish, English, and analogies.',
    inputSchema: {
      type: 'object',
      properties: {
        term: {
          type: 'string',
          description: 'Concept or abbreviation to lookup (e.g. "rag", "fine-tuning", "prompt-as-code", "mcp").'
        }
      },
      required: ['term']
    }
  },
  {
    name: 'get_daily_report',
    description: 'Get TreScout daily tech intelligence report overview, highlighted projects, and editorial summary for a given date or latest.',
    inputSchema: {
      type: 'object',
      properties: {
        date: {
          type: 'string',
          description: 'Date in YYYY-MM-DD format (e.g. "2026-08-25"). Leave empty to get the latest available report.'
        }
      }
    }
  },
  {
    name: 'list_recent_reports',
    description: 'List recent TreScout daily tech intelligence reports available in the archive.',
    inputSchema: {
      type: 'object',
      properties: {
        limit: {
          type: 'number',
          description: 'Number of recent reports to list (default: 10).'
        }
      }
    }
  }
];

// Tool Executors
function handleSearchTools(args) {
  loadData();
  const query = (args.query || '').trim().toLowerCase();
  const tag = (args.tag || '').trim().toLowerCase();
  const limit = Math.min(Math.max(Number(args.limit) || 10, 1), 50);

  let results = catalogData;

  if (query) {
    results = results.filter(item => {
      const matchTitle = (item.title || '').toLowerCase().includes(query);
      const matchTagline = (item.tagline || '').toLowerCase().includes(query);
      const matchTaglineEn = (item.tagline_en || '').toLowerCase().includes(query);
      const matchTags = (item.tags || []).some(t => t.toLowerCase().includes(query));
      const matchSlug = (item.slug || '').toLowerCase().includes(query);
      return matchTitle || matchTagline || matchTaglineEn || matchTags || matchSlug;
    });
  }

  if (tag) {
    results = results.filter(item => {
      return (item.tags || []).some(t => t.toLowerCase().includes(tag));
    });
  }

  results = results.slice(0, limit).map(item => ({
    slug: item.slug,
    title: item.title,
    tagline: item.tagline,
    tagline_en: item.tagline_en || item.tagline,
    stars: item.stars,
    tags: item.tags || [],
    date_discovered: item.date,
    url: `https://trescout.com/discover/${item.slug}/`
  }));

  return {
    total_found: results.length,
    tools: results
  };
}

function handleGetToolDetail(args) {
  loadData();
  const slug = (args.slug || '').trim().toLowerCase();
  if (!slug) throw new Error('Missing required parameter: slug');

  const tool = catalogData.find(item => item.slug.toLowerCase() === slug);
  if (!tool) {
    return { error: `Tool not found for slug: "${slug}"` };
  }

  return {
    slug: tool.slug,
    title: tool.title,
    headline: tool.headline || tool.title,
    tagline: tool.tagline,
    tagline_en: tool.tagline_en || '',
    meta: tool.meta || '',
    stars: tool.stars || 0,
    tags: tool.tags || [],
    date: tool.date,
    last_review: tool.last_review || tool.date,
    updates: tool.guncellemeler || [],
    commands: tool.cmds || {},
    web_url: `https://trescout.com/discover/${tool.slug}/`,
    english_url: `https://trescout.com/en/discover/${tool.slug}/`
  };
}

function handleLookupTerm(args) {
  loadData();
  const termQuery = (args.term || '').trim().toLowerCase();
  if (!termQuery) throw new Error('Missing required parameter: term');

  const directMatch = dictionaryData.find(item =>
    item.slug.toLowerCase() === termQuery ||
    (item.en && item.en.toLowerCase() === termQuery) ||
    (item.full && item.full.toLowerCase() === termQuery)
  );

  if (directMatch) {
    return {
      slug: directMatch.slug,
      term: directMatch.en || directMatch.slug,
      full_name: directMatch.full || '',
      category: directMatch.cat || 'general',
      definition_tr: directMatch.kisa || '',
      definition_en: directMatch.kisa_en || '',
      web_url: `https://trescout.com/dictionary/${directMatch.slug}/`
    };
  }

  // Fuzzy match
  const results = dictionaryData.filter(item =>
    (item.slug && item.slug.toLowerCase().includes(termQuery)) ||
    (item.en && item.en.toLowerCase().includes(termQuery)) ||
    (item.kisa && item.kisa.toLowerCase().includes(termQuery)) ||
    (item.full && item.full.toLowerCase().includes(termQuery))
  ).slice(0, 5).map(item => ({
    slug: item.slug,
    term: item.en || item.slug,
    full_name: item.full || '',
    definition_tr: item.kisa || '',
    definition_en: item.kisa_en || '',
    web_url: `https://trescout.com/dictionary/${item.slug}/`
  }));

  if (results.length > 0) {
    return { matches: results };
  }

  return { error: `No dictionary term found matching: "${termQuery}"` };
}

function handleGetDailyReport(args) {
  let targetDate = (args.date || '').trim();

  // If no date specified, pick latest report from reports folder
  if (!targetDate && fs.existsSync(REPORTS_DIR)) {
    const dates = fs.readdirSync(REPORTS_DIR)
      .filter(d => /^\d{4}-\d{2}-\d{2}$/.test(d))
      .sort()
      .reverse();
    if (dates.length > 0) {
      targetDate = dates[0];
    }
  }

  if (!targetDate) {
    return { error: 'No report found.' };
  }

  const reportPath = path.join(REPORTS_DIR, targetDate, 'index.html');
  if (!fs.existsSync(reportPath)) {
    return { error: `Report not found for date: ${targetDate}` };
  }

  const html = fs.readFileSync(reportPath, 'utf8');

  // Extract structured editorial & metadata
  const titleMatch = html.match(/<h1 class="rep-title">(.*?)<\/h1>/);
  const editorialMatch = html.match(/<p class="rep-editorial">(.*?)<\/p>/);
  const chipsMatch = html.match(/<div class="rep-chips">(.*?)<\/div>/);
  const capturedMatch = html.match(/<p class="rep-captured"[^>]*>(.*?)<\/p>/);

  const featuredTools = [];
  const toolRegex = /<a class="rep-link-item" href="\/discover\/([^/]+)\/">([^<]+)<\/a>/g;
  let match;
  while ((match = toolRegex.exec(html)) !== null) {
    featuredTools.push({ slug: match[1], name: match[2].replace(' →', '').trim() });
  }

  const featuredTerms = [];
  const termRegex = /<a class="rep-link-item" href="\/dictionary\/([^/]+)\/">([^<]+)<\/a>/g;
  while ((match = termRegex.exec(html)) !== null) {
    featuredTerms.push({ slug: match[1], name: match[2].replace(' →', '').trim() });
  }

  return {
    date: targetDate,
    title: titleMatch ? titleMatch[1].replace(/<[^>]+>/g, '').trim() : targetDate,
    editorial_summary: editorialMatch ? editorialMatch[1].replace(/<[^>]+>/g, '').trim() : '',
    chips: chipsMatch ? chipsMatch[1].replace(/<[^>]+>/g, ' · ').replace(/\s+/g, ' ').trim() : '',
    captured: capturedMatch ? capturedMatch[1].replace(/<[^>]+>/g, '').trim() : '',
    featured_tools: featuredTools,
    featured_terms: featuredTerms,
    report_url: `https://trescout.com/reports/${targetDate}/`,
    pdf_url: `https://trescout.com/reports/trescout-rapor-${targetDate}.pdf`
  };
}

function handleListRecentReports(args) {
  const limit = Math.min(Math.max(Number(args.limit) || 10, 1), 30);
  if (!fs.existsSync(REPORTS_DIR)) {
    return { reports: [] };
  }

  const dates = fs.readdirSync(REPORTS_DIR)
    .filter(d => /^\d{4}-\d{2}-\d{2}$/.test(d))
    .sort()
    .reverse()
    .slice(0, limit);

  const reports = dates.map(date => {
    const p = path.join(REPORTS_DIR, date, 'index.html');
    let editorial = '';
    if (fs.existsSync(p)) {
      const html = fs.readFileSync(p, 'utf8');
      const m = html.match(/<p class="rep-editorial">(.*?)<\/p>/);
      if (m) editorial = m[1].replace(/<[^>]+>/g, '').trim().slice(0, 160) + '...';
    }
    return {
      date: date,
      preview: editorial,
      url: `https://trescout.com/reports/${date}/`
    };
  });

  return {
    count: reports.length,
    reports: reports
  };
}

// Dispatch tool calls
async function callTool(name, args) {
  switch (name) {
    case 'search_tools':
      return handleSearchTools(args);
    case 'get_tool_detail':
      return handleGetToolDetail(args);
    case 'lookup_term':
      return handleLookupTerm(args);
    case 'get_daily_report':
      return handleGetDailyReport(args);
    case 'list_recent_reports':
      return handleListRecentReports(args);
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

// JSON-RPC Message Processor over Stdio
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

function sendResponse(id, result) {
  const message = {
    jsonrpc: '2.0',
    id: id,
    result: result
  };
  process.stdout.write(JSON.stringify(message) + '\n');
}

function sendError(id, code, message, data) {
  const response = {
    jsonrpc: '2.0',
    id: id,
    error: {
      code: code,
      message: message,
      data: data
    }
  };
  process.stdout.write(JSON.stringify(response) + '\n');
}

rl.on('line', async (line) => {
  const trimmed = line.trim();
  if (!trimmed) return;

  try {
    const request = JSON.parse(trimmed);
    const { id, method, params } = request;

    // Handle Notifications (no ID)
    if (id === undefined || id === null) {
      if (method === 'notifications/initialized') {
        // acknowledged
      }
      return;
    }

    if (method === 'initialize') {
      sendResponse(id, {
        protocolVersion: '2024-11-05',
        capabilities: {
          tools: {}
        },
        serverInfo: {
          name: 'trescout-mcp',
          version: '1.0.0'
        }
      });
    } else if (method === 'tools/list') {
      sendResponse(id, { tools: TOOLS });
    } else if (method === 'tools/call') {
      const toolName = params ? params.name : '';
      const toolArgs = (params && params.arguments) || {};

      try {
        const output = await callTool(toolName, toolArgs);
        sendResponse(id, {
          content: [
            {
              type: 'text',
              text: JSON.stringify(output, null, 2)
            }
          ]
        });
      } catch (err) {
        sendResponse(id, {
          isError: true,
          content: [
            {
              type: 'text',
              text: `Error executing ${toolName}: ${err.message}`
            }
          ]
        });
      }
    } else if (method === 'ping') {
      sendResponse(id, {});
    } else {
      sendError(id, -32601, `Method not found: ${method}`);
    }
  } catch (err) {
    sendError(null, -32700, `Parse error: ${err.message}`);
  }
});
