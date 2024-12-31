import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.resizable(False, False)
window.title("Mile <> Kilometer Converter")
window.config(padx=20, pady=20)

options = ["km","mi"]

def convert_mi_to_km():
    try:
        miles = float(number_input.get())
    except ValueError:
        return
    km = miles * 1.60934
    output_value.config(text=str(km))
    output_unit.config(text="km")

def convert_km_to_mi():
    try:
        km = float(number_input.get())
    except ValueError:
        return
    miles = km / 1.60934
    output_value.config(text=str(miles))
    output_unit.config(text="mi")

def convert_number():
    unit = unit_string.get()
    if unit_string.get() == "km":
        convert_km_to_mi()
    else:
        convert_mi_to_km()
    # output_value.config(text=str(output))

number_input = tk.Entry()
number_input.grid(row=0, column=1)

unit_string = tk.StringVar()
unit_string.set("mi")
input_unit = tk.OptionMenu(window, unit_string, *options)
input_unit.grid(row=0, column=2)

equal = tk.Label(text="is equal to")
equal.grid(row=1, column=0)
output_value = tk.Label(text="")
output_value.grid(row=1, column=1)
output_unit = tk.Label(text="")
output_unit.grid(row=1, column=2)
button = tk.Button(text="Calculate", command=convert_number)
button.grid(row=2, column=1)


window.mainloop()