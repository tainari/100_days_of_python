import tkinter

def button_clicked():
    x = input.get()
    my_label["text"] = x


window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500,height=300)


my_label = tkinter.Label(text="Label",font=("Courier",24,"bold"))
my_label.grid(row=0,column=0)

button = tkinter.Button(text="click me",command=button_clicked)
button.grid(row=1,column=1)

new_button = tkinter.Button(text="click me too",command=button_clicked)
new_button.grid(row=0,column=2)


input = tkinter.Entry()
input.grid(row=2,column=3)



window.mainloop()