from tkinter import *

window = Tk()
window.title("Miles to KM Converter Tool")
window.minsize(width=600, height=300)

user_input = Entry(width=9)
user_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row =0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column =1, row=1)

def milesToKm():

    miles = float(user_input.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")

calculate = Button(text="Calculate", command = milesToKm)
calculate.grid(column=2, row=2)


window.mainloop()