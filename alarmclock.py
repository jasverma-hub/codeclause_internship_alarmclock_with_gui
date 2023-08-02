import tkinter as tk
import datetime as dt
import time
import winsound as ws

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Alarm Clock")
        self.root.geometry("600x200")
        self.root.config(bg="#87BDD8")
        self.root.resizable(width=False, height=False)
        self.root.eval('tk::PlaceWindow . center')

        self.time_format_label = tk.Label(
            self.root,
            text="Remember to set time in 24-hour format!",
            fg="white",
            bg="#36486B",
            font=("Arial", 15)
        )
        self.time_format_label.place(x=0, y=160)

        self.add_time_label = tk.Label(
            self.root,
            text="Hour     Minute     Second",
            font=60,
            fg="white",
            bg="#87BDD8"
        )
        self.add_time_label.place(x=220, y=10)

        self.set_alarm_label = tk.Label(
            self.root,
            text="Set Time for Alarm: ",
            fg="white",
            bg="#034F84",
            relief="solid",
            font=("Helvetica", 13, "bold")
        )
        self.set_alarm_label.place(x=5, y=50)

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.second_var = tk.StringVar()

        self.hour_entry = tk.Entry(
            self.root,
            textvariable=self.hour_var,
            bg="#FEFBD8",
            width=4,
            font=20
        )
        self.hour_entry.place(x=220, y=53)

        self.minute_entry = tk.Entry(
            self.root,
            textvariable=self.minute_var,
            bg="#FEFBD8",
            width=4,
            font=20
        )
        self.minute_entry.place(x=297, y=53)

        self.second_entry = tk.Entry(
            self.root,
            textvariable=self.second_var,
            bg="#FEFBD8",
            width=4,
            font=20
        )
        self.second_entry.place(x=390, y=53)

        self.submit_button = tk.Button(
            self.root,
            text="Set The Alarm",
            fg="white",
            bg="#82B74B",
            width=15,
            command=self.get_alarm_time,
            font=20
        )
        self.submit_button.place(x=140, y=100)

    def get_alarm_time(self):
        alarm_set_time = f"{self.hour_var.get()} : {self.minute_var.get()} : {self.second_var.get()}"
        self.alarm(alarm_set_time)

    def alarm(self, set_alarm_timer):
        while True:
            time.sleep(1)
            actual_time = dt.datetime.now()
            current_time = actual_time.strftime("%H : %M : %S")
            current_date = actual_time.strftime("%d / %m / %Y")
            the_message = "Current Time: " + str(current_time)
            print(the_message)
            if current_time == set_alarm_timer:
                ws.PlaySound("alarm-clock.wav", ws.SND_ASYNC)
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
