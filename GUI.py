import threading
import tkinter as tk
from tkinter import ttk
import subprocess
import os
import signal

# Path to the macro file to be executed
MAIN_PATH = "main.py"
PRACTICE_PATH = "practice.py"

# State Storage
processes = {
    "main": None,
    "practice": None
}

# Macro Execution Function
def toggle_macro(name, script_path, button, status_label):
    global processes
    if processes[name] is None:
        # Run as subprocess (separate process)
        proc = subprocess.Popen(["python", script_path])
        processes[name] = proc
        button.config(text="Stop")
        status_label.config(text="Running", foreground="green")
    else:
        # End Process
        proc = processes[name]
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except:
            os.kill(proc.pid, signal.SIGTERM)
        processes[name] = None
        button.config(text="Start")
        status_label.config(text="Stopped", foreground="red")

# GUI Settings
root = tk.Tk()
root.title("Auto Heal Macro Controller")
root.geometry("350x180")
root.resizable(False, False)

# main.py 
frame_main = ttk.LabelFrame(root, text="main.py (main.py)")
frame_main.pack(fill="x", padx=10, pady=5)

btn_main = ttk.Button(frame_main, text="Start", width=15)
lbl_main_status = ttk.Label(frame_main, text="Stopped", foreground="red")
btn_main.pack(side="left", padx=10, pady=10)
lbl_main_status.pack(side="left", padx=10)

btn_main.config(command=lambda: toggle_macro("main", MAIN_PATH, btn_main, lbl_main_status))

# practice.py
frame_practice = ttk.LabelFrame(root, text="practice.py (practice.py)")
frame_practice.pack(fill="x", padx=10, pady=5)

btn_practice = ttk.Button(frame_practice, text="Start", width=15)
lbl_practice_status = ttk.Label(frame_practice, text="Stopped", foreground="red")
btn_practice.pack(side="left", padx=10, pady=10)
lbl_practice_status.pack(side="left", padx=10)

btn_practice.config(command=lambda: toggle_macro("practice", PRACTICE_PATH, btn_practice, lbl_practice_status))

# End all macros on terminate
def on_close():
    for proc in processes.values():
        if proc:
            proc.terminate()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()