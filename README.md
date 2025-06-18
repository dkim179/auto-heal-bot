# 🧪 Auto Potion Macro for Online MMORPG Game

A Python-based automation tool that monitors HP/MP bars in real-time and automatically uses potions during gameplay.

## ⚙️ Features
- Detects HP/MP bar percentage with OpenCV and PyAutoGUI
- Uses potions when HP < ???% or MP < ???%  ```user can choose set up the percentage```
- Keyboard macro with custom hotkeys (F1 to start, F2 to stop)
- Optimized for fast and responsive healing

## 🔧 Requirements
- Windows OS
- Python 3.10+
- Modules: `pyautogui`, `cv2`, `numpy`, `pydirectinput`, `keyboard`, `pillow`

## 🔧 Installation

- Clone this repo
- cd auto-heal-bot
- Open cmd using Administrator mode 

## Virtual Environment (Recommended)

- python -m venv venv
- venv\Scripts\activate

## Install dependencies via pip:

pip install -r requirements.txt
python "WhichEverFileYouWant".py

## Important!!
Adjust HP/MP region if needed
The script uses hard-coded regions:


⚠️ Before You Start

Adjust HP/MP region if needed
The script uses hard-coded regions:

hp_bar_region = (80, 8, 164, 6)
mp_bar_region = (80, 22, 164, 6)

Modify them if your UI layout differs.


**How It Works!!!**

Takes a screenshot of the HP/MP bar region

Masks excluded colors and enhances only bar-specific colors

Converts the image to HSV and calculates the colored pixel ratio

If HP or MP is below 87%, it:

Presses G or F 3 times very quickly

Waits 1.5 seconds before the next possible input
        
Feel free to change keys to match your own bindings.

⚠️ Disclaimer
This tool is for personal and educational use only.
Use at your own discretion. Some games may consider automated input as a violation of terms of service, so please check the game's policy before using this tool in competitive or online environments.
