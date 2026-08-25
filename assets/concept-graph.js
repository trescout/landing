/**
 * TreScout · Sözlük İnteraktif Kavram Haritası (Knowledge Graph Component)
 * =======================================================================
 * Teknik kavramların ilişkilerini interaktif SVG grafiği olarak görselleştirir.
 * Sıfır harici bağımlılık, erişilebilir ve hafif.
 */

(function () {
  'use strict';

  // Temel Kavram Ağacı İlişkileri (Knowledge Graph Model)
  var GRAPH_DATA = {
    nodes: [
      { id: 'llm', label: 'LLM', full: 'Large Language Model', cat: 'ai', slug: 'llm', r: 24 },
      { id: 'rag', label: 'RAG', full: 'Retrieval-Augmented Generation', cat: 'ai', slug: 'rag', r: 22 },
      { id: 'fine-tuning', label: 'Fine-tuning', full: 'Model Özelleştirme', cat: 'ai', slug: 'fine-tuning', r: 18 },
      { id: 'ai-agent', label: 'AI Agent', full: 'Otonom Yapay Zekâ Ajanı', cat: 'ai', slug: 'ai-agent', r: 22 },
      { id: 'multi-agent', label: 'Multi-Agent', full: 'Çoklu Ajan Mimarisi', cat: 'ai', slug: 'multi-agent', r: 18 },
      { id: 'mcp', label: 'MCP', full: 'Model Context Protocol', cat: 'ai', slug: 'mcp', r: 20 },
      { id: 'prompt-as-code', label: 'Prompt as Code', full: 'Kod Olarak İstem', cat: 'dev', slug: 'prompt-as-code', r: 16 },
      { id: 'local-first', label: 'Local-First', full: 'Yerel Öncelikli Mimari', cat: 'arch', slug: 'local-first', r: 18 },
      { id: 'ai-engineering', label: 'AI Engineering', full: 'Yapay Zekâ Mühendisliği', cat: 'dev', slug: 'ai-engineering', r: 20 }
    ],
    links: [
      { source: 'llm', target: 'rag' },
      { source: 'llm', target: 'fine-tuning' },
      { source: 'llm', target: 'ai-agent' },
      { source: 'ai-agent', target: 'multi-agent' },
      { source: 'ai-agent', target: 'mcp' },
      { source: 'rag', target: 'mcp' },
      { source: 'llm', target: 'prompt-as-code' },
      { source: 'ai-engineering', target: 'llm' },
      { source: 'ai-engineering', target: 'prompt-as-code' },
      { source: 'local-first', target: 'llm' }
    ]
  };

  function initConceptGraph(container) {
    var width = container.clientWidth || 700;
    var height = 400;

    container.innerHTML = [
      '<div class="kg-wrap">',
      '  <div class="kg-header">',
      '    <span class="kg-title">🕸️ İnteraktif Kavram Ağı</span>',
      '    <div class="kg-legend">',
      '      <span class="kg-badge kg-cat-ai">Yapay Zekâ</span>',
      '      <span class="kg-badge kg-cat-dev">Geliştirici</span>',
      '      <span class="kg-badge kg-cat-arch">Mimari</span>',
      '    </div>',
      '  </div>',
      '  <div class="kg-canvas-wrap">',
      '    <svg class="kg-svg" viewBox="0 0 ' + width + ' ' + height + '" preserveAspectRatio="xMidYMid meet"></svg>',
      '    <div class="kg-tooltip" style="display:none;"></div>',
      '  </div>',
      '</div>'
    ].join('\n');

    var svg = container.querySelector('.kg-svg');
    var tooltip = container.querySelector('.kg-tooltip');

    // Basit dairesel / kuvvet yerleşimi hesabı
    var centerX = width / 2;
    var centerY = height / 2;
    var radius = Math.min(width, height) * 0.38;

    var nodeMap = {};
    GRAPH_DATA.nodes.forEach(function (node, idx) {
      if (node.id === 'llm') {
        node.x = centerX;
        node.y = centerY;
      } else {
        var angle = ((idx - 1) / (GRAPH_DATA.nodes.length - 1)) * 2 * Math.PI;
        node.x = centerX + radius * Math.cos(angle);
        node.y = centerY + radius * Math.sin(angle);
      }
      nodeMap[node.id] = node;
    });

    // Çizgileri çiz
    var linksHtml = '';
    GRAPH_DATA.links.forEach(function (link) {
      var s = nodeMap[link.source];
      var t = nodeMap[link.target];
      if (s && t) {
        linksHtml += '<line class="kg-link" x1="' + s.x + '" y1="' + s.y + '" x2="' + t.x + '" y2="' + t.y + '" />';
      }
    });

    // Düğümleri çiz
    var nodesHtml = '';
    GRAPH_DATA.nodes.forEach(function (node) {
      nodesHtml += [
        '<g class="kg-node kg-node-' + node.cat + '" data-id="' + node.id + '" data-slug="' + node.slug + '" transform="translate(' + node.x + ',' + node.y + ')">',
        '  <circle r="' + node.r + '" class="kg-circle" />',
        '  <text class="kg-label" text-anchor="middle" dy="0.35em">' + node.label + '</text>',
        '</g>'
      ].join('\n');
    });

    svg.innerHTML = '<g class="kg-links">' + linksHtml + '</g><g class="kg-nodes">' + nodesHtml + '</g>';

    // Etkileşimler
    var nodeElements = svg.querySelectorAll('.kg-node');
    nodeElements.forEach(function (el) {
      var id = el.getAttribute('data-id');
      var node = nodeMap[id];

      el.addEventListener('mouseenter', function (e) {
        tooltip.style.display = 'block';
        tooltip.innerHTML = [
          '<strong>' + node.label + '</strong> ' + (node.full ? '<small>(' + node.full + ')</small>' : ''),
          '<p>İlişkili kavramları ve detaylı sözlük maddesini inceleyin.</p>',
          '<a class="kg-link-btn" href="/dictionary/' + node.slug + '/">Sözlükte Oku →</a>'
        ].join('\n');

        var rect = container.getBoundingClientRect();
        var left = node.x - (tooltip.offsetWidth / 2);
        var top = node.y - node.r - 80;

        tooltip.style.left = Math.max(10, Math.min(width - 220, left)) + 'px';
        tooltip.style.top = Math.max(10, top) + 'px';
      });

      el.addEventListener('click', function () {
        window.location.href = '/dictionary/' + node.slug + '/';
      });
    });

    container.addEventListener('mouseleave', function () {
      tooltip.style.display = 'none';
    });
  }

  window.TreScoutConceptGraph = {
    init: initConceptGraph
  };

  document.addEventListener('DOMContentLoaded', function () {
    var containers = document.querySelectorAll('.tre-concept-graph');
    containers.forEach(initConceptGraph);
  });
})();
