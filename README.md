# auto-heal-bot
Python automation tool that monitors health and mana bars in a game and automatically uses potions when thresholds are low.

# 🧪 Auto Potion Macro for Online MMORPG Game

A lightweight automation tool for the Korean MMORPG Ganme that monitors your character’s HP and MP bars and automatically uses potions when they fall below a specified threshold.

- ✅ Uses HP (`G`) or MP (`F`) potions automatically
- 🚀 Presses the potion key **3 times rapidly** for reliability
- ⏱ Waits 1.5 seconds before next use (cooldown)
- 🖥 Uses OpenCV + HSV color analysis to detect health/mana bars

---

## 🔧 Installation

### 1. Open cmd using Administrator mode 

### 2. Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies via pip:

pip install -r requirements.txt

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


**Hotkeys**

G: Use HP potion

F: Use MP potion

Defined here:

```
python
Copy
Edit
def use_g_potion_fast():
    for _ in range(3):
        pydirectinput.press('g')

def use_f_potion_fast():
    for _ in range(3):
        pydirectinput.press('f')
```
        
Feel free to change keys to match your own bindings.

⚠️ Disclaimer
This tool is for personal and educational use only.
Use at your own discretion. Some games may consider automated input as a violation of terms of service, so please check the game's policy before using this tool in competitive or online environments.


