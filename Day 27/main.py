import tkinter
# TODO 0: Set up window
window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=200,height=150)
window.config(padx=20,pady=20)

FONT = ("Courier",12)

# TODO 1: Calculate function
def convert_miles_to_km():
    n = miles_to_convert.get()
    try:
        val = float(n) * 1.609
        output_label["text"] = f"{val:.1f}"
    except (TypeError, ValueError):
        output_label["text"] = ""


# TODO 2: input at 1,2
miles_to_convert = tkinter.Entry(width=7)
miles_to_convert.grid(row=1,column=2)


# TODO 3: text at 1,3 saying "miles"
miles_label = tkinter.Label(text="miles",font=FONT)
miles_label.grid(row=1,column=3)

# TODO 4: text at 2,1 saying "is equal to"
equal_label = tkinter.Label(text="is equal to:",font=FONT)
equal_label.grid(row=2,column=1)

# TODO 6: Km at 2.3
km_label = tkinter.Label(text="km",font=FONT)
km_label.grid(row=2,column=3)

# TODO 7: Calculate button at 3,2
calculate_button = tkinter.Button(text="Calculate",command=convert_miles_to_km)
calculate_button.grid(row=3,column=2)

# TODO 5: converted output at 2,2
output_label = tkinter.Label(text="",font=FONT)
output_label.grid(row=2,column=2)

window.mainloop()