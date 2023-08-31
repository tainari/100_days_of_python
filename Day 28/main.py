import tkinter, time

# ---------------------------- CONSTANTS ------------------------------- #
#colours from color hunt
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEST_MIN = 0.1
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✅"

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
num_pomodoros_complete = 0
work_status = 1
def start_timer(num_minutes=TEST_MIN):
    countdown(int(num_minutes * 60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(seconds_remaining):
    if seconds_remaining > 0:
        print(seconds_remaining)
        minutes = seconds_remaining//60
        minutes = minutes if minutes >= 10 else "0"+str(minutes)
        seconds = seconds_remaining % 60
        seconds = seconds if seconds >= 10 else "0"+str(seconds)
        canvas.itemconfig(time_display,text=f"{minutes}:{seconds}")
        window.after(1000, countdown, seconds_remaining-1)
    else:
        num_pomodoros_complete += 1
        work_status *= -1
        if work_status < 0:
            if num_pomodoros_complete % 5 == 0:
                start_timer(LONG_BREAK_MIN)
            else:
                start_timer(SHORT_BREAK_MIN)
        else:
            start_timer(WORK_MIN)



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=200,pady=100,bg=YELLOW)
window.resizable(width=False,height=False)
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
bg_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=bg_image)
canvas.grid(row=1, column=1)
# canvas.pack()

# app_title = canvas.create_text(100,0,text="Timer",fill=GREEN,font=(FONT_NAME,40,"bold"))
time_display = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))

app_title = tkinter.Label(text="Timer",foreground=GREEN,background=YELLOW,font=(FONT_NAME,40,"bold"),justify="center")
app_title.grid(row=0, column=1)
# app_title.place(x=50,y=-50)

start = tkinter.Button(text="Start",command=start_timer,highlightbackground=YELLOW)#,highlightthickness=0,padx=0,pady=0,bd=0,borderwidth=0,background=YELLOW)
start.grid(row=2,column=0)
# start.place(x=-20,y=220)


reset = tkinter.Button(text="Reset",command=reset_timer,highlightbackground=YELLOW)#,highlightthickness=0,padx=0,pady=0,bd=0,borderwidth=0,background=YELLOW)
reset.grid(row=2,column=2)
# reset.place(x=160,y=220)

pomodoros_complete_label = tkinter.Label(text=CHECK, background=YELLOW, justify="center", font=(FONT_NAME,12),borderwidth=0)
pomodoros_complete_label.grid(row=3,column=1)
# pomodoros_complete_label.place(x=80,y=250)

# window.minsize(width=500,height=500)
# bg = tkinter.Label(image=bg_image)
# bg.place(x=0,y=0)


window.mainloop()