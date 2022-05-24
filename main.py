from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text = 'Timer', fg=GREEN)
    check_marks['text'] = ''
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global label_timer
    global check_marks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        label_timer['text'] = "Work"
        label_timer['fg'] = GREEN
        count_down(work_sec)
    elif reps in [8]:
        label_timer['text'] ="Break"
        label_timer['fg'] = RED
        check_marks['text'] += "✔"
        count_down(long_break_sec)
        reps = 0
    elif reps in [2, 4, 6]:
        label_timer['text'] ="Break"
        label_timer['fg'] = PINK
        check_marks['text'] += "✔"
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(count_min, count_sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Label Timer
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
# my_label["text"] = "New Text"
label_timer.grid(column=1, row=0)

# Label Ticker
check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "normal"))
# my_label["text"] = "New Text"
check_marks.grid(column=1, row=3)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()