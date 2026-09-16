import streamlit as st
import random
import time

st.set_page_config(page_title="카지노 777 슬롯머신", page_icon="🎰", layout="centered")

st.title("🎰 잭팟 777 슬롯머신")
st.caption("🚨 경고: 극악의 확률! 환급률(RTP) 10% 미만 극악 세팅")

if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "spins" not in st.session_state:
    st.session_state.spins = 0

col1, col2 = st.columns(2)
with col1:
    st.metric("💰 보유 금액", f"{st.session_state.balance:,} 원")
with col2:
    st.metric("🔄 총 스핀 횟수", f"{st.session_state.spins} 회")

bet = st.radio("베팅 금액 선택:", [1000, 5000, 10000], horizontal=True)

symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

if st.button("🎰 슬롯 돌리기!", use_container_width=True):
    if st.session_state.balance < bet:
        st.error("잔액이 부족합니다! 충전해 주세요.")
    else:
        st.session_state.balance -= bet
        st.session_state.spins += 1
        
        slot_placeholder = st.empty()
        for _ in range(10):
            temp_reels = [random.choice(symbols) for _ in range(3)]
            slot_placeholder.markdown(
                f"<h1 style='text-align: center; font-size: 70px;'>[ {' | '.join(temp_reels)} ]</h1>", 
                unsafe_allow_html=True
            )
            time.sleep(0.1)

        rand_val = random.random()
        
        if rand_val < 0.001:
            reels = ["7️⃣", "7️⃣", "7️⃣"]
            win_amount = bet * 100
            msg = "🎉대잭팟 발생! 777 축하합니다! (100배)🎉"
        elif rand_val < 0.02:
            reels = ["🍒", "🍒", "🍒"]
            win_amount = bet * 3
            msg = "🍒 체리 3개 당첨! (3배)"
        else:
            win_amount = 0
            if random.random() < 0.4:
                s = random.choice(symbols)
                other = random.choice([x for x in symbols if x != s])
                reels = [s, s, other]
            else:
                reels = random.sample(symbols, 3)
            msg = "💸 꽝입니다! 탕진했습니다."

        slot_placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 70px;'>[ {' | '.join(reels)} ]</h1>", 
            unsafe_allow_html=True
        )
        
        if win_amount > 0:
            st.session_state.balance += win_amount
            st.success(f"{msg} (+{win_amount:,}원)")
            st.balloons()
        else:
            st.error(msg)

st.divider()
if st.button("💵 10,000원 대출(충전)하기", use_container_width=True):
    st.session_state.balance += 10000
    st.toast("10,000원이 충전되었습니다!")
    st.rerun()
