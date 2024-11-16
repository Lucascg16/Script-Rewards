#pip install pyautogui
#pip install pillow
#pip install opencv-python
#pip install pynput

import pyautogui as pa
import time
import random

letras = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5']

time.sleep(1)

for i in letras:
    barra_pesquisa = pa.locateCenterOnScreen('imagens/barra_de_pesquisa.png', confidence= 0.8)
    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)
    
    time.sleep(0.5)
    pa.press(i)
    time.sleep(0.5)

    arrows_down = random.randint(1, 7)
    for i in range(arrows_down):
        pa.press('down')

    time.sleep(1)
    pa.press('enter')

    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)

    time.sleep(7)

    pa.click(x = barra_pesquisa.x, y = barra_pesquisa.y)

    apagar= pa.locateCenterOnScreen('imagens/apagar.png', confidence= 0.8)
    pa.click(x = apagar.x, y = apagar.y)

    pa.click(x = apagar.x + 150, y = apagar.y)

    time.sleep(2)