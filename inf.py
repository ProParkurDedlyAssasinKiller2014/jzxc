import tkinter as tk
from tkinter import *
from tkinter import messagebox
import  os
def onerej():
    from random import random

    n1 = random() * 100
    n1 = round(n1)
    n2 = random() * 100
    n2 = round(n2)
    n1str = str(n1)
    n2str = str(n2)
    vopros = n1str + '+' + n2str
    plus = n1 + n2

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:
            n1 = random() * 100
            n1 = round(n1)
            n2 = random() * 100
            n2 = round(n2)
            n1str = str(n1)
            n2str = str(n2)
            vopros = n1str + '+' + n2str

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



    n1 = random() * 100
    n1 = round(n1)
    n2 = random() * 100
    n2 = round(n2)
    n1str = str(n1)
    n2str = str(n2)
    vopros = n1str + '-' + n2str
    plus = n1 - n2

    def otv():

        otvet = int(polotv.get())
        if otvet == plus:
            messagebox.showinfo('Верно', 'Ответ верен, так держать')
        else:
            messagebox.showinfo('Неверно', 'Ответ неверен')
        quit()

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
    n1 = random() * 100
    n1 = round(n1)
    n2 = random() * 10
    n2 = round(n2)
    n1str = str(n1)
    n2str = str(n2)
    vopros = n1str + '*' + n2str
    plus = n1 * n2

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
window = Tk()
window.geometry('500x600')
window.title("Main")
frame = Frame( window, padx=10, pady=10)
frame.pack(expand=True)
height_lb = Label(
   frame,
   text="Выберите режим игры "
)
height_lb.grid(row=3, column=1)


cal_btn = Button(
   frame,
   text='1 режим',
   command=onerej
)
cal_btn.grid(row=5, column=0)
cal_btn1 = Button(
   frame,
   text='2 режим',
   command=tworej
)
cal_btn1.grid(row=5, column=1)
cal_btn2 = Button(
   frame,
   text='3 режим',
   command=threerej
)
cal_btn2.grid(row=5, column=2)













window.mainloop()