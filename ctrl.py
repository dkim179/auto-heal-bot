import time
import pydirectinput
import keyboard

pydirectinput.PAUSE = 0.11

macro_running = False

def start_macro():
    global macro_running
    macro_running = True
    print("▶ Ctrl 매크로 시작됨 (F1)")

def stop_macro():
    global macro_running
    macro_running = False
    print("⏹ Ctrl 매크로 정지됨 (F2)")

keyboard.add_hotkey('F1', start_macro)
keyboard.add_hotkey('F2', stop_macro)

print("🟢 Ctrl 매크로 대기 중 - F1: 시작 / F2: 정지 / Ctrl+C: 종료")

try:
    while True:
        if macro_running:
            pydirectinput.press('ctrl')
            print(">> Ctrl 입력됨")
            time.sleep(0.01)  # 너무 빠르면 0.1로 살짝 올려도 돼
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n❌ 매크로 종료됨.")