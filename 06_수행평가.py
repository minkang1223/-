import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="전세계 인기있는 주종",
    layout="wide"
)

st.title("전세계 인기있는 주종")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
try:
    df = pd.read_csv("Global_alcohol_consumption.csv", encoding="utf-8")
except:
    df = pd.read_csv("Global_alcohol_consumption.csv", encoding="latin1")

# -----------------------------------
# 컬럼명 확인
# -----------------------------------
country_col = df.columns[0]

# 주종 컬럼 찾기
beer_col = [c for c in df.columns if "beer" in c.lower()][0]
wine_col = [c for c in df.columns if "wine" in c.lower()][0]
spirit_col = [c for c in df.columns if "spirit" in c.lower()][0]
other_col = [c for c in df.columns if "other" in c.lower()][0]

# -----------------------------------
# 국가 선택
# -----------------------------------
selected_country = st.selectbox(
    "나라를 선택하세요",
    sorted(df[country_col].unique())
)

row = df[df[country_col] == selected_country].iloc[0]

# -----------------------------------
# 그래프 데이터
# -----------------------------------
drink_types = ["맥주", "와인", "증류주", "기타"]

values = [
    float(row[beer_col]),
    float(row[wine_col]),
    float(row[spirit_col]),
    float(row[other_col])
]

# -----------------------------------
# 그래프 생성
# -----------------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=values,
        y=drink_types,
        mode="lines+markers",
        line=dict(
            color="orange",
            width=4
        ),
        marker=dict(
            size=10,
            color="orange"
        )
    )
)

# -----------------------------------
# 그래프 디자인
# -----------------------------------
fig.update_layout(
    title="전세계 인기있는 주종",

    font=dict(
        family="Malgun Gothic",
        size=14
    ),

    paper_bgcolor="skyblue",
    plot_bgcolor="skyblue",

    xaxis=dict(
        title="알코올 소비량(%)",
        gridcolor="white"
    ),

    yaxis=dict(
        title="인기있는 주종"
    ),

    height=600
)

st.plotly_chart(fig, use_container_width=True)
