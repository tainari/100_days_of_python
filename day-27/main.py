import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.resizable(False, False)
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)



def convert_mi_to_km():
    try:
        miles = float(number_input.get())
    except ValueError:
        return
    km = miles * 1.60934
    km_value.config(text=str(km))

number_input = tk.Entry()
number_input.grid(row=0, column=1)
mi = tk.Label(text="Miles")
mi.grid(row=0, column=2)
equal = tk.Label(text="is equal to")
equal.grid(row=1, column=0)
km_value = tk.Label(text="")
km_value.grid(row=1, column=1)
km = tk.Label(text="Km")
km.grid(row=1, column=2)
button = tk.Button(text="Calculate", command=convert_mi_to_km)
button.grid(row=2, column=1)


window.mainloop()