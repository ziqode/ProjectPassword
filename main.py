from tkinter import *
from tkinter import messagebox
import json


window = Tk()
window.title("Project Password")
window.config(padx=50, pady=50, bg="teal")


canvas = Canvas(width=200, height=200, bg="teal", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

def save_detail():
    search_text.set("Wait ah...")
    account = account_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data= {
        account:{
            "username": username,
            "password": password
        }
    }
    if len(account) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Your boxes are empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            account_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password():
    account = account_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if account in data:
            username = data[account]["username"]
            password = data[account]["password"]
            messagebox.showinfo(title=account, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{account} not found.")



#Label
account_label = Label(text="Account:", bg="teal")
account_label.grid(column=0, row=1)
username_label = Label(text="Username:", bg="teal")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="teal")
password_label.grid(column=0, row=3)

#Entry
account_entry = Entry(width=20)
account_entry.grid(column=1, row=1)
username_entry = Entry(width=20)
username_entry.grid(column=1, row=2)
username_entry.get()
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)
password_entry.get()

#Button
save_button = Button(text="Save", bg="teal", command=save_detail)
save_button.grid(column=3, row=2)

#Search Button
search_text = StringVar()
search_button = Button(textvariable=search_text, font=("georgia", 8), bg="teal", fg="white", width=21, height=2
                       , command=search_password)
search_text.set("Search")
search_button.grid(column=1, row=4)


window.mainloop()