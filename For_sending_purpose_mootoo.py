import cv2
import numpy as np
import time
import mss
import pydirectinput
import keyboard

pydirectinput.PAUSE = 0.065

# Define screen regions for HP and MP bars (x, y, width, height)
hp_bar_region = (80, 8, 164, 6)
mp_bar_region = (80, 22, 164, 6)

# List of RGB colors representing HP bar gradient colors
hp_rgb_list = [
    (165, 0, 0), (181, 0, 0), (247, 0, 0),
    (255, 0, 0), (255, 8, 8), (255, 74, 74),
]

# List of RGB colors representing MP bar gradient colors
mp_rgb_list = [
    (0, 24, 132), (0, 24, 148), (0, 57, 206),
    (0, 123, 255), (8, 189, 255), (74, 239, 255),
]

# Colors to be excluded from detection (e.g., background or UI elements)
excluded_rgb_list = [
    (189, 206, 214), (90, 99, 115), (41, 41, 49),
    (255, 255, 255), (12, 0, 0)
]

# Baseline maximum percentage values for HP and MP bars for calibration
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

# Precompute HSV ranges for excluded colors
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

def capture_region(region):
    x, y, width, height = region
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

def get_bar_percentage(region, gradient_rgb_list, max_baseline):
    img = capture_region(region)
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

def use_hp_potion():
    pydirectinput.press('del')
    pydirectinput.press('del')

def use_mp_potion():
    pydirectinput.press('end')
    pydirectinput.press('end')

# ------------------- Macro control and main loop -------------------

macro_running = False
HP_THRESHOLD = 81 # 피 82.0%에 먹음 문대용임
MP_THRESHOLD = 85 # 귀 58.6%에 먹음 문대용임
CHECK_INTERVAL = 0.05  # check every 50ms

def start_macro():
    global macro_running
    if not macro_running:
        macro_running = True
        print("▶ Start (F1)")

def stop_macro():
    global macro_running
    if macro_running:
        macro_running = False
        print("⏹ Pause (F2)")

keyboard.add_hotkey('F1', start_macro)
keyboard.add_hotkey('F2', stop_macro)

print("🟢 Program has been started - F1: Start / F2: Pause / Ctrl+C to exit")

try:
    while True:
        if macro_running:
            hp = get_bar_percentage(hp_bar_region, hp_rgb_list, HP_MAX_BASELINE)
            mp = get_bar_percentage(mp_bar_region, mp_rgb_list, MP_MAX_BASELINE)

            print(f"HP: {hp:.1f}% | MP: {mp:.1f}%")

            if hp < HP_THRESHOLD:
                use_hp_potion()
                print(">> Use HP Potion (DEL)")

            if mp < MP_THRESHOLD:
                use_mp_potion()
                print(">> Use MP Potion (END)")

        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\n❌ Program terminated.")