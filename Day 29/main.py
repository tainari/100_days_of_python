import csv, pyperclip, random, tkinter
from tkinter import messagebox as mb

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_file = "passwords.csv"

ASCII_LOW = 33
ASCII_HIGH = 126
PASSWORD_LENGTH = 12

def generate_password():
    password = "".join([chr(random.randint(ASCII_LOW,ASCII_HIGH+1)) for _ in range(PASSWORD_LENGTH)])
    password_input.delete(0,tkinter.END)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pw = password_input.get()
    ws = website_input.get()
    eu = email_input.get()
    if pw == "":
        mb.showerror(title="Error", message="Must generate password")
    elif ws == "":
        mb.showerror(title="Error", message="Must enter URL")
    elif eu == "":
        mb.showerror(title="Error", message="Must enter email/username")
    else:
        with open(password_file,'a') as f:
            wr = csv.writer(f)
            wr.writerow([ws,eu,pw])
        mb.showinfo(title="Success",message="Password added successfully")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(width=500,height=500,padx=100,pady=100,background="#FFFFFF",cursor='xterm black')
window.resizable(width=False,height=False)

text = tkinter.Text(window)
text.config(foreground="white", background='black')

logo_image = tkinter.PhotoImage(file="./logo.png")
logo = tkinter.Label(image=logo_image,background="white")
logo.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:",background="white",foreground="black",cursor='xterm red')
website_label.grid(row=1,column=0,padx=5,pady=5)

website_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=35)
website_input.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
website_input.focus_set()


email_label = tkinter.Label(text="Email/Username:",background="white",foreground="black")
email_label.grid(row=2,column=0,padx=5,pady=5)

email_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=35)
email_input.grid(row=2,column=1,columnspan=2,padx=5,pady=5)

password_label = tkinter.Label(text="Password:",background="white",foreground="black")
password_label.grid(row=3,column=0,padx=5,pady=5)

password_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=24)
password_input.grid(row=3,column=1,columnspan=1,padx=5,pady=5)

password_generate_button = tkinter.Button(text="Generate",command=generate_password,highlightbackground="white")
password_generate_button.grid(row=3,column=2,padx=5,pady=5)


add_button = tkinter.Button(text="Add",command=add_password,highlightbackground="white",width=20)
add_button.grid(row=4,column=1,columnspan=2,padx=5,pady=5)


window.mainloop()