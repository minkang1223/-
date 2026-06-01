import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import zipfile

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="전세계 인기있는 주종",
    layout="wide"
)

st.title("전세계 인기있는 주종")

# -----------------------------------
# ZIP 파일 읽기
# -----------------------------------
with zipfile.ZipFile("archive.zip") as z:

    # ZIP 안의 CSV 찾기
    csv_files = [f for f in z.namelist() if f.endswith(".csv")]

    if len(csv_files) == 0:
        st.error("ZIP 파일 안에 CSV 파일이 없습니다.")
        st.stop()

    csv_file = csv_files[0]

    try:
        df = pd.read_csv(z.open(csv_file), encoding="utf-8")
    except:
        try:
            df = pd.read_csv(z.open(csv_file), encoding="cp949")
        except:
            df = pd.read_csv(z.open(csv_file), encoding="latin1")

# -----------------------------------
# 컬럼 확인
# -----------------------------------
st.write("데이터 컬럼 확인")
st.write(df.columns.tolist())

# -----------------------------------
# 국가 컬럼
# -----------------------------------
country_col = df.columns[0]

# -----------------------------------
# 주종 컬럼 자동 찾기
# -----------------------------------
beer_col = None
wine_col = None
spirit_col = None
other_col = None

for col in df.columns:

    lower = col.lower()

    if "beer" in lower:
        beer_col = col

    elif "wine" in lower:
        wine_col = col

    elif "spirit" in lower:
        spirit_col = col

    elif "other" in lower:
        other_col = col

# 컬럼 못 찾으면 종료
if not all([beer_col, wine_col, spirit_col, other_col]):
    st.error(
        "맥주/와인/증류주/기타 컬럼을 찾지 못했습니다. 위에 출력된 컬럼명을 확인해주세요."
    )
    st.stop()

# -----------------------------------
# 국가 선택
# -----------------------------------
countries = sorted(df[country_col].dropna().unique())

selected_country = st.selectbox(
    "나라를 선택하세요",
    countries
)

# -----------------------------------
# 선택 국가 데이터
# -----------------------------------
row = df[df[country_col] == selected_country].iloc[0]

# -----------------------------------
# 그래프 데이터
# -----------------------------------
drink_types = [
    "맥주",
    "와인",
    "증류주",
    "기타"
]

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
            width=5
        ),
        marker=dict(
            size=10,
            color="orange"
        )
    )
)

# -----------------------------------
# 디자인
# -----------------------------------
fig.update_layout(
    title="전세계 인기있는 주종",

    font=dict(
        family="Malgun Gothic",
        size=14,
        color="black"
    ),

    paper_bgcolor="skyblue",
    plot_bgcolor="skyblue",

    xaxis=dict(
        title="알코올 소비량 (%)",
        gridcolor="white"
    ),

    yaxis=dict(
        title="인기있는 주종"
    ),

    height=650
)

# -----------------------------------
# 출력
# -----------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)
