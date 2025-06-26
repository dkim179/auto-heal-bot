import pyautogui
import time

print("마우스를 HP 바 시작점으로 이동하세요...")
time.sleep(5)
x, y = pyautogui.position()
print(f"현재 마우스 위치: x={x}, y={y}")