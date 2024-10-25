import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 앱 제목 설정
st.title("엑셀 파일을 그래프로 변환하기")

# 엑셀 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 선택하세요", type=["xlsx"])

if uploaded_file:
    # 엑셀 파일 읽기
    df = pd.read_excel(uploaded_file)

    # 데이터프레임 표시
    st.write("데이터프레임:")
    st.dataframe(df)

    # 그래프에 사용할 열 선택
    column = st.selectbox("플롯할 열 선택", df.columns)

    # 간단한 선 그래프 생성
    plt.figure(figsize=(10, 5))
    plt.plot(df[column])
    plt.title(f'{column}의 플롯')
    plt.xlabel('인덱스')
    plt.ylabel(column)
    plt.grid()
    st.pyplot(plt)
