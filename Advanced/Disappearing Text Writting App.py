# The project is 
#  An online writing app where if you stop typing, your work will disappear. 

import tkinter as tk
from threading import Timer

class WriteOrLoseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Write or Lose Your Work")
        
        # Label
        self.label = tk.Label(
            root, text="Keep typing, or your work will vanish!", font=("Arial", 14)
        )
        self.label.pack(pady=10)

        # Text area
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        # Bind text area to keypress events
        self.text_area.bind("<Key>", self.reset_timer)

        # Start the timer
        self.timer = None
        self.start_timer()

    def start_timer(self):
        """Starts or resets the timer to clear text."""
        if self.timer is not None:
            self.timer.cancel()
        self.timer = Timer(5.0, self.clear_text)  # 5-second timeout
        self.timer.start()

    def reset_timer(self, event=None):
        """Resets the timer when the user types."""
        self.start_timer()

    def clear_text(self):
        """Clears the text area."""
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "You stopped typing! Start again.")
        self.start_timer()

    def on_close(self):
        """Cleans up the timer on close."""
        if self.timer is not None:
            self.timer.cancel()
        self.root.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = WriteOrLoseApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # Handle window close
    root.mainloop()
