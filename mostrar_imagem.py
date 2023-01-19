from tkinter import *
import os

pastaImg = os.path.dirname(__file__)

oppening = Tk()
oppening.geometry("500x400")
oppening.configure(background="#B0B0E0")
oppening.title("      BEM VINDO !")


def show():

    img = PhotoImage(file=pastaImg+"\\gato_fofo.png")
    msg02 = msg01.config(image=img)
    msg02.place(x=250, y=300)


def end():
    exit()


msg01 = Label(oppening, text="Ver uma imagem fofinha? ", background="yellow", font=("Helvetica", 25, "bold"))
msg01.pack(pady=10)

button = Button(oppening, text="sim \n :)", background="yellow", fg="black", command=show)
button.pack(pady=10)

button2 = Button(oppening, text=" fechar \n:(", background="black", fg="white", command=end)
button2.pack(pady=10)

oppening.mainloop()
