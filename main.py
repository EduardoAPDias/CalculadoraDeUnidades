from tkinter import *
from tkinter import ttk

#importando Pillow

from PIL import ImageTk, Image

#cores

cor1 = '#3b3b3b' #preto
cor2 = '#ffffff' #branco
cor3 = '#48b3e0' #azul
cor4 = '#f7901b' #laranja


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

#configurando funcionalidade

unidades = {'peso':[{'g': 1},{'kg': 1000},{'mg': 0.001},{'lb': 0.00220462},{'oz': 0.035274}],
            'comprimento':[],
            'volume':[],
            'tempo':[]
            }

def mostrar_menu():
    
    unidade_de = []
    unidade_para = []
    unidade_valores = []

#configurando frame esquerda

#Botao Massa
img_0= Image.open('images/icons8-weight-50.png')
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text='Peso',image=img_0, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_0.grid(row=0, column=0, sticky= NSEW, pady=5, padx=5)

#Botao Tempo
img_1= Image.open('images/icons8-time-50.png')
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, text='Tempo',image=img_1, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_1.grid(row=0, column=1, sticky= NSEW, pady=5, padx=5)

#Botao Comprimento
img_2= Image.open('images/icons8-length-50.png')
img_2 = img_2.resize((46,46))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, text='Comprimento',image=img_2, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_2.grid(row=0, column=2, sticky= NSEW, pady=5, padx=5)

#Botao Area
img_3= Image.open('images/icons8-square-50.png')
img_3 = img_3.resize((50,50))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text='Area',image=img_3, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_3.grid(row=1, column=0, sticky= NSEW, pady=5, padx=5)

#Botao Volume
img_4= Image.open('images/icons8-measuring-cup-50.png')
img_4 = img_4.resize((50,50))
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_esquerda, text='Volume',image=img_4, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_4.grid(row=1, column=1, sticky= NSEW, pady=5, padx=5)

#Botao Velocidade
img_5= Image.open('images/icons8-speed-50.png')
img_5 = img_5.resize((50,50))
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_esquerda, text='Velocidade',image=img_5, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_5.grid(row=1, column=2, sticky= NSEW, pady=5, padx=5)

#Botao Temperatura
img_6= Image.open('images/icons8-temperature-50.png')
img_6 = img_6.resize((50,50))
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_esquerda, text='Temperatura',image=img_6, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_6.grid(row=3, column=0, sticky= NSEW, pady=5, padx=5)

#Botao Energia
img_7= Image.open('images/icons8-energy-50.png')
img_7 = img_7.resize((50,50))
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_esquerda, text='Energia',image=img_7, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_7.grid(row=3, column=1, sticky= NSEW, pady=5, padx=5)

#Botao Pressão
img_8= Image.open('images/icons8-pipeline-50.png')
img_8 = img_8.resize((50,50))
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_esquerda, text='Pressão',image=img_8, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid' , anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
b_8.grid(row=3, column=2, sticky= NSEW, pady=5, padx=5)



#Frame direito
l_unidade_nome = Label(frame_direita, text='Unidade', height=2,width=15, padx=4, relief='groove', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor1)
l_unidade_nome.place(x=0, y=0)

l_de = Label(frame_direita, text='De', height=1, padx=4, relief='groove', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_de.place(x=0, y=70)
c_de = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_de.place(x=28, y=70)

l_para = Label(frame_direita, text='Para', height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_para.place(x=140, y=70)


















janela.mainloop()