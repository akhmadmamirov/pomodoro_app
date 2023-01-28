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
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    windoow.after_cancel(my_timer)
    timer_text.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer,text=f"00:00")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    #8th rep
    if reps == 8:
        count_down(long_break_sec)
        timer_text.config(text="Break", fg=RED)
        
    #1st/3rd/5th/7th reps
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)
        
    #2nd/4th/6th reps
    else:
        count_down(short_break_sec)
        timer_text.config(text="Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = count //  60
    count_sec = count % 60
    
  
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
        
    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = windoow.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in work_sessions:
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
windoow = Tk()
windoow.title("Pomodoro")
windoow.config(padx=100,pady=50, bg=YELLOW)

#Button Commands


#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img)
timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))

#Buttons
start_button = Button(text="Start!", highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset!", highlightbackground=YELLOW, command=timer_reset)

#Texts
timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
check_marks = Label(fg=GREEN, bg=YELLOW)

#Grid
timer_text.grid(row=0, column=1)
canvas.grid(row=1,column=1)
start_button.grid(row=2,column=0)
reset_button.grid(row=2, column=2)
check_marks.grid(row=3, column=1)


windoow.mainloop()