#bibliotecas
# qt, gtk, wxwindows, tk

# Importa todas as classes e funções do módulo tkinter
from tkinter import *
# Cria uma instância da classe Tk, que representa a janela principal da aplicação
janela = Tk()
# Define o título da janela como "Empresa"
janela.title("Empresa")
# Define o ícone da janela, que é carregado a partir do arquivo "photos.ico"
janela.iconbitmap("photos.ico")
# Define a cor de fundo da janela como "DeepSkyBlue"
janela["bg"] = "DeepSkyBlue"
etiqueta = Label(janela,height=20, width=80, text="Olá python!", cursor= "dot")
etiqueta.pack()

janela.geometry ("1500x400+50+20")
# Inica o loop principal da interface gráfica, mantendo a janela aberta e interativa
janela.mainloop()


