# author Jobin S
# email: jobins9633@gmail.com
# follow me on Github

# -----------------------------|
from tkinter import *        # |
from tkinter import font     # |
                             # |
# imported required modules  # |
# -----------------------------|

window = Tk()
value = " "
intro = "SIMPLE CALCULATOR    "
screen = Label(window,
               text=intro,
               bg="#2ecc71",
               fg="#ecf0f1",
               width=22,
               height=2,
               anchor=E,
               font=("Verdana", 22),
               borderwidth=6,
               relief="raised",
               wraplength=410,
               justify="right"
               )
myFont = font.Font(size=12, weight='bold')


# --------Functions for every operations and add values to the display(label)

def btn_clicked(number):
    global value
    value = value + str(number)
    screen.configure(text=value)
    if len(value) > 44:
        screen.configure(font=("Verdana", 15),
                         width=30,
                         height=3);

        if len(value) > 90:
            screen.configure(font=("Verdana", 22),
                             width=22,
                             height=2,
                             text="Error")
            value = " "

    else:
        screen.configure(font=("Verdana", 22),
                         width=22,
                         height=2)


def equal_btn():
    global value
    answer = str(eval(value))
    screen.configure(text=answer)
    value = " "


def clear_btn():
    global value
    value = " "
    screen.configure(text=value)


def backspace_btn():
    global value
    value = value[0:-1]
    screen.configure(text=value)


# -------------------------------------functions ends-------------------

# ---------Hover Effects added to Buttons by the enter and leave event--
def num7enter(event):
    num7['background'] = '#eb4d4b'


def num8enter(event):
    num8['background'] = '#eb4d4b'


def num9enter(event):
    num9['background'] = '#eb4d4b'


def num4enter(event):
    num4['background'] = '#eb4d4b'


def num5enter(event):
    num5['background'] = '#eb4d4b'


def num6enter(event):
    num6['background'] = '#eb4d4b'


def num1enter(event):
    num1['background'] = '#eb4d4b'


def num2enter(event):
    num2['background'] = '#eb4d4b'


def num3enter(event):
    num3['background'] = '#eb4d4b'


def num0enter(event):
    num0['background'] = '#eb4d4b'


def num7leave(event):
    num7['background'] = '#f9ca24'


def num8leave(event):
    num8['background'] = '#f9ca24'


def num9leave(event):
    num9['background'] = '#f9ca24'


def num4leave(event):
    num4['background'] = '#f9ca24'


def num5leave(event):
    num5['background'] = '#f9ca24'


def num6leave(event):
    num6['background'] = '#f9ca24'


def num1leave(event):
    num1['background'] = '#f9ca24'


def num2leave(event):
    num2['background'] = '#f9ca24'


def num3leave(event):
    num3['background'] = '#f9ca24'


def num0leave(event):
    num0['background'] = '#f9ca24'


# --------------------------Hover Effects ends---------------------------


# row 1
num7 = Button(window,
              text=7,
              height=4,
              width=8,
              command=lambda: btn_clicked(7),
              bg='#f9ca24',
              )
num7['font'] = myFont

num8 = Button(window,
              text=8,
              height=4,
              width=8,
              command=lambda: btn_clicked(8),
              bg='#f9ca24')
num8['font'] = myFont

num9 = Button(window,
              text=9,
              height=4,
              width=8,
              command=lambda: btn_clicked(9),
              bg='#f9ca24')
num9['font'] = myFont

mulbtn = Button(window,
                text="X",
                height=4,
                width=8,
                command=lambda: btn_clicked("*"),
                bg='#3498db')
mulbtn['font'] = myFont
# row 1 ends
# row 2
num4 = Button(window,
              text=4,
              height=4,
              width=8,
              command=lambda: btn_clicked(4),
              bg='#f9ca24')
num4['font'] = myFont

num5 = Button(window,
              text=5,
              height=4,
              width=8,
              command=lambda: btn_clicked(5),
              bg='#f9ca24')
num5['font'] = myFont

num6 = Button(window,
              text=6,
              height=4,
              width=8,
              command=lambda: btn_clicked(6),
              bg='#f9ca24')
