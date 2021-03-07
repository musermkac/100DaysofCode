from tkinter import *

window = Tk()
window.title("My First GUI Project")
window.minsize(width=600, height=300)

my_label = Label(text="Hey there!", font=("Times New Roman", 24, "bold"))
my_label.pack()


def button_click():
    print("Button was clicked")
    my_label.config(text="Button was clicked")

button = Button(text="Click Me!", command = button_click)
button.pack()










window.mainloop()