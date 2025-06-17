import pyautogui
import cv2
import numpy as np

hp_bar_region = (80, 8, 164, 6)  
  # 이 부분 본인 환경에 맞게 조정하세요

screenshot = pyautogui.screenshot(region=hp_bar_region)
img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

cv2.imwrite("hp_bar_sample.png", img)
print("hp_bar_sample.png 저장 완료!")