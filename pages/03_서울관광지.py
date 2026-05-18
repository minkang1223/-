# app.py

import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("지도에서 관광지를 클릭해보세요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "경복궁역 5분",
        "fun": "한복 체험, 궁궐 산책, 야간개장"
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9827,
        "station": "명동역 바로 앞",
        "fun": "쇼핑, 길거리 음식, 화장품 투어"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "홍대입구역 3분",
        "fun": "버스킹, 카페, 클럽"
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역 + 케이블카",
        "fun": "야경, 사랑의 자물쇠, 전망대"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역 7분",
        "fun": "전통 한옥, 사진 촬영, 공방 체험"
    },
    {
        "name": "롯데월드",
        "lat": 37.5110,
        "lon": 127.0980,
        "station": "잠실역 연결",
        "fun": "놀이기구, 아이스링크, 퍼레이드"
    },
    {
        "name": "한강공원",
        "lat": 37.5206,
        "lon": 126.9393,
        "station": "여의나루역 5분",
        "fun": "치킨 피크닉, 자전거, 야경"
    },
    {
        "name": "성수동",
        "lat": 37.5447,
        "lon": 127.0557,
        "station": "성수역 3분",
        "fun": "감성카페, 팝업스토어, 편집샵"
    },
    {
        "name": "코엑스",
        "lat": 37.5125,
        "lon": 127.0588,
        "station": "삼성역 연결",
        "fun": "별마당도서관, 쇼핑, 아쿠아리움"
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9992,
        "station": "종로5가역 2분",
        "fun": "빈대떡, 육회, 먹거리 투어"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=12
)

# 클릭 시 하단 정보 표시용 JS
bottom_info = """
<div id="info-box"
style="
position: fixed;
bottom: 10px;
left: 50%;
transform: translateX(-50%);
z-index:9999;
background:white;
padding:15px;
border-radius:10px;
box-shadow:0 0 10px rgba(0,0,0,0.3);
width:70%;
text-align:center;
font-size:18px;
font-weight:bold;
">
관광지를 클릭하면 정보가 표시됩니다.
</div>
"""

m.get_root().html.add_child(folium.Element(bottom_info))

# 마커 추가
for place in places:

    js = f"""
    document.getElementById('info-box').innerHTML =
    '🚇 가까운 지하철역: {place["station"]} | 🎉 놀거리: {place["fun"]}';
    """

    popup_html = f"""
    <div style="width:200px">
        <h4>{place["name"]}</h4>
        <button onclick="{js}">
            정보 보기
        </button>
    </div>
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# 지도 출력
html(m._repr_html_(), height=700)
