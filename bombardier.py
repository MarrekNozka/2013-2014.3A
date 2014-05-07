#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  bombardier.py
# Datum:   7.5.2014
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   malá zábavná hra.
###################################################

import random
import pylab as lab
import matplotlib.animation as animation

############################################
SIRKA = 64
VYSKA = 43
PSLOUPCU = SIRKA
PRADKU = VYSKA
############################################
CERNA = 10
SEDA = 5
BILA = 0
############################################
"""Vrtulník je na začátku v levém horním rohu"""
vrtulnik = [1, 0]
data = []


def on_key(event):
    print('you pressed', event.key, event.xdata, event.ydata)


def step(event):
    """
    Tato funkce se opakovaně spouští každých X ms. Podle toho jak je nastaveno
    ve funkci animation.FuncAnimation
    """
    global vrtulnik
    global data
    (r, s) = vrtulnik
    try:
        data[r][s] = SEDA
    except IndexError:
        data[r][-1] = BILA
        r += 1
        s = 0
    data[r][s-1] = BILA
    s += 1
    vrtulnik = [r, s]
    print vrtulnik
    grid.set_array(data)

############################################
#data = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11]]
#data[1][0] = 11

"""Vytvořím prázdnou matici číse obsahujcí nuly"""
for r in range(PRADKU):
    radek = [BILA for i in range(PSLOUPCU)]
    data.append(radek)

"""Vytvořím pohoří"""
for s in range(PSLOUPCU):
    hranice = int(0.15*VYSKA) + random.randint(0, int(0.7*VYSKA))
    for r in range(PRADKU):
        if r > hranice:
            data[r][s] = CERNA


############################################
fig = lab.figure()
sub = lab.subplot(111)
sub.axes.get_xaxis().set_visible(False)
sub.axes.get_yaxis().set_visible(False)

grid = lab.imshow(data, interpolation='none', cmap='binary')
lab.grid()

cid = fig.canvas.mpl_connect('key_press_event', on_key)
anim = animation.FuncAnimation(fig, step, interval=200)

lab.show()
