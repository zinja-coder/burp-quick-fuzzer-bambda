# /// script
# dependencies = [
#   "pyautogui",
#   "tk",
# ]
# ///

"""
Burp Suite GUI Automation - 16 Step Flow with Tkinter

Reads 20 coordinate values (10 pairs) from CSV.
Executes 16 steps with clicks and keyboard shortcuts.
Loops automation for a fixed number of times (configurable).
"""

import pyautogui
import time
import csv
import os
import sys
import tkinter as tk
import threading

CSV_FILE = "coordinates.csv"

class BurpAutomation:
    def __init__(self, coord_file=CSV_FILE, max_runs=3):
        self.coord_file = coord_file
        self.coords = []
        self.max_runs = max_runs
        self.load_coordinates()

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1

    def load_coordinates(self):
        if not os.path.exists(self.coord_file):
            print(f"Coordinate file '{self.coord_file}' not found!")
            sys.exit(1)

        with open(self.coord_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                flat = [int(x.strip()) for x in row if x.strip()]
                if len(flat) != 20:
                    print(f"Expected 20 coordinate values (10 pairs), got {len(flat)}")
                    sys.exit(1)
                self.coords = [(flat[i], flat[i+1]) for i in range(0, 20, 2)]
                break  # only read first line

        print(f"Loaded {len(self.coords)} coordinates from '{self.coord_file}'")

    def click(self, index, label=""):
        x, y = self.coords[index]
        print(f"Clicking {label or f'coord #{index + 1}'} at ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(0.1)

    def right_click(self, index, label=""):
        x, y = self.coords[index]
        print(f"Right-clicking {label or f'coord #{index + 1}'} at ({x}, {y})")
        pyautogui.rightClick(x, y)
        time.sleep(0.1)

    def send_keys(self, combo):
        print(f"Sending keys: {combo}")
        pyautogui.hotkey(*combo.split('+'))
        time.sleep(0.1)

    def execute_steps(self):
        try:
            print("Executing steps 1-11...")
            self.click(0, "Step 1")
            self.click(1, "Step 2")
            self.click(2, "Step 3")
            self.send_keys("ctrl+a")  # Step 4
            self.send_keys("ctrl+c")  # Step 5
            self.click(3, "Step 6")
            self.click(4, "Step 7")
            self.click(5, "Step 8")
            self.send_keys("ctrl+a")  # Step 9
            self.send_keys("ctrl+v")  # Step 10
            self.click(6, "Step 11")
            time.sleep(1)

            self.click(7, "Step 12")
            self.right_click(8, "Step 13 (right click)")
            self.click(9, "Step 14")

            print("Completed one full cycle of 16 steps.")
        except Exception as e:
            print(f"Error during execution: {e}")

    def run_macro_loop(self):
        print(f"Macro loop started. Will execute {self.max_runs} cycles.")
        for i in range(self.max_runs):
            print(f"Cycle {i+1} of {self.max_runs}")
            self.execute_steps()
        print("Automation completed all cycles.")
        print("You can now close the window.")

    def start_gui(self):
        root = tk.Tk()
        root.title("Burp Automation Running...")
        root.geometry("350x80")
        label = tk.Label(root, text=f"Running automation for {self.max_runs} cycle(s)...", font=("Arial", 12))
        label.pack(pady=20)

        threading.Thread(target=self.run_macro_loop, daemon=True).start()
        root.mainloop()

if __name__ == "__main__":
    print("Countdown before UI automation starts:")
    for i in range(1, 5):
        print(i)
        time.sleep(1)

    # Change max_runs to control how many times automation runs
    automation = BurpAutomation(max_runs=3)
    automation.start_gui()
