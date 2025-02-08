import tkinter as tk
from tkinter import Toplevel, Label, Button
from datetime import datetime
from khayyam import JalaliDate

def show_cute_message(title, message, button_color="#28a745"):

    msg_window = Toplevel(root)
    msg_window.title(title)
    msg_window.geometry("500x300")
    msg_window.configure(bg="#f4f4f9")
    msg_window.resizable(False, False)

    frame = tk.Frame(msg_window, bg="#f4f4f9", padx=30, pady=30)
    frame.pack(fill="both", expand=True)

    message_label = Label(frame, text=message, font=("Comic Sans MS", 16, "bold"), bg="#f4f4f9", fg="#343a40", justify="center")
    message_label.pack(pady=50)

    ok_button = Button(frame, text="OK", font=("Comic Sans MS", 14, 'bold'), bg=button_color, fg="white", command=msg_window.destroy, width=15, height=2, relief="flat", bd=0)
    ok_button.pack(pady=20)


    def on_enter(e):
        ok_button.config(bg="#218838")
    
    def on_leave(e):
        ok_button.config(bg=button_color)

    ok_button.bind("<Enter>", on_enter)
    ok_button.bind("<Leave>", on_leave)


def is_jalali(year, month, day):
    try:

        JalaliDate(year, month, day)
        return True
    except ValueError:
        return False

def calculate_exact_age():
    day_input = day_entry.get().strip()
    month_input = month_entry.get().strip()
    year_input = year_entry.get().strip()

    current_day_input = current_day_entry.get().strip()
    current_month_input = current_month_entry.get().strip()
    current_year_input = current_year_entry.get().strip()

    if not day_input or not month_input or not year_input or not current_day_input or not current_month_input or not current_year_input:
        show_cute_message("Error", "Please enter a valid birthdate and current date!", button_color="#ff6347")
        return

    try:

        is_birthdate_jalali = is_jalali(int(year_input), int(month_input), int(day_input))
        is_current_date_jalali = is_jalali(int(current_year_input), int(current_month_input), int(current_day_input))

        if is_birthdate_jalali:
            dob = JalaliDate(int(year_input), int(month_input), int(day_input)).todate()
        else:
            dob = datetime(int(year_input), int(month_input), int(day_input))

        if is_current_date_jalali:
            current_date = JalaliDate(int(current_year_input), int(current_month_input), int(current_day_input)).todate()
        else:
            current_date = datetime(int(current_year_input), int(current_month_input), int(current_day_input))

        today = datetime.today()

        age_in_seconds = (current_date - dob).total_seconds()

        years = int(age_in_seconds // (365.25 * 24 * 3600))
        age_in_seconds %= (365.25 * 24 * 3600)

        months = int(age_in_seconds // (30.44 * 24 * 3600))
        age_in_seconds %= (30.44 * 24 * 3600)

        days = int(age_in_seconds // (24 * 3600))
        age_in_seconds %= (24 * 3600)


        seconds = int(age_in_seconds)


        show_cute_message("Exact Age Calculation", 
                           f"Yay! 🎉\nYour Age is: {years} years,\n{months} months,\n{days} days,\n{seconds} seconds 🎂",
                           button_color="#28a745")
    except ValueError:
        show_cute_message("Error", "Invalid date format! Please enter valid numbers for day, month, and year.", button_color="#ff6347")


root = tk.Tk()
root.title("Exact Age Calculator")
root.geometry("440x780")
root.resizable(False, False)
root.configure(bg="#f4f4f9")


frame = tk.Frame(root, bg="#ffffff", padx=30, pady=40, relief="solid", bd=2, highlightbackground="#17a2b8", highlightthickness=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

day_label = tk.Label(frame, text="Day:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
day_label.grid(row=0, column=0, pady=15)
day_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
day_entry.grid(row=0, column=1, pady=15)

month_label = tk.Label(frame, text="Month:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
month_label.grid(row=1, column=0, pady=15)
month_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
month_entry.grid(row=1, column=1, pady=15)

year_label = tk.Label(frame, text="Year:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
year_label.grid(row=2, column=0, pady=15)
year_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
year_entry.grid(row=2, column=1, pady=15)

separator = tk.Canvas(frame, height=2, width=350, bg="#343a40", bd=1, highlightthickness=0)
separator.grid(row=3, columnspan=5, pady=20)

current_day_label = tk.Label(frame, text="Current Day:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
current_day_label.grid(row=4, column=0, pady=15)
current_day_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
current_day_entry.grid(row=4, column=1, pady=15)

current_month_label = tk.Label(frame, text="Current Month:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
current_month_label.grid(row=5, column=0, pady=15)
current_month_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
current_month_entry.grid(row=5, column=1, pady=15)

current_year_label = tk.Label(frame, text="Current Year:", font=("Arial", 18, 'bold'), bg="#ffffff", fg="#343a40")
current_year_label.grid(row=6, column=0, pady=15)
current_year_entry = tk.Entry(frame, font=("Arial", 18), width=12, bd=2, relief="solid", borderwidth=1, highlightbackground="#28a745", highlightthickness=2)
current_year_entry.grid(row=6, column=1, pady=15)

calculate_button = tk.Button(frame, text="Calculate Exact Age", font=("Arial", 16, 'bold'), bg="#28a745", fg="white", command=calculate_exact_age, width=25, height=2, relief="solid", bd=2)
calculate_button.grid(row=7, columnspan=2, pady=30)


exit_button = tk.Button(frame, text="Exit", font=("Arial", 16, 'bold'), bg="#dc3545", fg="white", command=root.quit, width=25, height=2, relief="solid", bd=2)
exit_button.grid(row=8, columnspan=2, pady=20)


root.mainloop()
