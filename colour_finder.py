import cv2
import numpy as np
import pyautogui

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        pixel_hsv = hsv[y, x]
        print(f"Clicked at ({x},{y}) - HSV: {pixel_hsv}")

# 전체 화면 캡처
screenshot = pyautogui.screenshot()
img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

cv2.namedWindow('screen')
cv2.setMouseCallback('screen', mouse_callback)

while True:
    cv2.imshow('screen', img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 누르면 종료
        break

cv2.destroyAllWindows()