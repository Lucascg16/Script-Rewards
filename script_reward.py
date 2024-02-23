#pip install pyautogui
#pip install pillow
#pip install opencv-python

import pyautogui as pa
import time
import random

#clicar na barra de pesquisa
#pesquisar usando um for
#descer nos resultados de 1 a 7 vezez
#vai apertar enter
#esperar mais ou menos 7 sec
#colocar o mouse na barra de pesquisa
#clicar no x

letras = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

time.sleep(1)

for i in letras:
    barra_pesquisa = pa.locateCenterOnScreen('imagens/barra_de_pesquisa.png', confidence= 0.8)
    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)

    pa.press(i)
    
    arrows_down = random.randint(1, 7)
    for i in range(arrows_down):
        pa.press('down')

    time.sleep(0.3)
    pa.press('enter')

    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)

    time.sleep(7)

    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)

    apagar= pa.locateCenterOnScreen('imagens/apagar.png', confidence= 0.9)
    pa.click(x = apagar.x, y = apagar.y)

    pa.click(x = apagar.x + 150, y = apagar.y)

    time.sleep(2)