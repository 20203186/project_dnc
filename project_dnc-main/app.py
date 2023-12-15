# Streamlit 라이브러리
#  - Python으로 손쉽게 웹사이트를 생성할 수 있는 라이브러리
#  - 기존에는 HTML, CSS, JS 등과 같은 기술을 공부해야 웹 사이트 구현 가능
#  - Streamlit을 사용하면 위의 기술을 모르더라도 블럭 쌓듯이 손쉽게 구현 가능
#  - 단, 단점은 우리가 원하는 디테일한 작업은 불가능

# streamlit 실행 코드
# 터미널 >> streamlit run ./app.py  -> (.)은 현재위치 (/) 는 더블클릭
# 절대경로(사용x)  streamlit run C:\developer\workspace\project_dnc-main\project_dnc-main\app.py

import streamlit as st
from datetime import datetime
from src.collector import news_collector

news_category = {
    "society": "사회",
    "politics": "정치",
    "economic": "경제",
    "foreign": "국제",
    "culture": "문화",
    "entertain": "연예",
    "sports": "스포츠",
    "digital": "IT",
}

st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./image/favicon_01.png"
)

st.title(":red[NEWS] COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False, encoding="cp949")


flag = False
with st.form(key="form"):
    category = st.text_input("카테고리 입력").strip()  # 검색창
    submitted = st.form_submit_button("수집")  # 버튼

    if submitted:  # "Submit" 버튼을 누르면!
        if category in list(news_category.keys()):
            st.write(f'"{news_category[category]}" 뉴스를 수집 합니다.')
            df_news, count = news_collector(category)
            # dataframe -> csv 형식
            csv = convert_df(df_news)
            flag = True
        else:
            st.write("올바른 뉴스 카테고리를 입력해주세요.")

if flag:
    st.write(f'"{news_category[category]}"뉴스 {count}건 수집 완료')
    now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    st.download_button(
        label="저장",
        data=csv,
        mime="test/csv",
        file_name=f"{news_category[category]}_뉴스_{now}"  # 스포츠_뉴스_2023_12_15_.csv
    )