#importante abri o bloco antes de rodar o comando

import pyautogui as pg
import pyperclip as pc
from time import sleep

pg.PAUSE = 0.1

pg.click(x=563, y=460)
pc.copy("Lista de nomes aleatórios")
pg.hotkey('ctrl','v')
pg.press('enter')
pg.press('enter')


lista_nomes = ['João','Maria',"Iris",'Camila',"Julia",
               'Lucas','Anderson',"Gabriel",'Talita']

for i in lista_nomes:
    pc.copy(i)
    pg.hotkey('ctrl','v')
    pg.press(',')
    #sleep(0.2)


pg.press('enter')
pg.press('enter')

num = [1,2,3,4,5]
tipo = ['casa@','carro?','biké','lixô','me\sa']
tamanho = ['G','M','P','PP','X']

for i in range(len(num)):
    numuro = num[i]
    coisa = tipo[i]
    tam = tamanho[i]
    pc.copy(f'{numuro}, {coisa}, {tam}')
    pg.hotkey('ctrl', 'v')
    pg.press('enter')

pg.hotkey('ctrl','s')
