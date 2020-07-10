from tkinter import *
from tkinter import font

window = Tk()

value = StringVar
value = " "
screen = Label(window,
               text=value,
               bg="#2ecc71",
               fg="#ecf0f1",
               width=22,
               height=2,
               anchor=E,
               font=("Verdana", 22), borderwidth=6, relief="raised"
               )

myFont = font.Font(size=12, weight='bold')


def btn_clicked(number):
    global new_value
    new_value = new_value + str(number)
    screen.configure(text=new_value)


def equal_btn():
    global new_value
    answer = str(eval(new_value))
    screen.configure(text=answer)
    new_value = " "


def clear_btn():
    global new_value
    new_value = " "
    screen.configure(text=new_value)


def backspace_btn():
    global new_value
    new_value = new_value[0:-1]
    screen.configure(text=new_value)



new_value = " "

# row 1
num7 = Button(window,
              text=7,
              height=4,
              width=8,
              command=lambda: btn_clicked(7))
num7['font'] = myFont


num8 = Button(window,
              text=8,
              height=4,
              width=8,
              command=lambda: btn_clicked(8))
num8['font'] = myFont

num9 = Button(window,
              text=9,
              height=4,
              width=8,
              command=lambda: btn_clicked(9))
num9['font'] = myFont

mulbtn = Button(window,
                text="X",
                height=4,
                width=8,
                command=lambda: btn_clicked("*"))
mulbtn['font'] = myFont
# row 1 ends
# row 2
num4 = Button(window,
              text=4,
              height=4,
              width=8,
              command=lambda: btn_clicked(4))
num4['font'] = myFont

num5 = Button(window,
              text=5,
              height=4,
              width=8,
              command=lambda: btn_clicked(5))
num5['font'] = myFont

num6 = Button(window,
              text=6,
              height=4,
              width=8,
              command=lambda: btn_clicked(6))
num6['font'] = myFont

minusbtn = Button(window,
                  text="-",
                  height=4,
                  width=8,
                  command=lambda: btn_clicked("-"))
minusbtn['font'] = myFont
# row 2ends
# row 3
num1 = Button(window,
              text=1,
              height=4,
              width=8,
              command=lambda: btn_clicked(1))
num1['font'] = myFont

num2 = Button(window,
              text=2,
              height=4,
              width=8,
              command=lambda: btn_clicked(2))
num2['font'] = myFont

num3 = Button(window,
              text=3,
              height=4,
              width=8,
              command=lambda: btn_clicked(3))
num3['font'] = myFont

addbtn = Button(window,
                text="+",
                height=4,
                width=8,
                command=lambda: btn_clicked("+"))
addbtn['font'] = myFont
# row3 ends
# row4
dot = Button(window,
             text=".",
             height=4,
             width=8,
             command=lambda: btn_clicked("."))
dot['font'] = myFont

num0 = Button(window,
              text=0,
              height=4,
              width=8,
              command=lambda: btn_clicked(0))
num0['font'] = myFont

divbtn = Button(window,
                text="/",
                height=4,
                width=8,
                command=lambda: btn_clicked("/"))
divbtn['font'] = myFont

equalbtn = Button(window,
                  text="=",
                  height=2,
                  width=8,
                  command=equal_btn)
equalbtn['font'] = myFont

clear_btn = Button(window,
                   text="C",
                   height=1,
                   width=3,
                   command=clear_btn)
clear_btn['font'] = myFont
photo = PhotoImage(file="./images/backspace.png")
backspace_btn = Button(window,
                       image=photo,
                       height=27,
                       width=35,
                       command=backspace_btn)
# row4 ends

window.geometry("440x530+420+110")
window.resizable(False, False)
window.title("Calculator -by Jobin")
window.iconbitmap(default='./images/calculator-icon.ico')
window.configure(bg='#95a5a6')

# positions
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
equalbtn.place(x=339, y=425)
clear_btn.place(x=339, y=482)
backspace_btn.place(x=388, y=482)

window.mainloop()
