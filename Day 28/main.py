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
running = True
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global running
    running = False
    pomodoros_complete_label["text"] = ""
    canvas.itemconfig(time_display,text="00:00")
    start.config(state="normal")
    app_title["text"] = "Timer"


# ---------------------------- TIMER MECHANISM ------------------------------- #
# num_pomodoros_complete = 0
# work_status = 1
def start_timer(num_minutes=WORK_MIN,num_pomodoros_complete=0,work_status=1):
    global running
    running = True
    app_title["text"] = "Work" if work_status > 0 else "Rest"
    start.config(state="disabled")
    countdown(int(num_minutes * 60),num_pomodoros_complete,work_status)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(seconds_remaining,num_pomodoros_complete = 0, work_status=1):
    if running:
        if seconds_remaining > 0:
            minutes = seconds_remaining//60
            minutes = minutes if minutes >= 10 else "0"+str(minutes)
            seconds = seconds_remaining % 60
            seconds = seconds if seconds >= 10 else "0"+str(seconds)
            canvas.itemconfig(time_display,text=f"{minutes}:{seconds}")
            window.after(1000, countdown, seconds_remaining-1,num_pomodoros_complete,work_status)
        else:
            work_status *= -1
            if work_status < 0:
                window.tkraise()
                num_pomodoros_complete += 1
                pomodoros_complete_label["text"] = CHECK * num_pomodoros_complete
                if num_pomodoros_complete % 5 == 0:
                    start_timer(LONG_BREAK_MIN,0,-1)
                else:
                    start_timer(SHORT_BREAK_MIN,num_pomodoros_complete,-1)
            else:
                pomodoros_complete_label["text"] = CHECK * num_pomodoros_complete
                start_timer(WORK_MIN,num_pomodoros_complete,work_status)



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=200,pady=100,bg=YELLOW)
window.resizable(width=False,height=False)
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
bg_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=bg_image)
canvas.grid(row=1, column=1)

time_display = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))

app_title = tkinter.Label(text="Timer",foreground=GREEN,background=YELLOW,font=(FONT_NAME,40,"bold"),justify="center")
app_title.grid(row=0, column=1)

start = tkinter.Button(text="Start",command=start_timer,highlightbackground=YELLOW)#,highlightthickness=0,padx=0,pady=0,bd=0,borderwidth=0,background=YELLOW)
start.grid(row=2,column=0)


reset = tkinter.Button(text="Reset",command=reset_timer,highlightbackground=YELLOW)#,highlightthickness=0,padx=0,pady=0,bd=0,borderwidth=0,background=YELLOW)
reset.grid(row=2,column=2)

pomodoros_complete_label = tkinter.Label(text="", background=YELLOW, justify="center", font=(FONT_NAME,12),borderwidth=0)
pomodoros_complete_label.grid(row=3,column=1)


window.mainloop()