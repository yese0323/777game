import streamlit as st
import streamlit.components.v1 as components

# Streamlit 페이지 설정
st.set_page_config(
    page_title="🎰 라스베이거스 777 카지노 슬롯머신",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 화려한 카지노 UI 및 슬롯머신 웹 앱 (HTML/CSS/JS)
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
            color: var(--neon-green);
            font-weight: 700;
            font-size: 0.95rem;
            text-align: center;
            margin-bottom: 25px;
            text-shadow: 0 0 10px rgba(0, 255, 102, 0.6);
            letter-spacing: 1px;
        }

        /* 슬롯 머신 프레임 */
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
            padding: 30px 40px;
            width: 100%;
            max-width: 620px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* 대형 전광판 */
        .display-board {
            width: 100%;
            background: #000;
            border: 3px solid var(--gold-dark);
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: inset 0 0 15px rgba(255, 204, 0, 0.2);
        }

        .stat-box {
            text-align: center;
            flex: 1;
        }

        .stat-label {
            font-size: 0.75rem;
            color: #888;
            margin-bottom: 4px;
            font-weight: 700;
        }

        .stat-value {
            font-family: 'Orbitron', monospace;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--neon-gold);
            text-shadow: 0 0 8px rgba(255, 204, 0, 0.7);
        }

        /* 배당표 안내판 */
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
            margin-bottom: 25px;
            width: 100%;
            justify-content: center;
        }

        .payline-indicator {
            position: absolute;
            left: 0;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            height: 2px;
            background: rgba(255, 0, 85, 0.7);
            box-shadow: 0 0 8px var(--neon-red);
            z-index: 5;
            pointer-events: none;
        }

        .reel-window {
            width: 120px;
            height: 140px;
            background: linear-gradient(180deg, #111 0%, #222 50%, #111 100%);
            border: 2px solid #444;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            box-shadow: inset 0 10px 20px rgba(0,0,0,0.8), inset 0 -10px 20px rgba(0,0,0,0.8);
        }

        .reel-strip {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .symbol {
            width: 120px;
            height: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
        }

        /* 베팅 및 컨트롤 영역 */
        .controls-panel {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 15px;
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
            font-size: 0.9rem;
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
            gap: 12px;
        }

        .spin-btn {
            flex: 2;
            padding: 18px;
            background: linear-gradient(180deg, #ff4e50, #f9d423);
            border: none;
            border-radius: 12px;
            color: #000;
            font-family: 'Noto Sans KR', sans-serif;
            font-weight: 900;
            font-size: 1.4rem;
            cursor: pointer;
            box-shadow: 0 6px 0 #990000, 0 10px 20px rgba(0,0,0,0.5);
            transition: all 0.1s;
            text-transform: uppercase;
        }

        .spin-btn:active {
            transform: translateY(4px);
            box-shadow: 0 2px 0 #990000, 0 5px 10px rgba(0,0,0,0.5);
        }

        .spin-btn:disabled {
            background: #555;
            color: #888;
            box-shadow: none;
            cursor: not-allowed;
            transform: none;
        }

        .loan-btn {
            flex: 1;
            background: linear-gradient(180deg, #00b09b, #96c93d);
            border: none;
            border-radius: 12px;
            color: #000;
            font-weight: 900;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 0 4px 0 #005522;
        }

        .loan-btn:active {
            transform: translateY(2px);
            box-shadow: 0 2px 0 #005522;
        }

        /* 상태 메시지 */
        .status-message {
            margin-top: 15px;
            text-align: center;
            font-weight: 700;
            font-size: 1.1rem;
            height: 30px;
            color: var(--gold-light);
            text-shadow: 0 0 8px rgba(0,0,0,0.8);
        }

        .loss { color: var(--neon-red); }
        .win { color: var(--neon-green); animation: pulse 0.5s infinite alternate; }

        @keyframes pulse {
            from { transform: scale(1); }
            to { transform: scale(1.05); }
        }
    </style>
</head>
<body>

    <div class="casino-title">🎰 CASINO 777 🎰</div>
    <div class="subtitle">✨ 당첨 확률 대폭 UP! 모든 이모티콘 3개 일치 시 당첨!</div>

    <div class="machine-container">
        <!-- 상단 스탯 전광판 -->
        <div class="display-board">
            <div class="stat-box">
                <div class="stat-label">보유 금액 (BALANCE)</div>
                <div class="stat-value" id="balance">10,000 원</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">스핀 횟수 (SPINS)</div>
                <div class="stat-value" id="spin-count">0</div>
            </div>
        </div>

        <!-- 배당 안내 -->
        <div class="paytable">
            <div>7️⃣7️⃣7️⃣ <span>50배</span></div>
            <div>💎💎💎 <span>10배</span></div>
            <div>🔔/🍋/🍉 <span>3배</span></div>
            <div>🍒🍒🍒 <span>1.5배</span></div>
            <div>🍒🍒? (체리2개) <span>1.1배</span></div>
        </div>

        <!-- 3개 릴 스롯 하우징 -->
        <div class="reels-frame">
            <div class="payline-indicator"></div>
            
            <div class="reel-window">
                <div class="reel-strip" id="reel-0">
                    <div class="symbol">🎰</div>
                </div>
            </div>
            <div class="reel-window">
                <div class="reel-strip" id="reel-1">
                    <div class="symbol">🎰</div>
                </div>
            </div>
            <div class="reel-window">
                <div class="reel-strip" id="reel-2">
                    <div class="symbol">🎰</div>
                </div>
            </div>
        </div>

        <!-- 베팅 컨트롤 영역 -->
        <div class="controls-panel">
            <div class="bet-selector">
                <button class="bet-btn active" onclick="setBet(1000, this)">1,000원</button>
                <button class="bet-btn" onclick="setBet(5000, this)">5,000원</button>
                <button class="bet-btn" onclick="setBet(10000, this)">10,000원</button>
            </div>

            <div class="action-btns">
                <button class="spin-btn" id="spin-button" onclick="spin()">SPIN!</button>
                <button class="loan-btn" onclick="getLoan()">💵 대출 받기</button>
            </div>
        </div>

        <div class="status-message" id="status-msg">행운을 빕니다! 버튼을 누르세요.</div>
    </div>

    <script>
        const SYMBOLS = ['7️⃣', '💎', '🔔', '🍋', '🍒', '🍉'];
        let balance = 10000;
        let spins = 0;
        let currentBet = 1000;
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
                osc.start();
                osc.stop(audioCtx.currentTime + 0.05);
            } else if (type === 'win') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
                osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1);
                gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.4);
            } else if (type === 'small_win') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);
            } else if (type === 'loan') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(300, audioCtx.currentTime);
                osc.frequency.setValueAtTime(600, audioCtx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);
            }
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
            document.getElementById('spin-count').innerText = spins;
        }

        function getLoan() {
            balance += 10000;
            updateDisplay();
            playSound('loan');
            document.getElementById('status-msg').innerText = "💵 카지노 긴급 대출 10,000원이 지급되었습니다!";
            document.getElementById('status-msg').className = "status-message";
        }

        function spin() {
            if (isSpinning) return;
            if (balance < currentBet) {
                document.getElementById('status-msg').innerText = "❌ 잔액이 부족합니다! 대출을 받아보세요.";
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

            // 높은 당첨 확률 로직 설정 (체험용 높은 승률)
            let finalResult = [];
            const rand = Math.random();

            if (rand < 0.01) { 
                // 1% - 대잭팟 777 (50배)
                finalResult = ['7️⃣', '7️⃣', '7️⃣'];
            } else if (rand < 0.05) { 
                // 4% - 다이아몬드 3개 (10배)
                finalResult = ['💎', '💎', '💎'];
            } else if (rand < 0.15) { 
                // 10% - 종/레몬/수박 중 3개 일치 (3배)
                const sym = ['🔔', '🍋', '🍉'][Math.floor(Math.random() * 3)];
                finalResult = [sym, sym, sym];
            } else if (rand < 0.30) { 
                // 15% - 체리 3개 일치 (1.5배)
                finalResult = ['🍒', '🍒', '🍒'];
            } else if (rand < 0.65) { 
                // 35% - 소액 보너스: 체리 2개 포함 (1.1배) -> 자주 당첨됨!
                finalResult = ['🍒', '🍒', SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)]];
                // 섞어주기
                finalResult.sort(() => Math.random() - 0.5);
            } else { 
                // 35% - 꽝
                let s1 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s2 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                let s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                while (s1 === s2 && s2 === s3) s3 = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
                finalResult = [s1, s2, s3];
            }

            // 릴 회전 애니메이션
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

                    // 당첨 판정 및 배당 계산
                    let winMultiplier = 0;
                    let winText = "";

                    if (finalResult[0] === '7️⃣' && finalResult[1] === '7️⃣' && finalResult[2] === '7️⃣') {
                        winMultiplier = 50;
                        winText = "🎉 GRAND JACKPOT! 777 대박! (50배)";
                    } else if (finalResult[0] === '💎' && finalResult[1] === '💎' && finalResult[2] === '💎') {
                        winMultiplier = 10;
                        winText = "💎 DIAMOND JACKPOT! (10배)";
                    } else if (finalResult[0] === finalResult[1] && finalResult[1] === finalResult[2]) {
                        if (finalResult[0] === '🍒') {
                            winMultiplier = 1.5;
                            winText = "🍒 체리 3개 당첨! (1.5배)";
                        } else {
                            winMultiplier = 3;
                            winText = `${finalResult[0]} 트리플 당첨! (3배)`;
                        }
                    } else {
                        // 체리 2개 보너스 체크 (1.1배)
                        const cherryCount = finalResult.filter(s => s === '🍒').length;
                        if (cherryCount >= 2) {
                            winMultiplier = 1.1;
                            winText = "🍒 체리 2개 보너스 당첨! (1.1배)";
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
                        document.getElementById('status-msg').innerText = "💸 아깝게 꽝! 다음 기회에...";
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

# Streamlit 내부에 렌더링
components.html(casino_html, height=780, scrolling=False)
