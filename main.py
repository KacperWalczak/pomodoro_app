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
    checkmarks.config(text='')
    title_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count/60)
    if minutes < 10:
        minutes = f'0{minutes}'
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        start_timer()
        checks = ''
        for i in range(math.floor(reps/2)):
            checks += '✓'
        checkmarks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


section = title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg='white', border=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg='white', border=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()



