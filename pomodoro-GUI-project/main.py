from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=200, height=224)
#pomo_image = PhotoImage(file = "pomodoro-timer-flat-icon-vector-concept-time-managment-effective-distribution-working-isolated-white-style-83744456.jpg")
pomo_image= PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image= pomo_image)
canvas.pack()

window.mainloop()