# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

# 네이버 서치어드바이저 사이트 소유확인 메타태그 (메인 페이지에만 삽입)
_NAVER = '<meta name="naver-site-verification" content="10ea6afce82c35f36193a7c0e14c3d6e8e9c7e67" />\n'

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "안산시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 안산시"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "안산시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 상록구·단원구 대표 행정동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "중앙역이나 초지역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "본오1동과 본오2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "본오1동부터 본오3동까지는 본오동 대표 페이지에서 통합 안내하며, 선부1~3동도 선부동 페이지로 묶어 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 안산시 전지역</p>
    <h1>안산 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>2개</strong><span>행정구</span></li>
      <li><strong>21개</strong><span>대표 행정동</span></li>
      <li><strong>13개</strong><span>역세권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>안산 출장마사지·홈타이 서비스 안내</h2>
<p>안산 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 그래서 이 페이지에서는 가능 지역, 예약 절차, 코스 선택 기준, 이용 전 확인사항을 한곳에 정리했습니다. 안산시는 상록구와 단원구 두 행정구로 나뉘고 생활권 성격이 서로 다르므로, 이 메인 페이지는 안산시 전체 구조를 설명하는 허브 역할을 하고 더 자세한 내용은 행정구별·대표 행정동별·지하철역별·테마별 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내해 드립니다.</p>
</section>

<section id="reason">
<h2>안산시에서 출장마사지를 찾는 이유</h2>
<p>안산은 상록구와 단원구로 나뉘고, 두 행정구의 생활권 성격이 다릅니다. 상록구는 상록수역·한대앞역·중앙역 주변의 주거·상권 수요가 있고, 사동과 해양동은 한양대 에리카와 시화호 인접 생활권을 함께 고려해야 합니다. 단원구는 고잔동·중앙동·호수동처럼 중심 상권과 행정 수요가 있는 지역이 있고, 원곡동·초지동·선부동·신길동은 역세권과 산업단지 이동 수요가 함께 있는 지역입니다. 같은 안산시라도 동마다 주거 형태와 생활 리듬이 달라 방문 시간대와 공간 준비 안내도 지역별로 조금씩 다릅니다.</p>
</section>

<section id="diff">
<h2>상록구·단원구 생활권 차이</h2>
<p>안산시 홈타이 안내에서 가장 중요한 부분은 행정구와 대표 행정동 구조를 정확하게 나누는 것입니다. 안산은 상록구와 단원구가 있으므로 메인 페이지 아래에 행정구 페이지를 먼저 두고, 그 아래 대표 행정동 페이지와 지하철역 페이지를 연결합니다. 번호가 붙은 행정동은 개별 페이지로 만들지 않습니다. 상록구의 본오1·2·3동은 본오동 대표 페이지로, 단원구의 선부1·2·3동은 선부동 대표 페이지로 통합합니다. 이렇게 하면 페이지 수는 줄지만 중복 콘텐츠 위험이 낮아지고, 이용자는 본인이 있는 지역을 더 빠르게 찾을 수 있습니다.</p>
</section>

<section id="coverage">
<h2>안산시 전지역 방문 가능 안내</h2>
<p>방문 범위는 안산시 전체입니다. 상록구는 상록수역·한대앞역·사리역·반월역 생활권을 중심으로, 단원구는 중앙역·고잔역·초지역·안산역·선부역·원시역 생활권을 중심으로 구성되어 있습니다. 거주하시거나 머무시는 위치의 생활권 특징과 방문 조건은 각 대표 행정동 페이지에서 확인하실 수 있습니다. 안산시 경계와 맞닿은 인접 지역도 위치에 따라 가능할 수 있으니 전화로 문의해 주세요.</p>
</section>

