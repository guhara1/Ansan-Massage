# 간다GO — 안산 출장마사지·홈타이 안내 사이트

경기도 안산시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (루트 /) + JSON-LD·히어로
  areas.py          # 지역: 안산시 허브 + 상록구·단원구 허브 (+ 대표 동 import)
  dong_sangnok.py   # 상록구 대표 행정동 11개
  dong_danwon.py    # 단원구 대표 행정동 10개
  stations.py       # 역 허브 (+ 역 13개 import)
  stations_data.py  # 지하철역 13개
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 허브 + 아티클
  about.py          # 운영자 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
  _builders.py      # 대표 동·역 페이지 공통 빌더
assets/             # CSS, 모바일 내비 JS, 파비콘
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## 페이지 구성 (스펙 42개 + 테마·매거진·코스 확장)

- 메인 1 (루트 `/`)
- 지역 허브 1 (`/ansan/`) + 행정구 2 (상록구·단원구)
- 대표 행정동 21 (상록구 11 + 단원구 10) — 번호 동(본오1~3동, 선부1~3동)은 대표 동으로 통합
- 지하철역 허브 1 (`/ansan/stations/`) + 역 13 (안산선·수인분당선·서해선)
- 안내 페이지: 안산 출장마사지(`/massage/`), 코스안내, 예약안내, 이용가이드, 후기, 고객센터, 개인정보처리방침, 이용약관
- 테마 허브 + 14개 테마, 매거진 허브 + 아티클, 운영자 소개

## URL 구조

```
/                                              메인
/ansan/                                        지역 허브
/ansan/sangnok-gu-chuljangmassage/             상록구
/ansan/danwon-gu-chuljangmassage/              단원구
/ansan/sangnok/{dong}-chuljangmassage/         상록구 대표 동
/ansan/danwon/{dong}-chuljangmassage/          단원구 대표 동
/ansan/stations/                               역 허브
/ansan/{역}-station-chuljangmassage/           지하철역
```

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 번호 행정동(본오1~3동, 선부1~3동)은 대표 동으로 통합 — 별도 색인 페이지 없음
- 환승역(초지역 등)도 URL 하나 — 노선별·출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 예정역(신안산선 한양대역, 성포역, 안산시청역, 초지역 KTX·신안산선)은 단독 페이지 없이 관련 동·역 본문에서 보조 설명
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 네이버 디스크립션은 80자 이내

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
4. `assets/og-image.png`, `icon-*.png`, `apple-touch-icon.png` 등 래스터 브랜드 이미지는
   간다GO 로고로 교체 (현재 SVG 파비콘은 브랜드 중립 다이아몬드 마크로 교체됨)

## 검색엔진 색인 (빠른 인덱싱)

### 소유확인·맵 파일 (빌드/커밋에 포함, 사이트 루트 제공)
- `sitemap.xml` — 색인 허용 페이지 전체 + `lastmod` (build.py 자동 생성)
- `rss.xml` — 매거진 글 피드 (네이버 서치어드바이저 RSS 제출용, build.py 자동 생성)
- `robots.txt` — `Sitemap:` 라인 포함
- `naver1bcd5202285eb31a097868b6f346d95c.html` — 네이버 HTML 소유확인
- 메인 페이지 `<head>` 의 `naver-site-verification` 메타태그 (메타 방식 병행)
- `127898ad5d2ed878af4659f45774aba9.txt` — IndexNow 키 파일

> 최초 1회: 네이버 서치어드바이저·구글 Search Console 에 사이트 등록 후
> `sitemap.xml` 과 (네이버) `rss.xml` 을 제출. 이후 색인 통보는 아래 자동화가 처리.

### IndexNow — 빙·네이버 즉시 색인 통보
```bash
python3 tools/indexnow.py --all        # sitemap 전체 제출
python3 tools/indexnow.py --changed    # 직전 커밋 대비 변경 페이지만
python3 tools/indexnow.py <URL> ...    # 지정 URL
```
키는 `content/site.py` 의 `INDEXNOW_KEY`, 키 파일은 루트의 `{KEY}.txt`. 둘이 일치해야 한다.
(구글은 IndexNow 미참여)

### Google Indexing API (선택, 보조 수단)
```bash
GOOGLE_SA_JSON='{서비스계정 키 JSON}' python3 tools/google_indexing.py --changed
```
- 서비스 계정에 Indexing API 권한 + Search Console 소유자 등록 필요
- 공식 지원 대상은 JobPosting/BroadcastEvent — 일반 페이지는 sitemap 제출이 정석

> 참고: 구글·빙의 비인증 `sitemap ping` 엔드포인트는 폐지되어 지원하지 않는다.
> 일반 페이지 색인은 ① Search Console sitemap 제출 + ② IndexNow(빙·네이버)가 가장 빠른 경로.

### 자동화 — 글 올릴 때마다 즉시 통보
`.github/workflows/index-notify.yml` 가 **프로덕션 브랜치(main) 푸시** 시 변경 URL을
IndexNow(빙·네이버)에 자동 통보한다. `GOOGLE_SA_JSON` 시크릿을 등록하면 구글에도 통보.
- 워크플로의 `branches: [main]` 을 Cloudflare Pages 의 프로덕션 브랜치와 일치시킬 것
- 수동 실행(`workflow_dispatch`)으로 `all`/`changed` 선택 가능
