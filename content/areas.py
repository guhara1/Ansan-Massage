# 지역별 안내 — 안산시 허브 + 행정구 2개(상록구·단원구) + 대표 행정동 21개.
# 번호 행정동(본오1~3동, 선부1~3동)은 개별 페이지를 만들지 않고 대표 동으로 통합한다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from .dong_sangnok import PAGES as SANGNOK_DONGS
from .dong_danwon import PAGES as DANWON_DONGS

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

# ── 안산시 전체 허브 ──────────────────────────────────────────────
_HUB_BODY = """
<p class="lead">안산시 방문 관리는 상록구와 단원구 두 행정구를 허브로 두고, 그 아래 대표 행정동과 지하철역을 연결하는 구조로 안내합니다. 거주하시는 행정동이 숫자로 나뉘어 있어도 아래 대표 동 페이지에서 모든 정보를 확인하실 수 있습니다.</p>

<section>
<h2>안산시 지역 안내 구성</h2>
<p>안산시는 상록구와 단원구 두 개의 행정구로 이루어져 있습니다. 상록구는 상록수역·한대앞역·중앙역 주변 주거·상권과 한양대 에리카·시화호 인접 생활권이 섞여 있고, 단원구는 고잔동·중앙동·호수동의 중심 상권과 원곡동·초지동·선부동·신길동의 역세권·산업단지 생활권이 함께 있습니다. 이 사이트는 행정구 페이지를 먼저 두고 그 아래 대표 행정동 페이지와 지하철역 페이지를 연결합니다. 행정동을 잘게 쪼개면 같은 생활권을 두고 비슷한 설명이 반복되기 때문에, 대표 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 검색엔진에도 명확합니다.</p>
</section>

<section>
<h2>두 개의 행정구</h2>
<ul class="card-grid">
<li><a href="/ansan/sangnok-gu-chuljangmassage/">상록구 출장마사지</a></li>
<li><a href="/ansan/danwon-gu-chuljangmassage/">단원구 출장마사지</a></li>
</ul>
<p>상록구 페이지는 상록수역·한대앞역·사리역·반월역 생활권을 중심으로, 단원구 페이지는 중앙역·고잔역·초지역·안산역·선부역·원시역 생활권을 중심으로 작성되어 있습니다. 본인이 계신 위치가 어느 행정구인지 헷갈리신다면 행정구 페이지에서 대표 동 목록을 보고 가까운 동을 고르시면 됩니다.</p>
</section>

<section>
<h2>상록구 대표 행정동</h2>
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
<p>본오1동·본오2동·본오3동은 본오동 페이지 하나에서 통합 안내합니다. 숫자 동 단위 개별 페이지는 만들지 않는 것이 원칙이며, 방문은 행정동 경계가 아니라 정확한 주소로 안내됩니다.</p>
</section>

<section>
<h2>단원구 대표 행정동</h2>
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
<p>선부1동·선부2동·선부3동은 선부동 페이지로 통합합니다. 대부동은 대부도 외곽 생활권으로 차량 이동 기준이 중요해, 예약 전 추가 이동비와 가능 시간을 함께 확인해 주시는 것이 좋습니다.</p>
</section>

<section>
<h2>지역과 역세권을 함께 확인하세요</h2>
<p>안산은 4호선(안산선)·수인분당선·서해선이 지나는 지역이라 동 기준보다 역 기준이 익숙한 분들도 많습니다. 중앙역, 초지역, 안산역, 상록수역 인근 위치에서 예약하실 때는 <a href="/ansan/stations/">지하철역별 안내</a>를 함께 확인해 보세요. 역 페이지에서는 해당 역세권의 생활권과 인접 동을 연결해 설명합니다. 다만 역과 동, 테마를 조합한 별도 페이지는 운영하지 않으므로, 원하시는 관리 유형은 <a href="/themes/">테마별 안내</a>에서 따로 확인하시면 됩니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>어느 동이든 예약 절차는 동일합니다. 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정 순서로 진행되며, 저녁 시간대와 주말은 문의가 몰릴 수 있어 미리 연락 주시는 편이 좋습니다. 아파트 단지는 동·호수와 공동현관 출입 방법을, 오피스텔과 숙소는 건물 출입 안내를 함께 알려주시면 방문이 한층 매끄럽습니다. 안산시 경계와 맞닿은 군포, 수원, 시흥, 화성 방면 주소도 위치에 따라 방문이 가능할 수 있으니 전화로 확인해 주세요. 자세한 준비사항은 <a href="/guide/">이용가이드</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>안산시 생활권과 방문 수요</h2>
<p>안산시는 같은 시 안에서도 생활권의 성격이 크게 갈립니다. 상록구의 상록수역·한대앞역 주거권은 대단지 아파트 중심이라 가족 단위 자택 예약이 많고, 한양대 에리카가 있는 사동·해양동은 학생과 1인 가구의 원룸 방문 수요가 학기 일정에 따라 오르내립니다. 단원구의 중앙역·안산역 중심 상권은 숙박·오피스텔이 밀집해 늦은 시간 숙소 방문 문의가 많고, 신길동·초지동·원시동의 반월·시화 산업단지 생활권은 교대 근무자의 시간대별 예약이 더해집니다. 대부동은 대부도 외곽이라 차량 이동을 전제로 한 예약이 기본입니다. 이렇게 주거형·상권형·산업단지형·외곽형 생활권이 한 도시 안에 모두 있어, 같은 안산이라도 방문 시간대와 준비 안내가 지역마다 달라집니다. 본인 위치가 어느 생활권에 가까운지 보면 어느 동·역 페이지를 봐야 할지 빠르게 판단하실 수 있습니다.</p>
</section>

<section>
<h2>처음 이용하실 때</h2>
<p>안산에서 방문 관리를 처음 이용하신다면 위치 기준부터 정하시면 편합니다. 거주지나 숙소가 어느 동·역에 가까운지 먼저 확인한 뒤, 해당 페이지에서 생활권 특징과 방문 조건을 보시고, 원하는 관리 유형은 <a href="/themes/">테마별 안내</a>에서 고르신 다음 예약 전화로 위치와 시간을 알려주시면 됩니다. 가격과 코스 구성은 <a href="/courses/">코스안내</a>에, 결제·변경·취소 기준은 <a href="/reservation/">예약안내</a>에 정리되어 있으니 예약 전에 한 번 확인해 두시면 상담이 훨씬 빠르게 진행됩니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>우리 동네 행정동 이름이 안 보여요.</h3>
<p>번호가 붙은 행정동은 대표 동 페이지에 통합되어 있습니다. 예를 들어 본오2동은 본오동 페이지, 선부3동은 선부동 페이지를 보시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>동 경계가 애매한 위치는 어떻게 하나요?</h3>
<p>경계 지역은 어느 동 페이지를 보셔도 무방합니다. 실제 방문은 주소 기준으로 진행되므로 예약 전화에서 정확한 주소만 알려주시면 됩니다.</p>
</div>
</section>
""" + PRICING + _CTA

