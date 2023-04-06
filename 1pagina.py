import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pygame


# creación de ventana para el juego, logo
ventana=tk.Tk()
ventana.title("Desarrollo juego")
ventana.geometry("1430x745+-10+-8")
ventana.config(bg="black")
# insertar imagen capa 1
image = Image.open("nlogo.png")
image = image.resize((1400, 750), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
lbl_img = Label(ventana, image=img)
lbl_img.pack()
#envía saludo del usuario
def envio_boton():
    ventana2 = Toplevel()
    ventana2.title("No lleves bloque completo")
    ventana2.geometry("1430x745+-10+-8")
    valor_entrada = entrada.get()
    etiqueta = Label(ventana2, text="Hola Comandante "+valor_entrada+", el mundo te necesita")
entrada = Entry(ventana, width=20)
entrada.grid(row=0)
envia = Button(ventana, text="empecemos", command=envio_boton)

"""Configurar la musica de inicio"""
pygame.mixer.init()
pygame.mixer.music.load("musica_inicio.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

ventana.mainloop()
