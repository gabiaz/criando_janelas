from tkinter import *
from tkinter import font
import datetime

oppening = Tk()
oppening.geometry("500x300")
oppening.configure(background="#B0B0E0")
oppening.title("      BEM VINDO !")


def clock_time():

    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S\n%d-%m-%Y"))
    txt.set(time)
    oppening.after(1000, clock_time)


def end():
    exit()


msg01 = Label(oppening, text="Visualize data e hora\n clicando no botão com o smile.",
              bg='#B0B0E0', fg='brown', font=("Helvetica", 15))
msg01.pack(pady=10)

button = Button(oppening, text="       \n    :)    \n      ", bg='Linen', fg='brown', command=clock_time)
button.pack(pady=10)

button2 = Button(oppening, text=" Fechar ", bg='Linen', fg='brown', command=end)
button2.pack()

fonte = font.Font(family="Helvetica", size=34, weight='bold')
txt = StringVar()
lbl = Label(oppening, textvariable=txt, font=fonte, foreground="brown", background="#B0B0E0")
lbl.pack()

oppening.mainloop()