_HUB = {
    "path": "ansan/",
    "title": "안산 지역별 출장마사지·홈타이 | 상록구·단원구 방문 안내",
    "desc": "안산 출장마사지·홈타이 지역 안내입니다. 상록구·단원구와 대표 행정동을 확인하세요.",
    "h1": "안산시 지역별 방문 관리 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지역별 안내", None)],
}

# ── 상록구 허브 ───────────────────────────────────────────────────
_SANGNOK_BODY = """
<p class="lead">상록구는 상록수역·한대앞역·중앙역을 끼고 있는 안산 동부 생활권으로, 한양대 에리카와 시화호를 함께 품은 행정구입니다. 일동·이동·사동을 비롯한 11개 대표 행정동을 이 허브에서 연결합니다.</p>

<section>
<h2>상록구 생활권 성격</h2>
<p>상록구는 안산시 동쪽 절반을 차지하는 행정구입니다. 상록수역과 한대앞역을 중심으로 한 주거·상권 수요가 두텁고, 본오동·일동처럼 대단지 아파트가 밀집한 주거권이 넓게 펼쳐져 있습니다. 남쪽 사동과 해양동은 한양대학교 에리카캠퍼스와 시화호에 인접해 대학가 원룸·오피스텔과 신도시 아파트가 섞여 있고, 동쪽 끝 반월동·안산동은 반월역과 수암·장상 일대의 외곽 생활권으로 차량 이동 비중이 높습니다. 같은 상록구라도 역세권 주거지, 대학가, 외곽 생활권의 결이 모두 달라, 방문 시간대와 공간 준비 안내도 동마다 조금씩 다릅니다.</p>
</section>

<section>
<h2>상록구 대표 행정동</h2>
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
<p>일동과 이동은 상록수역·한대앞역 접근성을 함께, 사동·사이동·해양동은 한양대 에리카·사리역·시화호 인근 생활권을 다룹니다. 본오동은 상록수역 주거권, 부곡동·월피동은 차량 이동과 생활 상권, 성포동은 중앙역·성포 생활권을 중심으로 설명합니다. 본오1~3동은 본오동 페이지로 통합됩니다.</p>
</section>

<section>
<h2>상록구 주요 역세권</h2>
<p>상록구에서는 4호선(안산선)의 <a href="/ansan/sangnoksu-station-chuljangmassage/">상록수역</a>, <a href="/ansan/hanyang-univ-ansan-station-chuljangmassage/">한대앞역</a>, <a href="/ansan/sari-station-chuljangmassage/">사리역</a>, <a href="/ansan/banwol-station-chuljangmassage/">반월역</a>이 주요 거점입니다. 상록수역은 본오동·일동 생활권, 한대앞역은 이동·사동 인근, 사리역은 사동·해양동 생활권, 반월역은 반월동 생활권을 끼고 있습니다. 역 인근 위치에서 예약하실 때는 각 역 페이지를 참고하시고, 예약 전화에서는 역 이름과 함께 정확한 주소를 알려주시면 도착 시간이 정확해집니다.</p>
</section>

<section>
<h2>상록구 방문·예약 안내</h2>
<p>상록구는 대단지 아파트 비중이 높아 가족 단위 자택 예약이 많고, 한양대 에리카 인근은 학생·1인 가구의 원룸 방문 문의가 꾸준합니다. 아파트는 동·호수와 공동현관 출입 방법을, 원룸·오피스텔은 건물 입구 안내를 미리 알려주시면 방문이 매끄럽습니다. 반월동·안산동 외곽은 차량 이동 기준이 중요하니 큰길 기준 진입 방향과 주차 가능 여부를 함께 확인해 주세요. 관리 유형이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>를, 예약 절차는 <a href="/reservation/">예약안내</a>를 참고하시면 됩니다.</p>
</section>

<section>
<h2>상록구 생활권별 방문 패턴</h2>
<p>상록구는 한 행정구 안에서도 생활권에 따라 예약이 들어오는 시간대와 형태가 다릅니다. 상록수역·한대앞역을 낀 일동·이동·본오동 같은 대단지 주거권에서는 평일 저녁과 주말 낮에 가족 단위 자택 예약이 가장 많습니다. 하루 일과를 마친 뒤 거실이나 안방에 매트를 펴고 받는 형태가 일반적이라, 예약 시 조용한 공간 확보 여부와 단지 출입 방법을 함께 확인해 두면 도착이 빨라집니다. 사동·사이동·해양동의 한양대 에리카 생활권은 학기 중 시험 기간 전후로 1인 가구 원룸 예약이 몰리고, 방학에는 문의가 줄어드는 흐름이 뚜렷합니다. 부곡동·월피동·성포동의 생활 상권 지역은 차량으로 이동하는 직장인 수요가 더해지고, 반월동·안산동 외곽은 시간대에 따라 방문 가능 여부가 달라질 수 있어 미리 연락 주시는 편이 안전합니다. 본인 생활권과 비슷한 패턴을 참고하시면 원하는 시간대를 잡기가 한결 수월합니다.</p>
</section>

<section>
<h2>상록구에서 많이 찾는 관리</h2>
<p>상록구에서 들어오는 예약을 보면 누적된 피로를 푸는 전신 이완 관리와 어깨·목 중심의 집중 관리가 가장 많습니다. 책상 앞에 오래 앉아 있는 학생과 직장인이 많은 한양대 에리카·역세권 주거권에서는 굳은 어깨와 거북목을 풀고 싶다는 문의가 잦고, 가정에서는 부모님을 위한 부드러운 관리나 부부가 차례로 받는 순차 예약이 많습니다. 늦은 시간 귀가 후 그대로 잠들고 싶다는 분, 운동 후 근육을 정리하고 싶다는 분도 꾸준합니다. 어떤 관리가 본인에게 맞을지 고민되시면 예약 전화에서 그날 컨디션과 불편한 부위를 말씀해 주세요. 시간과 구성을 함께 정해 드리며, 관리 유형별 특징은 <a href="/themes/">테마별 안내</a>에서 미리 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>상록구 어느 동까지 방문되나요?</h3>
<p>일동·이동·사동·사이동·해양동·본오동·부곡동·월피동·성포동·반월동·안산동 전역이 방문 범위입니다. 외곽 위치는 시간대에 따라 가능 여부를 확인해 드립니다.</p>
</div>
<div class="faq-item">
<h3>한양대 에리카 근처도 가능한가요?</h3>
<p>사동·해양동 생활권에 포함되어 방문 가능합니다. 원룸·기숙사 인근은 건물 출입 방법을 함께 알려주세요.</p>
</div>
</section>
""" + PRICING + _CTA

