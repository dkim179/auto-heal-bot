import pyautogui
import cv2
import numpy as np
import time
import pydirectinput
import keyboard

hp_bar_region = (80, 8, 164, 6)
mp_bar_region = (80, 22, 164, 6)

# 색상 리스트
hp_rgb_list = [
    (165, 0, 0), (181, 0, 0), (247, 0, 0),
    (255, 0, 0), (255, 8, 8), (255, 74, 74),
]

mp_rgb_list = [
    (0, 24, 132), (0, 24, 148), (0, 57, 206),
    (0, 123, 255), (8, 189, 255), (74, 239, 255),
]

excluded_rgb_list = [
    (189, 206, 214), (90, 99, 115), (41, 41, 49),
    (255, 255, 255), (12, 0, 0)
]

HP_MAX_BASELINE = 87.5
MP_MAX_BASELINE = 74.0

def rgb_to_hsv_range(r, g, b, tol=10):
    color = np.uint8([[[b, g, r]]])
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)[0][0]
    hsv_int = hsv.astype(int)
    lower = np.array([max(hsv_int[0] - tol, 0), max(hsv_int[1] - tol, 0), max(hsv_int[2] - tol, 0)])
    upper = np.array([min(hsv_int[0] + tol, 179), min(hsv_int[1] + tol, 255), min(hsv_int[2] + tol, 255)])
    return lower, upper

def convert_rgb_list_to_hsv_ranges(rgb_list, tol=10):
    lowers, uppers = [], []
    for rgb in rgb_list:
        low, up = rgb_to_hsv_range(*rgb, tol=tol)
        lowers.append(low)
        uppers.append(up)
    return lowers, uppers

excluded_lowers, excluded_uppers = convert_rgb_list_to_hsv_ranges(excluded_rgb_list, tol=5)

def mask_excluded_colors(hsv_img):
    mask = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
    for low, up in zip(excluded_lowers, excluded_uppers):
        temp_mask = cv2.inRange(hsv_img, low, up)
        mask = cv2.bitwise_or(mask, temp_mask)
    return mask

def apply_gradient_over_mask(img, mask, gradient_rgb_list):
    h, w = img.shape[:2]
    for y in range(h):
        color_rgb = gradient_rgb_list[y]
        bgr_color = (color_rgb[2], color_rgb[1], color_rgb[0])
        for x in range(w):
            if mask[y, x] != 0:
                img[y, x] = bgr_color
    return img

def get_bar_percentage(region, gradient_rgb_list, max_baseline):
    screenshot = pyautogui.screenshot(region=region)
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    excluded_mask = mask_excluded_colors(hsv_img)
    img = apply_gradient_over_mask(img, excluded_mask, gradient_rgb_list)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowers, uppers = convert_rgb_list_to_hsv_ranges(gradient_rgb_list, tol=15)
    combined_mask = None
    for low, up in zip(lowers, uppers):
        mask = cv2.inRange(hsv_img, low, up)
        combined_mask = mask if combined_mask is None else cv2.bitwise_or(combined_mask, mask)

    colored_pixels = cv2.countNonZero(combined_mask)
    total_pixels = region[2] * region[3]
    raw_percentage = (colored_pixels / total_pixels) * 100

    corrected = min((raw_percentage / max_baseline) * 100, 100)
    return corrected

def use_g_potion_fast():
    for _ in range(3):
        pydirectinput.press('g')
    time.sleep(0.001)

def use_f_potion_fast():
    for _ in range(3):
        pydirectinput.press('f')
    time.sleep(0.001)

# ------------------- 매크로 제어 로직 -------------------
macro_running = False
cooldown = 1.5
last_hp_pot_time = 0
last_mp_pot_time = 0

def start_macro():
    global macro_running
    if not macro_running:
        macro_running = True
        print("▶ 매크로 시작됨 (F1)")

def stop_macro():
    global macro_running
    if macro_running:
        macro_running = False
        print("⏹ 매크로 중지됨 (F2)")

keyboard.add_hotkey('F1', start_macro)
keyboard.add_hotkey('F2', stop_macro)

print("🟢 프로그램 실행됨 - F1: 시작 / F2: 중지 / Ctrl+C로 종료")

try:
    while True:
        if macro_running:
            hp = get_bar_percentage(hp_bar_region, hp_rgb_list, HP_MAX_BASELINE)
            mp = get_bar_percentage(mp_bar_region, mp_rgb_list, MP_MAX_BASELINE)

            print(f"HP: {hp:.1f}% | MP: {mp:.1f}%")

            now = time.time()

            if hp < 80.3 and now - last_hp_pot_time > cooldown:
                use_g_potion_fast()
                last_hp_pot_time = now
                print(">> G키 빠르게 3번 (HP 87% 미만)")

            if mp < 90 and now - last_mp_pot_time > cooldown:
                use_f_potion_fast()
                last_mp_pot_time = now
                print(">> F키 빠르게 3번 (MP 87% 미만)")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n❌ 프로그램 종료됨.")