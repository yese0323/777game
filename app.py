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
    <title>🎰 라스베이거스 럭셔리 777 슬롯머신</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold-light: #fff2a3;
            --gold-mid: #d4af37;
            --gold-dark: #aa7c11;
            --gold-shadow: #5c4100;
            --bg-dark: #0a0612;
            --neon-red: #ff0055;
            --neon-green: #00ff66;
            --neon-gold: #ffcc00;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }

        body {
            background-color: var(--bg-dark);
            background-image: 
                radial-gradient(circle at 50% 20%, #2a0845 0%, #0a0612 80%),
                radial-gradient(circle at 20% 80%, #15002a 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, #1d0010 0%, transparent 50%);
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

        .casino-title {
            font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
            font-size: 2.5rem;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(180deg, #fff 0%, var(--gold-mid) 50%, var(--gold-shadow) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(212, 175, 55, 0.5);
            margin-bottom: 5px;
            letter-spacing: 2px;
        }

        .subtitle {
            color: var(--gold-light);
            font-weight: 700;
            font-size: 0.95rem;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.6);
            letter-spacing: 1px;
        }

        /* 머신 컨테이너 */
        .machine-container {
            position: relative;
            background: linear-gradient(145deg, #2c2114, #110b06);
            border: 8px solid var(--gold-mid);
            border-image: linear-gradient(to bottom, var(--gold-light), var(--gold-mid), var(--gold-dark)) 1;
            border-radius: 24px;
            box-shadow: 
                0 0 40px rgba(212, 175, 55, 0.3),
                inset 0 0 20px rgba(0,0,0,0.8),
                0 20px 50px rgba(0,0,0,0.9);
            padding: 25px 35px;
            width: 100%;
            max-width: 640px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* 초기 설정 모달/오버레이 */
        .setup-modal {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(10, 6, 18, 0.95);
            z-index: 100;
            border-radius: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
            text-align: center;
        }

        .setup-title {
            font-size: 1.6rem;
            color: var(--gold-mid);
            font-weight: 900;
            margin-bottom: 15px;
        }

        .setup-input-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
            max-width: 320px;
            margin-bottom: 20px;
        }

        .setup-btn {
            background: linear-gradient(180deg, var(--gold-mid), var(--gold-dark));
            color: #000;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-weight: 900;
            font-size: 1.1rem;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(212, 175, 55, 0.4);
        }

        .preset-btns {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        .preset-btn {
            background: rgba(255,255,255,0.1);
            border: 1px solid var(--gold-mid);
            color: #fff;
            padding: 8px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
        }

        /* 전광판 */
        .display-board {
            width: 100%;
            background: #000;
            border: 3px solid var(--gold-dark);
            border-radius: 12px;
            padding: 10px 15px;
            margin-bottom: 15px;
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 10px;
            box-shadow: inset 0 0 15px rgba(255, 204, 0, 0.2);
        }

        .stat-box { text-align: center; }
        .stat-label { font-size: 0.7rem; color: #888; margin-bottom: 2px; font-weight: 700; }
        .stat-value {
            font-family: 'Orbitron', monospace;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--neon-gold);
            text-shadow: 0 0 8px rgba(255, 204, 0, 0.7);
        }
        .stat-value.debt { color: var(--neon-red); text-shadow: 0 0 8px rgba(255, 0, 85, 0.7); }

        /* 배당표 */
        .paytable {
            width: 100%;
            background: rgba(0,0,0,0.5);
            border: 1px solid var(--gold-dark);
            border-radius: 8px;
            padding: 8px;
            margin-bottom: 15px;
            font-size: 0.75rem;
            display: flex;
            justify-content: space-around;
            text-align: center;
            color: #ddd;
        }
        .paytable span { color: var(--gold-light); font-weight: bold; }

        /* 릴 하우징 */
        .reels-frame {
            background: #050505;
            border: 4px solid var(--gold-mid);
            border-radius: 16px;
            padding: 15px;
            display: flex;
            gap: 12px;
            box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.95);
            position: relative;
            margin-bottom: 20px;
            width: 100%;
            justify-content: center;
        }

        .payline-indicator {
            position: absolute;
            left: 0; right: 0; top: 50%;
            transform: translateY(-50%);
            height: 2px;
            background: rgba(255, 0, 85, 0.7);
            box-shadow: 0 0 8px var(--neon-red);
            z-index: 5;
            pointer-events: none;
        }

        .reel-window {
            width: 120px;
            height: 130px;
            background: linear-gradient(180deg, #111 0%, #222 50%, #111 100%);
            border: 2px solid #444;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 10px 20px rgba(0,0,0,0.8), inset 0 -10px 20px rgba(0,0,0,0.8);
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
            height: 130px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3.8rem;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
        }

        /* 컨트롤 영역 */
        .controls-panel {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .bet-selector {
            display: flex;
            justify-content: space-between;
            background: rgba(0,0,0,0.4);
            padding: 8px;
            border-radius: 12px;
            border: 1px solid rgba(212, 175, 55, 0.3);
        }

        .bet-btn {
            flex: 1;
            margin: 0 4px;
            padding: 10px 0;
            background: linear-gradient(180deg, #3a3a3a, #1a1a1a);
            border: 1px solid var(--gold-dark);
            border-radius: 8px;
            color: #ccc;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        .bet-btn.active {
            background: linear-gradient(180deg, var(--gold-mid), var(--gold-dark));
            color: #000;
            border-color: var(--gold-light);
            box-shadow: 0 0 12px rgba(212, 175, 55, 0.6);
        }

        .action-btns {
            display: flex;
            gap: 10px;
        }

        .spin-btn {
            flex: 2;
            padding: 16px;
            background: linear-gradient(180deg, #ff4e50, #f9d423);
            border: none;
            border-radius: 12px;
            color: #000;
            font-weight: 900;
            font-size: 1.3rem;
            cursor: pointer;
            box-shadow: 0 5px 0 #990000;
        }

        .loan-btn {
            flex: 1;
            background: linear-gradient(180deg, #00b09b, #96c93d);
            border: none;
            border-radius: 12px;
            color: #000;
            font-weight: 900;
            font-size: 0.95rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #005522;
        }

        .cashout-btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(180deg, #e1eec3, #f05053);
            border: none;
            border-radius: 12px;
            color: #fff;
            font-weight: 900;
            font-size: 1.1rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #880000;
            margin-top: 5px;
        }

        .status-message {
            margin-top: 12px;
            text-align: center;
            font-weight: 700;
            font-size: 1rem;
            height: 25px;
            color: var(--gold-light);
        }

        .loss { color: var(--neon-red); }
        .win { color: var(--neon-green); }

        /* 정산 결과 모달 */
        .result-modal {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(10, 6, 18, 0.98);
            z-index: 200;
            border-radius: 16px;
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 25px;
            text-align: center;
            border: 4px solid var(--gold-mid);
        }

        .result-title {
            font-size: 1.8rem;
            color: var(--gold-light);
            font-weight: 900;
            margin-bottom: 15px;
        }

        .result-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--gold-dark);
            border-radius: 12px;
            padding: 15px;
            width: 100%;
            max-width: 350px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .result-row {
            display: flex;
            justify-content: space-between;
            font-size: 0.95rem;
            color: #ccc;
        }

        .result-row.final {
            border-top: 1px solid #555;
            padding-top: 8px;
            font-weight: 900;
            font-size: 1.1rem;
        }

        .comment-box {
            font-size: 1.05rem;
            font-weight: bold;
            color: var(--neon-gold);
            margin-bottom: 20px;
            line-height: 1.4;
        }
    </style>
</head>
<body>

    <div class="casino-title">🎰 CASINO 777 🎰</div>
    <div class="subtitle">🎰 초고액 배팅 연출! 정산 및 대출 상환 기능 탑재</div>

    <div class="machine-container">
        <!-- 1. 초기 자본금 설정 모달 -->
        <div class="setup-modal" id="setup-modal">
            <div class="setup-title">💰 시작 보유 금액 설정</div>
            <p style="color:#aaa; font-size:0.85rem; margin-bottom:15px;">시작할 때 사용할 자본금을 선택하거나 입력하세요.</p>
            <div class="setup-input-group">
                <div class="preset-btns">
                    <button class="preset-btn" onclick="setPreset(100000)">10 만원</button>
                    <button class="preset-btn" onclick="setPreset(500000)">50 만원</button>
                    <button class="preset-btn" onclick="setPreset(1000000)">100 만원</button>
                    <button class="preset-btn" onclick="setPreset(5000000)">500 만원</button>
                </div>
                <input type="number" id="init-balance-input" value="1000000" style="padding:10px; border-radius:6px; border:1px solid var(--gold-dark); background:#000; color:#fff; text-align:center; font-size:1.1rem; font-weight:bold;">
                <button class="setup-btn" onclick="startGame()">게 임 시 작</button>
            </div>
        </div>

        <!-- 2. 게임 정산 결과 모달 -->
        <div class="result-modal" id="result-modal">
            <div class="result-title">📊 정산 최종 결과표</div>
            <div class="result-card">
                <div class="result-row"><span>시작 자본금:</span><span id="res-init">0원</span></div>
                <div class="result-row"><span>현재 보유금:</span><span id="res-balance">0원</span></div>
                <div class="result-row"><span>총 대출금 차감:</span><span id="res-debt" style="color:var(--neon-red);">-0원</span></div>
                <div class="result-row final"><span>최종 수령액:</span><span id="res-final" style="color:var(--neon-green);">0원</span></div>
            </div>
            <div class="comment-box" id="res-comment">평가 중...</div>
            <button class="setup-btn" onclick="location.reload()" style="width:200px;">🔄 다시 도전하기</button>
        </div>

        <!-- 전광판 -->
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

        <!-- 배당 안내 -->
        <div class="paytable">
            <div>7️⃣7️⃣7️⃣ <span>100배</span></div>
            <div>💎💎💎 <span>15배</span></div>
            <div>🔔/🍋/🍉 <span>3배</span></div>
            <div>🍒🍒🍒 <span>1.5배</span></div>
            <div>2개 일치 <span>1.1배</span></div>
        </div>

        <!-- 릴 영역 -->
        <div class="reels-frame">
            <div class="payline-indicator"></div>
            <div class="reel-window"><div class="reel-strip" id="reel-0"><div class="symbol">🎰</div></div></div>
            <div class="reel-window"><div class="reel-strip" id="reel-1"><div class="symbol">🎰</div></div></div>
            <div class="reel-window"><div class="reel-strip" id="reel-2"><div class="symbol">🎰</div></div></div>
        </div>

        <!-- 컨트롤 영역 (베팅 금액 0 하나 더 붙임) -->
        <div class="controls-panel">
            <div class="bet-selector">
                <button class="bet-btn active" onclick="setBet(10000, this)">10,000원</button>
                <button class="bet-btn" onclick="setBet(50000, this)">50,000원</button>
                <button class="bet-btn" onclick="setBet(100000, this)">100,000원</button>
            </div>

            <div class="action-btns">
                <button class="spin-btn" id="spin-button" onclick="spin()">SPIN!</button>
                <button class="loan-btn" onclick="getLoan()">💵 대출 (10만)</button>
            </div>

            <button class="cashout-btn" onclick="cashOut()">💵 돈 출금 & 정산 완료하기</button>
        </div>

        <div class="status-message" id="status-msg">시작 자본금을 설정해 주세요.</div>
    </div>

    <script>
        const SYMBOLS = ['7️⃣', '💎', '🔔', '🍋', '🍒', '🍉'];
        let initialBalance = 1000000;
        let balance = 1000000;
        let debt = 0;
        let spins = 0;
        let currentBet = 10000; // 0 하나 더 붙임
        let isSpinning = false;

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
                gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
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
            } else if (type === 'loan') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(300, audioCtx.currentTime);
                osc.frequency.setValueAtTime(600, audioCtx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
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
            updateDisplay();
            document.getElementById('setup-modal').style.display = 'none';
            document.getElementById('status-msg').innerText = "행운을 빕니다! SPIN 버튼을 누르세요.";
        }

        function setBet(amount, btn) {
            if (isSpinning) return;
            currentBet = amount;
            document.querySelectorAll('.bet-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            playSound('tick');
        }

        function updateDisplay() {
            document.getElementById('balance').innerText = balance.toLocaleString() + ' 원';
            document.getElementById('debt').innerText = debt.toLocaleString() + ' 원';
            document.getElementById('spin-count').innerText = spins;
        }

        function getLoan() {
            if (isSpinning) return;
            const loanAmount = 100000; // 10만원 대출
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
            document.getElementById('res-final').innerText = finalPayout.toLocaleString() + '원';

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

        function spin() {
            if (isSpinning) return;
            if (balance < currentBet) {
                document.getElementById('status-msg').innerText = "❌ 잔액 부족! 대출 버튼을 누르거나 출금하세요.";
                document.getElementById('status-msg').className = "status-message loss";
                return;
            }

            isSpinning = true;
            balance -= currentBet;
            spins++;
            updateDisplay();

            document.getElementById('spin-button').disabled = true;
            document.getElementById('status-msg').innerText = "🎰 릴 회전 중...";
            document.getElementById('status-msg').className = "status-message";

            let finalResult = [];
            const rand = Math.random();

            if (rand < 0.002) { 
                finalResult = ['7️⃣', '7️⃣', '7️⃣']; // 100배
            } else if (rand < 0.01) { 
                finalResult = ['💎', '💎', '💎']; // 15배
            } else if (rand < 0.025) { 
                const sym = ['🔔', '🍋', '🍉'][Math.floor(Math.random() * 3)];
                finalResult = [sym, sym, sym]; // 3배
            } else if (rand < 0.04) { 
                finalResult = ['🍒', '🍒', '🍒']; // 1.5배
            } else if (rand < 0.32) { 
                const sym = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while (other === sym) other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                finalResult = [sym, sym, other].sort(() => Math.random() - 0.5); // 1.1배
            } else if (rand < 0.70) { 
                const sym = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while (other === sym) other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                finalResult = [sym, sym, other]; // 꽝 (아까운 연출)
            } else { 
                let s1 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s2 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while ((s1 === s2) || (s2 === s3) || (s1 === s3)) {
                    s2 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                    s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                }
                finalResult = [s1, s2, s3]; // 꽝
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
                    } else {
                        if (rand < 0.32) {
                            winMultiplier = 1.1;
                            winText = "✨ 2개 심볼 연결 보너스! (1.1배)";
                        }
                    }

                    if (winMultiplier > 0) {
                        const winAmount = Math.floor(currentBet * winMultiplier);
                        balance += winAmount;
                        
                        if (winMultiplier >= 3) playSound('win');
                        else playSound('small_win');

                        document.getElementById('status-msg').innerText = `${winText} (+${winAmount.toLocaleString()}원)`;
                        document.getElementById('status-msg').className = "status-message win";
                    } else {
                        if (finalResult[0] === finalResult[1]) {
                            document.getElementById('status-msg').innerText = "😱 아깝다! 한 끗 차이로 꽝!";
                        } else {
                            document.getElementById('status-msg').innerText = "💸 꽝입니다! 다음 스핀에 잭팟을 노려보세요.";
                        }
                        document.getElementById('status-msg').className = "status-message loss";
                    }
                    updateDisplay();
                }
            }, 60);
        }
    </script>
</body>
</html>
"""

components.html(casino_html, height=820, scrolling=False)