_SANGNOK_GU = {
    "path": "ansan/sangnok-gu-chuljangmassage/",
    "title": "상록구 출장마사지·홈타이 | 상록수·한대앞 생활권 안내",
    "desc": "상록구 출장마사지·홈타이 예약 전 상록수역, 한대앞역 생활권을 확인하세요.",
    "h1": "상록구 방문 관리 안내",
    "body": _SANGNOK_BODY,
    "breadcrumb": [("지역별 안내", "/ansan/"), ("상록구", None)],
}

# ── 단원구 허브 ───────────────────────────────────────────────────
_DANWON_BODY = """
<p class="lead">단원구는 중앙역·고잔역·초지역·안산역을 끼고 있는 안산 서부 생활권으로, 중심 상권과 산업단지 이동 수요가 함께 있는 행정구입니다. 고잔동·중앙동·초지동을 비롯한 10개 대표 행정동을 이 허브에서 연결합니다.</p>

<section>
<h2>단원구 생활권 성격</h2>
<p>단원구는 안산시 서쪽 절반을 차지하는 행정구입니다. 고잔동·중앙동·호수동은 안산 중심 상권과 행정기관, 고잔신도시·호수공원 생활권을 끼고 있어 유동 인구가 많습니다. 원곡동과 백운동은 안산역과 원곡동 다문화 상권을 중심으로 하고, 신길동·초지동·선부동은 신길온천역·초지역·선부역 역세권과 반월·시화 산업단지 이동 수요가 함께 있는 지역입니다. 서쪽 끝 대부동은 대부도 외곽 생활권으로 차량 이동이 기본입니다. 중심 상권형, 역세권·산업단지형, 외곽형 생활권이 한 행정구 안에 모두 있어 방문 안내도 지역마다 다릅니다.</p>
</section>

<section>
<h2>단원구 대표 행정동</h2>
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
<p>고잔동·중앙동은 안산 중심 상권과 행정기관 접근성을, 호수동은 고잔신도시·호수공원 생활권을 다룹니다. 원곡동·백운동은 안산역과 원곡동 다문화 상권, 신길동은 신길온천역·산업단지, 초지동은 초지역 환승권, 선부동은 선부역·달미역 주변 주거권을 중심으로 설명합니다. 선부1~3동은 선부동 페이지로 통합됩니다.</p>
</section>

<section>
<h2>단원구 주요 역세권</h2>
<p>단원구에서는 <a href="/ansan/jungang-station-chuljangmassage/">중앙역</a>, <a href="/ansan/gojan-station-chuljangmassage/">고잔역</a>, <a href="/ansan/choji-station-chuljangmassage/">초지역</a>, <a href="/ansan/ansan-station-chuljangmassage/">안산역</a>, <a href="/ansan/seonbu-station-chuljangmassage/">선부역</a>이 주요 거점입니다. 중앙역은 안산 중심 상권, 고잔역은 고잔동·호수동, 초지역은 4호선·수인분당선·서해선이 만나는 환승 거점, 안산역은 원곡동·백운동, 선부역은 선부동 생활권을 끼고 있습니다. 초지역은 노선이 여러 개라도 페이지는 하나만 운영하고 본문에서 환승 특징을 설명합니다.</p>
</section>

<section>
<h2>단원구 방문·예약 안내</h2>
<p>단원구는 중심 상권과 숙박·오피스텔이 많아 심야·숙소 방문 문의가 많고, 산업단지 인근은 교대 근무자의 시간대별 예약이 더해집니다. 중심 상권 숙소는 건물 출입 안내를, 아파트 단지는 동·호수와 공동현관 출입 방법을 알려주시면 됩니다. 대부동은 대부도 외곽이라 차량 이동 기준이 중요하니 추가 이동비와 예약 가능 시간을 함께 확인해 주세요. 관리 유형이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>를, 예약 절차는 <a href="/reservation/">예약안내</a>를 참고하시면 됩니다.</p>
</section>

<section>
<h2>단원구 생활권별 방문 패턴</h2>
<p>단원구는 생활권 성격이 뚜렷하게 갈려 예약 흐름도 지역마다 다릅니다. 중앙역·고잔동·중앙동의 중심 상권에서는 약속이나 회식이 끝난 늦은 시간에 숙소나 자택으로 방문을 요청하는 경우가 많아 심야 문의 비중이 높습니다. 호수동의 고잔신도시·호수공원 생활권은 신축 대단지가 모여 있어 평일 저녁과 주말 낮 가족 단위 자택 예약이 중심이고, 예약 시 단지 공동현관 출입 방법을 함께 알려주시면 도착이 정확합니다. 원곡동·백운동은 안산역 상권과 다문화 생활권의 영향으로 다양한 시간대에 문의가 들어오고, 신길동·초지동·선부동의 역세권·산업단지 지역은 교대 근무에 맞춰 낮과 새벽 예약이 섞입니다. 대부동은 외곽이라 이동 시간을 넉넉히 두고 미리 연락 주시는 편이 안전합니다. 본인 생활권과 비슷한 흐름을 참고하시면 원하는 시간대 예약이 수월해집니다.</p>
</section>

<section>
<h2>단원구에서 많이 찾는 관리</h2>
<p>단원구에서는 숙소·오피스텔에서 받는 휴식형 전신 관리와 산업단지 근무자의 피로 회복 관리 문의가 특히 많습니다. 중심 상권 숙소에서는 여행이나 출장 중 컨디션을 정리하려는 분, 회식 후 묵직한 몸을 풀려는 분이 늦은 시간에 많이 찾으시고, 호수동·고잔동 주거권에서는 가족이 함께 받거나 부모님을 위해 예약하는 경우가 많습니다. 교대 근무가 잦은 신길동·초지동 인근은 야간 근무 전후로 짧고 효율적인 관리를 원하시는 문의가 꾸준합니다. 그날 컨디션과 불편한 부위를 예약 전화에서 말씀해 주시면 시간과 구성을 맞춰 드리며, 관리 유형별 특징은 <a href="/themes/">테마별 안내</a>에서 미리 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>단원구 어느 동까지 방문되나요?</h3>
<p>와동·고잔동·중앙동·호수동·원곡동·백운동·신길동·초지동·선부동·대부동 전역이 방문 범위입니다. 대부도 등 외곽은 시간대에 따라 가능 여부를 확인해 드립니다.</p>
</div>
<div class="faq-item">
<h3>초지역 환승권 쪽도 가능한가요?</h3>
<p>초지역 인근은 초지동 생활권에 포함되어 방문 가능합니다. 환승역이지만 페이지는 하나로 운영하니 위치만 정확히 알려주시면 됩니다.</p>
</div>
</section>
""" + PRICING + _CTA

_DANWON_GU = {
    "path": "ansan/danwon-gu-chuljangmassage/",
    "title": "단원구 출장마사지·홈타이 | 중앙역·초지역·안산역 안내",
    "desc": "단원구 출장마사지·홈타이 이용 전 중앙역, 초지역, 안산역 기준을 확인하세요.",
    "h1": "단원구 방문 관리 안내",
    "body": _DANWON_BODY,
    "breadcrumb": [("지역별 안내", "/ansan/"), ("단원구", None)],
}

PAGES = [_HUB, _SANGNOK_GU, _DANWON_GU] + SANGNOK_DONGS + DANWON_DONGS
