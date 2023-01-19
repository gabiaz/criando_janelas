from tkinter import *
import os

pastaImg = os.path.dirname(__file__)

oppening = Tk()
oppening.geometry("500x400")
oppening.configure(background="DarkMagenta")
oppening.title("      BEM VINDO !")


def show():

    img = PhotoImage(file=pastaImg+"\\gato_fofo.png")
    msg02 = msg01.config(image=img)
    msg02.place(x=250, y=300)


def end():
    exit()


msg01 = Label(oppening, text="Ver uma imagem fofinha? ", background="DarkGoldenRod", font=("Helvetica", 25, "bold"))
msg01.pack(pady=10)

button = Button(oppening, text="sim \n :)", background="DarkGoldenRod", fg="black", command=show)
button.pack(pady=10)

button2 = Button(oppening, text=" fechar ", background="black", fg="white", command=end)
button2.pack()

oppening.mainloop()
