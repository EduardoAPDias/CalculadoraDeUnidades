from tkinter import *
from tkinter import ttk

#importando Pillow

from PIL import ImageTk, Image

#cores

cor1 = '#3b3b3b' #preto
cor2 = '#ffffff' #branco
cor3 = '#48b3e0' #azul
cor4 = '#f7901b' #azul


janela = Tk()
janela.title('')
janela.geometry('652x260')
janela.configure(bg=cor1)


# frames para janela

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#estilo para janela

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#configurando frame cima

l_app_nome = Label(frame_cima, text='Calculadora de Medidas', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

#configurando frame esquerda

#Botao Massa
img_0= Image.open('images/icons8-weight-40.png')
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text='Peso',image=img_0, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky= NSEW, pady=5, padx=5)

#Botao Tempo
img_1= Image.open('images/icons8-time-40.png')
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, text='Tempo',image=img_1, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_1.grid(row=0, column=1, sticky= NSEW, pady=5, padx=5)

#Botao Comprimento
img_2= Image.open('images/icons8-length-40.png')
img_2 = img_2.resize((46,46))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, text='Comprimento',image=img_2, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_2.grid(row=0, column=2, sticky= NSEW, pady=5, padx=5)

#Botao Area
img_3= Image.open('images/icons8-length-40.png')
img_3 = img_3.resize((46,46))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text='Area',image=img_3, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky= NSEW, pady=5, padx=5)

#Botao Volume
img_3= Image.open('images/icons8-measuring-cup-40.png')
img_3 = img_3.resize((46,46))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text='Area',image=img_3, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky= NSEW, pady=5, padx=5)




janela.mainloop()