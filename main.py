from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter.ttk import *
from Download import *

programa = Tk()
menu1 = Menu(programa)


#JANELA DO PROGRAMA

programa.title("Сonversor YouTube para Mp3")
programa.geometry('400x200')



#UTILITAROS


esp = Entry(programa,width=50)
esp.pack(fill=X,pady=80)



#TEXTO URL:


labelframe0 = LabelFrame(programa, text="COLE A URL:", width=80, height=15)
labelframe0.pack(fill=X,ipady=10)
labelframe0.place(x=160, y=60)


#BOTAO DE LIMPAR


def limpar():
 esp.delete(0,99999999)


B = Button(programa, width=20, text ="LIMPAR", command=limpar)
B.pack(fill=X,ipady=10)
B.place(x=230, y=110)

#BOTÃO DOWNLOAD


def clicked_mp3():
 url = esp.get()
 download_mp3(url)


B2 = Button(programa, width=20, text ="DOWNLOAD", command=clicked_mp3)
B2.pack(fill=X,ipady=10)
B2.place(x=40, y=110)


labelframe1 = LabelFrame(programa, text="Criado por Henrique Wagner")
labelframe1.pack(fill="both", expand="yes")


#MENU (ARQUIVOS)

menu = Menu(menu1, tearoff=0)

menu.add_separator()

menu.add_command(label="Sair", command=programa.quit)

menu1.add_cascade(label="Arquivos", menu=menu)


#MENU (SOBRE)

def donothing():
 messagebox.showinfo("Ajuda", "teste@gmail.com",)

helpmenu = Menu(menu1, tearoff=0)
helpmenu.add_command(label="Contato", command=donothing)
menu1.add_cascade(label="Ajuda", menu=helpmenu)

programa.config(menu=menu1)
programa.mainloop()