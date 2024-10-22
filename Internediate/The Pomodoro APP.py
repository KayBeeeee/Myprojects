#The POMODORO APP using Tkinter 
#This can be used as a timer for achieving tasks


import tkinter as tk
from tkinter import ttk
import time

class PomodoroApp:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro App")

        self.work_time = 25 * 60  # 25 minutes in seconds
        self.short_break_time = 5 * 60  # 5 minutes in seconds
        self.long_break_time = 15 * 60  # 15 minutes in seconds

        self.current_time = self.work_time
        self.is_running = False

        self.label = ttk.Label(master, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.reset_button = ttk.Button(master, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def format_time(self, time_in_seconds):
        minutes = time_in_seconds // 60
        seconds = time_in_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

        while self.is_running and self.current_time > 0:
            self.label.config(text=self.format_time(self.current_time))
            self.master.update()
            time.sleep(1)
            self.current_time -= 1

        if self.current_time == 0:
            self.stop_timer()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.current_time = self.work_time
        self.label.config(text=self.format_time(self.current_time))
        self.stop_timer()

root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()