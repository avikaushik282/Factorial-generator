from tkinter import *

def fact():
    n = int(inp.get())
    print(n)
    f = 1
    if n == 0:
        out.config(text='1')
    else:
        for i in range(1,n+1):
            f *= i
        out.config(text=str(f))

def table():
    n = int(inp.get())
    r = [i*n for i in range(1,11)]
    out.config(text=r)

def even():
    n = int(inp.get())
    if n%2 == 0:
        out.config(text='Even')
    else:
        out.config(text='Odd')

def addition():
    n = int(inp.get())
    s = 0
    for i in range(1, n+1):
        s += i
    out.config(text=str(s))

window = Tk()
window.title("Factorial")
window.config(pady=50, padx=50)

label = Label(text='Put any Number: ')
label.grid(row=0, column=0)

inp = Entry()
inp.grid(row=1, column=0)

button = Button(text='Table', command=table)
button.grid(row=2, column= 0)

button = Button(text='Factorial', command=fact)
button.grid(row=3, column= 0)

button = Button(text='Even/Odd', command=even)
button.grid(row=4, column= 0)

button = Button(text='Addition', command=addition)
button.grid(row=5, column= 0)

out = Label(text='Output')
out.grid(row=6,column=0)

window.mainloop()
