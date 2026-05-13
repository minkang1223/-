import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼")

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "career": "데이터 분석가",
            "major": "데이터사이언스학과, 컴퓨터공학과",
            "personality": "논리적이고 분석적인 성격",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "건축가",
            "major": "건축학과",
            "personality": "계획적이고 창의적인 성격",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "INTP": [
        {
            "career": "프로그래머",
            "major": "컴퓨터공학과",
            "personality": "호기심이 많고 문제 해결을 좋아하는 성격",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "career": "연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구심이 강하고 집중력이 높은 성격",
            "salary": "평균 연봉 약 5,200만원"
        }
    ],
    "ENTJ": [
        {
            "career": "기업 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력이 있는 성격",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "career": "마케팅 기획자",
            "major": "경영학과, 광고홍보학과",
            "personality": "전략적 사고를 잘하는 성격",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ENTP": [
        {
            "career": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적이고 아이디어가 많은 성격",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "career": "창업가",
            "major": "경영학과",
            "personality": "도전을 즐기고 활동적인 성격",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "INFJ": [
        {
            "career": "상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 성격",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "career": "작가",
            "major": "문예창작학과",
            "personality": "감수성이 풍부한 성격",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "INFP": [
        {
            "career": "디자이너",
            "major": "시각디자인학과",
            "personality": "창의적이고 감성적인 성격",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "career": "작곡가",
            "major": "실용음악과",
            "personality": "예술적 감각이 뛰어난 성격",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ENFJ": [
        {
            "career": "교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 것을 좋아하는 성격",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "인사 담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 성격",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ENFP": [
        {
            "career": "유튜버",
            "major": "미디어커뮤니케이션학과",
            "personality": "활발하고 표현력이 풍부한 성격",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "career": "여행 기획자",
            "major": "관광경영학과",
            "personality": "새로운 경험을 좋아하는 성격",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ISTJ": [
        {
            "career": "공무원",
            "major": "행정학과",
            "personality": "책임감이 강하고 성실한 성격",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 체계적인 성격",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ISFJ": [
        {
            "career": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 성격",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "사회복지사",
            "major": "사회복지학과",
            "personality": "도움을 주는 것을 좋아하는 성격",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "ESTJ": [
        {
            "career": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙적이고 리더십 있는 성격",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "관리자",
            "major": "경영학과",
            "personality": "체계적이고 책임감 있는 성격",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ESFJ": [
        {
            "career": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 성격",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 성격",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ISTP": [
        {
            "career": "정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 실용적인 성격",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "career": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력이 좋은 성격",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],
    "ISFP": [
        {
            "career": "플로리스트",
            "major": "원예학과",
            "personality": "감성적이고 섬세한 성격",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "career": "사진작가",
            "major": "사진영상학과",
            "personality": "예술 감각이 뛰어난 성격",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ESTP": [
        {
            "career": "스포츠 트레이너",
            "major": "체육학과",
            "personality": "활동적이고 에너지가 많은 성격",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "career": "영업 전문가",
            "major": "경영학과",
            "personality": "사교적이고 설득력이 좋은 성격",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ESFP": [
        {
            "career": "배우",
            "major": "연극영화과",
            "personality": "표현력이 뛰어나고 밝은 성격",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "방송인",
            "major": "방송연예학과",
            "personality": "사람들과 어울리는 것을 좋아하는 성격",
            "salary": "평균 연봉 약 5,000만원"
        }
    ]
}

st.title("💼 MBTI 진로 추천 프로그램")
st.write("자신의 MBTI를 선택하면 추천 진로 2가지를 알려줍니다!")

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(career_data.keys())
)

if st.button("진로 추천 받기"):
    st.subheader(f"{mbti} 유형 추천 진로")

    for idx, item in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.write(f"📚 적합한 학과: {item['major']}")
        st.write(f"😊 적합한 성격: {item['personality']}")
        st.write(f"💰 {item['salary']}")
        st.markdown("---")
