from tkinter import *
window = Tk()
window.title("Shhh... It's your Secret Manager!")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
#logo_img = PhotoImage(file = "kisspng-computer-icons-password-portable-network-graphics-user-dashboard-5c57ecf8a47e61.7758533815492661686738.jpg")
logo = PhotoImage(file = "download.png")
canvas.grid(row =0, column=1)

web_label = Label(text = "Which Website?")
web_label.grid(row = 1, column = 0)
web_label.focus()

usern_label = Label(text = "Username")
usern_label.grid(row = 2, column = 0)

pass_label =  Label(text = "Password")
pass_label.grid(row = 3, column = 0)

web_box = Entry(width = 35)
web_box.grid(row = 1, column = 1)

usern_box = Entry(width = 35)
usern_box.grid(row = 2, column = 1)

pass_box = Entry(width = 21)
pass_box.grid(row = 3, column = 1)
gen_pass = Button (text = "Generate Password")
gen_pass.grid(row =3, column = 2)

add_pass = Button(text = "Add", width = 36)
add_pass.grid(row = 4, column = 1, columnspan = 2)

def save_pass():
    website = web_box.get()
    username = usern_box.get()
    password = pass_box.get()

    with open("secrets.txt", "a") as f:
        f.write(f"WEBSITE: {website}   | USERNAME: {username}   | PASSWORD: {password}  \n")


window.mainloop()
