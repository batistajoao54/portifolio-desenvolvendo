#importando as bibliotecas que iremos usar
from tkinter import  ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

#cores que usaremos no nosso projeto
cor_preta = "#000000"
cor_cinza = "#f0f3f5"
cor_branca = "#feffff"
cor_valor = "#38576b"
cor_letra = "#403d3d"
cor_azul = "#6f9fbd"
cor_vermelha = "#ef5350"
cor_verde = "#93cd95"

#criando a janela
janela = Tk()
janela.title("")
janela.geometry('500x450')
janela.configure(background=cor_cinza)
janela.resizable(width=FALSE,height=FALSE)

style = Style(janela)
style.theme_use("clam")

#criando frames
frame_cima = Frame(janela,width=500,height=50,bg=cor_valor,relief="flat")
frame_cima.grid(row=0,column=0,padx=0,pady=1,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=150,bg=cor_cinza,relief="flat")
frame_baixo.grid(row=1,column=0,padx=0,pady=1,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=cor_branca,relief="flat")
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

#configurando frame cima
l_nome = Label(frame_cima,text="Agenda Telefónica", anchor=NE, font=('arial 20 bold'),bg=cor_valor, fg= cor_branca)
l_nome.place(x=120,y=5)

l_linha = Label(frame_cima,text="",width=500, anchor=NE, font=('arial 1'),bg=cor_branca, fg= cor_branca)
l_linha.place(x=0,y=48)

#configurando frame baixo
#espaço do nome
l_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10'),bg=cor_cinza,fg= cor_letra)
l_nome.place(x=10,y=20)
e_nome = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
e_nome.place(x=80,y=20)

#espaço do sexo
l_sexo = Label(frame_baixo,text='Sexo *', anchor=NW, font=('Ivy 10'),bg=cor_cinza,fg= cor_letra)
l_sexo.place(x=10,y=50)
c_sexo = Combobox(frame_baixo,width=27)
c_sexo['value'] = ('','F','M')
c_sexo.place(x=80,y=50)

#espaço do telefone
l_tel = Label(frame_baixo,text='Telefone *', anchor=NW, font=('Ivy 10'),bg=cor_cinza,fg= cor_letra)
l_tel.place(x=10,y=80)
e_tel = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
e_tel.place(x=80,y=80)

#espaço do email
l_email = Label(frame_baixo,text='Email *', anchor=NW, font=('Ivy 10'),bg=cor_cinza,fg= cor_letra)
l_email.place(x=10,y=110)
e_email = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
e_email.place(x=80,y=110)

#espaço procurar
b_procurar = Button(frame_baixo,text='Procurar',font=('Ivy 8 bold'),bg=cor_cinza,fg= cor_letra,relief=RAISED,overrelief=RIDGE)
b_procurar.place(x=290,y=20)
e_procurar = Entry(frame_baixo,width=16,justify='left',font=('',11),highlightthickness=1)
e_procurar.place(x=350,y=21)

#espaço ver dados
b_ver_dados = Button(frame_baixo,text='Ver dados',width=10,font=('Ivy 8 bold'),bg=cor_cinza,fg= cor_letra,relief=RAISED,overrelief=RIDGE)
b_ver_dados.place(x=290,y=50)

#botões de alterações
b_adicionar = Button(frame_baixo,text='Adicionar',width=10,font=('Ivy 8 bold'),bg=cor_cinza,fg= cor_letra,relief=RAISED,overrelief=RIDGE)
b_adicionar.place(x=400,y=50)

b_atualizar = Button(frame_baixo,text='Atualizar',width=10,font=('Ivy 8 bold'),bg=cor_cinza,fg= cor_letra,relief=RAISED,overrelief=RIDGE)
b_atualizar.place(x=400,y=80)

b_deletar = Button(frame_baixo,text='Deletar',width=10,font=('Ivy 8 bold'),bg=cor_cinza,fg= cor_letra,relief=RAISED,overrelief=RIDGE)
b_deletar.place(x=400,y=110)

#configurando o frame tabela
list_header = ['Nome', 'Sexo', 'Telefone', 'Email']

dados = [
    ['João','M','8934786','joao@gmail.com'],
    ['Maria','F','123456','maria@gmail.com']
         ]

tree = ttk.Treeview(frame_tabela,selectmode="extended",columns=list_header,show="headings")

#scroll vertical
vsb = ttk.Scrollbar(
    frame_tabela,orient='vertical',command=tree.yview()
)

#scroll horizontal
hsb = ttk.Scrollbar(
    frame_tabela,orient='horizontal',command=tree.xview()
)

tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

tree.grid(column=0,row=0,sticky='nsew')
vsb.grid(column=1,row=0,sticky='ns')
hsb.grid(column=0,row=1,sticky='ew')

#tree cabecalho
tree.heading(0,text='Nome',anchor=NW)
tree.heading(1,text='Sexo',anchor=NW)
tree.heading(2,text='Telefone',anchor=NW)
tree.heading(3,text='Email',anchor=NW)

#tree corpo
tree.column(0,width=150,anchor='nw')
tree.column(1,width=50,anchor='nw')
tree.column(2,width=100,anchor='nw')
tree.column(3,width=170,anchor='nw')

for item in dados:
    tree.insert("", 'end', values=item)


janela.mainloop()
