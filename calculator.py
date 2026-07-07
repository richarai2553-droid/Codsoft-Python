from tkinter import *


root = Tk()
root.title("GUI Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

expression = ""


def press(key):
    global expression
    expression += str(key)
    display.delete(0, END)
    display.insert(END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, END)
        display.insert(END, result)
        expression = result
    except:
        display.delete(0, END)
        display.insert(END, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    display.delete(0, END)



display = Entry(root,
                font=("Arial", 22),
                bd=10,
                relief=RIDGE,
                justify="right")

display.pack(fill="both", padx=10, pady=15, ipady=10)



frame = Frame(root, bg="#f0f0f0")
frame.pack()

buttons = [
    ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
    ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
    ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
    ('0',3,0), ('.',3,1), ('=',3,2), ('+',3,3)
]

for (text,row,col) in buttons:

    if text == "=":
        Button(frame,
               text=text,
               width=8,
               height=3,
               bg="green",
               fg="white",
               font=("Arial",12,"bold"),
               command=equal).grid(row=row,column=col,padx=3,pady=3)

    else:
        Button(frame,
               text=text,
               width=8,
               height=3,
               bg="white",
               font=("Arial",12,"bold"),
               command=lambda t=text: press(t)).grid(row=row,column=col,padx=3,pady=3)

Button(root,
       text="Clear",
       bg="red",
       fg="white",
       font=("Arial",12,"bold"),
       width=35,
       height=2,
       command=clear).pack(pady=15)

root.mainloop()