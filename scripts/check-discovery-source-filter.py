#!/usr/bin/env python3
"""Contract test for discover-sync GitHub item source selection.

This test is local-only: it imports definitions, creates temporary JSON fixtures,
and never calls Gemini, GitHub, or any remote endpoint.
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('discover_sync', root / 'scripts' / 'discover-sync.py')
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_turkish_report_json('/tmp/trescout-rapor-2026-08-25.json')
assert module.is_turkish_report_json('/tmp/trescout-rapor-tekrarsiz-2026-08-25.json')
assert not module.is_turkish_report_json('/tmp/trescout-report-2026-08-25-en.json')
assert not module.is_turkish_report_json('/tmp/trescout-report-fresh-2026-08-25-fr.json')
assert not module.is_turkish_report_json('/tmp/trescout-report-2026-08-25-pt.json')

with tempfile.TemporaryDirectory() as directory:
    reports = Path(directory)
    (reports / 'trescout-rapor-2026-08-25.json').write_text(json.dumps({
        'date': '2026-08-25',
        'sections': [{
            'sourceName': 'github',
            'items': [{
                'title': 'owner/turkish-project',
                'url': 'https://github.com/owner/turkish-project',
                'summary': 'Bu proje Türkçe özet metnidir.',
                'meta': 'Python · ★ 1.234 · +123 bugün'
            }]
        }]
    }, ensure_ascii=False), encoding='utf-8')
    (reports / 'trescout-report-2026-08-25-pt.json').write_text(json.dumps({
        'date': '2026-08-25',
        'sections': [{
            'sourceName': 'github',
            'items': [{
                'title': 'owner/turkish-project',
                'url': 'https://github.com/owner/turkish-project',
                'summary': 'Este projeto tem texto em português que não deve sobrepor o turco.',
                'meta': 'Python · ★ 1.234 · +123 hoje'
            }]
        }]
    }, ensure_ascii=False), encoding='utf-8')
    (reports / 'trescout-report-2026-08-25-en.json').write_text(json.dumps({
        'date': '2026-08-25',
        'sections': [{
            'sourceName': 'github',
            'items': [{
                'title': 'owner/english-only',
                'url': 'https://github.com/owner/english-only',
                'summary': 'English-only summary that must not enter Turkish catalog.',
                'meta': 'Python · ★ 500 · +50 today'
            }]
        }]
    }, ensure_ascii=False), encoding='utf-8')
    original_reports = module.REPORTS
    module.REPORTS = str(reports)
    try:
        items = module.report_items()
    finally:
        module.REPORTS = original_reports

    assert len(items) == 1, f"Expected 1 item, got {len(items)}"
    assert items[0]['title'] == 'owner/turkish-project'
    assert items[0]['summary'] == 'Bu proje Türkçe özet metnidir.'

print('✓ discover-sync source filter contract passed')
