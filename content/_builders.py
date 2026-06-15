# 대표 행정동 / 지하철역 페이지 공통 빌더.
# dong_sangnok.py, dong_danwon.py, stations.py 가 공유한다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING

_DONG_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_STATION_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>역 인근 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""


def dong_page(gu_slug, gu_name, gu_path, slug, name, title, desc, sections):
    """대표 행정동 페이지. path = ansan/{gu_slug}/{slug}/ (slug 에 -chuljangmassage 포함)."""
    return {
        "path": f"ansan/{gu_slug}/{slug}/",
        "title": title,
        "desc": desc,
        "h1": f"{name} 방문 관리 안내",
        "body": sections + PRICING + _DONG_CTA,
        "breadcrumb": [("지역별 안내", "/ansan/"), (gu_name, gu_path), (name, None)],
    }


def station_page(slug, name, title, desc, sections):
    """지하철역 페이지. path = ansan/{slug}/ (slug 에 -station-chuljangmassage 포함)."""
    return {
        "path": f"ansan/{slug}/",
        "title": title,
        "desc": desc,
        "h1": f"{name} 인근 방문 관리 안내",
        "body": sections + PRICING + _STATION_CTA,
        "breadcrumb": [("지하철역별 안내", "/ansan/stations/"), (name, None)],
    }
