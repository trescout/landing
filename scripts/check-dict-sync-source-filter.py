#!/usr/bin/env python3
"""Contract test for dict-sync glossary source selection.

This test is local-only: it imports definitions, creates temporary JSON fixtures,
and never calls Gemini, GitHub, Resend, or any endpoint.
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dict_sync', root / 'scripts' / 'dict-sync.py')
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_turkish_report_json('/tmp/trescout-rapor-2026-08-25.json')
assert module.is_turkish_report_json('/tmp/trescout-rapor-tekrarsiz-2026-08-25.json')
assert not module.is_turkish_report_json('/tmp/trescout-report-2026-08-25-en.json')
assert not module.is_turkish_report_json('/tmp/trescout-report-fresh-2026-08-25-fr.json')
assert module.is_turkish_report_pdf('/tmp/trescout-rapor-2026-08-25.pdf')
assert not module.is_turkish_report_pdf('/tmp/trescout-report-2026-08-25-de.pdf')

with tempfile.TemporaryDirectory() as directory:
    reports = Path(directory)
    (reports / 'trescout-rapor-2026-08-25.json').write_text(json.dumps({
        'glossary': [{'term': 'same term', 'explanation': 'Türkçe kaynak açıklaması.'}],
    }, ensure_ascii=False), encoding='utf-8')
    (reports / 'trescout-report-2026-08-25-en.json').write_text(json.dumps({
        'glossary': [{'term': 'same term', 'explanation': 'A much longer English explanation that must not be selected by the Turkish dictionary enrichment source.'}],
    }), encoding='utf-8')
    (reports / 'trescout-report-2026-08-25-fr.json').write_text(json.dumps({
        'glossary': [{'term': 'French-only term', 'explanation': 'Une explication qui ne doit pas entrer dans la source turque.'}],
    }), encoding='utf-8')
    original_reports = module.REPORTS
    module.REPORTS = str(reports)
    try:
        selected = module.collect_glossary()
    finally:
        module.REPORTS = original_reports
    assert selected == [{'term': 'same term', 'explanation': 'Türkçe kaynak açıklaması.'}], selected

print('✓ dict-sync glossary source filter contract passed')