<section id="districts">
<h2>행정구별 안내</h2>
<p>행정구별 안내는 안산시의 두 허브인 상록구와 단원구로 나뉩니다. 각 페이지에서 해당 행정구의 생활권 성격과 주요 역세권, 대표 행정동을 한눈에 연결해 드립니다.</p>
<ul class="card-grid">
<li><a href="/ansan/sangnok-gu-chuljangmassage/">상록구 출장마사지</a></li>
<li><a href="/ansan/danwon-gu-chuljangmassage/">단원구 출장마사지</a></li>
</ul>
<p>안산시 전체 구조가 궁금하시면 <a href="/ansan/">안산시 전체 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>대표 행정동 페이지는 세부 지역 검색을 담당합니다. 각 페이지에서는 생활권 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다.</p>
<p class="sub-label">상록구</p>
<ul class="card-grid">
<li><a href="/ansan/sangnok/il-dong-chuljangmassage/">일동</a></li>
<li><a href="/ansan/sangnok/i-dong-chuljangmassage/">이동</a></li>
<li><a href="/ansan/sangnok/sa-dong-chuljangmassage/">사동</a></li>
<li><a href="/ansan/sangnok/sai-dong-chuljangmassage/">사이동</a></li>
<li><a href="/ansan/sangnok/haeyang-dong-chuljangmassage/">해양동</a></li>
<li><a href="/ansan/sangnok/bono-dong-chuljangmassage/">본오동</a></li>
<li><a href="/ansan/sangnok/bugok-dong-chuljangmassage/">부곡동</a></li>
<li><a href="/ansan/sangnok/wolpi-dong-chuljangmassage/">월피동</a></li>
<li><a href="/ansan/sangnok/seongpo-dong-chuljangmassage/">성포동</a></li>
<li><a href="/ansan/sangnok/banwol-dong-chuljangmassage/">반월동</a></li>
<li><a href="/ansan/sangnok/ansan-dong-chuljangmassage/">안산동</a></li>
</ul>
<p class="sub-label">단원구</p>
<ul class="card-grid">
<li><a href="/ansan/danwon/wa-dong-chuljangmassage/">와동</a></li>
<li><a href="/ansan/danwon/gojan-dong-chuljangmassage/">고잔동</a></li>
<li><a href="/ansan/danwon/jungang-dong-chuljangmassage/">중앙동</a></li>
<li><a href="/ansan/danwon/hosu-dong-chuljangmassage/">호수동</a></li>
<li><a href="/ansan/danwon/wongok-dong-chuljangmassage/">원곡동</a></li>
<li><a href="/ansan/danwon/baegun-dong-chuljangmassage/">백운동</a></li>
<li><a href="/ansan/danwon/singil-dong-chuljangmassage/">신길동</a></li>
<li><a href="/ansan/danwon/choji-dong-chuljangmassage/">초지동</a></li>
<li><a href="/ansan/danwon/seonbu-dong-chuljangmassage/">선부동</a></li>
<li><a href="/ansan/danwon/daebu-dong-chuljangmassage/">대부동</a></li>
</ul>
</section>

<section id="stations">
<h2>중앙역·초지역·안산역 주요 역세권 안내</h2>
<p>지하철역별 안내는 안산을 지나는 4호선(안산선)·수인분당선·서해선 주요 역세권을 기준으로 구성합니다. 중앙역 출장마사지, 고잔역 출장마사지, 초지역 출장마사지, 안산역 출장마사지, 상록수역 출장마사지처럼 실제 검색어와 가까운 제목을 사용해 검색 의도를 분명히 했습니다. 같은 역을 노선별로 나누면 중복 페이지 위험이 생기므로, 초지역처럼 여러 노선이 만나는 환승역도 페이지는 하나만 운영하고 본문에서 환승 특징과 주변 생활권을 설명합니다. 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/ansan/banwol-station-chuljangmassage/">반월역</a></li>
<li><a href="/ansan/sangnoksu-station-chuljangmassage/">상록수역</a></li>
<li><a href="/ansan/hanyang-univ-ansan-station-chuljangmassage/">한대앞역</a></li>
<li><a href="/ansan/sari-station-chuljangmassage/">사리역</a></li>
<li><a href="/ansan/jungang-station-chuljangmassage/">중앙역</a></li>
<li><a href="/ansan/gojan-station-chuljangmassage/">고잔역</a></li>
<li><a href="/ansan/choji-station-chuljangmassage/">초지역</a></li>
<li><a href="/ansan/ansan-station-chuljangmassage/">안산역</a></li>
<li><a href="/ansan/singiloncheon-station-chuljangmassage/">신길온천역</a></li>
<li><a href="/ansan/seonbu-station-chuljangmassage/">선부역</a></li>
<li><a href="/ansan/dalmi-station-chuljangmassage/">달미역</a></li>
<li><a href="/ansan/siu-station-chuljangmassage/">시우역</a></li>
<li><a href="/ansan/wonsi-station-chuljangmassage/">원시역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>안산 출장마사지 사이트 이용 가이드</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다. 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스이며, 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 안산시는 같은 시 안에서도 상록구 주거권, 단원구 중심 상권, 반월·시화 산업단지 생활권, 대부동 외곽 생활권의 이동 시간이 다를 수 있어 저녁 시간대나 주말에는 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>안산 홈타이 예약 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 특히 대부동, 반월동, 원시동·시화공단 인근은 차량 이동 기준이 중요할 수 있으므로 추가 이동비와 예약 가능 시간을 함께 확인해 주세요. 숙소나 오피스텔로 방문을 요청하실 때는 건물 출입 안내와 예약 시간대 연락 가능 여부를 알려주시면 됩니다. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 이용 전 서비스 범위와 유의사항을 확인해 주시고, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 안내드립니다. 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>안산시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 상록구·단원구 대표 행정동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>중앙역이나 초지역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>본오1동과 본오2동은 왜 따로 없나요?</h3>
<p>본오1동부터 본오3동까지는 본오동 대표 페이지에서, 선부1~3동은 선부동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>안산시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "안산 출장마사지·홈타이 | 안산시 전지역 방문 마사지 예약 안내",
    "desc": "안산 출장마사지·홈타이 예약 전 상록구, 단원구, 역세권 정보를 정리했습니다.",
    "h1": "안산 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
