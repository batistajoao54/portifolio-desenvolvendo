from tkinter import *

janela = Tk()

janela.resizable(width=FALSE, height=FALSE)
janela.geometry("1000x600")
janela.title("Sacolas Idez")
janela.configure(bg = "#000000")
janela.iconphoto(False, PhotoImage(file="idez.png"))

#criando o app
app_nome_frame = Frame(janela, width=200,height=50, bg='blue', relief="flat")
app_nome_frame.grid(row=0, column=0, )

app_nome_frame1 = Frame(janela, width=300,height=100, bg='red', relief="flat")
app_nome_frame1.grid(row=400, column=3,)

janela.mainloop()
