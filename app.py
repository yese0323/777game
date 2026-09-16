import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🎰 라스베이거스 777 카지노 슬롯머신",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

casino_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎰 라스베이거스 카지노 슬롯머신</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold-light: #fff2a3;
            --gold-mid: #d4af37;
            --gold-dark: #8a6409;
            --bg-dark: #07030a;
            --neon-red: #ff0055;
            --neon-green: #00ff66;
            --neon-gold: #ffcc00;
            --neon-blue: #00ccff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }

        body {
            background-color: var(--bg-dark);
            /* 실제 카지노 붉은 융단 바닥 및 화려한 네온 조명 분위기 연출 */
            background-image: 
                radial-gradient(ellipse at 50% 0%, rgba(140, 20, 80, 0.45) 0%, transparent 70%),
                radial-gradient(circle at 15% 90%, rgba(200, 30, 30, 0.3) 0%, transparent 40%),
                radial-gradient(circle at 85% 90%, rgba(60, 20, 100, 0.4) 0%, transparent 40%),
                repeating-linear-gradient(45deg, rgba(80, 10, 30, 0.8) 0, rgba(80, 10, 30, 0.8) 15px, rgba(40, 5, 15, 0.9) 15px, rgba(40, 5, 15, 0.9) 30px);
            font-family: 'Noto Sans KR', sans-serif;
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-x: hidden;
        }

        /* 3D 슬롯머신 구조체 전체 포장 */
        .machine-wrapper {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            max-width: 680px;
            margin-top: 30px;
        }

        /* 머신 본체 (실제 카지노 묵직한 캐비닛 느낌) */
        .machine-container {
            position: relative;
            background: linear-gradient(180deg, #2b1d0e 0%, #150d06 40%, #0d0804 100%);
            border: 6px solid var(--gold-mid);
            border-radius: 40px 40px 20px 20px;
            box-shadow: 
                0 0 50px rgba(255, 180, 0, 0.3),
                inset 0 0 30px rgba(0,0,0,0.9),
                0 30px 60px rgba(0,0,0,0.95);
            padding: 25px 25px 15px 25px;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            z-index: 2;
        }

        /* 상단 아치형 전광판 (Marquee Top Header) */
        .marquee-top {
            position: relative;
            width: 110%;
            background: linear-gradient(180deg, #ffd700, #b8860b 40%, #4a3400 100%);
            border: 4px solid #fff;
            border-radius: 120px 120px 15px 15px;
            padding: 18px 10px 12px 10px;
            margin-top: -55px;
            margin-bottom: 15px;
            text-align: center;
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.7), inset 0 2px 10px #fff;
        }

        /* 반짝이는 3개의 별 (Blinking Stars) */
        .star-group {
            position: absolute;
            top: -26px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 15px;
        }

        .star-icon {
            font-size: 2rem;
            color: #fff;
            text-shadow: 0 0 15px #ff0055, 0 0 25px #ffcc00;
            animation: blinkStar 0.8s infinite alternate ease-in-out;
        }
        .star-icon:nth-child(2) { animation-delay: 0.3s; font-size: 2.6rem; margin-top: -8px; }
        .star-icon:nth-child(3) { animation-delay: 0.6s; }

        @keyframes blinkStar {
            from { opacity: 0.4; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1.15); filter: drop-shadow(0 0 10px #fff); }
        }

        .marquee-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 900;
            letter-spacing: 2px;
            color: #111;
            text-shadow: 0 1px 0 #fff, 0 -1px 0 #888;
        }

        /* 실물 인쇄형 유리 페이테이블 (Glass Paytable Display) */
        .glass-paytable {
            width: 100%;
            background: linear-gradient(180deg, rgba(15, 10, 25, 0.95), rgba(5, 2, 10, 0.98));
            border: 2px solid var(--gold-mid);
            border-radius: 12px;
            padding: 10px;
            margin-bottom: 12px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 6px;
            box-shadow: inset 0 0 15px rgba(252, 211, 77, 0.15);
        }

        .pay-item {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 6px;
            padding: 4px 2px;
            text-align: center;
            font-size: 0.75rem;
        }
        .pay-item .syms { display: block; margin-bottom: 2px; }
        .pay-item .mult { color: var(--neon-gold); font-weight: bold; font-family: 'Orbitron', monospace; }

        /* 클래식 사이드 3D 레버 */
        .lever-container {
            position: absolute;
            right: -52px;
            top: 170px;
            width: 55px;
            height: 270px;
            z-index: 1;
            cursor: pointer;
        }
        .lever-base {
            position: absolute;
            bottom: 30px; left: 0;
            width: 32px; height: 65px;
            background: linear-gradient(90deg, #222, #777, #111);
            border-radius: 0 10px 10px 0;
            border: 2px solid var(--gold-dark);
        }
        .lever-arm {
            position: absolute;
            bottom: 55px; left: 8px;
            width: 16px; height: 170px;
            background: linear-gradient(90deg, #aaa, #fff, #666);
            border-radius: 8px;
            transform-origin: bottom center;
            transition: transform 0.15s ease-in;
        }
        .lever-ball {
            position: absolute;
            top: -24px; left: -16px;
            width: 48px; height: 48px;
            background: radial-gradient(circle at 30% 30%, #ff4444, #880000);
            border-radius: 50%;
            border: 2px solid #ffaaaa;
            box-shadow: 0 4px 10px rgba(255,0,0,0.6);
        }
        .lever-arm.pulled { transform: rotateX(75deg) scaleY(0.5); }

        /* 디지털 LED 전광판 */
        .display-board {
            width: 100%;
            background: #000;
            border: 3px solid var(--gold-dark);
            border-radius: 10px;
            padding: 8px 12px;
            margin-bottom: 12px;
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 8px;
            box-shadow: inset 0 0 12px rgba(255, 204, 0, 0.3);
        }
        .stat-box { text-align: center; }
        .stat-label { font-size: 0.68rem; color: #aaa; font-weight: 700; margin-bottom: 2px; }
        .stat-value {
            font-family: 'Orbitron', monospace;
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--neon-gold);
            text-shadow: 0 0 6px rgba(255, 204, 0, 0.8);
        }
        .stat-value.debt { color: var(--neon-red); text-shadow: 0 0 6px rgba(255, 0, 85, 0.8); }

        /* 3D 릴 프레임 (스피닝 영역) */
        .reels-frame {
            background: #000;
            border: 5px solid var(--gold-mid);
            border-radius: 16px;
            padding: 12px;
            display: flex;
            gap: 10px;
            box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.95), 0 0 15px rgba(212, 175, 55, 0.4);
            position: relative;
            margin-bottom: 15px;
            width: 100%;
            justify-content: center;
        }
        .payline-indicator {
            position: absolute;
            left: 0; right: 0; top: 50%;
            transform: translateY(-50%);
            height: 3px;
            background: rgba(255, 0, 85, 0.85);
            box-shadow: 0 0 10px var(--neon-red);
            z-index: 5;
            pointer-events: none;
        }
        .reel-window {
            width: 120px;
            height: 125px;
            background: linear-gradient(180deg, #0a0a0a 0%, #222 50%, #0a0a0a 100%);
            border: 2px solid #444;
            border-radius: 8px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 12px 20px rgba(0,0,0,0.9), inset 0 -12px 20px rgba(0,0,0,0.9);
        }
        .reel-strip {
            position: absolute;
            top: 0; left: 0; width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .symbol {
            width: 120px;
            height: 125px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3.6rem;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.7));
        }

        /* 컨트롤 영역 */
        .controls-panel {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .bet-selector {
            display: flex;
            justify-content: space-between;
            background: rgba(0,0,0,0.5);
            padding: 5px;
            border-radius: 10px;
            border: 1px solid rgba(212, 175, 55, 0.4);
            gap: 6px;
        }
        .bet-btn {
            flex: 1;
            padding: 8px 0;
            background: linear-gradient(180deg, #3a3a3a, #1a1a1a);
            border: 1px solid var(--gold-dark);
            border-radius: 6px;
            color: #ccc;
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-weight: 700;
            font-size: 0.8rem;
            cursor: pointer;
        }
        .bet-btn.active {
            background: linear-gradient(180deg, var(--gold-mid), var(--gold-dark));
            color: #000;
            border-color: #fff;
            box-shadow: 0 0 10px rgba(212, 175, 55, 0.7);
        }
        .bet-btn.all-in-btn.active {
            background: linear-gradient(180deg, #ff0055, #ffcc00);
            color: #000;
            box-shadow: 0 0 12px rgba(255, 0, 85, 0.9);
        }

        .action-btns { display: flex; gap: 8px; }
        .spin-btn {
            flex: 2;
            padding: 14px;
            background: linear-gradient(180deg, #ff4e50, #f9d423);
            border: none;
            border-radius: 10px;
            color: #000;
            font-weight: 900;
            font-size: 1.25rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #990000;
        }
        .loan-btn {
            flex: 1;
            background: linear-gradient(180deg, #00b09b, #96c93d);
            border: none;
            border-radius: 10px;
            color: #000;
            font-weight: 900;
            font-size: 0.9rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #005522;
        }
        .cashout-btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(180deg, #e1eec3, #f05053);
            border: none;
            border-radius: 10px;
            color: #fff;
            font-weight: 900;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #880000;
        }

        /* 하단 메탈 코인 트레이 (Payout Tray) */
        .coin-tray {
            width: 100%;
            height: 35px;
            background: linear-gradient(180deg, #111 0%, #444 50%, #222 100%);
            border: 3px solid var(--gold-dark);
            border-radius: 0 0 15px 15px;
            margin-top: 10px;
            box-shadow: inset 0 5px 10px #000;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
            color: #777;
            letter-spacing: 2px;
        }

        .status-message {
            margin-top: 8px;
            text-align: center;
            font-weight: 700;
            font-size: 0.95rem;
            height: 22px;
            color: var(--gold-light);
        }
        .loss { color: var(--neon-red); }
        .win { color: var(--neon-green); }
        .payback { color: var(--neon-blue); }

        /* 초기 및 정산 모달 팝업 */
        .setup-modal, .result-modal {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(10, 6, 18, 0.98);
            z-index: 100;
            border-radius: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 25px;
            text-align: center;
        }
        .result-modal { display: none; border: 4px solid var(--gold-mid); z-index: 200; }
        .setup-title, .result-title { font-size: 1.6rem; color: var(--gold-mid); font-weight: 900; margin-bottom: 12px; }
        .setup-btn {
            background: linear-gradient(180deg, var(--gold-mid), var(--gold-dark));
            color: #000; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 900; font-size: 1rem; cursor: pointer;
        }
        .preset-btns { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px; }
        .preset-btn { background: rgba(255,255,255,0.1); border: 1px solid var(--gold-mid); color: #fff; padding: 6px; border-radius: 6px; cursor: pointer; }
        
        .result-card {
            background: rgba(255,255,255,0.05); border: 1px solid var(--gold-dark); border-radius: 10px;
            padding: 12px; width: 100%; max-width: 360px; margin-bottom: 15px; display: flex; flex-direction: column; gap: 8px;
        }
        .result-row { display: flex; justify-content: space-between; font-size: 0.9rem; color: #ccc; }
        .result-row.won { color: var(--neon-green); font-weight: bold; }
        .result-row.lost { color: var(--neon-red); font-weight: bold; }
        .result-row.final { border-top: 1px solid #555; padding-top: 6px; font-weight: 900; font-size: 1.1rem; }
    </style>
</head>
<body>

    <div class="machine-wrapper">
        <div class="machine-container">
            
            <!-- 상단 아치 전광판 & 반짝이는 별 -->
            <div class="marquee-top">
                <div class="star-group">
                    <i class="fa-solid fa-star star-icon"></i>
                    <i class="fa-solid fa-star star-icon"></i>
                    <i class="fa-solid fa-star star-icon"></i>
                </div>
                <div class="marquee-title">KING 777 JACKPOT</div>
            </div>

            <!-- 유리판 인쇄형 페이테이블 -->
            <div class="glass-paytable">
                <div class="pay-item"><span class="syms">7️⃣7️⃣7️⃣</span><span class="mult">100배</span></div>
                <div class="pay-item"><span class="syms">💎💎💎</span><span class="mult">15배</span></div>
                <div class="pay-item"><span class="syms">🔔/🍋/🍉</span><span class="mult">3배</span></div>
                <div class="pay-item"><span class="syms">🍒🍒🍒</span><span class="mult">1.5배</span></div>
                <div class="pay-item"><span class="syms">2개 일치</span><span class="mult">1.1배</span></div>
                <div class="pay-item"><span class="syms">🍒 1개</span><span class="mult">0.4배</span></div>
                <div class="pay-item"><span class="syms">🍋 1개</span><span class="mult">0.2배</span></div>
                <div class="pay-item"><span class="syms">ALL IN</span><span class="mult">🔥 역전</span></div>
            </div>

            <!-- 1. 초기 자본금 설정 모달 -->
            <div class="setup-modal" id="setup-modal">
                <div class="setup-title">💰 시작 보유 금액 설정</div>
                <p style="color:#aaa; font-size:0.8rem; margin-bottom:12px;">시작 자본금을 선택하거나 입력하세요.</p>
                <div style="width:100%; max-width:300px;">
                    <div class="preset-btns">
                        <button class="preset-btn" onclick="setPreset(100000)">10 만원</button>
                        <button class="preset-btn" onclick="setPreset(500000)">50 만원</button>
                        <button class="preset-btn" onclick="setPreset(1000000)">100 만원</button>
                        <button class="preset-btn" onclick="setPreset(5000000)">500 만원</button>
                    </div>
                    <input type="number" id="init-balance-input" value="1000000" style="width:100%; padding:8px; border-radius:6px; border:1px solid var(--gold-dark); background:#000; color:#fff; text-align:center; font-size:1.1rem; font-weight:bold; margin-bottom:12px;">
                    <button class="setup-btn" style="width:100%;" onclick="startGame()">게 임 시 작</button>
                </div>
            </div>

            <!-- 2. 최종 정산 모달 -->
            <div class="result-modal" id="result-modal">
                <div class="result-title">📊 정산 최종 결과표</div>
                <div class="result-card">
                    <div class="result-row"><span>시작 자본금:</span><span id="res-init">0원</span></div>
                    <div class="result-row"><span>현재 보유금:</span><span id="res-balance">0원</span></div>
                    <div class="result-row"><span>총 대출금 차감:</span><span id="res-debt" style="color:var(--neon-red);">-0원</span></div>
                    <div class="result-row won"><span>🎉 순수 딴 돈 (+수익):</span><span id="res-won">+0원</span></div>
                    <div class="result-row lost"><span>💸 순수 잃은 돈 (-손실):</span><span id="res-lost">-0원</span></div>
                    <div class="result-row final"><span>최종 손익 수령액:</span><span id="res-final">0원</span></div>
                </div>
                <div id="res-comment" style="font-weight:bold; color:var(--neon-gold); margin-bottom:15px; font-size:0.95rem;">평가 중...</div>
                <button class="setup-btn" onclick="location.reload()" style="width:180px;">🔄 다시 도전하기</button>
            </div>

            <!-- 디지털 LED 전광판 -->
            <div class="display-board">
                <div class="stat-box">
                    <div class="stat-label">보유 금액</div>
                    <div class="stat-value" id="balance">0 원</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">누적 대출금</div>
                    <div class="stat-value debt" id="debt">0 원</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">스핀 횟수</div>
                    <div class="stat-value" id="spin-count">0</div>
                </div>
            </div>

            <!-- 릴 영역 -->
            <div class="reels-frame">
                <div class="payline-indicator"></div>
                <div class="reel-window"><div class="reel-strip" id="reel-0"><div class="symbol">🎰</div></div></div>
                <div class="reel-window"><div class="reel-strip" id="reel-1"><div class="symbol">🎰</div></div></div>
                <div class="reel-window"><div class="reel-strip" id="reel-2"><div class="symbol">🎰</div></div></div>
            </div>

            <!-- 버튼 조작반 -->
            <div class="controls-panel">
                <div class="bet-selector">
                    <button class="bet-btn active" onclick="setBet(10000, this)">1만</button>
                    <button class="bet-btn" onclick="setBet(50000, this)">5만</button>
                    <button class="bet-btn" onclick="setBet(100000, this)">10만</button>
                    <button class="bet-btn all-in-btn" id="allin-btn" onclick="setAllIn(this)">🔥 ALL IN</button>
                </div>

                <div class="action-btns">
                    <button class="spin-btn" id="spin-button" onclick="pullLeverAndSpin()">SPIN!</button>
                    <button class="loan-btn" onclick="getLoan()">💵 대출 (10만)</button>
                </div>

                <button class="cashout-btn" onclick="cashOut()">💵 돈 출금 & 정산 완료하기</button>
            </div>

            <div class="status-message" id="status-msg">시작 자본금을 설정해 주세요.</div>

            <!-- 메탈 코인 트레이 -->
            <div class="coin-tray">CASINO COIN TRAY</div>
        </div>

        <!-- 3D 클래식 레버 -->
        <div class="lever-container" onclick="pullLeverAndSpin()">
            <div class="lever-base"></div>
            <div class="lever-arm" id="lever-arm">
                <div class="lever-ball"></div>
            </div>
        </div>
    </div>

    <script>
        const SYMBOLS = ['7️⃣', '💎', '🔔', '🍋', '🍒', '🍉'];
        let initialBalance = 1000000;
        let balance = 1000000;
        let debt = 0;
        let spins = 0;
        let currentBet = 10000;
        let isAllIn = false;
        let isSpinning = false;

        let totalWon = 0;
        let totalLost = 0;

        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        function playSound(type) {
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);

            if (type === 'tick') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(120, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.05);
                osc.start(); osc.stop(audioCtx.currentTime + 0.05);
            } else if (type === 'win') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
                osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                osc.start(); osc.stop(audioCtx.currentTime + 0.4);
            } else if (type === 'small_win') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start(); osc.stop(audioCtx.currentTime + 0.2);
            } else if (type === 'payback') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(330, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
                osc.start(); osc.stop(audioCtx.currentTime + 0.15);
            } else if (type === 'loan') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(300, audioCtx.currentTime);
                osc.frequency.setValueAtTime(600, audioCtx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start(); osc.stop(audioCtx.currentTime + 0.2);
            } else if (type === 'lever') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(180, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(60, audioCtx.currentTime + 0.2);
                gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start(); osc.stop(audioCtx.currentTime + 0.2);
            }
        }

        function setPreset(val) {
            document.getElementById('init-balance-input').value = val;
        }

        function startGame() {
            const val = parseInt(document.getElementById('init-balance-input').value);
            if (isNaN(val) || val <= 0) {
                alert("올바른 금액을 입력하세요!");
                return;
            }
            initialBalance = val;
            balance = val;
            debt = 0;
            spins = 0;
            totalWon = 0;
            totalLost = 0;
            updateDisplay();
            document.getElementById('setup-modal').style.display = 'none';
            document.getElementById('status-msg').innerText = "행운을 빕니다! 레버를 당기거나 SPIN을 누르세요.";
        }

        function setBet(amount, btn) {
            if (isSpinning) return;
            isAllIn = false;
            currentBet = amount;
            document.querySelectorAll('.bet-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playSound('tick');
            document.getElementById('status-msg').innerText = `베팅금이 ${amount.toLocaleString()}원으로 설정되었습니다.`;
        }

        function setAllIn(btn) {
            if (isSpinning) return;
            if (balance <= 0) {
                document.getElementById('status-msg').innerText = "❌ 보유 잔액이 없어 올인이 불가능합니다. 대출을 받으세요!";
                document.getElementById('status-msg').className = "status-message loss";
                return;
            }

            isAllIn = true;
            currentBet = balance;
            document.querySelectorAll('.bet-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playSound('tick');
            document.getElementById('status-msg').innerText = `🔥 ALL IN! 전액(${balance.toLocaleString()}원)을 베팅합니다!`;
            document.getElementById('status-msg').className = "status-message win";
        }

        function updateDisplay() {
            if (isAllIn && balance > 0) {
                currentBet = balance;
            }
            document.getElementById('balance').innerText = balance.toLocaleString() + ' 원';
            document.getElementById('debt').innerText = debt.toLocaleString() + ' 원';
            document.getElementById('spin-count').innerText = spins;
        }

        function getLoan() {
            if (isSpinning) return;
            const loanAmount = 100000;
            balance += loanAmount;
            debt += loanAmount;
            updateDisplay();
            playSound('loan');
            document.getElementById('status-msg').innerText = "💵 긴급 대출 100,000원이 승인되었습니다!";
            document.getElementById('status-msg').className = "status-message";
        }

        function cashOut() {
            if (isSpinning) return;
            const finalPayout = balance - debt;
            
            document.getElementById('res-init').innerText = initialBalance.toLocaleString() + '원';
            document.getElementById('res-balance').innerText = balance.toLocaleString() + '원';
            document.getElementById('res-debt').innerText = '-' + debt.toLocaleString() + '원';
            document.getElementById('res-won').innerText = '+' + totalWon.toLocaleString() + '원';
            document.getElementById('res-lost').innerText = '-' + totalLost.toLocaleString() + '원';
            
            const resFinalEl = document.getElementById('res-final');
            resFinalEl.innerText = finalPayout.toLocaleString() + '원';
            if (finalPayout >= initialBalance) {
                resFinalEl.style.color = "var(--neon-green)";
            } else {
                resFinalEl.style.color = "var(--neon-red)";
            }

            let comment = "";
            const profit = finalPayout - initialBalance;

            if (finalPayout < 0) {
                comment = "💀 대출금도 못 갚고 파산하셨습니다... 영장 발부 예정입니다.";
            } else if (profit > initialBalance) {
                comment = "🎉 대박! 카지노를 털어버리셨습니다. 즉시 현금화하세요!";
            } else if (profit > 0) {
                comment = "👍 소소하게 이득을 보셨네요! 현명한 퇴장입니다.";
            } else if (profit === 0) {
                comment = "😐 본전치기! 하우스에 봉사 활동 하셨습니다.";
            } else {
                comment = "💸 탕진 완료! 다음엔 대출받지 말고 재도전해 보세요.";
            }

            document.getElementById('res-comment').innerText = comment;
            document.getElementById('result-modal').style.display = 'flex';
        }

        function pullLeverAndSpin() {
            if (isSpinning) return;
            if (balance <= 0 || balance < currentBet) {
                document.getElementById('status-msg').innerText = "❌ 잔액 부족! 대출 버튼을 누르거나 출금하세요.";
                document.getElementById('status-msg').className = "status-message loss";
                return;
            }

            const leverArm = document.getElementById('lever-arm');
            leverArm.classList.add('pulled');
            playSound('lever');

            setTimeout(() => {
                leverArm.classList.remove('pulled');
            }, 300);

            spin();
        }

        function spin() {
            isSpinning = true;
            
            const betPlaced = currentBet;
            balance -= betPlaced;
            totalLost += betPlaced;
            
            spins++;
            updateDisplay();

            document.getElementById('spin-button').disabled = true;
            document.getElementById('status-msg').innerText = isAllIn ? "🔥 ALL IN!! 인생을 건 스핀..." : "🎰 릴 회전 중...";
            document.getElementById('status-msg').className = "status-message";

            let finalResult = [];
            const rand = Math.random();

            if (rand < 0.002) { 
                finalResult = ['7️⃣', '7️⃣', '7️⃣'];
            } else if (rand < 0.01) { 
                finalResult = ['💎', '💎', '💎'];
            } else if (rand < 0.025) { 
                const sym = ['🔔', '🍋', '🍉'][Math.floor(Math.random() * 3)];
                finalResult = [sym, sym, sym];
            } else if (rand < 0.04) { 
                finalResult = ['🍒', '🍒', '🍒'];
            } else if (rand < 0.25) { 
                const sym = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while (other === sym) other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                finalResult = [sym, sym, other].sort(() => Math.random() - 0.5);
            } else if (rand < 0.45) { 
                let nonCherries = SYMBOLS.filter(s => s !== '🍒');
                let s1 = nonCherries[Math.floor(Math.random() * nonCherries.length)];
                let s2 = nonCherries[Math.floor(Math.random() * nonCherries.length)];
                finalResult = ['🍒', s1, s2].sort(() => Math.random() - 0.5);
            } else if (rand < 0.70) { 
                let nonLemons = SYMBOLS.filter(s => s !== '🍋' && s !== '🍒');
                let s1 = nonLemons[Math.floor(Math.random() * nonLemons.length)];
                let s2 = nonLemons[Math.floor(Math.random() * nonLemons.length)];
                finalResult = ['🍋', s1, s2].sort(() => Math.random() - 0.5);
            } else { 
                let s1 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s2 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while ((s1 === s2) || (s2 === s3) || (s1 === s3) || s1==='🍒' || s2==='🍒' || s3==='🍒' || s1==='🍋' || s2==='🍋' || s3==='🍋') {
                    s1 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                    s2 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                    s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                }
                finalResult = [s1, s2, s3];
            }

            const reelStrips = [
                document.getElementById('reel-0'),
                document.getElementById('reel-1'),
                document.getElementById('reel-2')
            ];

            let stops = [false, false, false];
            let counter = 0;

            const interval = setInterval(() => {
                counter++;
                playSound('tick');

                for (let i = 0; i < 3; i++) {
                    if (!stops[i]) {
                        const randomSym = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                        reelStrips[i].innerHTML = `<div class="symbol">${randomSym}</div>`;
                    }
                }

                if (counter > 12) stops[0] = true;
                if (counter > 20) stops[1] = true;
                if (counter > 28) stops[2] = true;

                if (stops[0]) reelStrips[0].innerHTML = `<div class="symbol">${finalResult[0]}</div>`;
                if (stops[1]) reelStrips[1].innerHTML = `<div class="symbol">${finalResult[1]}</div>`;
                if (stops[2]) reelStrips[2].innerHTML = `<div class="symbol">${finalResult[2]}</div>`;

                if (counter > 28) {
                    clearInterval(interval);
                    isSpinning = false;
                    document.getElementById('spin-button').disabled = false;

                    let winMultiplier = 0;
                    let winText = "";
                    let isPayback = false;

                    if (finalResult[0] === '7️⃣' && finalResult[1] === '7️⃣' && finalResult[2] === '7️⃣') {
                        winMultiplier = 100;
                        winText = "🎉 GRAND JACKPOT! 777 대박! (100배)";
                    } else if (finalResult[0] === '💎' && finalResult[1] === '💎' && finalResult[2] === '💎') {
                        winMultiplier = 15;
                        winText = "💎 DIAMOND JACKPOT! (15배)";
                    } else if (finalResult[0] === finalResult[1] && finalResult[1] === finalResult[2]) {
                        if (finalResult[0] === '🍒') {
                            winMultiplier = 1.5;
                            winText = "🍒 체리 3개 당첨! (1.5배)";
                        } else {
                            winMultiplier = 3;
                            winText = `${finalResult[0]} 트리플 당첨! (3배)`;
                        }
                    } else if (finalResult[0] === finalResult[1] || finalResult[1] === finalResult[2] || finalResult[0] === finalResult[2]) {
                        winMultiplier = 1.1;
                        winText = "✨ 2개 심볼 연결! (1.1배)";
                    } else if (finalResult.includes('🍒')) {
                        winMultiplier = 0.4;
                        winText = "🍒 체리 보너스 환급! (0.4배)";
                        isPayback = true;
                    } else if (finalResult.includes('🍋')) {
                        winMultiplier = 0.2;
                        winText = "🍋 레몬 위로금 환급! (0.2배)";
                        isPayback = true;
                    }

                    if (winMultiplier > 0) {
                        const winAmount = Math.floor(betPlaced * winMultiplier);
                        balance += winAmount;
                        totalWon += winAmount;

                        if (isPayback) {
                            playSound('payback');
                            document.getElementById('status-msg').innerText = `${winText} (+${winAmount.toLocaleString()}원 보전)`;
                            document.getElementById('status-msg').className = "status-message payback";
                        } else {
                            if (winMultiplier >= 3) playSound('win');
                            else playSound('small_win');
                            document.getElementById('status-msg').innerText = `${winText} (+${winAmount.toLocaleString()}원)`;
                            document.getElementById('status-msg').className = "status-message win";
                        }
                    } else {
                        document.getElementById('status-msg').innerText = "💸 꽝! (-" + betPlaced.toLocaleString() + "원) 다음 스핀을 노려보세요!";
                        document.getElementById('status-msg').className = "status-message loss";
                    }

                    if (isAllIn && balance === 0) {
                        isAllIn = false;
                        document.querySelectorAll('.bet-btn').forEach(b => b.classList.remove('active'));
                        document.querySelector('.bet-btn').classList.add('active');
                        currentBet = 10000;
                    }

                    updateDisplay();
                }
            }, 60);
        }
    </script>
</body>
</html>
"""

components.html(casino_html, height=860, scrolling=False)
