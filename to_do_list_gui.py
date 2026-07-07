from tkinter import *

# Create window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="lightblue")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def clear_tasks():
    listbox.delete(0, END)

# Heading
Label(root, text="My To-Do List",
      font=("Arial", 18, "bold"),
      bg="lightblue").pack(pady=10)

# Entry Box
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
Button(root, text="Add Task",
       command=add_task,
       bg="green",
       fg="white",
       width=15).pack(pady=5)

Button(root, text="Delete Task",
       command=delete_task,
       bg="red",
       fg="white",
       width=15).pack(pady=5)

Button(root, text="Clear All",
       command=clear_tasks,
       bg="orange",
       fg="white",
       width=15).pack(pady=5)

# Listbox
listbox = Listbox(root,
                  width=35,
                  height=12,
                  font=("Arial", 12))
listbox.pack(pady=15)

root.mainloop()