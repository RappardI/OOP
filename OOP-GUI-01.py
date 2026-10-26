import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("600x500")

answer = Text(width=10, height=5)
answer.place(x=500, y=400)


def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get("1.0", "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)

        else:
            answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0, END)



B1 = tk.Button(top, text="4", width = 10, height = 5, command=lambda: show("4"))
B1.place(x=100, y=300)

B2 = tk.Button(top, text="5", width = 10, height = 5, command=lambda: show("5"))
B2.place(x=200, y=300)

B3 = tk.Button(top, text="6", width = 10, height = 5, command=lambda: show("6"))
B3.place(x=300, y=300)

B4 = tk.Button(top, text="1", width = 10, height = 5,command=lambda: show("1"))
B4.place(x=100, y=400)

B5 = tk.Button(top, text="2", width = 10, height = 5, command=lambda: show("2"))
B5.place(x=200, y=400)

B6 = tk.Button(top, text="3", width = 10, height = 5, command=lambda: show("3"))
B6.place(x=300, y=400)

B7 = tk.Button(top, text="7", width = 10, height = 5, command=lambda: show("7"))
B7.place(x=100, y=200)

B8 = tk.Button(top, text="8", width = 10, height = 5, command=lambda: show("8"))
B8.place(x=200, y=200)

B9 = tk.Button(top, text="9", width = 10, height = 5, command=lambda: show("9"))
B9.place(x=300, y=200)

B10 = tk.Button(top, text="+/-", width = 10, height = 5, command=lambda: show("+/-"))
B10.place(x=400, y=200)

B11 = tk.Button(top, text="/", width = 10, height = 5, command=lambda: show("/"))
B11.place(x=400, y=300)

B12 = tk.Button(top, text="*", width = 10, height = 5, command=lambda: show("*"))
B12.place(x=400, y=400)





top.mainloop()