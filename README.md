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
- cd python-automation
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

Presses G or F 2 times very quickly

Feel free to change keys to match your own bindings.


----------------------------------------------------------------------------------------------------
## 🎮 Auto Heal Macro GUI Usage

### 1. Install pyinstaller

- cd python-automation
- venv\Scripts\activate
- pip install pyinstaller
- pyinstaller --onefile --windowed --uac-admin GUI.py

- This will generate a /build, /dist, GUI.spec
- ***GUI.exe is located in /dist folder/***

---

### 1.1. Location of GUI Executable

- Create a **New Folder** in your "Desktop"
- Copy and Paste "GUI.exe, practice.py, main.py"
- `GUI.exe`, `main.py`, and `practice.py` **must be located in the same folder**.

---

### 2. Key Features of the GUI

- Start/stop macros for **(main.py)** and **(practice.py)** with button clicks  
- Displays each macro's status (Running / Stopped)  
- Automatically stops all running macros when the program closes

---

### 3. How to Run

1. Run the GUI within a Python 3 environment, or  
2. Double-click the built `GUI.exe` file to launch it.

---

### 4. Administrator Privileges

- Administrator privileges are required to run the macros.  

---

### 5. Hotkeys

- F1: Start macro  
- F2: Pause macro

---

### 6. Notes

- You can directly modify the code to adjust thresholds, delays, and other settings.

---

If you have any questions or issues, please open a ticket on the [Issues](https://github.com/dkim179/python-automation/issues) tab!

⚠️ Disclaimer
This tool is for personal and educational use only.
Use at your own discretion. Some games may consider automated input as a violation of terms of service, so please check the game's policy before using this tool in competitive or online environments.
