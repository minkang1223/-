# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI Country Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# 데이터 로드
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

mbti_columns = [col for col in df.columns if col != "Country"]

# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #0f172a;
}

.stSelectbox label {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.title("🌍 국가별 MBTI 분석 대시보드")
st.markdown("국가별 MBTI 비율과 특정 MBTI가 높은 국가들을 인터랙티브하게 분석할 수 있습니다.")

# -----------------------------
# 탭 구성
# -----------------------------
tab1, tab2 = st.tabs([
    "📊 국가별 MBTI 보기",
    "🏆 MBTI 상위 10% 국가 보기"
])

# =========================================================
# TAB 1
# =========================================================
with tab1:

    st.subheader("국가 선택")

    selected_country = st.selectbox(
        "국가를 선택하세요",
        sorted(df["Country"].unique())
    )

    row = df[df["Country"] == selected_country].iloc[0]

    mbti_data = row.drop("Country").sort_values(ascending=False)

    top_mbti = mbti_data.idxmax()

    # 색상 생성
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

    colors = []

    gradient_index = 0

    for mbti in mbti_data.index:
        if mbti == top_mbti:
            colors.append("#ef4444")
        else:
            colors.append(
                blue_gradient[
                    gradient_index % len(blue_gradient)
                ]
            )
            gradient_index += 1

    # 그래프
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

    fig.update_layout(
        title=f"{selected_country} MBTI 비율",
        template="plotly_white",
        height=650,
        showlegend=False,
        title_x=0.5,
        font=dict(size=15)
    )

    fig.update_yaxes(
        title="비율",
        tickformat=".0%"
    )

    fig.update_xaxes(
        title="MBTI 유형"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        f"✅ {selected_country}에서 가장 높은 MBTI는 **{top_mbti}** 입니다."
    )

# =========================================================
# TAB 2
# =========================================================
with tab2:

    st.subheader("MBTI별 상위 10% 국가")

    selected_mbti = st.selectbox(
        "MBTI를 선택하세요",
        mbti_columns
    )

    # 상위 10%
    top_count = max(1, int(len(df) * 0.1))

    top_df = (
        df[["Country", selected_mbti]]
        .sort_values(by=selected_mbti, ascending=False)
        .head(top_count)
    )

    # 색상
    colors2 = []

    blue_gradient2 = [
        "#dbeafe",
        "#bfdbfe",
        "#93c5fd",
        "#60a5fa",
        "#3b82f6",
        "#2563eb",
        "#1d4ed8",
        "#1e40af",
    ]

    for i in range(len(top_df)):
        if i == 0:
            colors2.append("#ef4444")
        else:
            colors2.append(
                blue_gradient2[
                    i % len(blue_gradient2)
                ]
            )

    # 그래프 생성
    fig2 = go.Figure()

    fig2.add_trace(
        go.Bar(
            x=top_df["Country"],
            y=top_df[selected_mbti],
            marker_color=colors2,
            text=[f"{v:.1%}" for v in top_df[selected_mbti]],
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            f"{selected_mbti}: " +
            "%{y:.2%}<extra></extra>"
        )
    )

    fig2.update_layout(
        title=f"{selected_mbti} 비율 상위 10% 국가",
        template="plotly_white",
        height=700,
        title_x=0.5,
        showlegend=False,
        font=dict(size=15)
    )

    fig2.update_yaxes(
        title="비율",
        tickformat=".0%"
    )

    fig2.update_xaxes(
        title="국가"
    )

    st.plotly_chart(fig2, use_container_width=True)

    top_country = top_df.iloc[0]["Country"]
    top_value = top_df.iloc[0][selected_mbti]

    st.success(
        f"🏆 {selected_mbti} 비율이 가장 높은 국가는 "
        f"**{top_country} ({top_value:.2%})** 입니다."
    )

    with st.expander("상위 국가 데이터 보기"):
        temp = top_df.copy()
        temp[selected_mbti] = temp[selected_mbti].map(lambda x: f"{x:.2%}")
        st.dataframe(temp, use_container_width=True)
