
import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import winsound

def start_alarm(alarm_time):
    def alarm_thread():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                winsound.Beep(2000, 2000)
                messagebox.showinfo("Alarm", "Wake up! Alarm ringing...")
                break
            time.sleep(1)
    threading.Thread(target=alarm_thread, daemon=True).start()

class AlarmApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alarm App")
        self.geometry("300x200")

        tk.Label(self, text="Set Alarm (HH:MM:SS)", font=("Arial", 12)).pack(pady=10)
        self.time_entry = tk.Entry(self, font=("Arial", 14), justify="center")
        self.time_entry.pack(pady=5)

        tk.Button(self, text="Set Alarm", font=("Arial", 12), command=self.set_alarm).pack(pady=10)

        self.current_label = tk.Label(self, text="", font=("Arial", 12))
        self.current_label.pack(pady=10)

        self.update_time()

    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.current_label.config(text=f"Current Time: {now}")
        self.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time = self.time_entry.get()
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            start_alarm(alarm_time)
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Format", "Please enter time as HH:MM:SS")

if __name__ == "__main__":
    app = AlarmApp()
    app.mainloop()
