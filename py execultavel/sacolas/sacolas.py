import csv
import pandas as pd
from tkinter.ttk import *
from tkinter import *

#cores
branca,verde,amarelo,preto_cinza,verde_escuro = '#f4f4f2','#848775','#fad755',"#423a22","#334242"

#carregando os dados para dentro do sistema
df_os = pd.read_csv('os.csv')

#criando uma listra com o nome dos coladores e as OS
with open('coladores.csv', 'r', newline='') as coladores:
    arquivo = csv.reader(coladores)
    b = []
    for row in arquivo:
        b.append(row)

lista_os = list(df_os['OS'])

#criando uma janela
janela = Tk()

janela.title("CONTROLE DE SACOLAS")
janela.geometry('700x300')
janela.resizable(width=False,height=False)
janela.configure(background=preto_cinza)

#criando frames e separando a tela
frame_pesquisa = Frame(janela,width=700,height=150,bg=verde_escuro,relief='flat')
frame_pesquisa.grid(row=0,column=0,padx=0,pady=1,sticky=NSEW)

frame_resposta = Frame(janela,width=700,height=150,bg=verde,relief='flat')
frame_resposta.grid(row=1,column=0,padx=0,pady=1,sticky=NSEW)

#criando inputs para a coleta dos dados FRAME PESQUISA
label_dia = Label(frame_pesquisa, text="DIA",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_dia.place(x=5,y=5)
entry_dia = Entry(frame_pesquisa,width=3,justify='left',font=('arial',10),highlightthickness=1)
entry_dia.place(x=7, y=25)

label_mes = Label(frame_pesquisa, text="MÊS",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_mes.place(x=41,y=5)
entry_mes = Entry(frame_pesquisa,width=3,justify='left',font=('arial',10),highlightthickness=1)
entry_mes.place(x=45, y=25)

label_ano = Label(frame_pesquisa, text="ANO",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_ano.place(x=85,y=5)
entry_ano = Entry(frame_pesquisa,width=5,justify='left',font=('arial',10),highlightthickness=1)
entry_ano.place(x=83, y=25)

label_os = Label(frame_pesquisa, text="OS",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_os.place(x=230,y=5)
entry_os = Combobox(frame_pesquisa,width=18,)
entry_os['value'] = lista_os
entry_os.place(x=180, y=25)

label_descricao = Label(frame_pesquisa, text="DESCRIÇÃO:",font=('arial 8 bold'),
                   fg = branca, bg=verde_escuro,anchor=NE)
label_descricao.place(x=330,y=5)

def os_busca():
    nome = entry_os.get()
    df_os_escolha = df_os[df_os["OS"] == nome].copy()
    df_os_escolha['texto'] =df_os_escolha['MARCA']+' '+df_os_escolha['TAMANHO']+" "+df_os_escolha['COR']
    texto = df_os_escolha.iloc[0,10]
    
    entry_descricao = Label(frame_pesquisa,font=('arial',10),text=f'{texto}                                    ',
                       fg=branca, bg=verde_escuro,anchor=NE )
    entry_descricao.place(x=330, y=25)
    
botao_buscar = Button(frame_pesquisa,text="VERIFICAR",font=('Ivy 6 bold'),bg=preto_cinza,
                         fg=amarelo,relief=RAISED,overrelief=RIDGE,command=os_busca)
botao_buscar.place(x=400,y=5)

label_colador = Label(frame_pesquisa, text="COLADOR(A)",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_colador.place(x=5,y=80)
entry_colador= Combobox(frame_pesquisa,width=23,)
entry_colador['value'] = (b[0])
entry_colador.place(x=7, y=100)

label_quantidade = Label(frame_pesquisa, text="QUANTIDADE",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_quantidade.place(x=193,y=80)
entry_quantidade= Entry(frame_pesquisa,width=10,justify='left',font=('arial',10),highlightthickness=1)
entry_quantidade.place(x=200, y=100)

label_status = Label(frame_pesquisa, text="STATUS",font=('arial 10 bold'),
                   fg = amarelo, bg=verde_escuro,anchor=NE)
label_status.place(x=310,y=80)
entry_status= Combobox(frame_pesquisa,width=12,)
entry_status['value'] = ('', "ENVIADO", "RECEBIDO")
entry_status.place(x=300, y=100)

#criando uma função que atualiza os dados assim q apertar os botões
def atualiza():
    dia = entry_dia.get()
    mes = entry_mes.get()
    ano = entry_ano.get()
    osbusca = entry_os.get()
    colador = entry_colador.get()
    quantidade = entry_quantidade.get()
    status_final = entry_status.get()
    
    df_os_atualiza = df_os[df_os["OS"] == osbusca].copy()
    
    marca = df_os_atualiza.iloc[0,4]
    tamanho = df_os_atualiza.iloc[0,5]
    cor = df_os_atualiza.iloc[0,6]
       
    return [dia,mes,ano,osbusca,marca,tamanho,cor,colador,quantidade,status_final]

def avancado():
    lista = atualiza()
    cabeçalho = ['DIA','MES','ANO','OS','MARCA','TAMANHO','COR','COLADOR''','QUANTIDADE','STATUS']
    #print(lista)
    with open("correria.csv","w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(cabeçalho)
        writer.writerow(lista)
      
    df = pd.read_csv('entrada e saida.csv')
    df2 = pd.read_csv('correria.csv')
    
    df_merge = pd.concat([df,df2])
    df_merge.to_csv('entrada e saida.csv', index=False)

    with open('entrada e saida.csv', 'r', newline='') as file:
        arquivo = csv.reader(file)
        a = []
        for row in arquivo:
            a.append(row)

    label_5 = Label(frame_resposta, text=f"{a[-1]}                               ",
                    font=('arial 10 bold'),
                    fg=preto_cinza, bg=verde, anchor=NE)
    label_5.place(x=5, y=35)

    label_4 = Label(frame_resposta, text=f"{a[-2]}                               ",
                    font=('arial 10 bold'),
                    fg=preto_cinza, bg=verde, anchor=NE)
    label_4.place(x=5, y=65)

    label_3 = Label(frame_resposta, text=f"{a[-3]}                               ",
                    font=('arial 10 bold'),
                    fg=preto_cinza, bg=verde, anchor=NE)
    label_3.place(x=5, y=95)

botao_pesquisar = Button(frame_pesquisa,text="ATUALIZAR",font=('Ivy 8 bold'),bg=preto_cinza,
                         fg=amarelo,relief=RAISED,overrelief=RIDGE,command=avancado)
botao_pesquisar.place(x=420,y=97)

#criando algumas saidas de dados no frame resposta
label_titulo = Label(frame_resposta, text="UTIMO REGISTRO",font=('arial 10 bold'),
                   fg = preto_cinza, bg=verde,anchor=NE)
label_titulo.place(x=300,y=5)

janela.mainloop()