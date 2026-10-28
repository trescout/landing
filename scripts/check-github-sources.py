#!/usr/bin/env python3
"""Keşif kaynakları için GitHub bütünlük guard'ı.

Tüm yayımlanmış keşif Markdown sayfalarındaki GitHub repo URL'lerini normalize
eder; 404/private/disabled kaynaklarda CI'ı kırar, arşivlenmiş depoları görünür
uyarı olarak raporlar. GitHub API için GITHUB_TOKEN veya GH_TOKEN önerilir.
"""
import concurrent.futures
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISC = os.path.join(ROOT, "discover")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "trescout-github-source-guard",
}
if TOKEN:
    HEADERS["Authorization"] = "Bearer " + TOKEN

# Kod örneklerindeki yer tutucular ve gerçek repo olmayan GitHub yolları.
IGNORE = {
    "features/actions",
    "majd/repo",
    "orgs",
    "topics",
    "settings",
    "user/my-skill",
    "yourorg/yourrepo",
    "your-username/your-new-repository",
}


def repos_from_catalog():
    found = set()
    pattern = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?)")
    for path in glob.glob(os.path.join(DISC, "*.md")):
        text = open(path, encoding="utf-8", errors="ignore").read()
        for raw in pattern.findall(text):
            repo = raw.rstrip(".,)/").split("#", 1)[0]
            if repo.lower().endswith(".git"):
                repo = repo[:-4]
            if repo.lower() not in IGNORE:
                found.add(repo)
    return sorted(found)


def check(repo):
    req = urllib.request.Request(
        "https://api.github.com/repos/" + repo,
        headers=HEADERS,
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.load(response)
            return {
                "repo": repo,
                "status": response.status,
                "archived": bool(data.get("archived")),
                "disabled": bool(data.get("disabled")),
            }
    except urllib.error.HTTPError as error:
        return {"repo": repo, "status": error.code}
    except Exception as error:  # network/DNS/timeout: unsafe to publish blindly
        return {"repo": repo, "status": "error", "error": str(error)[:160]}


def main():
    repos = repos_from_catalog()
    print(f"GitHub kaynak guard: {len(repos)} benzersiz depo kontrol ediliyor")
    workers = min(8, max(1, len(repos)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(check, repos))

    missing = [r for r in results if r["status"] != 200 or r.get("disabled")]
    archived = [r for r in results if r["status"] == 200 and r.get("archived")]
    for item in archived:
        print(f"::warning::Arşivlenmiş GitHub kaynağı: {item['repo']}")
    for item in missing:
        print(f"::error::Geçersiz GitHub kaynağı: {json.dumps(item, ensure_ascii=False)}")

    print(f"GitHub kaynak guard özeti: sağlıklı={len(results)-len(missing)} arşivli={len(archived)} geçersiz={len(missing)}")
    if missing:
        print("Katalogda 404/private/disabled/erişilemeyen kaynak var; yayın durduruldu.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
