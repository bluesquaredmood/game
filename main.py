import streamlit as st
import time
import threading

# 초기값 설정
잔여시간 = 0
cnt = 0
running = False
timer_thread = None

# 타이머 업데이트 함수
def update_timer():
    global 잔여시간, running, cnt
    while 잔여시간 > 0 and running:
        time.sleep(1)
        잔여시간 -= 1
        # 실시간 타이머 업데이트
        st.session_state.timer_text = f'Time left: {잔여시간} seconds'
        if 잔여시간 <= 0:
            running = False
            st.session_state.timer_text = 'TIME OVER'
            st.session_state.final_count = cnt
            st.session_state.start_button_disabled = False
            st.session_state.button_disabled = True
            break

# 시작 버튼 클릭시 호출되는 함수
def start_timer():
    global 잔여시간, cnt, running
    잔여시간 = 5  # 타이머 시간 설정 (초 단위)
    cnt = 0  # 클릭 횟수 초기화
    running = True
    st.session_state.timer_text = f'Time left: {잔여시간} seconds'
    st.session_state.current_count = f'현재 횟수: {cnt}'
    st.session_state.start_button_disabled = True
    st.session_state.button_disabled = False
    st.session_state.final_count = None

    # 타이머 쓰레드 실행
    threading.Thread(target=update_timer, daemon=True).start()

# 버튼 클릭시 호출되는 함수
def click():
    global cnt
    if running:
        cnt += 1
        st.session_state.current_count = f'현재 횟수: {cnt}'

# 초기 UI 설정
st.title('주어진 시간동안 최대한 많이 클릭하세요!')

# 타이머 상태 표시
st.text(st.session_state.get("timer_text", "Time left: 0 seconds"))

# 클릭 횟수 표시
st.text(st.session_state.get("current_count", "현재 횟수: 0"))

# 클릭 버튼
if st.button('Button', disabled=st.session_state.get("button_disabled", False)):
    click()

# 시작 버튼
if st.button('Start Timer', disabled=st.session_state.get("start_button_disabled", False)):
    start_timer()

# 리셋 버튼
if st.button('Reset'):
    cnt = 0
    st.session_state.current_count = '현재 횟수: 0'
    st.session_state.timer_text = 'Time left: 0 seconds'
    st.session_state.final_count = None
    st.session_state.start_button_disabled = False
    st.session_state.button_disabled = True
