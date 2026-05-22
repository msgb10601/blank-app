import streamlit as st

# 1. 앱의 제목 및 소개 설정
st.title("📱 나의 첫 스트림릿 웹 앱")
st.subheader("파이썬 코드를 웹 앱으로 멋지게 시각화합니다.")

st.divider() # 구분선

# 2. 사용자 입력 받기 (기존의 input() 함수들을 대체)
st.sidebar.header("⚙️ 입력 설정")
user_name = st.sidebar.text_input("이름을 입력하세요:", "홍길동")
user_value = st.sidebar.number_input("분석할 숫자를 입력하세요:", min_value=1, max_value=100, value=50)

# 3. 데이터 처리 및 비즈니스 로직 (기존 파이썬 프로그램의 핵심 로직)
def process_data(name, value):
    # 이 부분에 기존 파이썬 프로그램의 함수나 연산 로직을 넣으세요.
    result_calculated = value * 2
    return f"✨ {name}님, 선택하신 {value}의 2배는 {result_calculated}입니다!"

# 4. 결과 출력 및 시각화
st.header("📊 실행 결과")

# 실행 버튼 생성
if st.button("결과 보기"):
    with st.spinner('계산 중입니다...'):
        # 로직 실행
        result = process_data(user_name, user_value)
        
        # 결과 메시지 출력
        st.success("계산 완료!")
        st.write(result)
        
        # 예시 데이터 차트 그리기 (기존 코드에 그래프가 있다면 활용)
        st.bar_chart([user_value, user_value * 1.5, user_value * 2])
else:
    st.info("왼쪽 사이드바에서 값을 조정하고 '결과 보기' 버튼을 눌러보세요.")