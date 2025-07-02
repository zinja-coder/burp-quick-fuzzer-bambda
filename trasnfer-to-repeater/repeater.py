# /// script
# dependencies = [
#   "pyautogui",
#   "tk",
# ]
# ///

"""
Burp Suite GUI Automation - 16 Step Flow with Tkinter and Safety Features

Reads 20 coordinate values (10 pairs) from CSV.
Executes 16 steps with clicks and keyboard shortcuts.
Loops automation for a fixed number of times (configurable).

SAFETY FEATURES:
- Uses PyAutoGUI's built-in FailSafeException for emergency stop
- User can move mouse to any corner of screen to immediately stop
- Countdown before starting to allow user preparation
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
        self.automation_running = False
        self.was_stopped_by_failsafe = False
        self.load_coordinates()

        # Enable PyAutoGUI's built-in fail-safe
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
            print("Executing steps 1-14...")
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

            print("Completed one full cycle of 14 steps.")
            return True
            
        except pyautogui.FailSafeException:
            print("FAILSAFE TRIGGERED: Mouse moved to corner - automation stopped!")
            self.was_stopped_by_failsafe = True
            return False
        except Exception as e:
            print(f"Error during execution: {e}")
            return False

    def run_macro_loop(self):
        print(f"Macro loop started. Will execute {self.max_runs} cycles.")
        print("SAFETY: Move mouse to any screen corner to stop automation immediately")
        
        self.automation_running = True
        
        try:
            for i in range(self.max_runs):
                print(f"Cycle {i+1} of {self.max_runs}")
                if not self.execute_steps():
                    break
                    
        except pyautogui.FailSafeException:
            print("FAILSAFE TRIGGERED: Mouse moved to corner - automation stopped!")
            self.was_stopped_by_failsafe = True
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.automation_running = False
            
        if self.was_stopped_by_failsafe:
            print("AUTOMATION SAFELY TERMINATED BY FAILSAFE")
        else:
            print("Automation completed all cycles normally.")
        print("You can now close the window.")

    def start_gui(self):
        root = tk.Tk()
        root.title("Safe Burp Automation")
        root.geometry("450x180")
        
        # Main label
        main_label = tk.Label(root, text=f"Running automation for {self.max_runs} cycle(s)...", 
                             font=("Arial", 12))
        main_label.pack(pady=10)
        
        # Safety instruction
        safety_label = tk.Label(root, text="SAFETY: Move mouse to ANY screen corner to STOP", 
                               font=("Arial", 10, "bold"), fg="red")
        safety_label.pack(pady=5)
        
        # Additional info
        info_label = tk.Label(root, text="(This uses PyAutoGUI's built-in FailSafe feature)", 
                             font=("Arial", 9), fg="blue")
        info_label.pack(pady=2)
        
        # Status label
        self.status_label = tk.Label(root, text="Preparing to start...", 
                                    font=("Arial", 9), fg="blue")
        self.status_label.pack(pady=10)
        
        # Store root for updates
        self.root = root
        
        def update_status():
            if self.was_stopped_by_failsafe:
                self.status_label.config(text="STOPPED - FailSafe triggered (mouse to corner)", fg="red")
            elif self.automation_running:
                self.status_label.config(text="Running - Move mouse to corner to stop", fg="green")
            else:
                self.status_label.config(text="Completed", fg="blue")
            
            # Schedule next update
            root.after(500, update_status)
        
        # Start status updates
        update_status()
        
        threading.Thread(target=self.run_macro_loop, daemon=True).start()
        root.mainloop()

if __name__ == "__main__":
    print("SAFETY NOTICE:")
    print("This automation uses PyAutoGUI's built-in FailSafe feature.")
    print("Move your mouse to ANY corner of the screen to stop immediately.")
    print()
    print("Countdown before UI automation starts:")
    
    for i in range(5, 0, -1):
        print(f"{i}... (Move mouse to corner now if you want to cancel)")
        time.sleep(1)
    
    print("Starting automation - Move mouse to corner to stop!")
    
    # Change max_runs to control how many times automation runs
    automation = BurpAutomation(max_runs=3)
    automation.start_gui()