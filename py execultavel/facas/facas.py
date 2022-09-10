from tkinter.ttk import *
from tkinter import *

#cores
branca = '#f4f4f2'
azul_escuro = '#0034c4'
azul_claro = '#007fff'
verde = '#848775'
verde_claro = "#48cfae"
vermelho = "#f03f3b"



#criando a janela
janela = Tk()

janela.title("LOCALIZADOR")
janela.geometry('300x100')
janela.resizable(width=False,height=False)
janela.configure(background=verde)

#criando os frames

frame_pesquisa = Frame(janela,width=300,height=48,bg=azul_escuro,relief='flat')
frame_pesquisa.grid(row=0,column=0,padx=0,pady=1,sticky=NSEW)

frame_resposta = Frame(janela,width=300,height=50,bg=azul_escuro,relief='flat')
frame_resposta.grid(row=1,column=0,padx=0,pady=1,sticky=NSEW)

#configurando o frame_pesquisa

label_faca = Label(frame_pesquisa, text="Digite o número da faca:",font=('arial 12 bold'),
                   fg = branca, bg=azul_escuro,anchor=NE)
label_faca.place(x=4,y=12)

entry_faca = Entry(frame_pesquisa,width=5,justify='left',font=('arial',15),highlightthickness=1)
entry_faca.place(x=195, y=10)

#dados das facas

cima_c1 = ['2','180','121','120','109','104','107','13','183','105',
            '176','7','194','132','9','163','101','126','119','118',
            '117','125','218']

cima_c2 = [
    '154','193','202','201','187','123','185','5','205','164','139','211','141',
    '50','51','138','168','165','151','124','216','149','54','156','216','137',
    '212','140','148','144','146','136','162','217'
]

parede = [
    '57','166','145','197','55','158','172','159','173','142','147','174','60','61',
    '170','169','198','62','157','209','153','160','175','64','171','127b','167'
]

baixo_c1 = [
    '106','luciano','14','130','131','186','108','112','190','200','116','129',
    '3','8','210','127a','133','219','182'
]

baixo_c2 = [
    '10','134','135','58','59','16','111','110','192','196','189','102',
    '181','115','17','114','203','214','195','188','199'
]

estante_baixo = [
    '207','103','6','113','208','204','128','122','52','152','155','200',
    '4','191','150','215','213','143','199b','206','161',
]

parede_interna = [
    '228','223b','225','222','226','227','223','224','229',
    '230','231','232','233','234','235','236','237','238','239',
    '240','241','242','243','244','245','246','247','249','250','251',
    '252',
]

#=================================================================================

#criando uma função pro label da resposta
def saida_dados(saida):    
    label_resposta = Label(frame_resposta, text=saida,font=('arial 12 bold'),
                   fg = branca, bg=azul_escuro,anchor=NE)
    label_resposta.place(x=4,y=12)

def nome():
    faca=entry_faca.get()
    if faca in cima_c1:
        saida = 'LOCAL: CIMA_C1                          '
        saida_dados(saida)
    
    elif faca in cima_c2:
        saida = 'LOCAL: CIMA_C2                          '
        saida_dados(saida)
    
    elif faca in parede:
        saida = 'LOCAL: PAREDE                           '
        saida_dados(saida)
    
    elif faca in baixo_c1:
        saida = 'LOCAL: BAIXO_C1                         '
        saida_dados(saida)
    
    elif faca in baixo_c2:
        saida = 'LOCAL: BAIXO_C2                         '
        saida_dados(saida)
    
    elif faca in estante_baixo:
        saida = 'LOCAL: ESTANTE                          '
        saida_dados(saida)
    
    elif faca in parede_interna:
        saida = 'LOCAL: PAREDE INTERNA'
        saida_dados(saida)
    
    else:
        saida = "NÃO ENCONTRADA!"
        saida_dados(saida)
    

    
    return faca

botao_pesquisar = Button(frame_pesquisa,text="OK",font=('Ivy 8 bold'),bg=verde_claro,
                         fg=vermelho,relief=RAISED,overrelief=RIDGE,command=nome)
botao_pesquisar.place(x=266,y=12)

#configurando frame_resposta
#esse parte tem que ficar dentro da funçao,ja que queremos que ela seja
#acionada com o comando do botão.

#label_resposta = Label(frame_resposta, text="Digite o número da faca:",font=('arial 12 bold'),
#                   fg = branca, bg=azul_escuro,anchor=NE)
#label_resposta.place(x=4,y=12)


janela.mainloop()















