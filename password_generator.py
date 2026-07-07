from tkinter import *
from tkinter import messagebox
import random
import string

# Window
root = Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#EAF6F6")
root.resizable(False, False)

# Function
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(random.choice(characters) for i in range(length))

        password_entry.delete(0, END)
        password_entry.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter a valid number")


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied successfully!")

def clear():
    length_entry.delete(0, END)
    password_entry.delete(0, END)

# Heading
Label(root,
      text="Password Generator",
      font=("Arial",18,"bold"),
      bg="#EAF6F6").pack(pady=10)

# Length
Label(root,
      text="Enter Password Length",
      bg="#EAF6F6",
      font=("Arial",12)).pack()

length_entry = Entry(root,font=("Arial",14))
length_entry.pack(pady=5)

# Password Box
password_entry = Entry(root,font=("Arial",14),width=30)
password_entry.pack(pady=10)

# Buttons
Button(root,
       text="Generate Password",
       bg="green",
       fg="white",
       command=generate_password).pack(pady=5)

Button(root,
       text="Copy Password",
       bg="blue",
       fg="white",
       command=copy_password).pack(pady=5)

Button(root,
       text="Clear",
       bg="red",
       fg="white",
       command=clear).pack(pady=5)

root.mainloop()