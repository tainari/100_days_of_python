import csv, pyperclip, random, tkinter, json
import io
from tkinter import messagebox as mb

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_file = "passwords.json"

ASCII_LOW = 33
ASCII_HIGH = 126
PASSWORD_LENGTH = 12

def generate_password():
    password = "".join([chr(random.randint(ASCII_LOW,ASCII_HIGH+1)) for _ in range(PASSWORD_LENGTH)])
    password_input.delete(0,tkinter.END)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- PASSWORD FINDER ------------------------------- #

def find_password():
    target_ws = website_input.get()
    if target_ws == "":
        mb.showerror(title="Error", message="Please enter a website name.")
    else:
        try:
            with open(password_file,'r') as f:
                data = json.load(f)
                if target_ws in data:
                    mb.showinfo(title=f"{target_ws} information", message=f"Username: {data[target_ws]['email']}\nPassword: {data[target_ws]['password']}")
                else:
                    mb.showerror(title="Error",message="Password not found.")
        except FileNotFoundError:
            mb.showerror(title="Error",message="Critical error: Password file not found.")
        except json.decoder.JSONDecodeError:
            mb.showerror(title="Error",message="Password not found.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pw = password_input.get()
    ws = website_input.get()
    eu = email_input.get()
    entry = {ws:{'email':eu,'password':pw}}
    if pw == "":
        mb.showerror(title="Error", message="Must generate password")
    elif ws == "":
        mb.showerror(title="Error", message="Must enter URL")
    elif eu == "":
        mb.showerror(title="Error", message="Must enter email/username")
    else:
        try:
            with open(password_file,'r') as f:
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError:
                    data = entry
                else:
                    if ws in data:
                        answer = mb.askokcancel(title="Overwrite?",message=f"Overwrite existing password for {ws}?")
                        if answer:
                            data.update(entry)
                    else:
                        data.update(entry)
        except FileNotFoundError:
            data = entry
        if answer:
            with open(password_file,"w") as f:
                json.dump(data, f,indent=4)
            password_input.delete(0, tkinter.END)
            website_input.delete(0, tkinter.END)
            mb.showinfo(title="Success",message="Password added successfully")
        else:
            mb.showinfo(title="Aborted", message="Password not updated.")


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

website_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=24)
website_input.grid(row=1,column=1,columnspan=1,padx=5,pady=5)
website_input.focus_set()

website_search_button = tkinter.Button(text="Find Password",command=find_password,highlightbackground="white",width=11)
website_search_button.grid(row=1,column=2,padx=5,pady=5)

email_label = tkinter.Label(text="Email/Username:",background="white",foreground="black")
email_label.grid(row=2,column=0,padx=5,pady=5)

email_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=40)
email_input.grid(row=2,column=1,columnspan=2,padx=5,pady=5)

password_label = tkinter.Label(text="Password:",background="white",foreground="black")
password_label.grid(row=3,column=0,padx=5,pady=5)

password_input = tkinter.Entry(background="white",foreground="black",highlightthickness=0,width=24)
password_input.grid(row=3,column=1,columnspan=1,padx=5,pady=5)

password_generate_button = tkinter.Button(text="Generate",command=generate_password,highlightbackground="white",width=11)
password_generate_button.grid(row=3,column=2,padx=5,pady=5)


add_button = tkinter.Button(text="Add",command=add_password,highlightbackground="white",width=20)
add_button.grid(row=4,column=1,columnspan=2,padx=5,pady=5)


window.mainloop()