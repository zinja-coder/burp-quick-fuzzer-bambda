# /// script
# dependencies = [
#   "pyautogui",
#   "tk",
# ]
# ///

"""
Mouse Coordinate Capture Script for Burp Suite Automation
This script helps capture mouse coordinates for GUI automation.
"""

import pyautogui
import tkinter as tk

def update_mouse_position():
    pos = pyautogui.position()
    mouse_label.config(text=f"Mouse position: ({pos.x}, {pos.y})")
    root.after(100, update_mouse_position)  # Update every 100ms

# Create basic window
root = tk.Tk()
root.title("Mouse Coordinate Viewer")
root.geometry("300x100")
root.attributes('-topmost', True)  # Keep on top

# Display label
mouse_label = tk.Label(root, text="", font=("Arial", 14))
mouse_label.pack(pady=20)

# Start tracking
update_mouse_position()

# Start GUI loop
root.mainloop()
