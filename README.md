import streamlit as st

# 앱의 제목 설정
st.title("📦 배송비 안내 프로그램")
st.write("주문 금액과 회원 자격에 따라 총 결제 금액을 계산합니다.")

st.divider() # 구분선

# 1. 입력부: 기존 input()을 스트림릿 컴포넌트로 변경
# 'y/n' 입력 대신 직관적인 라디오 버튼(선택 창)을 사용했습니다.
member_selection = st.radio(
    '정기 회원입니까?',
    ('예 (y)', '아니오 (n)')
)

# 기존 코드의 'y', 'n' 조건과 일치하도록 값을 변환해줍니다.
member = 'y' if member_selection == '예 (y)' else 'n'

# 금액 입력 (기존 int(input())을 number_input으로 변경, 숫지만 입력 가능)
total = st.number_input('주문 금액은 얼마입니까? (원):', min_value=0, value=0, step=1000)

st.divider()

# 계산 및 출력 버튼 생성
if st.button("💰 총 결제금액 계산하기"):
    
    # 2. 로직부: 원본 코드의 조건문과 연산을 그대로 유지
    if member == 'y':
        # print() 대신 st.success()를 사용해 초록색 알림창으로 표시합니다.
        st.success('정기 회원으로 배송비가 면제 됩니다.')
    else:
        # print() 대신 st.warning()을 사용해 노란색 알림창으로 표시합니다.
        st.warning('배송비 3000원이 추가 됩니다.')
        total = total + 3000

    # 3. 출력부: 최종 금액 표시
    # f-string 포맷을 유지하되 가독성을 위해 천 단위 콤마(,)를 추가했습니다.
    st.subheader(f'총 금액은 {total:,}원 입니다.')