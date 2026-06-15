#!/usr/bin/env python3
"""Google Indexing API 색인 통보.

구글은 IndexNow 에 참여하지 않으므로 별도 API 로 통보한다.
서비스 계정 키가 필요하며, 환경변수 GOOGLE_SA_JSON(키 JSON 내용 전체) 또는
GOOGLE_APPLICATION_CREDENTIALS(키 파일 경로)로 전달한다.
키가 없으면 아무 것도 하지 않고 정상 종료한다(자동화에서 안전하게 스킵).

사용법:
  GOOGLE_SA_JSON='{...}' python3 tools/google_indexing.py --all
  python3 tools/google_indexing.py --changed
  python3 tools/google_indexing.py URL [URL ...]

의존성: pip install google-auth requests

주의: Google Indexing API 는 공식적으로 JobPosting/BroadcastEvent 구조화 페이지를
대상으로 합니다. 일반 페이지에 대한 통보는 보장되지 않으므로, 일반 색인의
정석 경로는 Search Console 의 sitemap 제출입니다. 이 스크립트는 보조 수단입니다.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def _credentials():
    raw = os.environ.get("GOOGLE_SA_JSON", "").strip()
    path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
    if not raw and not path:
        return None
    try:
        from google.oauth2 import service_account  # type: ignore
    except ImportError:
        print("google-auth 미설치: pip install google-auth requests", file=sys.stderr)
        return None
    if raw:
        info = json.loads(raw)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return service_account.Credentials.from_service_account_file(path, scopes=SCOPES)


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def changed_urls():
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


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    creds = _credentials()
    if creds is None:
        print("구글 서비스 계정 키가 없어 Google Indexing API 통보를 건너뜁니다.")
        return
    import google.auth.transport.requests  # type: ignore
    import requests  # type: ignore

    if argv[0] == "--all":
        urls = sitemap_urls()
    elif argv[0] == "--changed":
        urls = changed_urls()
    else:
        urls = argv
    urls = [u for u in dict.fromkeys(urls) if u.startswith(BASE)]
    if not urls:
        print("제출할 URL 이 없습니다.")
        return

    creds.refresh(google.auth.transport.requests.Request())
    headers = {"Authorization": f"Bearer {creds.token}",
               "Content-Type": "application/json"}
    ok = 0
    for u in urls:
        body = json.dumps({"url": u, "type": "URL_UPDATED"})
        r = requests.post(ENDPOINT, data=body, headers=headers, timeout=30)
        print(f"  {u} -> {r.status_code}")
        if r.status_code == 200:
            ok += 1
    print(f"Google Indexing API: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main(sys.argv[1:])