num6['font'] = myFont

minusbtn = Button(window,
                  text="-",
                  height=4,
                  width=8,
                  command=lambda: btn_clicked("-"),
                  bg='#3498db')
minusbtn['font'] = myFont
# row 2ends
# row 3
num1 = Button(window,
              text=1,
              height=4,
              width=8,
              command=lambda: btn_clicked(1),
              bg='#f9ca24')
num1['font'] = myFont

num2 = Button(window,
              text=2,
              height=4,
              width=8,
              command=lambda: btn_clicked(2),
              bg='#f9ca24')
num2['font'] = myFont

num3 = Button(window,
              text=3,
              height=4,
              width=8,
              command=lambda: btn_clicked(3),
              bg='#f9ca24')
num3['font'] = myFont

addbtn = Button(window,
                text="+",
                height=4,
                width=8,
                command=lambda: btn_clicked("+"),
                bg='#3498db')
addbtn['font'] = myFont
# row3 ends
# row4
dot = Button(window,
             text=".",
             height=4,
             width=8,
             command=lambda: btn_clicked("."),
             bg='#3498db')
dot['font'] = myFont

num0 = Button(window,
              text=0,
              height=4,
              width=8,
              command=lambda: btn_clicked(0),
              bg='#f9ca24')
num0['font'] = myFont

divbtn = Button(window,
                text="/",
                height=4,
                width=8,
                command=lambda: btn_clicked("/"),
                bg='#3498db')
divbtn['font'] = myFont

equalbtn = Button(window,
                  text="=",
                  height=2,
                  width=8,
                  command=equal_btn,
                  bg='#4cd137')
equalbtn['font'] = myFont

clear_btn = Button(window,
                   text="C",
                   height=1,
                   width=3,
                   command=clear_btn,
                   bg='#3498db')
clear_btn['font'] = myFont
photo = PhotoImage(file="./images/backspace.png")
backspace_btn = Button(window,
                       image=photo,
                       height=27,
                       width=35,
                       command=backspace_btn,
                       bg='#3498db')
# row4 ends

# -----binding Hover effects------

num7.bind("<Enter>", num7enter)
num7.bind("<Leave>", num7leave)
num8.bind("<Enter>", num8enter)
num8.bind("<Leave>", num8leave)
num9.bind("<Enter>", num9enter)
num9.bind("<Leave>", num9leave)
num4.bind("<Enter>", num4enter)
num4.bind("<Leave>", num4leave)
num5.bind("<Enter>", num5enter)
num5.bind("<Leave>", num5leave)
num6.bind("<Enter>", num6enter)
num6.bind("<Leave>", num6leave)
num1.bind("<Enter>", num1enter)
num1.bind("<Leave>", num1leave)
num2.bind("<Enter>", num2enter)
num2.bind("<Leave>", num2leave)
num3.bind("<Enter>", num3enter)
num3.bind("<Leave>", num3leave)
num0.bind("<Enter>", num0enter)
num0.bind("<Leave>", num0leave)

# ---binding hover effects end----

# ----------------window modification--------------------
window.geometry("440x530+420+110")
window.resizable(False, False)
window.title("Calculator -by Jobin")
window.iconbitmap(default='./images/calculator-icon.ico')
window.configure(bg='#f5f6fa')
# --------windows modification ends-----------------------

# -----------positioning----------------------------------
screen.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
num7.grid(row=1, column=0, pady=10, padx=10)
num8.grid(row=1, column=1, padx=10)
num9.grid(row=1, column=2, padx=10)
mulbtn.grid(row=1, column=3, padx=10)
num4.grid(row=2, column=0, pady=10, padx=10)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
minusbtn.grid(row=2, column=3)
num1.grid(row=3, column=0, pady=10)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)
addbtn.grid(row=3, column=3, pady=10)
dot.grid(row=4, column=0)
num0.grid(row=4, column=1)
divbtn.grid(row=4, column=2)
equalbtn.place(x=339, y=434)
clear_btn.place(x=339, y=490)
backspace_btn.place(x=388, y=490)

# -------------positioning ends-----------------------------

window.mainloop()
