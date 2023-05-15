import tkinter as tk
from tkinter import *
from tkinter import messagebox
import  os
def onerej():
    from random import random

    vopros = '44+66?'
    plus = 110

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def tworej():
    from random import random

    vopros = '571+169?'
    plus = 740

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def threerej():
    from random import random

    vopros = '79+61?'
    plus = 140

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def fourrej():
    from random import random


    vopros = '199+201?'
    plus=400


    def otv():

        otvet = int(polotv.get())
        if otvet == plus:


            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')


    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def fiverej():
    from random import random

    vopros = '115+65?'
    plus = 180

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def sixrej():
    from random import random

    vopros = '150+618?'
    plus = 768

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def sevenrej():
    from random import random

    vopros = '722+88?'
    plus = 810

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def eightrej():
    from random import random

    vopros = '6165+1001?'
    plus = 7166

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:

            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
def ninerej():
    from random import random

    vopros = '405+78?'
    plus = 483

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:
            os.startfile(r'медаль.jpg')
            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')

    window = Tk()
    window.title("1 режим")
    window.geometry('400x300')
    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand=True)
    vopr = Label(
        frame,
        text=vopros
    )
    vopr.grid(row=3, column=1)
    polotv = Entry(
        frame,
    )
    polotv.grid(row=4, column=2, pady=5)
    cal_btn = Button(
        frame,
        text='Проверить',
        command=otv)
    cal_btn.grid(row=5, column=2)
window = Tk()
window.geometry('500x600')
window.title("Main")
frame = Frame( window, padx=10, pady=10)
frame.pack(expand=True)
height_lb = Label(
   frame,
   text="Выберите уровень "
)
height_lb.grid(row=3, column=1)


cal_btn = Button(
   frame,
   text='1 уровень',
   command=onerej
)
cal_btn.grid(row=5, column=0)
cal_btn1 = Button(
   frame,
   text='2 уровень',
   command=tworej
)
cal_btn1.grid(row=5, column=1)
cal_btn2 = Button(
   frame,
   text='3 уровень',
   command=threerej
)
cal_btn2.grid(row=5, column=2)
cal_btn3 = Button(
   frame,
   text='4 уровень',
   command=fourrej
)
cal_btn3.grid(row=6, column=0)
cal_btn4 = Button(
   frame,
   text='5 уровень',
   command=fiverej
)
cal_btn4.grid(row=6, column=1)
cal_btn5 = Button(
   frame,
   text='6 уровень',
   command=sixrej
)
cal_btn5.grid(row=6, column=2)
cal_btn6 = Button(
   frame,
   text='7 уровень',
   command=sevenrej
)
cal_btn6.grid(row=7, column=0)
cal_btn7 = Button(
   frame,
   text='8 уровень',
   command=eightrej
)
cal_btn7.grid(row=7, column=1)
cal_btn8 = Button(
   frame,
   text='9 уровень',
   command=ninerej
)
cal_btn8.grid(row=7, column=2)










window.mainloop()
