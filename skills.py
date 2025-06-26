import time
import pydirectinput
import keyboard

pydirectinput.PAUSE = 0.2  # 내부 딜레이 완전 제거

cycle_pattern = [
    '1', 'r', 'z', 'd', 'x', 'c', 'v', 'b', 'n', 'a', 'f',
    '2', 'r', 'z', 'd', 'x', 'c', 'v', 'b', 'n', 'a', 'f'
]

# d 키만 0.5초, 나머지는 0.05초
cooldowns = {
    key: 0.35 if key == 'd' else 0.02 for key in cycle_pattern
}

macro_running = False

def start_macro():
    global macro_running
    macro_running = True
    print("▶ 매크로 시작됨 (F1)")

def stop_macro():
    global macro_running
    macro_running = False
    print("⏹ 매크로 정지됨 (F2)")

keyboard.add_hotkey('F1', start_macro)
keyboard.add_hotkey('F2', stop_macro)

print("🟢 매크로 대기 중 - F1: 시작 / F2: 정지 / Ctrl+C: 종료")

try:
    while True:
        if macro_running:
            for key in cycle_pattern:
                if not macro_running:
                    break
                pydirectinput.press(key)
                print(f">> {key} 입력됨")
                time.sleep(cooldowns.get(key, 0.05))
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n❌ 매크로 종료됨.")