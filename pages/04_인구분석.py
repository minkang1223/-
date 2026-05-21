import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="서울시 행정구별 인구수", layout="wide")

st.title("서울시 행정구별 인구수")

# -----------------------------
# 한글 폰트 설정
# -----------------------------
font_family = "Malgun Gothic"

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding="utf-8")

# 컬럼 이름 공백 제거
df.columns = df.columns.str.strip()

# -----------------------------
# 행정구 컬럼 찾기
# -----------------------------
district_col = df.columns[0]

# -----------------------------
# 숫자형 데이터 변환
# -----------------------------
for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# 나이 관련 컬럼만 추출
# -----------------------------
age_columns = []

for col in df.columns:
    if "세" in col:
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
districts = df[district_col].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# -----------------------------
# 선택된 데이터
# -----------------------------
selected_data = df[df[district_col] == selected_district]

# -----------------------------
# 그래프 데이터 준비
# -----------------------------
ages = age_columns
population = selected_data[age_columns].iloc[0].values

# -----------------------------
# Plotly 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ages,
        y=population,
        mode="lines+markers",
        line=dict(color="red", width=3),
        marker=dict(size=6),
        name="인구수"
    )
)

# -----------------------------
# 그래프 스타일
# -----------------------------
fig.update_layout(
    title="서울시 행정구별 인구수",
    title_font=dict(size=24),
    font=dict(
        family=font_family,
        size=14,
        color="white"
    ),

    paper_bgcolor="#808080",
    plot_bgcolor="#808080",

    xaxis=dict(
        title="나이",
        tickangle=-45,
        color="white",
        gridcolor="lightgray"
    ),

    yaxis=dict(
        title="인구수",
        color="white",
        gridcolor="lightgray"
    ),

    height=700
)

st.plotly_chart(fig, use_container_width=True)
