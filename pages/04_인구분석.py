import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

# -----------------------------------
# 제목
# -----------------------------------
st.title("서울시 행정구별 인구수")

# -----------------------------------
# CSV 불러오기
# -----------------------------------
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="euc-kr")

# -----------------------------------
# 컬럼 공백 제거
# -----------------------------------
df.columns = df.columns.str.strip()

# -----------------------------------
# 행정구 컬럼
# -----------------------------------
district_col = df.columns[0]

# -----------------------------------
# 숫자형 변환
# -----------------------------------
for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------------
# 나이 컬럼만 추출
# -----------------------------------
age_columns = []

for col in df.columns:
    if "세" in col:
        age_columns.append(col)

# -----------------------------------
# 행정구 선택
# -----------------------------------
districts = df[district_col].unique()

selected_district = st.selectbox(
    "행정구 선택",
    districts
)

# -----------------------------------
# 선택 데이터
# -----------------------------------
selected_data = df[df[district_col] == selected_district]

# -----------------------------------
# 그래프 데이터
# -----------------------------------
x_data = age_columns
y_data = selected_data[age_columns].iloc[0].values

# -----------------------------------
# 그래프 생성
# -----------------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x_data,
        y=y_data,
        mode="lines+markers",
        line=dict(
            color="red",
            width=4
        ),
        marker=dict(
            size=7
        )
    )
)

# -----------------------------------
# 그래프 디자인
# -----------------------------------
fig.update_layout(
    title="서울시 행정구별 인구수",

    font=dict(
        family="Malgun Gothic",
        size=14,
        color="white"
    ),

    paper_bgcolor="gray",
    plot_bgcolor="gray",

    xaxis=dict(
        title="나이",
        tickangle=-45,
        gridcolor="lightgray",
        color="white"
    ),

    yaxis=dict(
        title="인구수",
        gridcolor="lightgray",
        color="white"
    ),

    height=700
)

# -----------------------------------
# 출력
# -----------------------------------
st.plotly_chart(fig, use_container_width=True)
