# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="MBTI Country Dashboard",
    page_icon="🌍",
    layout="wide"
)

# 제목
st.title("🌍 국가별 MBTI 비율 대시보드")
st.markdown("국가를 선택하면 해당 국가의 MBTI 분포를 인터랙티브 그래프로 확인할 수 있습니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

# 선택된 국가 데이터
row = df[df["Country"] == country].iloc[0]

# MBTI 데이터 추출
mbti_data = row.drop("Country").sort_values(ascending=False)

# 최고값 찾기
top_mbti = mbti_data.idxmax()

# 색상 설정
colors = []

blue_gradient = [
    "#dbeafe",
    "#bfdbfe",
    "#93c5fd",
    "#60a5fa",
    "#3b82f6",
    "#2563eb",
    "#1d4ed8",
    "#1e40af",
]

gradient_index = 0

for mbti in mbti_data.index:
    if mbti == top_mbti:
        colors.append("#ef4444")  # 빨간색
    else:
        colors.append(
            blue_gradient[gradient_index % len(blue_gradient)]
        )
        gradient_index += 1

# Plotly 그래프 생성
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_data.index,
        y=mbti_data.values,
        marker_color=colors,
        text=[f"{v:.1%}" for v in mbti_data.values],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# 그래프 꾸미기
fig.update_layout(
    title=f"{country} MBTI 분포",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    height=650,
    title_x=0.5,
    font=dict(size=15),
    hoverlabel=dict(font_size=15),
    showlegend=False
)

fig.update_yaxes(tickformat=".0%")

# 스트림릿에 출력
st.plotly_chart(fig, use_container_width=True)

# 추가 정보
st.subheader("📌 가장 높은 MBTI")
st.success(f"{country}에서 가장 높은 유형은 **{top_mbti}** 입니다.")

# 데이터 테이블
with st.expander("데이터 보기"):
    table_df = pd.DataFrame({
        "MBTI": mbti_data.index,
        "비율": [f"{v:.2%}" for v in mbti_data.values]
    })
    st.dataframe(table_df, use_container_width=True)
