#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 검색엔진에 URL을 알린다.

사용법:
  python3 tools/indexnow.py --all                 # sitemap.xml 의 모든 URL 제출
  python3 tools/indexnow.py --changed             # 직전 커밋 대비 변경된 페이지만 제출
  python3 tools/indexnow.py URL [URL ...]         # 지정한 URL 만 제출

키 파일({INDEXNOW_KEY}.txt)은 사이트 루트에 배포되어 있어야 한다.
구글은 IndexNow 미참여이므로 tools/google_indexing.py 를 사용한다.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)

# IndexNow 제출 엔드포인트. 하나에만 보내도 참여 엔진끼리 공유되지만,
# 전달 신뢰성을 위해 주요 엔드포인트에 모두 보낸다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def changed_urls():
    """직전 커밋 대비 변경/추가된 index.html 을 URL 로 변환."""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=ACMR", "HEAD~1", "HEAD"],
            cwd=ROOT, text=True,
        )
    except subprocess.CalledProcessError:
        return []
    urls = []
    for line in out.splitlines():
        line = line.strip()
        if line == "index.html":
            urls.append(BASE + "/")
        elif line.endswith("/index.html"):
            urls.append(BASE + "/" + line[: -len("index.html")])
    return urls


def submit(urls):
    urls = [u for u in dict.fromkeys(urls) if u.startswith(BASE)]
    if not urls:
        print("제출할 URL 이 없습니다.")
        return 0
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }).encode("utf-8")
    print(f"IndexNow 제출 {len(urls)}개 URL → {HOST}")
    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"  {ep} -> {resp.status} {resp.reason}")
        except urllib.error.HTTPError as e:
            # 200/202 외에도 일부 엔진은 빈 본문/4xx 를 반환할 수 있음
            print(f"  {ep} -> {e.code} {e.reason}")
        except Exception as e:  # noqa: BLE001
            print(f"  {ep} -> 오류: {e}")
    return len(urls)


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    if argv[0] == "--all":
        submit(sitemap_urls())
    elif argv[0] == "--changed":
        urls = changed_urls()
        if not urls:
            print("변경된 페이지가 없어 통보를 건너뜁니다.")
        else:
            submit(urls)
    else:
        submit(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
