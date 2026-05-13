import streamlit as st

st.set_page_config(
    page_title="영화 & 책 추천",
    page_icon="🎬",
    layout="centered"
)

# 추천 데이터
movies = [
    {
        "title": "인터스텔라",
        "year": "2014",
        "genre": "SF / 드라마",
        "description": "우주를 배경으로 한 감동적인 이야기와 뛰어난 영상미가 특징인 영화."
    },
    {
        "title": "탑건: 매버릭",
        "year": "2022",
        "genre": "액션 / 드라마",
        "description": "압도적인 비행 장면과 긴장감 넘치는 전개로 큰 인기를 얻은 영화."
    }
]

book = {
    "title": "아몬드",
    "author": "손원평",
    "year": "2017",
    "genre": "소설",
    "description": "감정을 잘 느끼지 못하는 소년의 성장 이야기를 담은 베스트셀러 소설."
}

# 제목
st.title("🎬 영화 & 📚 책 추천 프로그램")
st.write("2010년 이후 작품들만 추천해드립니다!")

# 영화 추천
st.header("🎥 추천 영화 2선")

for idx, movie in enumerate(movies, start=1):
    st.subheader(f"{idx}. {movie['title']} ({movie['year']})")
    st.write(f"🎭 장르: {movie['genre']}")
    st.write(f"📝 줄거리: {movie['description']}")
    st.markdown("---")

# 책 추천
st.header("📖 추천 책 1권")

st.subheader(f"{book['title']} ({book['year']})")
st.write(f"✍ 작가: {book['author']}")
st.write(f"📚 장르: {book['genre']}")
st.write(f"📝 소개: {book['description']}")

st.success("즐거운 감상 되세요 😊")
