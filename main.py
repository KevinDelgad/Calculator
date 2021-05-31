from tkinter import *
from tkinter.colorchooser import askcolor
root = Tk()
root.title("Calculator")

expression = ""

#Create Functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)


def clear():
    global expression
    expression = ""
    label_result.config(text = expression)


def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)

#Create GUI
label_result = Label(root, text='')
label_result.grid(row=0, column=0, columnspan=4)

#Buttons 1 - /
button_1 = Button(root, text="1", width = 4, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", width = 4, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", width = 4, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_Divide = Button(root, text="/", width = 4, command=lambda: add("/"))
button_Divide.grid(row=1, column=3)

#Buttons 4 - *
button_4 = Button(root, text="4", width = 4, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", width = 4, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", width = 4, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_Multiply = Button(root, text="*", width = 4, command=lambda: add("*"))
button_Multiply.grid(row=2, column=3)

#Buttons 7 - "-"
button_7 = Button(root, text="7", width = 4, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", width = 4, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", width = 4, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_Sub = Button(root, text="-", width = 4, command=lambda: add("-"))
button_Sub.grid(row=3, column=3)

#Buttons C - +
button_Clear = Button(root, text="C", width = 4, command=lambda: clear())
button_Clear.grid(row=4, column=0)

button_0 = Button(root, text="0", width = 4, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_Decimal = Button(root, text=".", width = 4, command=lambda: add("."))
button_Decimal.grid(row=4, column=2)

button_Plus = Button(root, text="+", width = 4, command=lambda: add("+"))
button_Plus.grid(row=4, column=3)

#EqualButton

button_Equal = Button(root, text="=", width=21, command=lambda: calculate())
button_Equal.grid(row=5, column=0, columnspan=4)

root.mainloop()